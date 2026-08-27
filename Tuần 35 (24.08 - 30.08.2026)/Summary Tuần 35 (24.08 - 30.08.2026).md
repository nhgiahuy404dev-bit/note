# 📊 TỔNG KẾT TUẦN 35 (24.08 - 30.08.2026)

> 📅 **Thời gian tổng kết:** 27/08/2026 10:54:24  
> 📁 **Tổng số ngày ghi chú trong tuần:** 3 ngày

---

## 🗓️ 1. Nhật ký hoạt động trong tuần (Daily Breakdown)

| Ngày | Thứ | Chủ đề chính | File ghi chú |
| :--- | :--- | :--- | :--- |
| 25/08/2026 | Thứ Ba | Quy trình Automation & Quản lý Code | [Ghi chú 25082026 - Quy trình Automation & Quản lý Code.md](./Ghi%20ch%C3%BA%2025082026%20-%20Quy%20tr%C3%ACnh%20Automation%20%26%20Qu%E1%BA%A3n%20l%C3%BD%20Code.md) |
| 26/08/2026 | Thứ Tư | Bảng quyết định & Instruction | [Ghi chú 26082026 - Bảng quyết định & Instruction.md](./Ghi%20ch%C3%BA%2026082026%20-%20B%E1%BA%A3ng%20quy%E1%BA%BFt%20%C4%91%E1%BB%8Bnh%20%26%20Instruction.md) |
| 27/08/2026 | Thứ Năm | Chuyển Jira sang Confluence | [Ghi chú 27082026 - Chuyển Jira sang Confluence.md](./Ghi%20ch%C3%BA%2027082026%20-%20Chuy%E1%BB%83n%20Jira%20sang%20Confluence.md) |

---

## ✅ 2. Những việc đã làm trong tuần (What I Did)

### 📌 Thứ Tư (26/08/2026) - Bảng quyết định & Instruction
- Học và nghiên cứu kỹ thuật thiết kế test case bằng Decision Table để bao phủ toàn bộ tổ hợp điều kiện nghiệp vụ.
- Phân loại rõ ràng giữa bản Instruction chính thức và bản nháp (`instruction/draft`).
- Kiểm tra tính đầy đủ của các bước thực thi trước khi đưa vào automation test.

### 📌 Thứ Năm (27/08/2026) - Chuyển Jira sang Confluence
- Đồng bộ và cập nhật thông tin từ Jira Ticket sang trang tài liệu Confluence mà vẫn giữ nguyên cấu trúc (template) của Confluence.
- [TEST EXECUTION]  GTO-16043 - Fiat withdrawal UI + E2E (Transfer Tool)

---

## 📚 3. Những kiến thức & Quy trình đã học (What I Learned)

### 💡 Thứ Ba (25/08/2026) - Quy trình Automation & Quản lý Code
- Làm endpoin
#### 🔹 QUY TRÌNH VIẾT AUTOMATION TEST
- Các bước cơ bản để xây dựng kịch bản tự động hóa:
- **Đọc requirement:** Nắm rõ yêu cầu của task và nghiệp vụ bài toán.
- **Viết prompt:** Chuẩn bị câu lệnh (prompt) rõ ràng, chi tiết.
- **Làm việc với AI:** Yêu cầu AI kiểm tra (check) và thiết lập kịch bản (scenario).
- **Review & Chỉnh sửa:** Kiểm tra lại kết quả do AI sinh ra và sửa chữa các điểm chưa hợp lý.
- **Chạy thử:** Hoàn thiện kịch bản và tiến hành chạy thử nghiệm (execute test).
#### 🔹 THAO TÁC VỚI TESTRAIL
- Phân biệt rõ 2 câu lệnh chính khi làm việc với TestRail:
- `/create-testrail`: Chỉ tạo test case, **không** tác động hay cập nhật gì lên ticket.
- `/sync-testrail`: **Đồng bộ và cập nhật (update)** các test case trực tiếp lên ticket.
#### 🔹 XỬ LÝ XÁC THỰC (AUTHORIZATION)
- Khi công cụ (Visual) hiển thị popup yêu cầu "Allow":
#### 🔹 Phân chia Branch
- **Quy tắc:** Mỗi branch chỉ làm việc cho **MỘT endpoint** duy nhất để dễ quản lý và review.
#### 🔹 Thao tác Review Code
- **Lệnh thực hiện:** `/review-code`
- **Mục đích:**
- Hỗ trợ *self-review* (tự đánh giá) và fix lỗi trước khi push code, giúp tiết kiệm thời gian cho reviewer.
- *Lưu ý:* File `pytest.ini` là file đã được AI review và tự động tạo ra.
#### 🔹 CẬP NHẬT PULL REQUEST (PR) LÊN GITHUB
- Khi mở PR trên hệ thống Git, cần hoàn thiện:
- **Mô tả (Description):** Dán toàn bộ nội dung PR Summary đã tạo ở bước trên vào phần mô tả.
- **Bằng chứng (Evidence):** Chụp ảnh màn hình các test case đã chạy thành công (passed/OK) và đính kèm vào PR.
- **Assign Reviewer:** Chọn và gắn tên người sẽ chịu trách nhiệm review code của bạn.

### 💡 Thứ Năm (27/08/2026) - Chuyển Jira sang Confluence
#### 🔹 📝 Quy trình thực hiện bằng AI Prompt
- **Chuẩn bị liên kết:**
- Link Jira Ticket: `[Link Jira]`
- Link Confluence: `[Link Confluence]`
- **Mẫu Prompt chuẩn sử dụng:**
- **Cập nhật & Kiểm tra:**

---

## ⏳ 4. Các mục tiêu / Việc còn tồn đọng (Pending Tasks)

- [ ] `[26/08/2026]` **Bảng quyết định (Decision Table):**
- [ ] `[26/08/2026]` **Review Instruction:**
- [ ] `[27/08/2026]` Kiểm tra bảng Test Table trong phần Test Section trên Confluence.
- [ ] `[27/08/2026]` Đối chiếu dữ liệu giữa Jira và Confluence.
- [ ] `[27/08/2026]` Lưu và xuất bản trang tài liệu.

---

## 🎯 5. Định hướng & Kế hoạch tuần tiếp theo (Next Week Focus)

- [ ] Tiếp tục thực thi và tối ưu các automation test cases.
- [ ] Rà soát các quy trình làm việc và tài liệu trên Confluence.
- [ ] 

---
*File tổng kết tuần được tự động tạo/cập nhật vào 27/08/2026 10:54:24*
