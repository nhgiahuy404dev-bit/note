---
name: formatting
description: Tự động format, chuẩn hóa và làm đẹp tài liệu ghi chú markdown, sổ tay quy trình, kịch bản test hoặc tài liệu kỹ thuật khi người dùng gõ /formatting hoặc /formating kèm file/nội dung.
---

# 🎨 Skill: Định Dạng & Chuẩn Hóa Tài Liệu (Formatting Note & Document)

Skill này kích hoạt khi người dùng gõ `/formatting`, `/formating`, hoặc yêu cầu định dạng, làm đẹp, chuẩn hóa lại nội dung một file ghi chú, tài liệu kỹ thuật, sổ tay quy trình.

---

## 🎯 Mục Tiêu Cốt Lõi
Biến mọi tài liệu nháp thô sơ, ghi chú lộn xộn hoặc tài liệu chưa chuẩn thành văn bản **Markdown chuyên nghiệp, trực quan, có cấu trúc rõ ràng, đẹp mắt** và tuân thủ chuẩn tài liệu của dự án.

---

## 📐 Bộ Quy Chuẩn Định Dạng (Formatting Standard)

### 1. Phân Cấp Tiêu Đề (Heading Hierarchy)
- **H1 (`#`)**: Tiêu đề chính duy nhất ở đầu file, kèm emoji phù hợp (ví dụ: `# 📝 Ghi chú ngày DD/MM/YYYY - [Chủ đề chính]`).
- **H2 (`##`)**: Các phần lớn được đánh số thứ tự hoặc kèm emoji đại diện (ví dụ: `## 🎯 Mục tiêu trong ngày`, `## 📋 Nội dung chi tiết`, `## ⚙️ Quy trình thực hiện`).
- **H3 (`###`)**: Các mục con chi tiết (ví dụ: `### 1.1. Chuẩn bị dữ liệu`, `### 2.2. Tạo Test Run`).
- **Đường kẻ phân cách (`---`)**: Ngăn cách giữa các khối H2 chính để tạo độ thông thoáng.

### 2. Trực Quan Hóa Nội Dung (Visual Enhancements)
- **Icon / Emoji chuẩn hóa**:
  - 🎯 Mục tiêu, mục đích, định hướng
  - 📋 Danh sách công việc, nội dung chi tiết
  - ⚙️ Quy trình, cấu hình, kỹ thuật
  - 🚀 Triển khai, thực thi, tự động hóa
  - 📌 Lưu ý quan trọng, quy ước
  - 💡 Mẹo, gợi ý (Tips & Tricks)
  - ⚠️ Cảnh báo, lỗi thường gặp
  - ✅ Trạng thái thành công, đã hoàn thành
- **In đậm từ khóa**: Luôn `**in đậm**` các thuật ngữ chính, ID, tên công cụ, trạng thái (ví dụ: `**Jira**`, `**TestRail**`, `**Passed**`, `**Suite ID**`).
- **Checklist**: Các đầu mục công việc phải đưa về dạng checklist chuẩn:
  - `- [ ]` Task chưa xong / đang chờ thực hiện
  - `- [x]` Task đã hoàn thành

### 3. Bảng Biểu (Markdown Tables)
- Mọi dữ liệu mang tính liệt kê tham số, ánh xạ ID, phân loại task, cấu hình hệ thống **PHẢI** được chuyển thành Table rõ ràng:
  ```markdown
  | Tham số | Giá trị / Định dạng | Mô tả |
  | :--- | :--- | :--- |
  | **Project ID** | `30` | ID dự án trên hệ thống TestRail |
  ```

### 4. Khối Mã & Lệnh Kỹ Thuật (Code Blocks)
- Mọi lệnh terminal, SQL, JSON, YAML, Curl, BDD/Gherkin Feature, Python code **PHẢI** được bọc trong code block có định danh ngôn ngữ:
  - ` ```bash ` cho shell / cmd / terminal
  - ` ```sql ` cho câu lệnh database
  - ` ```gherkin ` hoặc ` ```feature ` cho kịch bản BDD
  - ` ```json `, ` ```python `, ` ```yaml ` tương ứng
- Các lệnh ngắn, tên file, phím tắt hoặc biến inline bọc trong backticks: `` `run_daily.bat` ``, `` `/daily-report` ``.

### 5. Khối Ghi Chú Nổi Bật (GitHub Callouts)
- Sử dụng Callout cho các thông tin quan trọng thay vì viết text thường:
  ```markdown
  > [!NOTE]
  > Thông tin bổ sung hữu ích.

  > [!IMPORTANT]
  > Thông tin bắt buộc phải tuân thủ.

  > [!TIP]
  > Mẹo xử lý nhanh hoặc kinh nghiệm thực tế.

  > [!WARNING]
  > Cảnh báo rủi ro hoặc điểm dễ sai sót.
  ```

### 6. Nguyên Tắc Bảo Toàn Dữ Liệu
- **100% Bảo toàn thông tin**: Giữ nguyên tất cả các link, ID, code snippet, ý đồ kỹ thuật của tác giả.
- **Sửa lỗi diễn đạt**: Chỉnh sửa lỗi chính tả tiếng Việt, câu cú lủng củng, thống nhất đại từ và thuật ngữ chuyên ngành (QA, Automation, BDD, API).

### 7. Tự Động Nhận Diện Quy Trình Theo Loại Ticket (Auto-Detect Workflow)
- **Khi dòng task có từ khóa `endpoint`, tag `[API-QA]`, hoặc có URL path API (`/.../...`)**:
  ➔ Tự động format theo **Flow 11 bước Endpoint Automation**: `Create Test Scenario Prompt` ➔ `Create New Branch` ➔ `Complete Scenario` ➔ `Review Code` ➔ `Run Code` ➔ `Fix Code` ➔ `Create TestRail` ➔ `Commit and Push Code` ➔ `Create PR Summary` ➔ `Create Pull Request` ➔ `Update Review Status` (`Under Review`).
- **Khi dòng task có tag `[TEST EXECUTION]`, `[UI-QA]`, hoặc ticket chức năng/giao diện chung (`GTO-xxxx`)**:
  ➔ Tự động format theo **Flow 5 bước Ticket Thường**: `Read Request` ➔ `Designing` ➔ `Testing` ➔ `Pass Test` (đánh dấu ✅) ➔ `Create PR` (gán reviewers: **Mohit**, **Dastan**, và **Sandeep**).

---

## 🛠️ Quy Trình Thực Hiện Khi Nhận Lệnh `/formatting` hoặc `/formating`

1. **Xác định đối tượng**:
   - Nếu người dùng cung cấp đường dẫn file (hoặc file đang mở active): Đọc toàn bộ nội dung file đó.
   - Nếu người dùng paste trực tiếp text/markdown: Lấy nội dung text được cung cấp.

2. **Xử lý định dạng**:
   - Áp dụng toàn bộ **Bộ Quy Chuẩn Định Dạng** ở trên để tái cấu trúc lại nội dung.

3. **Lưu & Phản hồi**:
   - Nếu là file trên máy: Sử dụng công cụ `replace_file_content` hoặc `write_to_file` để ghi đè nội dung đẹp vào file.
   - Trả lời người dùng ngắn gọn, hiển thị link file [tên_file](file:///đường_dẫn_tuyệt_đối) và tóm tắt 3-4 điểm cải tiến chính đã thực hiện.
