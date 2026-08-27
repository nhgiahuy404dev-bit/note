# 📊 TỔNG KẾT TUẦN 33 (10.08 - 16.08.2026)

> 📅 **Thời gian tổng kết:** 27/08/2026 10:54:24  
> 📁 **Tổng số ngày ghi chú trong tuần:** 2 ngày

---

## 🗓️ 1. Nhật ký hoạt động trong tuần (Daily Breakdown)

| Ngày | Thứ | Chủ đề chính | File ghi chú |
| :--- | :--- | :--- | :--- |
| 11/08/2026 | Thứ Ba | Main Workspace | [Ghi chú 11082026 - Main Workspace.md](./Ghi%20ch%C3%BA%2011082026%20-%20Main%20Workspace.md) |
| 15/08/2026 | Thứ Bảy | QA Fundamentals | [Ghi chú 15082026 - QA Fundamentals.md](./Ghi%20ch%C3%BA%2015082026%20-%20QA%20Fundamentals.md) |

---

## ✅ 2. Những việc đã làm trong tuần (What I Did)

### 📌 Thứ Ba (11/08/2026) - Main Workspace
- **Tạo Ticket Todo:** Kéo thả task qua Todo và cập nhật status rõ ràng.
- **Label:** Tự add các label phù hợp cho ticket.
- **Khởi động hàng ngày:** Lúc nào mở máy cũng chạy lệnh `gdd`.

---

## 📚 3. Những kiến thức & Quy trình đã học (What I Learned)

### 💡 Thứ Ba (11/08/2026) - Main Workspace
#### 🔹 📌 Quy định làm việc & Trạng thái
- **Trạng thái làm việc:** Khi `off` hoặc đi ăn trưa cần chủ động set trạng thái (status).
- **Liên lạc:** Khi có tin nhắn/message cần báo ngay cho Leader/Anh hướng dẫn.
#### 🔹 🛠 Công cụ & Môi trường (Tools & Environment)
- **Database / Data Script:** Kết nối cơ sở dữ liệu giữa môi trường **QA** và **UAT**.
- **Email Data:** Kiểm tra hằng ngày và theo dõi thường xuyên các email dữ liệu.
- **Transfer Tool:** Có một số luồng cần sử dụng Transfer Tool để test gửi/nhận email.
- **Postman:** Sử dụng `My Collection` để quản lý các API request phục vụ testing.
- **GitHub / Repository:**
- Repo chính dùng để test API.
- Repo UI: có thể tìm hiểu thêm (2 profile).
- Sử dụng repo thường xuyên hoặc tự deploy lên.
- Mỗi ngày tạo ghi chú trên repo, điền đầy đủ thông tin và note lại tiến độ.
- **Trang Fortool (Internal Button):** Mở ra 2 trang quản trị là **QA** và **Operation** (trang test chính cho tool).
- **Test Artifact:** Khi User Group cần actual data thì tiến hành tạo test artifact.
#### 🔹 ⌨️ Phím tắt & Thao tác nhanh
- `Cmd + Shift + 4` rồi `Cmd + C`: Chụp ảnh màn hình nhanh và copy vào clipboard.
- `Tô đen + Shift`: Bôi đen nhanh toàn bộ một vùng văn bản.
- `wt review`: Lệnh review workspace.

### 💡 Thứ Bảy (15/08/2026) - QA Fundamentals
#### 🔹 Phân biệt Error - Defect/Bug - Failure

| Thuật ngữ | Khái niệm cốt lõi | Ví dụ minh họa |
| :--- | :--- | :--- |
| **Error (Sai sót)** | Sai sót do con người (Dev/BA) tạo ra trong quá trình thiết kế, viết code hoặc viết requirement. | Dev code nhầm điều kiện logic, BA ghi sai requirement. |
| **Defect / Bug (Lỗi phần mềm)** | Khiếm khuyết trong phần mềm làm kết quả thực tế (**Actual**) khác với mong đợi (**Expected**). | Requirement yêu cầu 8 ký tự nhưng trường nhập chỉ cho phép 6. |
| **Failure (Sự cố vận hành)** | Hệ thống hoạt động sai lệch trong môi trường thực tế khi người dùng thao tác. | Đăng nhập đúng thông tin nhưng hệ thống báo lỗi không vào được. |

#### 🔹 🟢 Smoke Test
- **Mục tiêu:** Kiểm tra nhanh bản build/version mới có đủ độ ổn định để tiếp tục test hay không.
- **Câu hỏi cốt lõi:** *"Version này có thể test tiếp được không?"*
- **Ví dụ flow:** Mở hệ thống -> Đăng nhập -> Kiểm tra các chức năng cơ bản nhất còn chạy được không.
#### 🔹 🟡 Sanity Test
- **Mục tiêu:** Kiểm tra nhanh và sâu vào phân hệ/chức năng vừa được fix lỗi hoặc vừa được sửa đổi.
- **Câu hỏi cốt lõi:** *"Chỗ vừa sửa có hoạt động ổn định không?"*
#### 🔹 🔵 Retest / Verification Testing
- **Mục tiêu:** Kiểm tra lại chính xác lỗi đã báo trước đó xem Dev đã sửa triệt để chưa.
- **Câu hỏi cốt lõi:** *"Bug này đã thực sự được fix hết chưa?"*
- **Quy trình xử lý:**
- **Pass:** Đóng bug (*Close*).
- **Fail:** Mở lại (*Reopen*) + bình luận chi tiết + đính kèm ảnh/video bằng chứng + version + điều kiện tái hiện.
#### 🔹 🟣 Regression Test (Kiểm thử hồi quy)
- **Mục tiêu:** Kiểm tra toàn bộ các chức năng liên quan để đảm bảo việc sửa code mới không làm phát sinh lỗi ở các chức năng cũ.
- **Câu hỏi cốt lõi:** *"Sửa chỗ này có làm hỏng chỗ khác không?"*
#### 🔹 🔄 Flow quy trình kiểm thử chuẩn
> **Deploy Build mới** ➔ **Smoke Test** ➔ *(Nếu Passed)* ➔ **Sanity / Functional Test** ➔ **Retest Bug** ➔ **Regression Test** ➔ **Release**.

---

## ⏳ 4. Các mục tiêu / Việc còn tồn đọng (Pending Tasks)

- [x] *Không có task tồn đọng chưa hoàn thành từ các ngày.*

---

## 🎯 5. Định hướng & Kế hoạch tuần tiếp theo (Next Week Focus)

- [ ] Tiếp tục thực thi và tối ưu các automation test cases.
- [ ] Rà soát các quy trình làm việc và tài liệu trên Confluence.
- [ ] 

---
*File tổng kết tuần được tự động tạo/cập nhật vào 27/08/2026 10:54:24*
