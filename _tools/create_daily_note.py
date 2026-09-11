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

def generate_weekly_summary(base_dir: str = None, target_date: datetime = None, week_folder_name: str = None) -> Optional[str]:
    """Tạo hoặc cập nhật file Markdown tổng kết tuần (What I Did & What I Learned)"""
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

    # Nếu không có file Ghi chú nào, thử tìm Daily Report
    if not md_files:
        for f in os.listdir(week_dir):
            if f.endswith(".md") and f.lower().startswith("daily report"):
                md_files.append(os.path.join(week_dir, f))

    if not md_files:
        print(f"[INFO] Không tìm thấy file ghi chú daily hợp lệ trong {week_folder_name} để tổng kết.")
        return None

    parsed_notes = [parse_daily_note(f) for f in md_files]
    parsed_notes.sort(key=lambda x: x["file_date"])

    now = datetime.now()
    summary_filename = f"Summary {week_folder_name}.md"
    summary_file_path = os.path.join(week_dir, summary_filename)

    custom_next_week_plan = extract_custom_section_from_existing(summary_file_path)

    # Dựng nội dung Markdown gọn gàng, súc tích (Executive Summary)
    md_lines = [
        f"# 📊 TỔNG KẾT TUẦN {week_num:02d} ({start_str} - {end_str})",
        "",
        f"> 📅 **Thời gian tổng kết:** {now.strftime('%d/%m/%Y %H:%M:%S')}  ",
        f"> 📁 **Tổng số ngày làm việc ghi nhận:** {len(parsed_notes)} ngày",
        "",
        "---",
        "",
        "## 🗓️ 1. Nhật ký hoạt động trong tuần (Daily Breakdown)",
        "",
        "| Ngày | Thứ | Chủ đề chính | File ghi chú |",
        "| :--- | :--- | :--- | :--- |"
    ]

    for note in parsed_notes:
        encoded_filename = urllib.parse.quote(note["file_name"])
        link = f"[{note['file_name']}](./{encoded_filename})"
        md_lines.append(f"| {note['date_str']} | {note['weekday_str']} | {note['main_topic']} | {link} |")
    
    md_lines.extend(["", "---", "", "## ✅ 2. Những việc đã làm trong tuần (What I Did)", ""])
    
    has_work = False
    for note in parsed_notes:
        note_work = []
        for w in note["work_items"]:
            if w not in note_work:
                note_work.append(w)
        for d in note["tasks_done"]:
            formatted = f"**[Đã hoàn thành]** {d}"
            if formatted not in note_work and d not in note_work:
                note_work.append(formatted)
            
        # Lọc gọn: Lấy tối đa 4-5 bullet tiêu biểu nhất mỗi ngày, bỏ các câu râu ria
        filtered_work = []
        for item in note_work:
            if not any(skip in item.lower() for skip in ["*(điều kiện", "*cập nhật", "hôm qua (", "phụ thuộc cốt lõi:"]):
                filtered_work.append(item)
            if len(filtered_work) >= 5:
                break
                
        if filtered_work:
            has_work = True
            md_lines.append(f"### 📌 {note['weekday_str']} ({note['date_str']}) - {note['main_topic']}")
            for item in filtered_work:
                md_lines.append(f"- {item}")
            md_lines.append("")
            
    if not has_work:
        md_lines.append("*(Chưa ghi nhận mục công việc cụ thể trong tuần)*\n")
        
    md_lines.extend(["---", "", "## 💡 3. Kiến thức & Điểm nổi bật (Key Learnings & Highlights)", ""])
    
    has_learnings = False
    for note in parsed_notes:
        learnings_sections = note["learnings_sections"]
        ideas = note["ideas_notes"]
        
        if learnings_sections or ideas:
            has_learnings = True
            md_lines.append(f"### 🌟 {note['weekday_str']} ({note['date_str']}) - {note['main_topic']}")
            
            for sec_name, blocks in learnings_sections.items():
                if sec_name in ["Nội dung chung", "🎯 Mục tiêu trong ngày"]:
                    continue
                if any(k in sec_name.lower() for k in ["daily report", "công thức tạo 1 branch"]):
                    continue
                    
                clean_sec_name = re.sub(r'^[^\w\s]+', '', sec_name).strip()
                md_lines.append(f"#### 🔹 {clean_sec_name}")
                
                bullet_count = 0
                for block_type, block_data in blocks:
                    if block_type == "quote":
                        md_lines.append(f"> {block_data}")
                    elif block_type == "bullet":
                        if bullet_count < 3:
                            md_lines.append(f"- {block_data}")
                            bullet_count += 1
                            
            if ideas:
                md_lines.append("#### 🧠 Ghi nhớ chính")
                for idea in ideas[:2]:
                    md_lines.append(f"- {idea}")
                    
            md_lines.append("")
            
    if not has_learnings:
        md_lines.append("*(Chưa ghi nhận mục kiến thức/quy trình cụ thể trong tuần)*\n")
        
    md_lines.extend(["---", "", "## ⏳ 4. Việc còn tồn đọng & Kế hoạch tuần tới (Pending & Next Focus)", ""])
    
    all_pending = []
    for note in parsed_notes:
        for p in note["tasks_pending"]:
            all_pending.append((note["date_str"], p))
            
    if all_pending:
        for d_str, task in all_pending:
            md_lines.append(f"- [ ] `[{d_str}]` {task}")
    else:
        md_lines.append("- [x] *Không có task tồn đọng chưa hoàn thành từ các ngày làm việc.*")
        
    md_lines.append("")

    if custom_next_week_plan:
        md_lines.append(custom_next_week_plan)
    else:
        md_lines.extend([
            "### 🎯 Kế hoạch trọng tâm tuần tiếp theo:",
            "- [ ] Triển khai kiểm thử End-to-End thực tế khi môi trường tích hợp hoàn tất (PR 8425 + BE Waves).",
            "- [ ] Thực thi Regression Suite cho các luồng Crypto Fireblocks.",
            "- [ ] Đồng bộ Test Cases lên TestRail và cập nhật trạng thái Jira.",
            "",
            "---",
            f"*Tự động tổng kết lúc {now.strftime('%H:%M:%S - %d/%m/%Y')}*"
        ])

    summary_content = "\n".join(md_lines) + "\n"

    with open(summary_file_path, "w", encoding="utf-8") as f:
        f.write(summary_content)

    print(f"[SUCCESS] Đã tạo/cập nhật Summary tuần thành công: {summary_file_path}")
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


def generate_all_summaries(base_dir: str = None):
    """Tổng kết toàn bộ các tuần trong thư mục"""
    if base_dir is None:
        base_dir = get_default_base_dir()
        
    week_folders = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and d.startswith("Tuần ")]
    week_folders.sort()
    
    print(f"[INFO] Tìm thấy {len(week_folders)} thư mục tuần cần tổng kết.")
    for folder in week_folders:
        generate_weekly_summary(base_dir=base_dir, week_folder_name=folder)

# ==============================================================================
# 5. ĐIỂM VÀO CHÍNH (CLI & INTERACTIVE MENU)
# ==============================================================================

if __name__ == "__main__":
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
        generate_all_summaries()
    elif "--summary" in sys.argv:
        generate_weekly_summary()
    elif "--week" in sys.argv:
        idx = sys.argv.index("--week")
        if idx + 1 < len(sys.argv):
            week_folder_arg = sys.argv[idx + 1]
            generate_weekly_summary(week_folder_name=week_folder_arg)
        else:
            print("[LỖI] Vui lòng chỉ định tên folder tuần sau cờ --week.")
    else:
        create_daily_note()

