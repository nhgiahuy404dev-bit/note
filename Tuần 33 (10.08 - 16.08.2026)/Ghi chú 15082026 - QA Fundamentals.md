# Ghi chú ngày 15/08/2026 (Thứ Bảy) - Kiến thức nền tảng QA Testing

---

## 1. Phân biệt Error - Defect/Bug - Failure

| Thuật ngữ | Khái niệm cốt lõi | Ví dụ minh họa |
| :--- | :--- | :--- |
| **Error (Sai sót)** | Sai sót do con người (Dev/BA) tạo ra trong quá trình thiết kế, viết code hoặc viết requirement. | Dev code nhầm điều kiện logic, BA ghi sai requirement. |
| **Defect / Bug (Lỗi phần mềm)** | Khiếm khuyết trong phần mềm làm kết quả thực tế (**Actual**) khác với mong đợi (**Expected**). | Requirement yêu cầu 8 ký tự nhưng trường nhập chỉ cho phép 6. |
| **Failure (Sự cố vận hành)** | Hệ thống hoạt động sai lệch trong môi trường thực tế khi người dùng thao tác. | Đăng nhập đúng thông tin nhưng hệ thống báo lỗi không vào được. |

---

## 2. Các cấp độ & Loại hình kiểm thử quan trọng

### 🟢 Smoke Test
* **Mục tiêu:** Kiểm tra nhanh bản build/version mới có đủ độ ổn định để tiếp tục test hay không.
* **Câu hỏi cốt lõi:** *"Version này có thể test tiếp được không?"*
* **Ví dụ flow:** Mở hệ thống -> Đăng nhập -> Kiểm tra các chức năng cơ bản nhất còn chạy được không.

### 🟡 Sanity Test
* **Mục tiêu:** Kiểm tra nhanh và sâu vào phân hệ/chức năng vừa được fix lỗi hoặc vừa được sửa đổi.
* **Câu hỏi cốt lõi:** *"Chỗ vừa sửa có hoạt động ổn định không?"*

### 🔵 Retest / Verification Testing
* **Mục tiêu:** Kiểm tra lại chính xác lỗi đã báo trước đó xem Dev đã sửa triệt để chưa.
* **Câu hỏi cốt lõi:** *"Bug này đã thực sự được fix hết chưa?"*
* **Quy trình xử lý:**
  * **Pass:** Đóng bug (*Close*).
  * **Fail:** Mở lại (*Reopen*) + bình luận chi tiết + đính kèm ảnh/video bằng chứng + version + điều kiện tái hiện.

### 🟣 Regression Test (Kiểm thử hồi quy)
* **Mục tiêu:** Kiểm tra toàn bộ các chức năng liên quan để đảm bảo việc sửa code mới không làm phát sinh lỗi ở các chức năng cũ.
* **Câu hỏi cốt lõi:** *"Sửa chỗ này có làm hỏng chỗ khác không?"*

---

## 🔄 Flow quy trình kiểm thử chuẩn
> **Deploy Build mới** ➔ **Smoke Test** ➔ *(Nếu Passed)* ➔ **Sanity / Functional Test** ➔ **Retest Bug** ➔ **Regression Test** ➔ **Release**.
