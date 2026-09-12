# Quy tắc định dạng tài liệu (Formatting Rule)

Khi người dùng gọi `/formating` hoặc `/formatting` (hoặc yêu cầu format một file/nội dung), hãy tự động kích hoạt skill `formating`:

1. **Chuẩn hóa cấu trúc**:
   - Sử dụng Tiêu đề cấp 1 `#` duy nhất kèm emoji phù hợp.
   - Chia các phần cấp 2 `##` bằng emoji (🎯, 📋, ⚙️, 🚀, 📌, 💡, ⚠️, ✅) và phân tách bằng đường kẻ `---`.
   - Chuyển đổi dữ liệu đối chiếu/cấu hình/tham số thành bảng Markdown (`| Cột 1 | Cột 2 |`).
   - Chuẩn hóa checklist công việc dạng `- [ ]` / `- [x]`.
   - Bao bọc lệnh, query SQL, kịch bản BDD/Feature trong đúng code blocks có syntax highlighting (`bash`, `sql`, `gherkin`, `python`, v.v.).
   - Sử dụng Callout (`> [!NOTE]`, `> [!IMPORTANT]`, `> [!TIP]`, `> [!WARNING]`) cho các lưu ý trọng tâm.

2. **Bảo toàn thông tin**:
   - Giữ nguyên 100% nội dung kỹ thuật, link, ID, code, không tự ý xóa bỏ chi tiết quan trọng.
   - Sửa lỗi chính tả và hành văn cho súc tích, mạch lạc.

3. **Tự động cập nhật file**:
   - Nếu file nằm trong workspace hoặc người dùng chỉ định đường dẫn, ghi đè trực tiếp nội dung đã format vào file.

4. **Cơ chế tự động nhận diện & Chuẩn hóa quy trình theo loại Ticket (Auto-Detect Workflow)**:
   - 🔍 **Dấu hiệu nhận biết 1 - Ticket Endpoint Automation**:
     - *Dấu hiệu:* Xuất hiện từ khóa `endpoint`, tag `[API-QA]`, hoặc có đường dẫn API (`/.../...`).
     - *Ví dụ:* `[X] [API-QA] - [QA-6700]: Implement automated tests for the missing Coordinator service endpoints /instruction/by-step-ref/{uniqueRef}`.
     - *Flow chuẩn 11 bước:*
       1. `Create Test Scenario Prompt`: Tạo prompt AI đọc test steps để sinh Scenarios.
       2. `Create New Branch`: Tạo branch `<branch-name>-<endpoint>`, chuyển status sang `Testing`.
       3. `Complete Scenario`: Rà soát và hoàn thiện kịch bản Scenarios trước khi code.
       4. `Review Code`: Review code test triển khai.
       5. `Run Code`: Chạy automated test cục bộ.
       6. `Fix Code`: Sửa lỗi phát sinh nếu có.
       7. `Create TestRail`: Tạo và cập nhật test cases lên TestRail.
       8. `Commit and Push Code`: Commit & push code lên remote branch.
       9. `Create PR Summary`: Soạn thảo nội dung PR summary.
       10. `Create Pull Request`: Tạo PR trên GitHub.
       11. `Update Review Status`: Chuyển status ticket sang `Under Review` khi hoàn tất endpoint.

   - 🔍 **Dấu hiệu nhận biết 2 - Ticket Thường / UI-QA / Test Execution**:
     - *Dấu hiệu:* Xuất hiện tag `[TEST EXECUTION]`, `[UI-QA]`, hoặc các ticket chức năng/giao diện chung (`GTO-xxxx`, enhancement không có URL endpoint).
     - *Ví dụ:* 
       - `[X] [TEST EXECUTION] - [QA-6880]: [GTO-16245], [GTO-16246] Restrict retry of a failed transfer to ops users only...`
       - `[ ] [UI-QA] - [GTO-16168]: Split Fireblocks section into Vault and Whitelisted Address...`
     - *Flow chuẩn 5 giai đoạn:*
       1. `Read Request`: Đọc và hiểu rõ tài liệu yêu cầu (Jira, Confluence, PRD, Slack).
       2. `Designing`: Đặt status `Designing`, thiết kế bộ test cases.
       3. `Testing`: Đặt status `Testing`, thực thi test Endpoint/UI/Regression/E2E, đẩy test artifacts lên Confluence.
       4. `Pass Test`: Chuyển status `Pass Test` khi nghiệm thu xong, đánh dấu hoàn thành ✅.
       5. `Create PR`: Mở PR và gán các reviewer chính: **Mohit**, **Dastan**, và **Sandeep**.
