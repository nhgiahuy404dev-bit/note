# 📝 QUY TRÌNH VIẾT AUTOMATION & QUẢN LÝ CODE
**Ngày cập nhật:** 25/08/2026

---

## 1. QUY TRÌNH CHUẨN 15 BƯỚC VIẾT AUTOMATION TEST (WORKFLOW 1)
Áp dụng cho các ticket có tag `[API-QA]`, `endpoint`, `parsing`, hoặc `automation BE`:

1. **Create Test Scenario Prompt:** Tạo prompt AI đọc test steps / API spec để tự động sinh Scenarios cho endpoints/logic cần test (Happy Path, Negative, Boundary, Adverse).
2. **Create New Branch:** Tạo branch độc lập `<branch-name>-<endpoint>` từ `main`, chuyển status Jira sang `In Project`. *(Quy tắc 1 branch - 1 endpoint)*.
3. **Complete Scenario:** Rà soát và hoàn thiện kịch bản kiểm thử (preconditions, headers, payload, response assertions) trước khi code.
4. **Review Code:** Tự review code test script, fixtures, auth headers. Nếu test tương tác Database bắt buộc gọi `load_dotenv()` ở đầu file.
5. **Run Code:** Thực thi chạy bộ test suite automation trên môi trường cục bộ đảm bảo **Pass 100%**.
6. **Fix Code:** Sửa các lỗi phát sinh về assertion, xử lý ngoại lệ và kiểu dữ liệu trả về từ parser.
7. **Create TestRail:** Dùng `/create-testrail` để tạo mới test cases trên TestRail và `/sync-testrail` để đồng bộ ID test cases trực tiếp lên Jira ticket.
8. **Run Review Code:** Chạy lại toàn bộ test suite sau khi tạo TestRail để đảm bảo không có regression (Pass 100%).
9. **Check Orphan Functions:** Kiểm tra và dọn dẹp các hàm mồ côi (orphan functions) sau khi hoàn thành bằng lệnh `/review-code`.
10. **Kiểm tra model Pydantic:** Rà soát lại toàn bộ model Pydantic đảm bảo khớp 100% với response schema thực tế, không bị thiếu trường hoặc crash type.
11. **Commit and Push Code:** Commit với message chuẩn convention và push code lên remote branch.
12. **Create PR Summary:** Chạy slash command `/pr summary` để AI tự động tạo phần tóm tắt cho Pull Request.
13. **Create Pull Request:** Tạo PR trên GitHub vào nhánh `main`, dán nội dung PR summary, đính kèm evidence test Pass 100% và gán reviewer (**Dastan**).
14. **Update Review Status:** Gán link PR vào Jira ticket và chuyển trạng thái ticket sang **`Under Review`**.
15. **Request Review & Merge ➔ `Done` ✅:** Đưa cho **Dastan** review PR, xử lý feedback qua `/resolve-pr`, nhận approval và merge vào nhánh chính; chuyển Jira sang **`Done`** ✅.

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
