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

# ==============================================================================
# 2. TẠO GHI CHÚ DAILY HÀNG NGÀY
# ==============================================================================

def create_daily_note(base_dir: str = None, auto_summary: bool = True) -> str:
    """Tạo file ghi chú daily hôm nay và tự động tổng kết tuần nếu là Thứ 7/Chủ Nhật"""
    if base_dir is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
    now = datetime.now()
    day_name = DAY_NAME_VI[now.weekday()]
    
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

    # TỰ ĐỘNG TỔNG KẾT VÀO CUỐI TUẦN (Thứ Bảy = 5, Chủ Nhật = 6)
    if auto_summary and now.weekday() >= 5:
        print(f"\n[AUTO-SUMMARY] Hôm nay là {day_name}, đang tự động tổng kết What I Did & What I Learned trong tuần...")
        generate_weekly_summary(base_dir=base_dir, target_date=now)

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

        # 1. Nhận diện khối bảng Markdown (| ... |)
        if stripped.startswith("|") and stripped.endswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|") and lines[i].strip().endswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            
            if len(table_lines) >= 2:
                # Đảm bảo có separator line
                if not any("---" in row for row in table_lines):
                    col_count = table_lines[0].count("|") - 1
                    sep = "| " + " | ".join([":---"] * col_count) + " |"
                    table_lines.insert(1, sep)
                
                if current_section not in learnings_sections:
                    learnings_sections[current_section] = []
                learnings_sections[current_section].append(("table", table_lines))
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

        # 5. Bắt task / ticket / công việc đặc biệt
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
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
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

    # Quét các file ghi chú daily (bỏ qua file Summary)
    md_files = []
    for f in os.listdir(week_dir):
        if f.endswith(".md"):
            lower_name = f.lower()
            if not (lower_name.startswith("summary") or lower_name.startswith("tong_ket") or lower_name.startswith("tổng kết")):
                md_files.append(os.path.join(week_dir, f))

    if not md_files:
        print(f"[INFO] Không tìm thấy file ghi chú daily nào trong {week_folder_name} để tổng kết.")
        return None

    parsed_notes = [parse_daily_note(f) for f in md_files]
    parsed_notes.sort(key=lambda x: x["file_date"])

    now = datetime.now()
    summary_filename = f"Summary {week_folder_name}.md"
    summary_file_path = os.path.join(week_dir, summary_filename)

    custom_next_week_plan = extract_custom_section_from_existing(summary_file_path)

    # Dựng nội dung Markdown
    md_lines = [
        f"# 📊 TỔNG KẾT TUẦN {week_num:02d} ({start_str} - {end_str})",
        "",
        f"> 📅 **Thời gian tổng kết:** {now.strftime('%d/%m/%Y %H:%M:%S')}  ",
        f"> 📁 **Tổng số ngày ghi chú trong tuần:** {len(parsed_notes)} ngày",
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
            note_work.append(w)
        for d in note["tasks_done"]:
            note_work.append(f"**[Đã hoàn thành]** {d}")
            
        if note_work:
            has_work = True
            md_lines.append(f"### 📌 {note['weekday_str']} ({note['date_str']}) - {note['main_topic']}")
            for item in note_work:
                md_lines.append(f"- {item}")
            md_lines.append("")
            
    if not has_work:
        md_lines.append("*(Chưa ghi nhận mục công việc cụ thể trong tuần)*\n")
        
    md_lines.extend(["---", "", "## 📚 3. Những kiến thức & Quy trình đã học (What I Learned)", ""])
    
    has_learnings = False
    for note in parsed_notes:
        learnings_sections = note["learnings_sections"]
        ideas = note["ideas_notes"]
        
        if learnings_sections or ideas:
            has_learnings = True
            md_lines.append(f"### 💡 {note['weekday_str']} ({note['date_str']}) - {note['main_topic']}")
            
            for sec_name, blocks in learnings_sections.items():
                if sec_name != "Nội dung chung":
                    md_lines.append(f"#### 🔹 {sec_name}")
                
                for block_type, block_data in blocks:
                    if block_type == "table":
                        md_lines.append("")
                        for row in block_data:
                            md_lines.append(row)
                        md_lines.append("")
                    elif block_type == "quote":
                        md_lines.append(f"> {block_data}")
                    elif block_type == "bullet":
                        md_lines.append(f"- {block_data}")
                        
            if ideas:
                md_lines.append("#### 🧠 Ghi nhớ & Ideas")
                for idea in ideas:
                    md_lines.append(f"- {idea}")
                    
            md_lines.append("")
            
    if not has_learnings:
        md_lines.append("*(Chưa ghi nhận mục kiến thức/quy trình cụ thể trong tuần)*\n")
        
    md_lines.extend(["---", "", "## ⏳ 4. Các mục tiêu / Việc còn tồn đọng (Pending Tasks)", ""])
    
    all_pending = []
    for note in parsed_notes:
        for p in note["tasks_pending"]:
            all_pending.append((note["date_str"], p))
            
    if all_pending:
        for d_str, task in all_pending:
            md_lines.append(f"- [ ] `[{d_str}]` {task}")
    else:
        md_lines.append("- [x] *Không có task tồn đọng chưa hoàn thành từ các ngày.*")
        
    md_lines.extend(["", "---", ""])

    if custom_next_week_plan:
        md_lines.append(custom_next_week_plan)
    else:
        md_lines.extend([
            "## 🎯 5. Định hướng & Kế hoạch tuần tiếp theo (Next Week Focus)",
            "",
            "- [ ] Tiếp tục thực thi và tối ưu các automation test cases.",
            "- [ ] Rà soát các quy trình làm việc và tài liệu trên Confluence.",
            "- [ ] ",
            "",
            "---",
            f"*File tổng kết tuần được tự động tạo/cập nhật vào {now.strftime('%d/%m/%Y %H:%M:%S')}*"
        ])

    summary_content = "\n".join(md_lines) + "\n"

    with open(summary_file_path, "w", encoding="utf-8") as f:
        f.write(summary_content)

    print(f"[SUCCESS] Đã tạo/cập nhật Summary tuần thành công: {summary_file_path}")
    return summary_file_path

def generate_all_summaries(base_dir: str = None):
    """Tổng kết toàn bộ các tuần trong thư mục"""
    if base_dir is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
    week_folders = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and d.startswith("Tuần ")]
    week_folders.sort()
    
    print(f"[INFO] Tìm thấy {len(week_folders)} thư mục tuần cần tổng kết.")
    for folder in week_folders:
        generate_weekly_summary(base_dir=base_dir, week_folder_name=folder)

# ==============================================================================
# 4. ĐIỂM VÀO CHÍNH (CLI & INTERACTIVE MENU)
# ==============================================================================

if __name__ == "__main__":
    if "--all-summaries" in sys.argv or "--all" in sys.argv:
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
