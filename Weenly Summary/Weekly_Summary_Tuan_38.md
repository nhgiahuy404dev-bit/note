* [Vsee - Galaxy] Weekly Summary + Demo

Attendees: Brian Pham Hau Duong (Hầu Dương) Huy Nguyễn Pháp Huỳnh Quốc Thai Huynh

* Notes

Meeting sẽ chia ra làm các phần chính như sau:

## Summary:

* List ra trong tuần rồi đã / đang làm ticket nào, progress như thế nào rồi:

### 📊 Bảng tổng hợp các Ticket trong tuần (Ticket Summary)

| STT | Ticket ID | Nội dung công việc | Phân loại | Thời gian | Trạng thái (Jira) | Ghi chú / Kết quả |
| :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| 1 | `QA-6916` | Enhance Slack Notification on Jenkins When Having Re-run | Code Enhancement | 14/09/2026 | **`Done`** ✅ | PR merged thành công sau review |
| 2 | `QA-5920`<br><sub>(GTO-15111)</sub> | Automation BE: Pending & History API endpoints | Endpoint Automation | 15/09/2026 | **`Done`** ✅ | Test suite Pass 100%, TestRail đầy đủ, PR merged |
| 3 | `QA-5915`<br><sub>(GTO-15105)</sub> | Automate BE: Poller Entity/Strategy Parsing | Endpoint Automation | 15/09 - 16/09/2026 | **`Done`** ✅ | Phủ toàn bộ parser sàn, PR merged |
| 4 | `GTO-16224` | Enable Datadog APM on transfer-gateway services | Test Execution | 16/09/2026 | **`Pass Test`** ✅ | Nghiệm thu Staging đạt 100% Passed qua Datadog APM |
| 5 | `QA-6885`<br><sub>(GTO-16167,<br>GTO-16282)</sub> | Alert on Transfer Tool when instruction are pending approval | UI & E2E Testing | 17/09 - 18/09/2026 | **`Pass Test`** ✅ | Hoàn tất 13 TCs + 1 RT trên Staging, Pass Test 100% |

---

### Chi tiết tiến độ từng ticket:

### 🎯 `QA-6916` - Enhance Slack Notification on Jenkins When Having Re-run (14/09/2026)

* **Loại công việc:** Code Enhancement / Fix logic trên Jenkins.
* **Trạng thái / Tiến độ:** Hoàn tất triển khai, kiểm thử CLI, review và merge PR ➔ **`Done`** ✅.
* **Ngày hoàn thành:** 14/09/2026 (Thứ Hai).
* **Branch:** `QA-6916-enhance-slack-notification-rerun`
* **Chi tiết thực hiện:**
  1. **Create New Branch:** Tạo branch độc lập `QA-6916-enhance-slack-notification-rerun` từ `main`, chuyển trạng thái Jira sang `Testing`.
  2. **Modify / Enhance Code:** Chỉnh sửa code logic đọc, gom và tổng hợp chính xác dữ liệu khi có nhiều file kết quả (`multi-file results`) trong các lượt re-run trên Jenkins, đảm bảo thông báo gửi về Slack phản ánh đúng toàn bộ kết quả test.
  3. **Review Code:** Tự rà soát và review lại các đoạn code xử lý parsing và aggregation dữ liệu.
  4. **Run Code / Test via Command:** Chạy test script qua command line (CLI) với dữ liệu multi-file results để kiểm tra logic tổng hợp và định dạng thông báo gửi về kênh Slack.
  5. **Fix Code:** Khắc phục triệt để các lỗi phát sinh về format payload và message Slack.
  6. **Commit and Push Code:** Commit đúng chuẩn convention và push code lên remote branch.
  7. **Create PR Summary:** Soạn thảo bản tóm tắt nội dung thay đổi của PR.
  8. **Create Pull Request:** Tạo Pull Request trên GitHub vào repository tương ứng.
  9. **Update Review Status:** Cập nhật trạng thái ticket Jira sang **`Under Review`**.
  10. **Request Review & Merge:** Đưa **Dastan** review PR, nhận approval và hoàn tất merge code vào nhánh chính; đóng ticket Jira sang **`Done`** ✅.

### 🎯 `QA-5920` (GTO-15111) - Automation BE: Pending & History API endpoints (15/09/2026)

* **Loại công việc:** Endpoint Automation Testing (Workflow 1 - 15 bước chuẩn).
* **Trạng thái / Tiến độ:** Hoàn tất bộ test suite tự động, review và merge PR ➔ **`Done`** ✅.
* **Ngày hoàn thành:** 15/09/2026 (Thứ Ba).
* **Branch:** `QA-5920-pending-history-endpoints`
* **Chi tiết thực hiện (Theo quy trình chuẩn 15 bước Endpoint Automation):**
  1. **Create Test Scenario Prompt:** Tạo prompt yêu cầu AI phân tích test steps và tự động sinh Scenarios cho endpoints Pending & History.
  2. **Create New Branch:** Tạo branch độc lập `QA-5920-pending-history-endpoints` và chuyển status ticket sang `In Project`.
  3. **Complete Scenario:** Rà soát và hoàn thiện các kịch bản kiểm thử (Happy Path, Negative Cases, Schema validation) trước khi viết code.
  4. **Review Code:** Tự review code triển khai test script và các câu lệnh assertions.
  5. **Run Code:** Chạy test suite automation cục bộ (Pass 100%).
  6. **Fix Code:** Sửa các lỗi phát sinh về assertion và kiểu dữ liệu trả về.
  7. **Create TestRail:** Tạo và cập nhật đầy đủ test cases lên hệ thống TestRail.
  8. **Run Review Code:** Chạy lại toàn bộ test suite sau khi tạo TestRail để đảm bảo không bị regression (Pass 100%).
  9. **Check Orphan Functions:** Kiểm tra và dọn dẹp các orphan functions sau khi hoàn thành bằng lệnh `/review-code`.
  10. **Kiểm tra model Pydantic:** Rà soát lại toàn bộ model Pydantic đảm bảo khớp 100% với response API thực tế.
  11. **Commit and Push Code:** Commit với message chuẩn và push code lên remote branch.
  12. **Create PR Summary:** Soạn thảo bản tóm tắt nội dung PR.
  13. **Create Pull Request:** Tạo PR trên GitHub vào nhánh `main`.
  14. **Update Review Status:** Cập nhật trạng thái ticket Jira sang **`Under Review`**.
  15. **Request Review & Merge:** Đưa **Dastan** review PR, nhận approval và hoàn tất merge vào `main`; chuyển Jira sang **`Done`** ✅.

### 🎯 `QA-5915` (GTO-15105) - Automate BE: Poller Entity/Strategy Parsing (15/09 - 16/09/2026)

* **Loại công việc:** Endpoint Automation Testing (Workflow 1 - 15 bước chuẩn).
* **Trạng thái / Tiến độ:** Hoàn tất triển khai kiểm thử tự động, review và merge PR ➔ **`Done`** ✅.
* **Thời gian thực hiện:** 15/09 - 16/09/2026.
* **Branch:** `QA-5915-poller-entity-strategy-parsing`
* **Chi tiết thực hiện (Theo quy trình chuẩn 15 bước Endpoint Automation):**
  1. **Create Test Scenario Prompt:** Tạo prompt yêu cầu AI phân tích test steps và tự động sinh Scenarios cho Poller Entity/Strategy Parsing (Kraken, Coinbase, Bullish, Bitstamp).
  2. **Create New Branch:** Tạo branch độc lập `QA-5915-poller-entity-strategy-parsing` và chuyển status ticket sang `In Project`.
  3. **Complete Scenario:** Rà soát và hoàn thiện các kịch bản kiểm thử: Strategy Parsing (chọn đúng Polling Strategy theo từng sàn), Entity Parsing (bóc tách và chuẩn hóa response payload sang entity nội bộ `status`, `s_unique_ref`, fee, timestamps), và Adverse Responses (Kraken trả HTTP 200 kèm error array, timeout mạng, lỗi HTTP 4xx/5xx).
  4. **Review Code:** Tự review code triển khai test script và các câu lệnh assertions.
  5. **Run Code:** Chạy test suite automation cục bộ (Pass 100%).
  6. **Fix Code:** Khắc phục triệt để các lỗi phát sinh về assertion và kiểu dữ liệu trả về từ parser.
  7. **Create TestRail:** Tạo và cập nhật đầy đủ test cases lên hệ thống TestRail.
  8. **Run Review Code:** Chạy lại toàn bộ test suite sau khi tạo TestRail để đảm bảo không bị regression (Pass 100%).
  9. **Check Orphan Functions:** Kiểm tra và dọn dẹp các orphan functions sau khi hoàn thành bằng lệnh `/review-code`.
  10. **Kiểm tra model Pydantic:** Rà soát lại toàn bộ model Pydantic của Poller response đảm bảo khớp schema 100%, không crash do thiếu trường hoặc sai kiểu dữ liệu.
  11. **Commit and Push Code:** Commit với message chuẩn convention và push code lên remote branch.
  12. **Create PR Summary:** Soạn thảo bản tóm tắt nội dung thay đổi của PR.
  13. **Create Pull Request:** Tạo PR trên GitHub vào nhánh `main`.
  14. **Update Review Status:** Cập nhật trạng thái ticket Jira sang **`Under Review`**.
  15. **Request Review & Merge:** Đưa **Dastan** review PR, nhận feedback approval và hoàn tất merge code vào nhánh chính; chuyển Jira sang **`Done`** ✅.

### 🎯 `GTO-16224` - Enable Datadog APM on transfer-gateway services (16/09/2026)

* **Loại công việc:** Test Execution / Feature Enhancement (Workflow 2 - 5 giai đoạn).
* **Trạng thái / Tiến độ:** Hoàn tất giai đoạn Designing, Test Artifact và thực thi nghiệm thu Staging ➔ **`Pass Test`** ✅.
* **Ngày thực hiện:** 16/09/2026 (Thứ Tư).
* **Chi tiết thực hiện (Theo quy trình chuẩn 5 giai đoạn):**
  1. **Read Request:** Phân tích yêu cầu kích hoạt Datadog APM (Application Performance Monitoring) trên service `transfer-gateway` nhằm giám sát hiệu năng thời gian thực (Distributed Tracing, Metrics, Latency P95/P99) ➔ Cập nhật Jira sang **`In Progress`**.
  2. **Designing:** Chuyển status Jira sang **`Designing`** ➔ Thiết kế bộ kịch bản kiểm thử toàn diện: Service Health Check sau inject `dd-trace`; Distributed Tracing & Context Propagation (`x-datadog-trace-id`, `traceparent`); Error & Exception Tracing (`error: 1`); Log-to-Trace Correlation (`dd.trace_id`, `dd.span_id`); Gateway Regression Test (overhead < 5ms). Chuẩn hóa Description, chạy lệnh `/create-test-artifact` để đồng bộ Confluence và gửi Dev chốt Test Section trên Slack.
  3. **Testing:** Chuyển status Jira sang **`Testing`** khi Dev deploy Staging ➔ Thực thi kiểm thử trực tiếp trên Datadog UI và hệ thống (xác nhận Flame Graph thông suốt, headers truyền đúng).
  4. **Pass Test:** Kiểm thử đạt chuẩn 100% Passed (không đứt đoạn trace, overhead < 5ms) ➔ Chuyển Jira sang **`Pass Test`**, đánh dấu hoàn thành ✅.
  5. **Create PR & Sign-off:** Xác nhận kết quả nghiệm thu với Dev và các reviewer chính (**Mohit**, **Dastan**, **Sandeep**).

### 🎯 `QA-6885` [GTO-16167] [GTO-16282] - Alert on Transfer Tool when instruction are pending approval (17/09 - 18/09/2026)

* **Loại công việc:** Test Execution / UI & E2E Testing (Workflow 2 - Quy trình chuẩn có Pre-check).
* **Trạng thái / Tiến độ:** Hoàn tất thực thi kiểm thử trên Staging (13 Test Cases + 1 Regression Test đạt 100% Passed) ➔ **`Pass Test`** ✅.
* **Thời gian thực hiện:** 17/09 - 18/09/2026.
* **Chi tiết thực hiện (Theo quy trình chuẩn kèm Pre-check Dastan):**
  0. **Pre-check with Dastan (Chống duplicate):** Trao đổi trực tiếp với Dastan trên Slack trước khi tạo draft ticket / test cases để đảm bảo không bị trùng lặp dữ liệu trên Jira & TestRail.
  1. **Read Request & Create Draft:** Đọc và phân tích kỹ tài liệu yêu cầu Jira (`QA-6885`, `GTO-16167`, `GTO-16282`), Confluence spec; chạy lệnh `/create-draft-test-execution` để AI sinh kịch bản nháp ➔ Cập nhật Jira sang **`In Progress`**.
  2. **Designing:** Chuyển status Jira sang **`Designing`** ➔ Rà soát kịch bản trên VS Code, chuẩn hóa Description (ghi rõ Endpoint `GET /ui/instruction/approvals/count`) và chạy `/create-test-artifact` đồng bộ Confluence.
  3. **Testing on Staging & Sign-off Pass Test:** Chuyển status Jira sang **`Testing`** khi Dev deploy Staging ➔ Thực thi kiểm thử 13 TCs + 1 RT đạt 100% Passed ➔ Nghiệm thu (Sign-off) và chuyển Jira sang **`Pass Test`** ✅, tag reviewer (**Dastan**, **Mohit**, **Sandeep**).
  4. **Dev Review:** Nghiệm thu hoàn tất ticket xong, nhắn tin Slack gửi link Jira để Dev review xác nhận.
  5. **Create TestRail:** Sau khi Dev review OK xong, chạy `/Create-testrail-cases-from-confluence` sinh file markdown draft test cases, rồi chạy `/Create-TR-Run-From-TR-Draft` tạo Test Run TestRail (Suite UI 946 & Suite E2E 947) và lưu evidence.



* Demo feature đã / đang làm:

  * **Demo 1: Trình diễn Cơ chế Alert Nav Badge & Polling Gate trên Transfer Tool (`QA-6885`):**
    * Trình diễn hiển thị Badge màu đỏ inline bên phải nhãn "Transfer Tool" trên Global Navigation Bar ở mọi trang trong hệ thống (Trading, Live Risk, Blotter).
    * Trình diễn tính năng đếm chính xác (1 - 9) và cap `9+` với container cố định 18px, hoàn toàn không làm giật vị trí thanh Nav.
    * Trình diễn cơ chế Optimistic UI: Khi User Approver click Approve/Reject, số lượng badge lập tức giảm hoặc ẩn ngay mà không cần đợi chu kỳ polling 60 giây.
    * Trình diễn Polling Gate trên tab Network: User có quyền gọi đều đặn 60s; User không có quyền gọi 1 lần nhận `eligible: false` và dừng hẳn.
  * **Demo 2: Trình diễn Bộ Test Automation Poller Entity/Strategy Parsing (`QA-5915`):**
    * Trình diễn bộ test automation chạy pass 100% kiểm tra bóc tách và chuẩn hóa dữ liệu từ các sàn đối tác (Kraken, Coinbase, Bullish, Bitstamp).
    * Trình diễn xử lý kịch bản ngoại lệ: Sàn Kraken trả HTTP 200 nhưng body chứa mảng error được parser bắt chính xác và map trạng thái `FAILED`.
  * **Demo 3: Trình diễn Quy trình Test Execution Chuẩn kết hợp AI Slash Commands:**
    * Trình diễn quy trình khép kín: Pre-check với Dastan chống duplicate ➔ Khởi tạo Draft qua Claude (`/create-draft-test-execution`) ➔ Review trên VS Code ➔ Chuẩn hóa Jira & Tạo Test Artifact (`/create-test-artifact`) ➔ Testing & Nghiệm thu Pass Test ➔ Gửi Dev Review ➔ Tạo Test Run TestRail (`/Create-TR-Run-From-TR-Draft`).

## Knowledge Sharing:

* Pick ra 1 topic trong feature mình đã làm để sharing knowledge (UI):

  * **Transfer tool manage permission & Alert on Transfer Tool (Nav Badge & Polling Gate):**
    * **Chủ đề lựa chọn:** Chiến lược kiểm thử UI/E2E cho cơ chế Nav Badge cảnh báo lệnh Pending Approval (`QA-6885`) và Kỹ thuật kiểm thử Polling Gate.
    * **1. Bài toán thực tế & Thách thức kiểm thử (Challenges & Approach):**
      * *Hiển thị đồng bộ đa trang (Cross-page rendering):* Badge nằm trên Global Nav Bar nên phải xuất hiện chính xác ở tất cả các trang của hệ thống (Trading, Live Risk, Blotter...) ngay từ lần render đầu tiên mà không yêu cầu người dùng phải reload trang.
      * *Tránh giật giao diện (Preventing Layout Shifts):* Khi số đếm chuyển đổi từ 1 chữ số sang dạng `9+`, container badge phải có min-width cố định (18px) để không làm co giãn hoặc xê dịch các menu item lân cận trên thanh điều hướng.
      * *Đảm bảo tính tức thì (Optimistic UI / Event-driven):* Nếu chỉ dựa vào chu kỳ poll 60s, sau khi Approver duyệt lệnh xong thì badge vẫn sẽ hiển thị số cũ trong tối đa 60 giây tiếp theo, gây hiểu nhầm rằng lệnh chưa được duyệt. Do đó, FE phải áp dụng Optimistic UI để trừ ngay số đếm trên badge ngay khi user click nút Approve/Reject.
    * **2. Cơ chế Polling Gate & Quản lý Network Calls (Resource Optimization):**
      * Endpoint: `GET /ui/instruction/approvals/count`.
      * *Gating phân quyền:*
        * User hoàn toàn không có quyền vào Transfer Tool: **0 network calls**.
        * User vào được Transfer Tool nhưng không có quyền duyệt lệnh: Gọi duy nhất **1 lần** lúc khởi tạo, BE trả về `eligible: false` ➔ FE hủy interval và dừng hẳn polling.
        * User đang có quyền nhưng bị thu hồi giữa chừng: Call tiếp theo nhận `eligible: false` ➔ Clear interval ngay lập tức.
      * *Silent Error Handling:* Khi API count gặp sự cố mạng hoặc trả về mã lỗi 500/503/Timeout, hệ thống giữ nguyên trạng thái cũ hoặc ẩn badge nhẹ nhàng, tuyệt đối không hiển thị popup/toast lỗi làm phiền người dùng.
    * **3. Phân tầng kiểm thử & Phân quyền Test Fixtures (Testing Scoping & Roles):**
      * Thiết lập ma trận 5 User Fixtures (User A - Initiator, User B - Approver, User C - Viewer, User D - Second Approver, User E - Restricted).
      * *Quy tắc Scoping quan trọng:*
        * Lệnh do chính mình tạo (*Self-initiated*): Tuyệt đối không tính vào badge của chính mình (tuân thủ nguyên tắc Maker-Checker).
        * Lệnh mình đã duyệt xong (*Already-acted*): Không đếm nữa (chuyển sang đếm cho Approver thứ 2 nếu là multi-approval).
        * Lệnh thuộc Grant mình không có quyền duyệt: Không được đếm.

* Example (Galaxy):

  * GET Whitelisting
  * G1
  * Kafka …
  * Settlement
  * Transfer tool manage permission
  * Transfer tool Instructions
  * On-Chain
  * ….

* Cách apply AI trong công việc:

  * **Quy trình ứng dụng thực chiến:** **Input → AI Hỗ trợ → QA Đánh giá & Rà soát → Kết quả cuối cùng**
    1. **Input:** Link Jira ticket (`QA-6885`, `GTO-16224`, `QA-5920`, `QA-5915`), tài liệu Confluence spec, git diff của PR và các đoạn thảo luận kỹ thuật.
    2. **AI Hỗ trợ:**
       * Bóc tách yêu cầu phức tạp và sinh nhanh bộ kịch bản Scenarios thông qua slash command `/create-draft-test-execution`.
       * Thiết kế ma trận test cases chi tiết: Happy Path, Negative Cases, Boundary, Polling Gate, Scoping và Optimistic UI.
       * Hỗ trợ viết test script automation cho API endpoints, kiểm tra model Pydantic và scan dọn dẹp orphan functions qua `/review-code`.
    3. **QA Đánh giá & Rà soát:**
       * Mở VS Code đọc kỹ từng kịch bản test, đối chiếu với logic nghiệp vụ thực tế.
       * Bắt buộc xác định và ghi rõ thông tin Endpoint API (`URL`, `Method`, `Payload`) để đưa vào Description Jira.
       * Ngay sau khi tạo ticket Jira xong, chạy ngay `/create-test-artifact` để đồng bộ test document chính thức lên Confluence.
       * Gửi Dev phụ trách review và thống nhất Test Section trên Slack.
    4. **Kết quả cuối cùng:**
       * Khi Dev deploy Staging, sử dụng `/Create-TR-Run-From-TR-Draft` để tự động tạo Test Run trên TestRail và tiến hành thực thi kiểm thử, đảm bảo chất lượng nghiệm thu đạt 100% Passed.

* Cách test regression tests và scope cần test trong regression tests:

  * **Chiến lược xác định phạm vi Regression cho Ticket Enhancement (UI & Backend):**
    * **1. Phân tích điểm chạm dùng chung (Shared Seams Analysis):**
      * Khi Dev thực hiện enhancement (ví dụ: thêm Badge cảnh báo trên Global Nav ở `QA-6885`, hoặc kích hoạt Datadog APM trên `GTO-16224`):
      * Xác định các component và service dùng chung tài nguyên với tính năng mới:
        * *Với UI Nav Badge:* Global Nav dùng chung cho tất cả các phân hệ ➔ Bắt buộc regression kiểm tra hiển thị trên Trading, Live Risk, Blotter xem layout có bị xê dịch hoặc xung đột CSS không.
        * *Với Backend Gateway:* Kích hoạt Datadog tracer ➔ Bắt buộc regression chạy lại luồng transfer cốt lõi xem overhead latency có vượt quá ngưỡng cho phép (< 5ms) hay gây lỗi kết nối downstream không.
    * **2. Mô hình 3 tầng xác định Regression Scope:**
      * *Tầng 1 - Core Feature Regression:* Kiểm tra các luồng nghiệp vụ chính của tính năng (tạo lệnh, duyệt lệnh, từ chối lệnh xem có kích hoạt đúng Optimistic UI và xóa badge không).
      * *Tầng 2 - Gỡ bỏ thành phần cũ (Legacy Cleanup Regression):* Kiểm tra các chỉ báo cũ (ví dụ: indicator chấm đỏ cũ tại header trang Transfer Tool) đã được gỡ bỏ hoàn toàn chưa, tránh hiển thị trùng lặp (**RT-01**).
      * *Tầng 3 - Boundary & Negative Regression:* Giả lập mất quyền giữa chừng, API lỗi 500/503 để đảm bảo hệ thống phục hồi mượt mà, không crash UI và không phát sinh lỗi ngoại lệ.

Cách test ticket enhancement của dev và regression scope mình cần làm tương ứng.

Action items:

* [x] Hoàn tất thực thi checklist kiểm thử trên Staging cho ticket `QA-6885` (Suite UI 946 & Suite E2E 947), cập nhật TestRail Run và nghiệm thu chuyển trạng thái sang `Pass Test` ✅.
* [x] Nhận feedback review PR từ Dastan cho các ticket endpoint automation đã submit: `QA-6916` (Slack notification re-run), `QA-5920` (Pending & History endpoints), `QA-5915` (Poller parsing) và hoàn tất merge PR (Done) ✅.
* [x] Phối hợp với Dev phụ trách ticket `GTO-16224` (Datadog APM), xác nhận bản deploy trên Staging và thực thi kiểm tra Distributed Tracing trên Datadog UI đạt chuẩn `Pass Test` ✅.
* [ ] Tiếp tục duy trì và mở rộng quy trình ứng dụng AI (`/create-draft-test-execution` ➔ `/create-test-artifact` ➔ `/Create-TR-Run-From-TR-Draft`) cho các ticket kiểm thử trong tuần tiếp theo.
