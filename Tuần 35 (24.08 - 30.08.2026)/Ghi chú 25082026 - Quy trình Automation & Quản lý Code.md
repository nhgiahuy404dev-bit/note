# Mục tiêu
Làm endpoin 
# 📝 QUY TRÌNH VIẾT AUTOMATION & QUẢN LÝ CODE
**Ngày cập nhật:** 25/08/2026

---

## 1. QUY TRÌNH VIẾT AUTOMATION TEST
Các bước cơ bản để xây dựng kịch bản tự động hóa:
1. **Đọc requirement:** Nắm rõ yêu cầu của task và nghiệp vụ bài toán.
2. **Viết prompt:** Chuẩn bị câu lệnh (prompt) rõ ràng, chi tiết.
3. **Làm việc với AI:** Yêu cầu AI kiểm tra (check) và thiết lập kịch bản (scenario).
4. **Review & Chỉnh sửa:** Kiểm tra lại kết quả do AI sinh ra và sửa chữa các điểm chưa hợp lý.
5. **Chạy thử:** Hoàn thiện kịch bản và tiến hành chạy thử nghiệm (execute test).

---

## 2. THAO TÁC VỚI TESTRAIL
Phân biệt rõ 2 câu lệnh chính khi làm việc với TestRail:
* `/create-testrail`: Chỉ tạo test case, **không** tác động hay cập nhật gì lên ticket.
* `/sync-testrail`: **Đồng bộ và cập nhật (update)** các test case trực tiếp lên ticket.

---

## 3. XỬ LÝ XÁC THỰC (AUTHORIZATION)
Khi công cụ (Visual) hiển thị popup yêu cầu "Allow":
1. Chuyển sang trình duyệt và đăng nhập vào **Jira**.
2. Quay lại trang web vừa xuất hiện khi nhấn "Allow" để xác nhận (confirm) cấp quyền kết nối.

---

## 4. QUẢN LÝ BRANCH & REVIEW CODE

### 4.1. Phân chia Branch
* **Quy tắc:** Mỗi branch chỉ làm việc cho **MỘT endpoint** duy nhất để dễ quản lý và review.

### 4.2. Thao tác Review Code
* **Lệnh thực hiện:** `/review-code`
* **Mục đích:**
  * Hỗ trợ *self-review* (tự đánh giá) và fix lỗi trước khi push code, giúp tiết kiệm thời gian cho reviewer.
  * *Lưu ý:* File `pytest.ini` là file đã được AI review và tự động tạo ra.

### 4.3. Đẩy code & Tạo tóm tắt PR
1. Tiến hành `commit` và `push` code lên remote repository.
2. Chạy lệnh `/pr summary` để AI tự động tạo phần tóm tắt cho Pull Request.

---

## 5. CẬP NHẬT PULL REQUEST (PR) LÊN GITHUB
Khi mở PR trên hệ thống Git, cần hoàn thiện:
* **Mô tả (Description):** Dán toàn bộ nội dung PR Summary đã tạo ở bước trên vào phần mô tả.
* **Bằng chứng (Evidence):** Chụp ảnh màn hình các test case đã chạy thành công (passed/OK) và đính kèm vào PR.
* **Assign Reviewer:** Chọn và gắn tên người sẽ chịu trách nhiệm review code của bạn.
