import os
import sys
import re
import urllib.parse
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple

# Đảm bảo hiển thị tiếng Việt không bị lỗi font trên Windows console
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ==============================================================================
# 1. CÁC HÀM XỬ LÝ NGÀY THÁNG & THƯ MỤC
# ==============================================================================

def get_default_base_dir() -> str:
    """Xác định thư mục gốc chứa các tuần ghi chú (Ghi chú daily)"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(current_dir).startswith(("_", "tool", "script")):
        return os.path.dirname(current_dir)
    return current_dir

DAY_NAME_VI = {
    0: "Thứ Hai", 1: "Thứ Ba", 2: "Thứ Tư", 3: "Thứ Năm",
    4: "Thứ Sáu", 5: "Thứ Bảy", 6: "Chủ Nhật"
}

def get_week_range_info(target_date: datetime) -> Tuple[int, datetime, datetime, str]:
    """Lấy thông tin tuần theo chuẩn ISO (Thứ 2 là đầu tuần)"""
    year, week_num, weekday = target_date.isocalendar()
    start_of_week = target_date - timedelta(days=weekday - 1)
    end_of_week = start_of_week + timedelta(days=6)
    folder_name = f"Tuần {week_num:02d} ({start_of_week.strftime('%d.%m')} - {end_of_week.strftime('%d.%m.%Y')})"
    return week_num, start_of_week, end_of_week, folder_name

def parse_week_info_from_folder_name(folder_name: str) -> Tuple[int, str, str]:
    """Trích xuất số tuần và khoảng ngày từ tên thư mục: 'Tuần 35 (24.08 - 30.08.2026)'"""
    match = re.search(r'Tuần\s*(\d+)\s*\(([\d\.]+)\s*-\s*([\d\.]+)\)', folder_name, re.IGNORECASE)
    if match:
        return int(match.group(1)), match.group(2), match.group(3)
    match_num = re.search(r'Tuần\s*(\d+)', folder_name, re.IGNORECASE)
    return int(match_num.group(1)) if match_num else 1, "", ""

def parse_date_from_filename(filename: str) -> Optional[datetime]:
    """Tìm ngày tháng DDMMYYYY trong tên file"""
    match = re.search(r'(\d{2})(\d{2})(\d{4})', filename)
    if match:
        day, month, year = int(match.group(1)), int(match.group(2)), int(match.group(3))
        try:
            return datetime(year, month, day)
        except ValueError:
            pass
    return None

def extract_main_topic(filename: str, content: str) -> str:
    """Trích xuất chủ đề chính từ tên file hoặc thẻ H1 đầu tiên"""
    base_no_ext = os.path.splitext(filename)[0]
    if " - " in base_no_ext:
        return base_no_ext.split(" - ", 1)[1].strip()
    
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("# "):
            h1_text = line[2:].strip()
            if " - " in h1_text:
                return h1_text.split(" - ", 1)[1].strip()
            if not re.match(r'^Ghi chú ngày \d{2}/\d{2}/\d{4}', h1_text):
                return h1_text
            
    return "Ghi chú công việc & học tập"

def clean_bullet_prefix(line: str) -> str:
    """Loại bỏ ký tự bullet (- , * , + , 1. ) ở đầu dòng nhưng bảo toàn in đậm ** """
    text = re.sub(r'^\s*[-*+]\s+', '', line)
    text = re.sub(r'^\s*\d+\.\s+', '', text)
    return text.strip()

def is_empty_or_template_note(file_path: str) -> bool:
    """Kiểm tra xem file ghi chú có phải chỉ là template trống hoặc không có nội dung thực tế không"""
    if not os.path.exists(file_path):
        return True
    try:
        size = os.path.getsize(file_path)
        if size < 350:
            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
            lines = [line.strip() for line in content.splitlines() if line.strip()]
            template_markers = ["- [ ]", "- [ ] ", "- ", "-", "---"]
            content_lines = []
            for line in lines:
                if line.startswith("#") or line.startswith("*") or line in template_markers:
                    continue
                content_lines.append(line)
            if not content_lines:
                return True
    except Exception:
        pass
    return False

# ==============================================================================
# 2. TẠO GHI CHÚ DAILY HÀNG NGÀY
# ==============================================================================

def create_daily_note(base_dir: str = None, auto_summary: bool = True) -> Optional[str]:
    """Tạo file ghi chú daily hôm nay (Thứ 2 - Thứ 6) hoặc tự động tổng kết tuần nếu là Thứ 7/Chủ Nhật"""
    if base_dir is None:
        base_dir = get_default_base_dir()
        
    now = datetime.now()
    day_name = DAY_NAME_VI[now.weekday()]
    
    # NẾU LÀ THỨ BẢY (5) HOẶC CHỦ NHẬT (6): KHÔNG TẠO NOTE DAILY, CHỈ TỔNG KẾT TUẦN
    if now.weekday() >= 5:
        print(f"[INFO] Hôm nay là {day_name}, cuối tuần không cần tạo ghi chú daily. Tiến hành tổng kết tuần...")
        if auto_summary:
            return generate_weekly_summary(base_dir=base_dir, target_date=now)
        return None
    
    # Cấu trúc tên file: Ghi chú DDMMYYYY.md
    file_name = f"Ghi chú {now.strftime('%d%m%Y')}.md"
    _, _, _, week_folder = get_week_range_info(now)
    target_dir = os.path.join(base_dir, week_folder)
    
    os.makedirs(target_dir, exist_ok=True)
    
    # Kiểm tra xem hôm nay đã có file ghi chú chưa (kể cả khi đã đổi tên thêm chủ đề)
    date_pattern = now.strftime('%d%m%Y')
    existing_file = None
    if os.path.exists(target_dir):
        for f in os.listdir(target_dir):
            if f.endswith(".md") and f.startswith("Ghi chú") and date_pattern in f:
                existing_file = os.path.join(target_dir, f)
                break

    if existing_file:
        file_path = existing_file
        print(f"[INFO] File daily note hôm nay đã tồn tại: {os.path.basename(file_path)}")
    else:
        file_path = os.path.join(target_dir, file_name)
        template = f"""# Ghi chú ngày {now.strftime('%d/%m/%Y')} ({day_name})

## 🎯 Mục tiêu trong ngày
- [ ] 

## 📝 Ghi chú công việc / Study
- 

## 💡 Ghi nhớ / Ideas
- 

---
*Tạo tự động vào lúc {now.strftime('%H:%M:%S')}*
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(template)
            
        print(f"[SUCCESS] Đã tạo ghi chú daily thành công: {file_path}")

    return file_path

# ==============================================================================
# 3. TRÍCH XUẤT NỘI DUNG & TỔNG HỢP SUMMARY TUẦN
# ==============================================================================

def parse_daily_note(file_path: str) -> Dict[str, Any]:
    """Phân tích nội dung file ghi chú daily và bóc tách thành các phần: What I Did, What I Learned, Pending"""
    file_name = os.path.basename(file_path)
    file_date = parse_date_from_filename(file_name)
    weekday_str = DAY_NAME_VI[file_date.weekday()] if file_date else "Trong tuần"
    date_str = file_date.strftime("%d/%m/%Y") if file_date else ""

    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    main_topic = extract_main_topic(file_name, content)
    
    tasks_done = []
    tasks_pending = []
    work_items = []
    ideas_notes = []
    learnings_sections: Dict[str, List[Tuple[str, Any]]] = {}
    
    lines = content.splitlines()
    current_section = "Nội dung chung"
    in_code_block = False
    
    i = 0
    while i < len(lines):
        raw_line = lines[i]
        stripped = raw_line.strip()
        
        # Bỏ qua code block delimiters
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            i += 1
            continue
        if in_code_block:
            i += 1
            continue
            
        # Bỏ qua dòng trống, đường kẻ ngang, metadata
        if not stripped or stripped.startswith("---") or stripped.startswith("*Tạo tự động") or stripped.startswith("*Ghi chú daily"):
            i += 1
            continue
        if stripped.lower().startswith("ngày cập nhật:") or stripped.lower().startswith("**ngày cập nhật:"):
            i += 1
            continue
        if stripped.startswith("# Ghi chú ngày") or stripped == "# Mục tiêu":
            i += 1
            continue

        # 1. Nhận diện khối bảng Markdown (| ... |) -> Tóm tắt súc tích, không dump nguyên bảng
        if stripped.startswith("|") and stripped.endswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|") and lines[i].strip().endswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            
            data_rows = [r for r in table_lines if not any(c in r for c in ["---", ":---"])][1:]
            if len(data_rows) > 0:
                summary_msg = f"Ma trận/Bảng dữ liệu: Đã xây dựng & bao phủ **{len(data_rows)} kịch bản chi tiết** (xem chi tiết trong file ghi chú ngày)."
                if current_section not in learnings_sections:
                    learnings_sections[current_section] = []
                learnings_sections[current_section].append(("bullet", summary_msg))
            continue

        # 2. Nhận diện tiêu đề mục H1, H2, H3
        if stripped.startswith("#") or re.match(r'^\d+\.\s+[A-ZÀ-Ỵ]', stripped):
            sec_title = re.sub(r'^[#\d\.\s]+', '', stripped).strip()
            if not re.match(r'^Ghi chú ngày \d{2}/\d{2}/\d{4}', sec_title) and sec_title != main_topic:
                current_section = sec_title
            i += 1
            continue

        # 3. Checkbox hoàn thành [x]
        if re.match(r'^[-*]\s*\[[xX]\]', stripped):
            item_text = re.sub(r'^[-*]\s*\[[xX]\]\s*', '', stripped).strip()
            if item_text:
                tasks_done.append(item_text)
            i += 1
            continue
            
        # 4. Checkbox chưa hoàn thành [ ]
        if re.match(r'^[-*]\s*\[\s*\]', stripped):
            item_text = re.sub(r'^[-*]\s*\[\s*\]\s*', '', stripped).strip()
            if item_text:
                tasks_pending.append(item_text)
            i += 1
            continue

        sec_lower = current_section.lower()
        is_idea_sec = any(k in sec_lower for k in ["ghi nhớ", "ideas", "ý tưởng"])
        is_issue_sec = any(k in sec_lower for k in ["lỗi", "issue", "bug", "blocker", "vấn đề", "cảnh báo"])

        # 5. Bắt task / ticket / công việc đặc biệt (chỉ khi không nằm trong Ideas hoặc Issues)
        if not is_idea_sec and not is_issue_sec:
            ticket_match = re.search(r'(\[TEST EXECUTION\]|\[API-QA\]|\[UI-QA\]|[A-Z]{2,10}-\d+)', stripped)
            if ticket_match:
                clean_item = clean_bullet_prefix(stripped)
                if clean_item and clean_item not in work_items:
                    work_items.append(clean_item)
                    i += 1
                    continue

        # 6. Nhận diện blockquote (> ...)
        if stripped.startswith(">"):
            quote_text = re.sub(r'^\s*>\s*', '', stripped).strip()
            if current_section not in learnings_sections:
                learnings_sections[current_section] = []
            learnings_sections[current_section].append(("quote", quote_text))
            i += 1
            continue

        clean_item = clean_bullet_prefix(stripped)
        if not clean_item or len(clean_item) < 3:
            i += 1
            continue

        sec_lower = current_section.lower()
        if any(k in sec_lower for k in ["ghi nhớ", "ideas", "ý tưởng"]):
            ideas_notes.append(clean_item)
        elif any(k in sec_lower for k in ["mục tiêu", "target", "goal", "todo"]):
            if clean_item not in tasks_done and clean_item not in tasks_pending and clean_item not in work_items:
                work_items.append(clean_item)
        else:
            if current_section not in learnings_sections:
                learnings_sections[current_section] = []
            
            existing_bullets = [d for t, d in learnings_sections[current_section] if t == "bullet"]
            if clean_item not in existing_bullets:
                learnings_sections[current_section].append(("bullet", clean_item))

        i += 1

    return {
        "file_name": file_name,
        "file_path": file_path,
        "date_str": date_str,
        "weekday_str": weekday_str,
        "file_date": file_date or datetime.min,
        "main_topic": main_topic,
        "tasks_done": tasks_done,
        "tasks_pending": tasks_pending,
        "work_items": work_items,
        "learnings_sections": learnings_sections,
        "ideas_notes": ideas_notes,
    }

def extract_custom_section_from_existing(existing_summary_path: str) -> Optional[str]:
    """Bảo tồn các ghi chú tùy chỉnh người dùng đã tự tay bổ sung vào mục Kế hoạch tuần tới"""
    if not os.path.exists(existing_summary_path):
        return None
    try:
        with open(existing_summary_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        pattern = r'(## 🎯 5\. Định hướng & Kế hoạch tuần tiếp theo.*)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            saved_part = match.group(1).strip()
            lines = saved_part.splitlines()
            user_added = False
            for line in lines[1:]:
                clean = line.strip()
                if clean and not clean.startswith("---") and not clean.startswith("*File tổng kết") and clean not in [
                    "- [ ]", "- [ ] ", "- ", "",
                    "- [ ] Tiếp tục thực thi và tối ưu các automation test cases.",
                    "- [ ] Rà soát các quy trình làm việc và tài liệu trên Confluence."
                ]:
                    user_added = True
                    break
            if user_added:
                return saved_part
    except Exception:
        pass
    return None

def format_weekly_summary_content(parsed_notes: List[Dict[str, Any]], week_num: int, start_str: str, end_str: str) -> str:
    """Xây dựng nội dung file Weekly Summary theo đúng cấu trúc request.md và tiêu chuẩn prompt.md"""
    lines = [
        "* [Vsee - Galaxy] Weekly Summary + Demo",
        "",
        "Attendees: Brian Pham Hau Duong (Hầu Dương) Huy Nguyễn Pháp Huỳnh Quốc Thai Huynh",
        "",
        "* Notes",
        "",
        "Meeting sẽ chia ra làm các phần chính như sau:",
        "",
        "## Summary:",
        "",
        "* List ra trong tuần rồi đã / đang làm ticket nào, progress như thế nào rồi:",
        ""
    ]

    # Thu thập các ticket và công việc từ các ngày
    all_work_raw = []
    for note in parsed_notes:
        for w in note["work_items"]:
            if w not in all_work_raw:
                all_work_raw.append(w)
        for d in note["tasks_done"]:
            if d not in all_work_raw:
                all_work_raw.append(d)
        for p in note["tasks_pending"]:
            if p not in all_work_raw:
                all_work_raw.append(p)

    # Phân nhóm và trích xuất ticket
    tickets_processed = []
    seen_ticket_keys = set()

    for item in all_work_raw:
        found_keys = re.findall(r'((?:QA|GTO)-\d+)', item)
        ticket_key = found_keys[0] if found_keys else None
        
        if not ticket_key:
            tag_match = re.search(r'(\[API-QA\]|\[TEST EXECUTION\]|\[UI-QA\])', item)
            if tag_match:
                ticket_key = tag_match.group(1).strip("[]")

        if ticket_key:
            if ticket_key in seen_ticket_keys:
                continue
            seen_ticket_keys.add(ticket_key)
        
        clean_item = clean_bullet_prefix(item)
        clean_item = re.sub(r'^\[[xX\s]\]\s*', '', clean_item)
        
        is_endpoint = any(k in item.lower() for k in [
            "endpoint", "api-qa", "/instruction", "/permission", "api automation", "coordinator", "service endpoint"
        ])
        
        is_done = any(item == d or d in item for note in parsed_notes for d in note["tasks_done"])
        is_in_progress = "(in progress)" in item.lower() or any(item == p or p in item for note in parsed_notes for p in note["tasks_pending"])
        
        if is_done and not is_in_progress:
            progress_str = "Hoàn thành kiểm thử và nghiệm thu ✅."
        elif is_in_progress:
            progress_str = "In Progress (Đang thực hiện)."
        else:
            progress_str = "Hoàn thành triển khai test suite ban đầu và các assertion cơ bản."

        tickets_processed.append({
            "key": ticket_key or "QA-TASK",
            "raw": clean_item,
            "is_endpoint": is_endpoint,
            "progress": progress_str
        })

    if not tickets_processed:
        for note in parsed_notes:
            if note["main_topic"] and note["main_topic"] != "Ghi chú công việc & học tập":
                is_endpoint = "endpoint" in note["main_topic"].lower() or "coordinator" in note["main_topic"].lower()
                tickets_processed.append({
                    "key": "TASK",
                    "raw": note["main_topic"],
                    "is_endpoint": is_endpoint,
                    "progress": "Hoàn thành trong tuần."
                })

    demo_items = []
    for t in tickets_processed:
        item_title = t["raw"]
        if t["key"] in item_title:
            title_display = f"**`{t['key']}` - {re.sub(r'^[\[\w\s\-]+\]\s*:\s*', '', item_title)}**"
        else:
            title_display = f"**`{t['key']}` - {item_title}**"
            
        lines.append(f"  * {title_display}:")
        
        if t["is_endpoint"]:
            lines.append("    * **Đã làm:** Xây dựng và triển khai automated test suite cho endpoint. Áp dụng đồng bộ **Quy trình chuẩn 11 bước triển khai kiểm thử tự động cho một Endpoint (Standard Flow for Endpoint Automation)**:")
            lines.append("        1. **Create Test Scenario Prompt:** Tạo prompt cho AI đọc các test steps và sinh ra bộ Scenarios để review.")
            lines.append("        2. **Create New Branch:** Tạo branch mới (chuẩn `<branch-name>-<endpoint>`) và chuyển trạng thái ticket sang `Testing`.")
            lines.append("        3. **Complete Scenario:** Hoàn thiện các Scenarios và review kỹ lưỡng trước khi bắt đầu viết code implementation.")
            lines.append("        4. **Review Code:** Review code triển khai của test.")
            lines.append("        5. **Run Code:** Chạy code và thực thi các bộ automated test.")
            lines.append("        6. **Fix Code:** Sửa các lỗi phát sinh nếu có.")
            lines.append("        7. **Create TestRail:** Tạo và cập nhật test cases lên hệ thống TestRail.")
            lines.append("        8. **Commit and Push Code:** Commit và push code lên đúng nhánh remote.")
            lines.append("        9. **Create PR Summary:** Soạn thảo bản tóm tắt nội dung PR.")
            lines.append("        10. **Create Pull Request:** Tạo Pull Request trên Git (GitHub).")
            lines.append("        11. **Update Review Status:** Cập nhật trạng thái ticket Jira sang **`Under Review`** khi hoàn tất endpoint.")
            demo_items.append(f"Trình diễn Flow chuẩn triển khai Endpoint Automation & Bộ Test Suite (`{t['key']}`)")
        else:
            lines.append("    * **Đã làm:** Thực hiện kiểm thử nghiệp vụ và giao diện. Áp dụng **Quy trình kiểm thử Ticket thường (Standard Feature/UI Testing Workflow)** gồm 5 giai đoạn:")
            lines.append("        1. **Read Request:** Đọc và phân tích kỹ tài liệu yêu cầu Jira & Confluence spec.")
            lines.append("        2. **Designing:** Chuyển status Jira sang `Designing`, thiết kế bộ test cases chi tiết.")
            lines.append("        3. **Testing:** Chuyển status Jira sang `Testing`, thực thi test Endpoint, Regression Test và E2E Test; đưa test artifacts lên Confluence.")
            lines.append("        4. **Pass Test:** Sau khi kiểm thử hoàn tất và đạt chuẩn, chuyển status Jira sang `Pass Test`, đánh dấu hoàn thành ✅.")
            lines.append("        5. **Create PR:** Tạo PR trên Git và gán các reviewer chính: **Mohit**, **Dastan**, và **Sandeep**.")
            demo_items.append(f"Trình diễn Feature/UI Test Execution & Quy trình nghiệm thu (`{t['key']}`)")
            
        lines.append(f"    * **Tiến độ hiện tại:** {t['progress']}")
        lines.append("")

    lines.append("* Demo feature đã / đang làm:")
    lines.append("")
    if not demo_items:
        demo_items = ["Trình diễn Flow chuẩn triển khai Endpoint Automation & Test Suite", "Trình diễn Feature / UI Test Execution & Quy trình nghiệm thu"]
        
    for i, demo in enumerate(demo_items[:3], 1):
        lines.append(f"  * **Demo {i}: {demo}:**")
        lines.append("    * Trình diễn toàn bộ chu trình kiểm thử, kết quả chạy automation test pass 100%, cập nhật TestRail và quy trình mở Pull Request.")

    lines.extend([
        "",
        "## Knowledge Sharing:",
        "",
        "* Pick ra 1 topic trong feature mình đã làm để sharing knowledge (UI):",
        ""
    ])

    found_learning_topic = None
    found_learning_points = []
    for note in parsed_notes:
        for sec_name, blocks in note["learnings_sections"].items():
            if any(k in sec_name.lower() for k in ["daily report", "nội dung chung", "mục tiêu", "nhật ký"]):
                continue
            clean_sec = re.sub(r'^[^\w\s]+', '', sec_name).strip()
            if len(clean_sec) > 5 and not found_learning_topic:
                found_learning_topic = clean_sec
                for b_type, b_data in blocks[:4]:
                    found_learning_points.append(b_data)
                break
        if found_learning_topic:
            break

    if found_learning_topic:
        lines.append(f"  * **{found_learning_topic}:**")
        lines.append(f"    * **Chủ đề lựa chọn:** Chia sẻ kinh nghiệm thực tế về {found_learning_topic}.")
        for pt in found_learning_points:
            lines.append(f"      * {pt}")
    else:
        lines.extend([
            "  * **Transfer tool manage permission & Instructions:**",
            "    * **Chủ đề lựa chọn:** Xử lý triệt để bẫy cờ `PENDING_APPROVAL` trên Jenkins và Chiến lược phân quyền kiểm thử cho tính năng Retry Failed Transfer.",
            "    * **1. Bài toán thực tế & Hướng xử lý (Flaky Test Fix):**",
            "      * Thiết lập pre-test setup chủ động reset và ép cấu hình approval về đúng trạng thái kỳ vọng của từng scenario trước khi chạy, sau đó dọn dẹp teardown.",
            "    * **2. Kiểm thử tính năng Dev Enhancement:**",
            "      * Xác định các điểm chạm dùng chung (Shared Seams), phân quyền RBAC và kiểm tra tính toàn vẹn trạng thái dữ liệu."
        ])

    lines.extend([
        "",
        "* Cách apply AI trong công việc:",
        "",
        "  * **Quy trình ứng dụng thực chiến:** **Input → AI Hỗ trợ → QA Đánh giá & Rà soát → Kết quả cuối cùng**",
        "    1. **Input:** Link Jira ticket, tài liệu Confluence PRD/spec, git diff của PR và các đoạn thảo luận kỹ thuật.",
        "    2. **AI Hỗ trợ:** Sử dụng AI để đọc test steps sinh Scenarios kiểm thử, thiết kế ma trận test cases, gợi ý kịch bản edge case và cấu trúc test assertions.",
        "    3. **QA Đánh giá & Rà soát:** QA rà soát tính đúng đắn logic nghiệp vụ, đối chiếu với spec thực tế, bổ sung assertions an toàn và tinh chỉnh kịch bản.",
        "    4. **Kết quả cuối cùng:** Test suites tự động pass 100%, test cases được đồng bộ lên TestRail và PR hoàn thiện.",
        "",
        "* Cách test regression tests và scope cần test trong regression tests:",
        "",
        "  * **Phương pháp xác định phạm vi Regression khi test ticket enhancement:**",
        "    * **Xác định các điểm chạm dùng chung (Shared Seams):** Kiểm tra các service, API và luồng dữ liệu dùng chung logic với tính năng được cập nhật.",
        "    * **Phân tách rõ vùng ảnh hưởng:** Luôn kiểm thử song song cả luồng cũ và luồng mới để đảm bảo tính năng mới không gây lỗi hồi quy cho các tính năng đang chạy ổn định.",
        "    * **Ngưỡng chặn hồi quy (Regression Gate):** Toàn bộ regression suite phải Pass 100% trước khi ký duyệt nghiệm thu.",
        "",
        "Cách test ticket enhancement của dev và regression scope mình cần làm tương ứng.",
        "",
        "Action items:",
        ""
    ])

    all_pending = []
    for note in parsed_notes:
        for p in note["tasks_pending"]:
            clean_p = clean_bullet_prefix(p)
            if clean_p and clean_p not in all_pending:
                all_pending.append(clean_p)

    if all_pending:
        for p in all_pending:
            lines.append(f"* {p}")
    else:
        lines.extend([
            "* Tiếp tục thực thi và tối ưu các automated test cases cho các endpoints tiếp theo.",
            "* Thực thi toàn bộ bộ test hồi quy (Regression Suite) trên môi trường staging.",
            "* Đồng bộ và cập nhật các test cases lên TestRail và liên kết Jira ticket tương ứng."
        ])

    lines.append("")
    return "\n".join(lines)


def generate_weekly_summary(base_dir: str = None, target_date: datetime = None, week_folder_name: str = None, force: bool = False) -> Optional[str]:
    """Tạo hoặc cập nhật file Weekly Summary tại Weenly Summary/Weekly_Summary_Tuan_{week_num}.md
    theo đúng cấu trúc request.md và tiêu chuẩn prompt.md."""
    if base_dir is None:
        base_dir = get_default_base_dir()
        
    if target_date is None:
        target_date = datetime.now()

    if week_folder_name is None:
        _, _, _, week_folder_name = get_week_range_info(target_date)

    week_num, start_str, end_str = parse_week_info_from_folder_name(week_folder_name)
    if not start_str or not end_str:
        _, start_dt, end_dt, _ = get_week_range_info(target_date)
        start_str = start_dt.strftime('%d.%m')
        end_str = end_dt.strftime('%d.%m.%Y')

    week_dir = os.path.join(base_dir, week_folder_name)
    if not os.path.exists(week_dir):
        print(f"[WARN] Thư mục tuần không tồn tại: {week_dir}")
        return None

    # Thư mục lưu trữ Weekly Summary tập trung
    summary_dir = os.path.join(base_dir, "Weenly Summary")
    os.makedirs(summary_dir, exist_ok=True)
    summary_filename = f"Weekly_Summary_Tuan_{week_num}.md"
    summary_file_path = os.path.join(summary_dir, summary_filename)

    # Bảo vệ an toàn nội dung nếu file đã tồn tại và có nội dung chi tiết (> 500 bytes)
    if os.path.exists(summary_file_path) and os.path.getsize(summary_file_path) > 500:
        if not force and "--force" not in sys.argv:
            print(f"[INFO] File Weekly Summary đã tồn tại ({os.path.getsize(summary_file_path)} bytes): {summary_file_path}")
            print("[INFO] Giữ nguyên nội dung đã biên soạn chi tiết. (Dùng cờ --force nếu muốn tạo lại hoàn toàn).")
            return summary_file_path

    # Quét các file ghi chú daily (chỉ lấy file ghi chú chính, bỏ qua summary, daily report và template trống)
    md_files = []
    seen_dates = set()
    for f in os.listdir(week_dir):
        if not f.endswith(".md"):
            continue
        lower_name = f.lower()
        if lower_name.startswith(("summary", "tong_ket", "tổng kết", "daily report", "weekly report")):
            continue
        full_path = os.path.join(week_dir, f)
        if is_empty_or_template_note(full_path):
            continue
        
        file_date = parse_date_from_filename(f)
        if file_date:
            date_key = file_date.strftime("%d%m%Y")
            if date_key in seen_dates:
                continue
            seen_dates.add(date_key)
            
        md_files.append(full_path)

    if not md_files:
        print(f"[INFO] Không tìm thấy file ghi chú daily hợp lệ trong {week_folder_name} để tổng kết.")
        return None

    parsed_notes = [parse_daily_note(f) for f in md_files]
    parsed_notes.sort(key=lambda x: x["file_date"])

    # Sinh nội dung chuẩn theo template request.md & prompt.md
    summary_content = format_weekly_summary_content(parsed_notes, week_num, start_str, end_str)

    with open(summary_file_path, "w", encoding="utf-8") as f:
        f.write(summary_content)

    print(f"[SUCCESS] Đã tạo/cập nhật Weekly Summary thành công: {summary_file_path}")
    return summary_file_path

# ==============================================================================
# 4. TẠO DAILY REPORT CUỐI NGÀY (17:35) TỪ GHI CHÚ DAILY (ENGLISH FORMAT)
# ==============================================================================

DAY_NAME_EN = {
    0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
    4: "Friday", 5: "Saturday", 6: "Sunday"
}

EN_TRANSLATION_RULES: List[Tuple[str, str]] = [
    (r'Nghiên cứu & thực hiện:\s*', 'Research & implement: '),
    (r'Nghiên cứu\s*&?\s*thực hiện\s*', 'Research & implement '),
    (r'Tìm hiểu / thực hiện:\s*', 'Research & implement: '),
    (r'Tìm hiểu\s*/\s*chuẩn hóa:\s*', 'Study & standardize: '),
    (r'Đồng bộ tài liệu:\s*', 'Document sync: '),
    (r'Task thực thi:\s*', 'Task execution: '),
    (r'Chuyển Jira sang Confluence', 'Sync Jira ticket details to Confluence'),
    (r'Cập nhật thông tin từ\s*\*\*?Jira Ticket\*\*?\s*sang trang\s*\*\*?Confluence\*\*?\s*mà vẫn bảo toàn nguyên vẹn template của Confluence\.?', 'Update Jira ticket details to Confluence while preserving Confluence template structure.'),
    (r'Kiểm tra bảng\s*\*\*?Test Table\*\*?\s*trong phần\s*\*\*?Test Section\*\*?\s*trên Confluence\.?', 'Verify Test Table in the Test Section on Confluence.'),
    (r'Đối chiếu dữ liệu giữa\s*\*\*?Jira\*\*?\s*và\s*\*\*?Confluence\*\*?\s*đảm bảo khớp nội dung\.?', 'Cross-check and verify data consistency between Jira and Confluence.'),
    (r'Lưu và xuất bản\s*\(Publish\)\s*trang tài liệu\.?', 'Save and publish Confluence documentation page.'),
    (r'Kết nối Database:\s*', 'Database connection: '),
    (r'Tìm hiểu cách kết nối cơ sở dữ liệu cho dự án\.?', 'Study and configure database connection for the project.'),
    (r'Phân tích mã nguồn:\s*', 'Source code analysis: '),
    (r'Đọc và hiểu code của\s*`?test transfer tool`?\s*và\s*`?transfer gateway`?\.?', 'Review and analyze code for test transfer tool and transfer gateway.'),
    (r'Kiểm thử BDD / Scenario:\s*', 'BDD / Scenario Testing: '),
    (r'Theo dõi cách viết kịch bản Smoke Test và Regression Test trong file\s*`?transfer_gateway\.feature`?\.?', 'Review Smoke Test and Regression Test scenarios in transfer_gateway.feature.'),
    (r'Kiểm tra dữ liệu kiểm thử trong bảng\s*`?Examples`?\s*xem còn khớp với version hiện tại không để cập nhật lại\.?', 'Check and update test data in Examples table to match current version.'),
    (r'Kỹ năng Báo cáo:\s*', 'Reporting skills: '),
    (r'Tập viết Daily Report và Test Report theo chuẩn\.?', 'Practice writing standard Daily Report and Test Report.'),
    (r'Công cụ hỗ trợ\s*\(Helper Scripts\):\s*', 'Helper Scripts: '),
    (r'Sử dụng script\s*`?Helper Script/check-new-apis`?\s*để kiểm tra danh sách các API mới\.?', 'Use Helper Script/check-new-apis to check new API list.'),
    (r'Cập nhật Roadmap dự án bằng lệnh\s*`?\./update-roadmap\.sh`?\.?', 'Update project roadmap via ./update-roadmap.sh.'),
    (r'Thực thi:\s*', 'Execution: '),
    (r'Chạy thử nghiệm và kiểm tra toàn bộ các test cases trong phần Instruction\.?', 'Execute and verify all test cases specified in Instruction.'),
    (r'Bảng quyết định\s*\(Decision Table\):\s*', 'Decision Table: '),
    (r'Học và nghiên cứu kỹ thuật thiết kế test case bằng Decision Table để bao phủ toàn bộ tổ hợp điều kiện nghiệp vụ\.?', 'Study test design techniques using Decision Table to cover business logic combinations.'),
    (r'Review Instruction:\s*', 'Review Instruction: '),
    (r'Phân loại rõ ràng giữa bản Instruction chính thức và bản nháp\s*\(`?instruction/draft`?\)\.?', 'Classify official Instruction vs draft versions (instruction/draft).'),
    (r'Kiểm tra tính đầy đủ của các bước thực thi trước khi đưa vào automation test\.?', 'Verify test steps completeness before applying to automation tests.'),
    (r'Tiếp tục hoàn thiện các nội dung liên quan đến\s*', 'Continue working on '),
    (r'Tiếp tục các đầu việc trong kế hoạch tiếp theo', 'Continue next planned tasks'),
    (r'Tiếp tục kế hoạch công việc ngày tiếp theo', 'Continue planned tasks for the next day'),
    (r'Tiếp tục các đầu việc ngày mai', 'Continue planned tasks tomorrow')
]

def translate_item_to_english(text: str) -> str:
    """Chuyển đổi các câu ghi chú tiếng Việt sang tiếng Anh chuẩn cho Daily Report"""
    result = text.strip()
    for pattern, repl in EN_TRANSLATION_RULES:
        result = re.sub(pattern, repl, result, flags=re.IGNORECASE)
    return result

def generate_daily_report(base_dir: str = None, target_date: datetime = None, target_date_str: str = None, note_file_path: str = None) -> Optional[str]:
    """
    Tự động tạo file Daily Report cuối ngày bằng tiếng Anh (What I’ve done, In Progress, Todo, Issues)
    từ file ghi chú daily của ngày hôm đó (chạy lúc 17:35 hoặc theo nhu cầu).
    """
    if base_dir is None:
        base_dir = get_default_base_dir()

    if target_date_str:
        clean_str = target_date_str.replace("/", "").replace("-", "").replace(".", "")
        if len(clean_str) == 8:
            try:
                target_date = datetime(int(clean_str[4:8]), int(clean_str[2:4]), int(clean_str[0:2]))
            except ValueError:
                target_date = datetime.now()
        else:
            target_date = datetime.now()
    elif target_date is None:
        target_date = datetime.now()

    day_en = DAY_NAME_EN[target_date.weekday()]
    date_formatted = target_date.strftime("%d/%m/%Y")
    date_code = target_date.strftime("%d%m%Y")
    
    _, _, _, week_folder = get_week_range_info(target_date)
    week_dir = os.path.join(base_dir, week_folder)

    # Tìm file ghi chú daily của ngày hôm đó nếu chưa có đường dẫn cụ thể
    if note_file_path is None:
        if os.path.exists(week_dir):
            for f in os.listdir(week_dir):
                if f.endswith(".md") and f.startswith("Ghi chú") and date_code in f:
                    note_file_path = os.path.join(week_dir, f)
                    break

    what_done: List[str] = []
    in_progress: List[str] = []
    todo: List[str] = []
    issues: List[str] = []

    if note_file_path and os.path.exists(note_file_path):
        parsed = parse_daily_note(note_file_path)
        main_topic = parsed.get("main_topic", "")
        tasks_done = parsed.get("tasks_done", [])
        tasks_pending = parsed.get("tasks_pending", [])
        work_items = parsed.get("work_items", [])
        learnings_sections = parsed.get("learnings_sections", {})
        
        # 1. Bóc tách What I've done:
        # Ưu tiên các task [x]
        for t in tasks_done:
            clean_t = clean_bullet_prefix(t)
            if clean_t:
                en_t = translate_item_to_english(clean_t)
                if en_t not in what_done:
                    what_done.append(en_t)
        
        # Thêm các ticket/công việc đặc biệt (e.g. [TEST EXECUTION], [API-QA], [UI-QA])
        for w in work_items:
            clean_w = clean_bullet_prefix(w)
            if clean_w:
                en_w = translate_item_to_english(clean_w)
                if en_w not in what_done:
                    what_done.append(en_w)
                
        # Nếu chưa có task [x], trích xuất chủ đề chính & các mục kiến thức đã học/làm
        if not what_done and main_topic and main_topic != "Ghi chú công việc & học tập":
            what_done.append(translate_item_to_english(f"Nghiên cứu & thực hiện: {main_topic}"))

        skip_keywords = ["ghi chú", "note", "ideas", "mẫu prompt", "chuẩn bị", "liên kết", "cảnh báo", "lưu ý", "nội dung chung"]
        for sec_name, blocks in learnings_sections.items():
            sec_lower = sec_name.lower()
            if not any(k in sec_lower for k in skip_keywords) and len(what_done) < 4:
                clean_sec = re.sub(r'^[^\w\s]+', '', sec_name).strip()
                sec_bullet = translate_item_to_english(f"Tìm hiểu / thực hiện: {clean_sec}")
                if sec_bullet not in what_done and clean_sec.lower() not in [x.lower() for x in what_done]:
                    what_done.append(sec_bullet)

        # 2. Bóc tách In Progress & Todo:
        if tasks_pending:
            for idx, p in enumerate(tasks_pending):
                clean_p = clean_bullet_prefix(p)
                if not clean_p:
                    continue
                en_p = translate_item_to_english(clean_p)
                # Nếu có từ khóa thể hiện đang làm hoặc là task đầu tiên cần xử lý tiếp
                if idx == 0 and len(tasks_pending) > 1 and any(k in clean_p.lower() for k in ["tiếp tục", "đang", "thực thi", "review", "kiểm thử"]):
                    in_progress.append(en_p)
                else:
                    todo.append(en_p)

        if not in_progress:
            if todo and len(todo) > 1:
                in_progress.append(todo.pop(0))
            elif what_done:
                in_progress.append(translate_item_to_english(f"Tiếp tục hoàn thiện các nội dung liên quan đến {main_topic}"))
            else:
                in_progress.append("None")
                
        if not what_done:
            what_done.append(f"Research and update documentation for {date_formatted}")
            
        if not todo:
            todo.append("Continue planned tasks for next day")

        # 3. Issues: thường issues không ghi -> Mặc định None trừ khi có mục riêng
        for sec_name, blocks in learnings_sections.items():
            if any(k in sec_name.lower() for k in ["lỗi", "issue", "bug", "blocker", "vấn đề", "cảnh báo"]):
                for b_type, b_data in blocks:
                    if b_type == "bullet":
                        issues.append(translate_item_to_english(b_data))

    else:
        what_done.append(f"Execute planned tasks for {date_formatted}")
        in_progress.append("None")
        todo.append("Continue planned tasks tomorrow")

    # Xây dựng nội dung file Daily Report bằng tiếng Anh
    report_lines = [
        f"# 📋 DAILY REPORT - {date_formatted} ({day_en})",
        "",
        f"> 🕒 **Generated at:** {datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}",
        "",
        "---",
        "",
        "What I’ve done:"
    ]
    for d in what_done:
        report_lines.append(f"- {d}")
        
    report_lines.extend(["", "In Progress:"])
    for p in in_progress:
        if p.strip() == "None":
            report_lines.append("None")
        else:
            report_lines.append(f"- {p}")
            
    report_lines.extend(["", "Todo:"])
    for t in todo:
        if t.strip() == "None":
            report_lines.append("None")
        else:
            report_lines.append(f"- {t}")
            
    report_lines.extend(["", "Issues:"])
    if issues:
        for iss in issues:
            report_lines.append(f"- {iss}")
    else:
        report_lines.append("None")
        
    report_lines.extend(["", "---", ""])

    report_content = "\n".join(report_lines)

    # Lưu vào file Daily Report DDMMYYYY.md trong thư mục tuần
    os.makedirs(week_dir, exist_ok=True)
    report_filename = f"Daily Report {date_code}.md"
    report_file_path = os.path.join(week_dir, report_filename)

    with open(report_file_path, "w", encoding="utf-8") as f:
        f.write(report_content)

    print("\n" + "="*60)
    print(f"  📋 DAILY REPORT - {date_formatted} ({day_en})")
    print("="*60)
    print("\nWhat I’ve done:")
    for d in what_done:
        print(f"- {d}")
    print("\nIn Progress:")
    for p in in_progress:
        print(f"- {p}" if p != "None" else "None")
    print("\nTodo:")
    for t in todo:
        print(f"- {t}" if t != "None" else "None")
    print("\nIssues:")
    if issues:
        for iss in issues:
            print(f"- {iss}")
    else:
        print("None")
    print("="*60)
    print(f"[SUCCESS] Saved Daily Report: {report_file_path}\n")

    return report_file_path


def generate_all_summaries(base_dir: str = None, force: bool = False):
    """Tổng kết toàn bộ các tuần trong thư mục vào Weenly Summary"""
    if base_dir is None:
        base_dir = get_default_base_dir()
        
    week_folders = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and d.startswith("Tuần ")]
    week_folders.sort()
    
    print(f"[INFO] Tìm thấy {len(week_folders)} thư mục tuần cần tổng kết.")
    for folder in week_folders:
        generate_weekly_summary(base_dir=base_dir, week_folder_name=folder, force=force)

# ==============================================================================
# 5. ĐIỂM VÀO CHÍNH (CLI & INTERACTIVE MENU)
# ==============================================================================

if __name__ == "__main__":
    force_flag = "--force" in sys.argv
    if "--report" in sys.argv:
        # Kiểm tra xem có truyền ngày cụ thể không: --report DDMMYYYY
        idx = sys.argv.index("--report")
        report_date_arg = None
        if idx + 1 < len(sys.argv) and not sys.argv[idx + 1].startswith("--"):
            report_date_arg = sys.argv[idx + 1]
        generate_daily_report(target_date_str=report_date_arg)
    elif "--report-date" in sys.argv:
        idx = sys.argv.index("--report-date")
        if idx + 1 < len(sys.argv):
            generate_daily_report(target_date_str=sys.argv[idx + 1])
        else:
            generate_daily_report()
    elif "--all-summaries" in sys.argv or "--all" in sys.argv:
        generate_all_summaries(force=force_flag)
    elif "--summary" in sys.argv:
        generate_weekly_summary(force=force_flag)
    elif "--week" in sys.argv:
        idx = sys.argv.index("--week")
        if idx + 1 < len(sys.argv):
            week_folder_arg = sys.argv[idx + 1]
            generate_weekly_summary(week_folder_name=week_folder_arg, force=force_flag)
        else:
            print("[LỖI] Vui lòng chỉ định tên folder tuần sau cờ --week.")
    else:
        create_daily_note()

