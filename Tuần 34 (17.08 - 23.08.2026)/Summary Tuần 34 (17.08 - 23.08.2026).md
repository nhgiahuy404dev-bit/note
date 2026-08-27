# 📊 TỔNG KẾT TUẦN 34 (17.08 - 23.08.2026)

> 📅 **Thời gian tổng kết:** 27/08/2026 10:54:24  
> 📁 **Tổng số ngày ghi chú trong tuần:** 5 ngày

---

## 🗓️ 1. Nhật ký hoạt động trong tuần (Daily Breakdown)

| Ngày | Thứ | Chủ đề chính | File ghi chú |
| :--- | :--- | :--- | :--- |
| 17/08/2026 | Thứ Hai | Quy trình Test Execution | [Ghi chú 17082026 - Quy trình Test Execution.md](./Ghi%20ch%C3%BA%2017082026%20-%20Quy%20tr%C3%ACnh%20Test%20Execution.md) |
| 18/08/2026 | Thứ Ba | Nghiên cứu Gateway & Automation | [Ghi chú 18082026 - Nghiên cứu Gateway & Automation.md](./Ghi%20ch%C3%BA%2018082026%20-%20Nghi%C3%AAn%20c%E1%BB%A9u%20Gateway%20%26%20Automation.md) |
| 19/08/2026 | Thứ Tư | Ghi chú công việc & học tập | [Ghi chú 19082026.md](./Ghi%20ch%C3%BA%2019082026.md) |
| 21/08/2026 | Thứ Sáu | Sổ tay Quy trình QA & Automation | [Ghi chú 21082026 - Sổ tay Quy trình QA & Automation.md](./Ghi%20ch%C3%BA%2021082026%20-%20S%E1%BB%95%20tay%20Quy%20tr%C3%ACnh%20QA%20%26%20Automation.md) |
| 22/08/2026 | Thứ Bảy | Quy trình Git Branch & AI Prompt | [Ghi chú 22082026 - Quy trình Git Branch & AI Prompt.md](./Ghi%20ch%C3%BA%2022082026%20-%20Quy%20tr%C3%ACnh%20Git%20Branch%20%26%20AI%20Prompt.md) |

---

## ✅ 2. Những việc đã làm trong tuần (What I Did)

### 📌 Thứ Ba (18/08/2026) - Nghiên cứu Gateway & Automation
- Theo dõi cách viết kịch bản Smoke Test và Regression Test trong file `transfer_gateway.feature`.
- Kiểm tra dữ liệu kiểm thử trong bảng `Examples` xem còn khớp với version hiện tại không để cập nhật lại.
- Sử dụng script `Helper Script/check-new-apis` để kiểm tra danh sách các API mới.
- Cập nhật Roadmap dự án bằng lệnh `./update-roadmap.sh`.

---

## 📚 3. Những kiến thức & Quy trình đã học (What I Learned)

### 💡 Thứ Hai (17/08/2026) - Quy trình Test Execution
#### 🔹 📋 1. Cấu trúc thông tin cần có trong Ticket & Spec
- **Spec:** Link URL tài liệu kỹ thuật / đặc tả yêu cầu.
- **Ticket:** Link URL ticket công việc trên Jira/Hệ thống.
- **Vision / Tester Tool:** Link môi trường và công cụ kiểm thử.
- **Tester:** Tên người thực hiện test.
- **Test Instruction:** Hướng dẫn / kịch bản thực thi test.
#### 🔹 🎯 2. Cấu hình User Group / Scope
- Lựa chọn 2 nhóm:
- `FBS:GDL:TSY`
- `FBS:GTA:MOTC`
#### 🔹 ✍️ 3. Quy trình Sign-off & Bàn giao
- **Yêu cầu từ Dev:** Gửi request lấy **Sign-off** trên giao diện Visual.
- **Đính kèm tài liệu:**
- Link email thông báo / phê duyệt.
- Bảng kết quả đánh giá (Evaluation report).
- **Hoàn tất:** Đánh dấu trạng thái **Completed** để các bên liên quan tự động kiểm tra và verify.

### 💡 Thứ Sáu (21/08/2026) - Sổ tay Quy trình QA & Automation
#### 🔹 QUY ƯỚC TẠO TASK (CẤU TRÚC ĐẶT TÊN)
- *(Lưu ý: Luôn chủ động tuân thủ cấu trúc chuẩn khi tạo task)*

| Loại công việc | Định dạng tiêu đề task |
| :--- | :--- |
| **Chạy test execution** | `[TEST EXECUTION] - [ID__TICKET] TITLE` |
| **Làm task cho API-QA** | `[API-QA] - [ID__TICKET] TITLE` |
| **Làm task cho UI-QA** | `[UI-QA] - [ID__TICKET] TITLE` |

#### 🔹 Tạo Test Cases
- **Lệnh thực hiện:** `/Create-Test-Cases-from-Confluent`
- **Thiết lập dự án:**
- `ProjectID`: **30**
- Nếu project trong **GTO** và **QA** chứa cả 3 suite (UI, API, E2E) thì gọi cả 3.
- **Xử lý file lớn (Large Files):**
- *Vấn đề:* Tránh dùng file local vì có thể lệch với file live, gây sai dữ liệu.
- *Giải pháp:* Sử dụng lệnh `Current:disable-run`.
- *Thao tác:* Create ➔ Copy ➔ Replace.
- **Phân loại & Tổng hợp:**
- Sắp xếp Test Cases vào đúng nhóm: **API / UI / E2E**.
- Yêu cầu hiển thị tóm tắt: *"Show Summary and API group"*.
- **Cập nhật hệ thống:**
- Lấy ID dán vào **Jira** và **GTO**.
- Chuyển trạng thái Automation thành **Candidate** (sẵn sàng tự động hóa).
#### 🔹 Tạo Test Run
- **Lệnh thực hiện:** `/Create-TR-RUN-from-TR-Daraf` + Đánh dấu dự án **All Passed**.
- **Khởi tạo Run:**
- Submit danh sách Test Case để estimate thời gian chạy.
- Kiểm tra kỹ Project ID và Suite ID:
- `ProjectID`: **30**
- `Suite ID API`: **945**
- `Suite ID UI`: **946**
- `Suite ID E2E`: **947**
- Kiểm tra lại toàn bộ status, đảm bảo tất cả đã chuyển sang **Passed**.
#### 🔹 QUY TRÌNH ỨNG DỤNG AI TẠO SCENARIO (CHO AUTOMATION)
- **Chuẩn bị dữ liệu (Check API):** Ghi chép đầy đủ log step:
- Các đoạn code query SQL.
- Dữ liệu xuất ra (output data).
- Các câu lệnh API curl và response trả về.
- Chi tiết dữ liệu đi kèm.
- **Tổng hợp:** Chạy lệnh `/pr summary` (dùng AI tóm tắt lại).
- **Tạo Scenario & Code:** Yêu cầu AI tạo Scenario, sau đó sinh code tương ứng cho từng class.
- **Kiểm tra (Review):** Review kỹ mã nguồn và logic AI sinh ra.
- **Cập nhật TestRail:** Tiến hành tạo test case trên TestRail.
- **Báo cáo & Ghi nhận:**
- Chạy lệnh `/pr summary`.
- Dán nội dung báo cáo lên **GitHub**.
- Vào **Confluence** dán link báo cáo (Hoàn thành phần nào, báo cáo dứt điểm phần đó).
- Kiểm tra và set trạng thái cuối cùng.
#### 🔹 QUY TRÌNH BÁO CÁO (DAILY REPORTING)
- **Lệnh thực hiện:** `/daily-report`
- **Quy tắc điền report:**
- *Nếu có làm dự án:* Ghi rõ ràng, chi tiết tiến độ. Báo cáo dứt điểm theo từng phần (Ví dụ: hoàn tất việc của `api-qa`).
- *Nếu không có thay đổi/không làm dự án:* Ghi chú: `"None cause not update anything on repos"`.

---

## ⏳ 4. Các mục tiêu / Việc còn tồn đọng (Pending Tasks)

- [ ] `[18/08/2026]` **Kết nối Database:** Tìm hiểu cách kết nối cơ sở dữ liệu cho dự án.
- [ ] `[18/08/2026]` **Phân tích mã nguồn:** Đọc và hiểu code của `test transfer tool` và `transfer gateway`.
- [ ] `[18/08/2026]` **Kiểm thử BDD / Scenario:**
- [ ] `[18/08/2026]` **Kỹ năng Báo cáo:** Tập viết Daily Report và Test Report theo chuẩn.
- [ ] `[18/08/2026]` **Công cụ hỗ trợ (Helper Scripts):**
- [ ] `[18/08/2026]` **Thực thi:** Chạy thử nghiệm và kiểm tra toàn bộ các test cases trong phần Instruction.
- [ ] `[19/08/2026]` Thực hiện các task kiểm thử theo kế hoạch.
- [ ] `[19/08/2026]` Cập nhật kết quả test lên hệ thống.

---

## 🎯 5. Định hướng & Kế hoạch tuần tiếp theo (Next Week Focus)

- [ ] Tiếp tục thực thi và tối ưu các automation test cases.
- [ ] Rà soát các quy trình làm việc và tài liệu trên Confluence.
- [ ] 

---
*File tổng kết tuần được tự động tạo/cập nhật vào 27/08/2026 10:54:24*
