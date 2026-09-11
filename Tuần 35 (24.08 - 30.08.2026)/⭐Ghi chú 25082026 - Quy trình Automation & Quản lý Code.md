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

## 2. THAO TÁC VỚI TESTRAIL & CẬP NHẬT TICKET
1. **Kết nối Jira Data:** Trước khi chạy sync, đảm bảo đã xác thực và kết nối dữ liệu từ **Jira** để lấy đầy đủ context của ticket.
2. **Các câu lệnh chính khi làm việc với TestRail:**
   * `/create-testrail`: Chỉ tạo test case, **không** tác động hay cập nhật gì lên ticket.
   * `/sync-testrail`: **Đồng bộ và cập nhật (update)** các test case trực tiếp lên ticket.
3. **Chụp ảnh Pass Test (Evidence):** Chụp ảnh màn hình kết quả chạy test thành công (passed 100%) và đính kèm trực tiếp vào **Jira Ticket**.
4. **Cập nhật trạng thái Ticket (Jira Status):** Khi đã hoàn thành viết test, chạy pass 100% và mở PR, tiến hành chuyển trạng thái (**Status**) của Jira Ticket từ **`In Progress`** sang **`Under Review`** để báo hiệu cho Reviewer/Leader tiến hành kiểm tra.

---

## 3. QUẢN LÝ BRANCH & REVIEW CODE

### 3.1. Phân chia Branch
* **Quy tắc:** Mỗi branch chỉ làm việc cho **MỘT endpoint** duy nhất để dễ quản lý và review.

### 3.2. Thao tác Review Code
* **Lệnh thực hiện:** `/review-code`
* **Mục đích:**
  * Hỗ trợ *self-review* (tự đánh giá) và fix lỗi trước khi push code, giúp tiết kiệm thời gian cho reviewer.
  * *Lưu ý:* File `pytest.ini` là file đã được AI review và tự động tạo ra.

### 3.3. Đẩy code & Tạo tóm tắt PR
1. Tiến hành `commit` và `push` code lên remote repository.
2. Chạy lệnh `/pr summary` để AI tự động tạo phần tóm tắt cho Pull Request.

---

## 4. CẬP NHẬT PULL REQUEST (PR) LÊN GITHUB & RESOLVE REVIEW

### 4.1. Mở Pull Request
Khi mở PR trên hệ thống Git, cần hoàn thiện:
* **Mô tả (Description):** Dán toàn bộ nội dung PR Summary đã tạo ở bước trên vào phần mô tả.
* **Bằng chứng (Evidence):** Chụp ảnh màn hình các test case đã chạy thành công (passed/OK) và đính kèm vào PR.
* **Assign Reviewer:** Chọn và gắn tên người sẽ chịu trách nhiệm review code của bạn.
* **Cập nhật trạng thái Jira:** Đính kèm link PR vào Jira ticket và chuyển trạng thái ticket sang **`Under Review`**.

### 4.2. Xử lý phản hồi Review (`/resolve-pr`)
* Khi Reviewer để lại nhận xét (comment) hoặc yêu cầu sửa đổi trên PR:
  1. Tiến hành sửa code theo feedback.
  2. Commit và push các thay đổi mới lên branch.
  3. Sử dụng lệnh **`/resolve-pr`** (hoặc Resolve Conversation) để đóng các luồng comment đã được xử lý xong, báo hiệu cho Reviewer biết code đã sẵn sàng để Approve và Merge.

---

> [!NOTE]
> **Lưu ý phụ (Xác thực Authorization):** Khi công cụ hiển thị popup yêu cầu *"Allow"*, chỉ cần đăng nhập **Jira** trên trình duyệt rồi quay lại trang web xác nhận cấp quyền kết nối.
