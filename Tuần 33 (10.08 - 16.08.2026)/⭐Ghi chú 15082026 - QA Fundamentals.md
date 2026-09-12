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

## 3. Phân biệt Verification (Xác minh) và Validation (Xác thực)

> [!TIP]
> **Quy tắc vàng ghi nhớ (Barry Boehm):**
> - **Verification:** *"Are we building the product right?"* (Chúng ta có đang xây dựng sản phẩm đúng cách / đúng thiết kế không?)
> - **Validation:** *"Are we building the right product?"* (Chúng ta có đang xây dựng đúng sản phẩm mà người dùng thực sự cần không?)

### 📊 Bảng so sánh chi tiết giữa Verification & Validation

| Tiêu chí | Verification (Xác minh) | Validation (Xác thực / Thẩm định) |
| :--- | :--- | :--- |
| **Định nghĩa** | Quá trình kiểm tra xem phần mềm có tuân thủ đúng các đặc tả thiết kế, kiến trúc và yêu cầu kỹ thuật ban đầu hay không. | Quá trình đánh giá xem sản phẩm hoàn thiện có đáp ứng đúng nhu cầu thực tế và mong đợi của người dùng cuối hay không. |
| **Bản chất kiểm thử** | **Static Testing (Kiểm thử tĩnh)**: Không cần thực thi hoặc chạy mã nguồn. | **Dynamic Testing (Kiểm thử động)**: Bắt buộc phải chạy ứng dụng/mã nguồn để quan sát hành vi thực tế. |
| **Các hoạt động chính** | Reviews tài liệu, Walkthroughs, Inspections, Code Review, Static Analysis. | Functional Testing, System Testing, API/UI Testing, UAT (User Acceptance Testing). |
| **Đối tượng kiểm tra** | Tài liệu SRS, bản thiết kế kiến trúc, Database schema, mã nguồn (Code). | Phần mềm/bản build thực tế đang vận hành trên môi trường test/staging/production. |
| **Thời điểm thực hiện** | Diễn ra sớm ngay từ các giai đoạn đầu (Phân tích yêu cầu, Thiết kế, Viết code). | Diễn ra sau khi đã có bản build phần mềm hoàn chỉnh hoặc từng module chạy được. |
| **Ai thực hiện?** | Dev, QA, Tech Lead, BA (thông qua review tài liệu và code). | Đội ngũ QA/QC, Product Owner, End User, Khách hàng (trong các đợt UAT). |
| **Mục tiêu cốt lõi** | Ngăn ngừa lỗi phát sinh từ sớm (**Bug Prevention**). | Phát hiện và bắt lỗi khi phần mềm đang chạy (**Bug Detection**). |

---

## 🔄 Flow quy trình kiểm thử chuẩn
> **Deploy Build mới** ➔ **Smoke Test** ➔ *(Nếu Passed)* ➔ **Sanity / Functional Test** ➔ **Retest Bug** ➔ **Regression Test** ➔ **Release**.
