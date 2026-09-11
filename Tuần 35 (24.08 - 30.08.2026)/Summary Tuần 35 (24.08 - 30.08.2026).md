# 📊 TỔNG KẾT TUẦN 35 (24.08 - 30.08.2026)

> 📅 **Thời gian tổng kết:** 29/08/2026 08:05:26  
> 📁 **Tổng số ngày ghi chú trong tuần:** 8 ngày

---

## 🗓️ 1. Nhật ký hoạt động trong tuần (Daily Breakdown)

| Ngày | Thứ | Chủ đề chính | File ghi chú |
| :--- | :--- | :--- | :--- |
|  | Trong tuần | 30.08.2026) | [Weekly Report Tuần 35 (24.08 - 30.08.2026).md](./Weekly%20Report%20Tu%E1%BA%A7n%2035%20%2824.08%20-%2030.08.2026%29.md) |
| 25/08/2026 | Thứ Ba | Quy trình Automation & Quản lý Code | [00. ⭐ [CORE GUIDELINE] Ghi chú 25082026 - Quy trình Automation & Quản lý Code.md](./00.%20%E2%AD%90%20%5BCORE%20GUIDELINE%5D%20Ghi%20ch%C3%BA%2025082026%20-%20Quy%20tr%C3%ACnh%20Automation%20%26%20Qu%E1%BA%A3n%20l%C3%BD%20Code.md) |
| 26/08/2026 | Thứ Tư | Bảng quyết định & Instruction | [Ghi chú 26082026 - Bảng quyết định & Instruction.md](./Ghi%20ch%C3%BA%2026082026%20-%20B%E1%BA%A3ng%20quy%E1%BA%BFt%20%C4%91%E1%BB%8Bnh%20%26%20Instruction.md) |
| 27/08/2026 | Thứ Năm | 27/08/2026 (Thursday) | [Daily Report 27082026.md](./Daily%20Report%2027082026.md) |
| 27/08/2026 | Thứ Năm | Chuyển Jira sang Confluence | [Ghi chú 27082026 - Chuyển Jira sang Confluence.md](./Ghi%20ch%C3%BA%2027082026%20-%20Chuy%E1%BB%83n%20Jira%20sang%20Confluence.md) |
| 28/08/2026 | Thứ Sáu | 28/08/2026 (Friday) | [Daily Report 28082026.md](./Daily%20Report%2028082026.md) |
| 28/08/2026 | Thứ Sáu | 📝 Ghi chú ngày 28/08/2026 (Thứ Sáu) | [Ghi chú 28082026.md](./Ghi%20ch%C3%BA%2028082026.md) |
| 29/08/2026 | Thứ Bảy | Ghi chú công việc & học tập | [Ghi chú 29082026.md](./Ghi%20ch%C3%BA%2029082026.md) |

---

## ✅ 2. Những việc đã làm trong tuần (What I Did)

### 📌 Trong tuần () - 30.08.2026)
- [API-QA] - [QA-6702]: Completed automation tests for 2 new endpoints:
- [TEST EXECUTION] - [QA-6741] & [QA-6742]: Reviewed documentation and prepared test scenarios for GTO-16043 (Fiat withdrawal UI/E2E) & GTO-15979 (Fiat withdrawal initiation - Transfer Tool).
- [QA-6742] - GTO-16043: Fiat withdrawal initiation test execution remains in Designing status.
- [QA-6742] - GTO-16043: Fiat withdrawal UI and E2E test execution remain in Designing status.
- Follow up on review feedback and resolve comments for PR #1318 ([QA-6702]).

### 📌 Thứ Tư (26/08/2026) - Bảng quyết định & Instruction
- Học và nghiên cứu kỹ thuật thiết kế test case bằng Decision Table để bao phủ toàn bộ tổ hợp điều kiện nghiệp vụ.
- Phân loại rõ ràng giữa bản Instruction chính thức và bản nháp (`instruction/draft`).
- Kiểm tra tính đầy đủ của các bước thực thi trước khi đưa vào automation test.

### 📌 Thứ Năm (27/08/2026) - 27/08/2026 (Thursday)
- **Task execution: ** `[TEST EXECUTION]` **GTO-16043** - Fiat withdrawal UI + E2E (Transfer Tool).

### 📌 Thứ Sáu (28/08/2026) - 28/08/2026 (Friday)
- **[API-QA] - [QA-6702]:** Implement test for new endpoint `/permission/validate/instruction`
- **[QA-6741] & [QA-6742]:** Review & prepare test execution for GTO-16043 & GTO-15979 (Fiat withdrawal UI/E2E & Initiation - Transfer Tool)
- **[QA-6742] - GTO-16043:** Fiat withdrawal initiation test execution remains Designing
- **[QA-6742] - GTO-16043:** Fiat withdrawal UI and E2E test execution remain Designing
- Theo dõi feedback và resolve PR #1318 (`[QA-6702]`)
- Tiếp tục hoàn thiện Test Execution cho GTO-16043 (Fiat withdrawal initiation & UI/E2E)
- Follow up merge PR #1318 và close ticket `[QA-6702]`

### 📌 Thứ Sáu (28/08/2026) - 📝 Ghi chú ngày 28/08/2026 (Thứ Sáu)
- 📋 **Rã test case (4 cases):**
- 2 Happy cases (Valid instruction, full permission check)
- 2 Negative cases (Invalid instruction data, unauthorized role/action)
- ⚙️ **Implement + chạy OK:** Chạy test suite đạt 100% Passed.
- 🔗 **Created TestRail link:** Đồng bộ và gán test case ID lên TestRail.
- 🚀 **Create PR:** **#1318** (đính kèm đầy đủ test evidence và pass screenshots).
- **[Đã hoàn thành]** **[API-QA] - [QA-6702]:** Implement test for new endpoint `/permission/validate/instruction`

---

## 📚 3. Những kiến thức & Quy trình đã học (What I Learned)

### 💡 Trong tuần () - 30.08.2026)
- What I’ve done:
- Endpoint `/permission/transfer-details`:
- Designed test cases (4 cases: 2 Happy Path, 2 Negative cases)
- Implemented & executed successfully (100% Passed)
- Created TestRail links mapped to test cases
- Created PR: #1318
- Endpoint `/permission/validate/instruction`:
- Designed test cases (6 cases: 4 Happy Path, 2 Negative cases)
- Created PR
- Researched & standardized technical guidelines: BDD keyword reusability, 4-tier code tracing workflow (API ➔ Service ➔ References ➔ DB), multi-environment dynamic DB queries.
- In Progress:
- Todo:
- Issues:
- None

### 💡 Thứ Ba (25/08/2026) - Quy trình Automation & Quản lý Code
#### 🔹 QUY TRÌNH VIẾT AUTOMATION TEST
- Các bước cơ bản để xây dựng kịch bản tự động hóa:
- **Đọc requirement:** Nắm rõ yêu cầu của task và nghiệp vụ bài toán.
- **Viết prompt:** Chuẩn bị câu lệnh (prompt) rõ ràng, chi tiết.
- **Làm việc với AI:** Yêu cầu AI kiểm tra (check) và thiết lập kịch bản (scenario).
- **Review & Chỉnh sửa:** Kiểm tra lại kết quả do AI sinh ra và sửa chữa các điểm chưa hợp lý.
- **Chạy thử:** Hoàn thiện kịch bản và tiến hành chạy thử nghiệm (execute test).
#### 🔹 THAO TÁC VỚI TESTRAIL & CẬP NHẬT TICKET
- **Kết nối Jira Data:** Trước khi chạy sync, đảm bảo đã xác thực và kết nối dữ liệu từ **Jira** để lấy đầy đủ context của ticket.
- **Các câu lệnh chính khi làm việc với TestRail:**
- `/create-testrail`: Chỉ tạo test case, **không** tác động hay cập nhật gì lên ticket.
- `/sync-testrail`: **Đồng bộ và cập nhật (update)** các test case trực tiếp lên ticket.
- **Chụp ảnh Pass Test (Evidence):** Chụp ảnh màn hình kết quả chạy test thành công (passed 100%) và đính kèm trực tiếp vào **Jira Ticket**.
#### 🔹 Phân chia Branch
- **Quy tắc:** Mỗi branch chỉ làm việc cho **MỘT endpoint** duy nhất để dễ quản lý và review.
#### 🔹 Thao tác Review Code
- **Lệnh thực hiện:** `/review-code`
- **Mục đích:**
- Hỗ trợ *self-review* (tự đánh giá) và fix lỗi trước khi push code, giúp tiết kiệm thời gian cho reviewer.
- *Lưu ý:* File `pytest.ini` là file đã được AI review và tự động tạo ra.
#### 🔹 Mở Pull Request
- Khi mở PR trên hệ thống Git, cần hoàn thiện:
- **Mô tả (Description):** Dán toàn bộ nội dung PR Summary đã tạo ở bước trên vào phần mô tả.
- **Bằng chứng (Evidence):** Chụp ảnh màn hình các test case đã chạy thành công (passed/OK) và đính kèm vào PR.
- **Assign Reviewer:** Chọn và gắn tên người sẽ chịu trách nhiệm review code của bạn.
#### 🔹 Xử lý phản hồi Review (`/resolve-pr`)
- Khi Reviewer để lại nhận xét (comment) hoặc yêu cầu sửa đổi trên PR:
#### 🔹 Sử dụng lệnh **`/resolve-pr`** (hoặc Resolve Conversation) để đóng các luồng comment đã được xử lý xong, báo hiệu cho Reviewer biết code đã sẵn sàng để Approve và Merge.
> [!NOTE]
> **Lưu ý phụ (Xác thực Authorization):** Khi công cụ hiển thị popup yêu cầu *"Allow"*, chỉ cần đăng nhập **Jira** trên trình duyệt rồi quay lại trang web xác nhận cấp quyền kết nối.

### 💡 Thứ Năm (27/08/2026) - 27/08/2026 (Thursday)
#### 🔹 📋 DAILY REPORT - 27/08/2026 (Thursday)
> 🕒 **Generated at:** 17:52:48 - 27/08/2026
- What I’ve done:
- Research & implement: Sync Jira ticket details to Confluence
- In Progress:
- **Document sync: ** Update Jira ticket details to Confluence while preserving Confluence template structure.
- Todo:
- Verify Test Table in the Test Section on Confluence.
- Cross-check and verify data consistency between Jira and Confluence.
- Save and publish Confluence documentation page.
- Issues:
- None

### 💡 Thứ Năm (27/08/2026) - Chuyển Jira sang Confluence
#### 🔹 Chuẩn bị liên kết
- **Jira Ticket Link:** `[Link Jira]`
- **Confluence Page Link:** `[Link Confluence]`
#### 🔹 📌 Ghi chú quan trọng (Note)
> [!IMPORTANT]
> * **x-api-key (TEST-AUTOMATION):** `802b1453-7149-as31-593530606dfa`

### 💡 Thứ Sáu (28/08/2026) - 28/08/2026 (Friday)
#### 🔹 📋 DAILY REPORT - 28/08/2026 (Friday)
> 🕒 **Generated at:** 17:35:01 - 28/08/2026
- What I’ve done:
- Rã test case (4 cases): 2 Happy cases, 2 Negative cases
- Implement + chạy OK (100% Passed)
- Created TestRail link to test cases
- Create PR: #1318
- Chuẩn hóa tài liệu kỹ thuật: Quy chuẩn BDD keyword reusability, trace code 4 tầng hệ thống, multi-environment DB queries
- In Progress:
- Todo:
- 📌 Lịch nghỉ phép: Thứ Hai (31/08/2026) off 1 ngày trọn vẹn
- Issues:
- None

### 💡 Thứ Sáu (28/08/2026) - 📝 Ghi chú ngày 28/08/2026 (Thứ Sáu)
#### 🔹 Chi tiết các bước thực hiện:
- **Chuẩn bị & Thiết kế kịch bản:**
- ✍️ **Viết prompt:** Chuẩn bị yêu cầu nghiệp vụ rõ ràng cho AI/công cụ.
- 🔍 **Yêu cầu review:** Kiểm tra tính hợp lệ và độ bao phủ của prompt.
- 📑 **Tạo file Scenario + Test cases:** Định nghĩa các kịch bản test chi tiết.
- **Triển khai & Kiểm thử:**
- 💻 **Implement test case:** Viết mã kiểm thử tự động (Step definitions, Table queries, Models).
- 🔎 **Review:** Thực hiện self-review code và kiểm tra convention (`/review-code`).
- 🛠️ **Fix:** Sửa lỗi phát sinh từ kết quả review.
- 🏃 **Run test:** Chạy bộ test suite (Pytest).
- ✅ **Test Pass:** Xác nhận toàn bộ kịch bản chạy thành công 100%.
- **Đồng bộ, Quản lý Git & Ticket:**
- 🔗 **Kết nối Jira Data:** Kết nối/xác thực với Jira Data trước để lấy đầy đủ context và liên kết ticket.
- 🔄 **Sync TestRail:** Chạy lệnh `/sync-testrail` để đồng bộ test case lên TestRail.
- 📸 **Chụp ảnh Pass Test (Evidence):** Chụp lại ảnh màn hình kết quả chạy test thành công (passed 100%).
- 📌 **Update Ticket:** Cập nhật tiến độ và đính kèm ảnh bằng chứng pass test lên Jira ticket.
- 🚀 **Summary PR + Mở PR:** Dùng `/pr summary` tạo mô tả PR và push code lên remote repository kèm evidence.
- 💬 **Resolve PR (`/resolve-pr`):** Khi Reviewer để lại comment/góp ý trên GitHub PR ➔ Tiến hành fix code, push commit mới và dùng `/resolve-pr` để giải quyết (resolve) toàn bộ các thread comment, sẵn sàng cho Reviewer Approve & Merge.
- 📌 **Update Ticket:** Đính kèm link PR vào Jira ticket.
- 🏁 **Close Ticket:** Hoàn tất và đóng ticket sau khi merge/đạt nghiệm thu.
#### 🔹 📐 2. Quy chuẩn thiết kế BDD & Tái sử dụng Keyword
- **Tái sử dụng keyword (Reusability First):**
- Tách nhỏ thành 2 step rõ ràng thay vì gộp chung làm phát sinh keyword mới.
- Tận dụng `bdd_context` để lưu trữ response, các step sau chỉ cần gọi lại cùng 1 keyword để trích xuất và so sánh giá trị.
- **Thứ tự verify chuẩn & Đặt tên ngắn gọn:**
- Luôn verify **Status Code** trước ➔ đến **Response Schema** ➔ rồi mới đến các trường chi tiết:
- **Minh bạch khi Assert (Không test "hộp mù"):**
- Khi kiểm tra lỗi, bắt buộc dùng **Table** thể hiện rõ `expected_code` và `expected_message`.
#### 🔹 🧭 1. Luồng phân tích và cách trace code hệ thống:
> [!TIP]
> **Cách đọc và trace code:** Bắt đầu từ file **Endpoints** ➔ Lần theo lời gọi đến **Service Layer** (`Transfer_gateway`) ➔ Tham chiếu tới các **Class** & **Transfer Type** ➔ Đào sâu vào **Database Layer** để nắm trọn vẹn luồng dữ liệu.
#### 🔹 🗄️ 2. Nguyên tắc Không Hardcode (Multi-Environment Ready)
- **Query động từ DB:** Mọi dữ liệu như `ttAccountId`, `id_security`, `id_price` phải viết hàm truy vấn động từ Database để test chạy bền vững trên cả môi trường **QA** và **UAT**.
- **Xử lý thời gian:** Dữ liệu stale price tính động bằng `now - 24h` hoặc `now - 48h`, không hardcode timestamp cố định.
- **Tối ưu hiệu năng Query:** Chỉ query đúng số lượng cần thiết (`x items` / limit / filter), không query toàn bộ bảng dữ liệu lớn nhiều lần trong lúc chạy test.
#### 🔹 ⚠️ 3. Làm chủ AI & Kiểm soát Git Diff
- **Không tin tưởng AI 100%:** AI có thể tự ý xóa các hàm helper, class hoặc endpoint cũ dùng chung của test khác.
- **Chỉ "Keep" khi đã hiểu:** Luôn soi kỹ Git Diff; chỉ chấp nhận thay đổi khi đã hiểu rõ 100% logic để tránh làm gãy bộ test cũ.
- **Code phòng thủ trong Python:** Dùng `.get('key')` thay vì `['key']` khi lấy dữ liệu dict để tránh văng lỗi `KeyError`.
#### 🔹 📌 Ghi chú hành chính (Off-day)
- **31/08/2026:** Đăng ký off **1 ngày** trọn vẹn.
- *Cập nhật vào lúc 15:30:15 - 28/08/2026*

---

## ⏳ 4. Các mục tiêu / Việc còn tồn đọng (Pending Tasks)

- [ ] `[]` Complete test execution for GTO-16043 (Fiat withdrawal initiation & UI/E2E).
- [ ] `[]` Follow up on merging PR #1318 and close ticket [QA-6702].
- [ ] `[]` 📌 Day off: Monday (31/08/2026) full day off.
- [ ] `[26/08/2026]` **Bảng quyết định (Decision Table):**
- [ ] `[26/08/2026]` **Review Instruction:**
- [ ] `[27/08/2026]` **Đồng bộ tài liệu:** Cập nhật thông tin từ **Jira Ticket** sang trang **Confluence** mà vẫn bảo toàn nguyên vẹn template của Confluence.
- [ ] `[27/08/2026]` **Task thực thi:** `[TEST EXECUTION]` **GTO-16043** - Fiat withdrawal UI + E2E (Transfer Tool).
- [ ] `[27/08/2026]` Kiểm tra bảng **Test Table** trong phần **Test Section** trên Confluence.
- [ ] `[27/08/2026]` Đối chiếu dữ liệu giữa **Jira** và **Confluence** đảm bảo khớp nội dung.
- [ ] `[27/08/2026]` Lưu và xuất bản (Publish) trang tài liệu.

---

## 🎯 5. Định hướng & Kế hoạch tuần tiếp theo (Next Week Focus)

- [ ] Tiếp tục thực thi và tối ưu các automation test cases.
- [ ] Rà soát các quy trình làm việc và tài liệu trên Confluence.
- [ ] 

---
*File tổng kết tuần được tự động tạo/cập nhật vào 29/08/2026 08:05:26*
