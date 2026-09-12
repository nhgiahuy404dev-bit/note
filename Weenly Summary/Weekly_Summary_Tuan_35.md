* [Vsee - Galaxy] Weekly Summary + Demo

Attendees: Brian Pham Hau Duong (Hầu Dương) Huy Nguyễn Pháp Huỳnh Quốc Thai Huynh

* Notes

Meeting sẽ chia ra làm các phần chính như sau:

## Summary:

* List ra trong tuần rồi đã / đang làm ticket nào, progress như thế nào rồi:

  * **`QA-6702` - Automation Tests cho 2 Endpoints của Permission Service:**
    * **Đã làm:** 
      * Áp dụng đồng bộ **Quy trình chuẩn 11 bước triển khai kiểm thử tự động cho một Endpoint (Standard Flow for Endpoint Automation)**:
        1. **Create Test Scenario Prompt:** Tạo prompt cho AI đọc các test steps và sinh ra bộ Scenarios để review cho 2 endpoint mới: `/permission/transfer-details` và `/permission/validate/instruction`.
        2. **Create New Branch:** Tạo branch độc lập cho từng endpoint theo quy tắc mỗi branch một endpoint và chuyển trạng thái ticket sang `Testing`.
        3. **Complete Scenario:** Hoàn thiện kịch bản: 4 test cases cho endpoint `/permission/transfer-details` (2 Happy Path, 2 Negative cases) và 6 test cases cho endpoint `/permission/validate/instruction` (4 Happy Path, 2 Negative cases).
        4. **Review Code:** Tự review code triển khai test script bằng lệnh `/review-code` để loại bỏ các cảnh báo và lỗi cú pháp.
        5. **Run Code:** Chạy test suite automation cục bộ (Pass 100%).
        6. **Fix Code:** Sửa các lỗi phát sinh về assertion và kiểu dữ liệu trả về.
        7. **Create TestRail:** Tạo và đồng bộ các test cases lên TestRail (`/create-testrail` và `/sync-testrail`).
        8. **Commit and Push Code:** Commit với message chuẩn và push code lên remote branch.
        9. **Create PR Summary:** Chạy lệnh `/pr summary` chuẩn bị nội dung tóm tắt PR.
        10. **Create Pull Request:** Tạo PR **#1318** trên GitHub và gắn đầy đủ evidence pass test.
        11. **Update Review Status:** Theo dõi feedback từ reviewer, xử lý các comments, merge PR và chuyển status ticket sang `Under Review` rồi hoàn thành nghiệm thu.
    * **Tiến độ hiện tại:** Hoàn thành 100%, PR #1318 đã được merge thành công ✅.

  * **`QA-6741` & `QA-6742` (GTO-16043, GTO-15979) - Fiat withdrawal initiation, UI & E2E (Transfer Tool):**
    * **Đã làm:** 
      * Áp dụng **Quy trình kiểm thử Ticket thường (Standard Feature/UI Testing Workflow)** gồm 5 giai đoạn:
        1. **Read Request:** Đọc và phân tích tài liệu PRD, spec trên Jira & Confluence về tính năng rút tiền Fiat (Fiat withdrawal UI & Initiation).
        2. **Designing:** Chuyển status Jira sang `Designing`, thiết kế ma trận kịch bản kiểm thử (Test Scenario Matrix), xây dựng bảng quyết định (Decision Table) để bao phủ đầy đủ các tổ hợp điều kiện và phân biệt rõ ràng giữa bản Instruction chính thức và bản nháp (`instruction/draft`).
        3. **Testing:** Chuẩn bị sẵn sàng bộ dữ liệu kiểm thử và câu lệnh SQL query để sẵn sàng test khi môi trường staging deploy code.
        4. **Pass Test:** Đang trong quá trình hoàn thiện thiết kế kịch bản.
        5. **Create PR:** Sẽ tạo PR khi hoàn tất kiểm thử thực tế.
    * **Tiến độ hiện tại:** In Progress (Đang ở trạng thái Designing, hoàn thành thiết kế kịch bản kiểm thử).

  * **Quy trình Chuẩn hóa Tài liệu Jira sang Confluence:**
    * **Đã làm:** Chuẩn hóa quy trình chuyển giao dữ liệu từ Jira Ticket sang Confluence: bảo toàn nguyên vẹn cấu trúc template Confluence, đối chiếu bảng kiểm thử (**Test Table**) trong phần **Test Section**, rà soát tính nhất quán dữ liệu giữa 2 hệ thống trước khi Publish.
    * **Tiến độ hiện tại:** Đã hoàn tất và lưu vào tài liệu hướng dẫn nội bộ.

* Demo feature đã / đang làm:

  * **Demo 1: Trình diễn Flow chuẩn triển khai Endpoint Automation cho Permission Service (`QA-6702`):**
    * Trình diễn toàn bộ chu trình 11 bước từ tạo Scenario bằng AI, tách branch độc lập, thực thi test suite pass 100%, cập nhật TestRail đến mở PR #1318 và xử lý review feedback.
    * Trình diễn bộ test tự động kiểm thử 2 endpoint: `/permission/transfer-details` (4 cases) và `/permission/validate/instruction` (6 cases).
  * **Demo 2: Thiết kế Bảng Quyết định (Decision Table) cho luồng Fiat Withdrawal (`QA-6741` & `QA-6742`):**
    * Trình diễn phương pháp bóc tách tổ hợp điều kiện bằng Decision Table, phân biệt lệnh chuyển tiền chính thức và lệnh nháp, cùng quy trình chuẩn đồng bộ tài liệu sang Confluence.

## Knowledge Sharing:

* Pick ra 1 topic trong feature mình đã làm để sharing knowledge (UI):

  * **Kỹ thuật thiết kế Ma trận Bảng Quyết định (Decision Table) & Quy trình Code Tracing 4 tầng:**
    * **Chủ đề lựa chọn:** Phương pháp bao phủ kịch bản kiểm thử bằng Decision Table cho luồng nghiệp vụ phức tạp và Kỹ thuật lần vết mã nguồn 4 tầng (Code Tracing Workflow) phục vụ viết Automation Test.
    * **1. Kỹ thuật thiết kế Test Cases bằng Decision Table:**
      * **Bản chất:** Sử dụng bảng ma trận tổ hợp giữa các điều kiện đầu vào (Conditions) và kết quả hành động mong đợi (Actions/Outputs).
      * **Ứng dụng cho Fiat Withdrawal:** Phân biệt rõ giữa tài khoản thụ hưởng Whitelist vs Non-whitelist, lệnh có phê duyệt (`approval_required = true`) vs không phê duyệt, và lệnh chính thức vs bản nháp (`draft`). Giúp tránh bỏ sót các ca kiểm thử biên và trường hợp ngoại lệ.
    * **2. Quy trình Code Tracing 4 tầng (4-Tier Code Tracing):**
      * *Tầng 1 (API Layer):* Bắt endpoint, method và contract dữ liệu request/response payload.
      * *Tầng 2 (Service Layer):* Lần vết business logic, các bước xử lý dữ liệu và kiểm tra quyền hạn (permission checks).
      * *Tầng 3 (References Layer):* Kiểm tra các module, dependencies và service phụ thuộc (Kafka, Redis, Notification).
      * *Tầng 4 (Database Layer):* Xác định chính xác các bảng dữ liệu bị tác động, phục vụ viết câu truy vấn SQL assert dữ liệu động đa môi trường.

* Cách apply AI trong công việc:

  * **Quy trình ứng dụng thực chiến:** **Input → AI Hỗ trợ → QA Đánh giá & Rà soát → Kết quả cuối cùng**
    1. **Input:** Tài liệu đặc tả endpoint mới của Permission service và mã nguồn Backend liên quan.
    2. **AI Hỗ trợ:** Sử dụng AI hỗ trợ thực hiện Code Tracing 4 tầng, sinh các test cases dạng BDD Gherkin với từ khóa tái sử dụng cao, và đề xuất các assertion kiểm tra cơ sở dữ liệu.
    3. **QA Đánh giá & Rà soát:** QA rà soát tính hợp lệ của câu lệnh truy vấn database, tự chạy lệnh `/review-code` để rà soát lỗi logic và chuẩn hóa assertion trước khi push code.
    4. **Kết quả cuối cùng:** Test suite hoàn thiện, pass 100% kiểm thử cục bộ và PR #1318 được merge thành công.

* Cách test regression tests và scope cần test trong regression tests:

  * **Phương pháp xác định phạm vi Regression khi test ticket enhancement:**
    * **Xác định các điểm chạm dùng chung (Shared Seams):** Khi cập nhật logic kiểm tra quyền của Permission Service (`validate/instruction`), các endpoint liên quan đến transfer hay order routing đều có nguy cơ bị ảnh hưởng.
    * **Phân tách rõ vùng ảnh hưởng:** Chạy toàn bộ regression suite của module Permission trước, sau đó kích hoạt regression kiểm tra các luồng transfer cơ bản để đảm bảo không xảy ra hiện tượng chặn nhầm lệnh hợp lệ.
    * **Ngưỡng chặn hồi quy (Regression Gate):** Không có bất kỳ test case nào bị fail (100% Passed) trên môi trường tích hợp thì mới được phép release.

Cách test ticket enhancement của dev và regression scope mình cần làm tương ứng.

Action items:

* Tiếp tục theo dõi tiến độ chuẩn bị môi trường và deploy code Backend/Frontend cho tính năng Fiat Withdrawal (`GTO-16043`, `GTO-15979`).
* Hoàn thiện chi tiết kịch bản kiểm thử End-to-End và các kịch bản UI guard cho giao diện rút tiền Fiat (`QA-6742`).
* Chuẩn bị sẵn sàng bộ test data và câu lệnh truy vấn SQL cho đợt kiểm thử tích hợp tiếp theo.
