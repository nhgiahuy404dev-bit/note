* [Vsee - Galaxy] Weekly Summary + Demo

Attendees: Brian Pham Hau Duong (Hầu Dương) Huy Nguyễn Pháp Huỳnh Quốc Thai Huynh

* Notes

Meeting sẽ chia ra làm các phần chính như sau:

## Summary:

* List ra trong tuần rồi đã / đang làm ticket nào, progress như thế nào rồi:

### 🎯 `QA-6700` - Coordinator Service Endpoints Automation (11/09/2026)

* **Endpoint 1: `GET /instruction/by-step-ref/{uniqueRef}` (11/09/2026):**
  * **Trạng thái / Tiến độ:** Hoàn tất 11 bước ➔ **`Under Review`** (Đã tạo PR & gán reviewer).
  * **Ngày hoàn thành:** 11/09/2026 (Thứ Sáu).
  * **Branch:** `QA-6700-instruction-by-step-ref`
  * **Chi tiết thực hiện (Quy trình chuẩn 11 bước):**
    1. **Create Test Scenario Prompt:** Tạo prompt cho AI đọc các test steps, sinh bộ Scenarios kiểm tra response `200 OK`, schema dữ liệu và tính toàn vẹn của step execution reference.
    2. **Create New Branch:** Tạo branch độc lập `QA-6700-instruction-by-step-ref` từ `main` và chuyển trạng thái ticket sang `Testing`.
    3. **Complete Scenario:** Rà soát và hoàn thiện kịch bản Scenarios trước khi viết code test.
    4. **Review Code:** Tự review code triển khai test script và các câu lệnh assertions.
    5. **Run Code:** Thực thi chạy bộ kiểm thử tự động cục bộ (Pass 100%).
    6. **Fix Code:** Tinh chỉnh các assertions và format dữ liệu trả về chuẩn xác.
    7. **Create TestRail:** Tạo và cập nhật đầy đủ test cases lên hệ thống TestRail.
    8. **Commit and Push Code:** Commit đúng chuẩn convention và push code lên remote branch.
    9. **Create PR Summary:** Soạn thảo bản tóm tắt nội dung PR.
    10. **Create Pull Request:** Tạo Pull Request trên GitHub vào nhánh `main`.
    11. **Update Review Status:** Cập nhật trạng thái ticket Jira sang **`Under Review`**.
* **Endpoint 2: `GET /instruction/request/status` (11/09/2026):**
  * **Trạng thái / Tiến độ:** **Tạm hoãn (Postponed)** — Dời kế hoạch thực hiện sang tuần tới.
  * **Ngày ghi nhận:** 11/09/2026 (Thứ Sáu).
  * **Ghi chú:** Chưa tạo branch riêng, đã chuẩn bị trước prompt phân tích test steps.

### 🎯 `QA-6703` - Automation Tests cho Permission Endpoints (08/09/2026 - 11/09/2026)

* **Endpoint 1: `ui/permission/pending` (08/09/2026):**
  * **Trạng thái / Tiến độ:** Hoàn tất triển khai test ban đầu ➔ **`Under Review`** (Đang chờ duyệt PR).
  * **Ngày hoàn thành:** 08/09/2026 (Thứ Ba).
  * **Branch:** `QA-6703-ui-permission-pending`
  * **Chi tiết thực hiện (Quy trình chuẩn 11 bước):**
    1. **Create Test Scenario Prompt:** Sử dụng prompt AI đọc test steps để tự động sinh Scenarios kiểm tra danh sách quyền chờ duyệt.
    2. **Create New Branch:** Tạo branch độc lập `QA-6703-ui-permission-pending` từ `main`, chuyển trạng thái sang `Testing`.
    3. **Complete Scenario:** Hoàn thiện kịch bản Scenarios kiểm tra dữ liệu pending permission.
    4. **Review Code:** Review cấu trúc code test và các assertions.
    5. **Run Code:** Chạy automated test cục bộ thành công.
    6. **Fix Code:** Khắc phục lỗi phát sinh và hoàn thiện kịch bản.
    7. **Create TestRail:** Đồng bộ và cập nhật test cases lên TestRail.
    8. **Commit and Push Code:** Commit và push code lên remote branch.
    9. **Create PR Summary:** Soạn thảo tóm tắt PR.
    10. **Create Pull Request:** Tạo PR trên GitHub.
    11. **Update Review Status:** Cập nhật trạng thái ticket Jira sang **`Under Review`**.
* **Endpoint 2: `ui/permission/rule - config` (08/09/2026 - 11/09/2026):**
  * **Trạng thái / Tiến độ:** **`In Progress`** (Đang tiếp tục hoàn thiện kịch bản & code test).
  * **Thời gian thực hiện:** 08/09/2026 - 11/09/2026 (Hoàn thành Scenario ngày 08/09, đang tiếp tục hoàn thiện negative cases).
  * **Branch:** `QA-6703-ui-permission-rule-config`
  * **Chi tiết thực hiện (Theo quy trình 11 bước):**
    * Đã hoàn thành các bước 1 ➔ 5: Tạo Scenario bằng AI, lập branch riêng, hoàn thiện kịch bản cấu hình tham số quy tắc (rule config), triển khai code test và chạy thử kịch bản chính.
    * Đang thực hiện các bước 6 ➔ 11: Mở rộng các kịch bản biên (edge cases), negative test, cập nhật TestRail và chuẩn bị tạo PR.

### 🎯 `QA-6880` (GTO-16245, GTO-16246) - Restrict retry of a failed transfer to ops users only, and drop the retry time window (10/09/2026)

* **Đã làm:** Phân tích yêu cầu nghiệp vụ về việc giới hạn quyền retry các giao dịch failed chỉ dành riêng cho Ops users, đồng thời loại bỏ cửa sổ giới hạn thời gian retry. Đã hoàn thành thiết kế ma trận kịch bản kiểm thử (Test Scenario Matrix) và bản thảo Test Execution.
* **Ngày hoàn thành thiết kế (Design):** 10/09/2026 (Thứ Năm).
* **Tiến độ hiện tại:** In Progress (Đang thực hiện). Đang chờ Dev deploy code lên môi trường staging/test để bắt đầu tiến hành kiểm thử thực tế (cập nhật ngày 11/09/2026).

### 🎯 `GTO-16168` - Split Fireblocks section into Vault and Whitelisted Address (07/09/2026)

* **Đã làm:** 
  * Áp dụng **Quy trình kiểm thử Ticket thường (Standard Feature/UI Testing Workflow)** gồm 5 giai đoạn:
    1. **Read Request:** Đọc và phân tích kỹ yêu cầu tách mục Fireblocks section từ Jira & Confluence.
    2. **Designing:** Chuyển status Jira sang `Designing`, thiết kế bộ test cases chi tiết cho component permissions account picker.
    3. **Testing:** Chuyển status Jira sang `Testing`, thực thi test Endpoint, Regression Test và E2E Test; đưa test artifacts lên Confluence.
    4. **Pass Test:** Sau khi kiểm thử hoàn tất và đạt chuẩn, chuyển status Jira sang `Pass Test`, đánh dấu hoàn thành ✅.
    5. **Create PR:** Tạo PR và gán các reviewer chính: **Mohit**, **Dastan**, và **Sandeep**.
* **Ngày hoàn thành (Pass Test ✅):** 07/09/2026 (Thứ Hai).
* **Tiến độ hiện tại:** Hoàn thành kiểm thử giao diện và đã nghiệm thu Pass Test ✅.

### ⚙️ Quy trình Quản lý Secret Jenkins & DevOps Workflow (10/09/2026)

* **Đã làm:** Chuẩn hóa và ghi chép chi tiết quy trình thêm Secret mới cho Jenkins (Repo `terraform` làm trước ➔ lưu ý key secret phải thêm dấu sao `*` vào cuối key ➔ Xin approval từ SRE-ONCALL trên kênh Slack `#production_assistance` ➔ Gõ `atlantis apply` trên GitHub PR ➔ Đợi apply thành công mới Merge ➔ Repo `jenkins` do Team QA duyệt).
* **Ngày hoàn thành:** 10/09/2026 (Thứ Năm).
* **Tiến độ hiện tại:** Đã hoàn tất và lưu vào tài liệu ghi chú của team.

* Demo feature đã / đang làm:

  * **Demo 1: Trình diễn Flow chuẩn triển khai Endpoint Automation & Bộ Test Coordinator (`QA-6700`):**
    * Trình diễn toàn bộ chu trình 11 bước từ tạo Scenario bằng AI, tạo branch, run test pass 100%, cập nhật TestRail đến mở PR và cập nhật trạng thái ticket sang `Under Review`.
    * Thực thi test tự động kiểm thử endpoint `GET /instruction/by-step-ref/{uniqueRef}` với assertion chuẩn xác.
  * **Demo 2: Trình diễn Flow chuẩn & Bộ Test Permission Service (`QA-6703`):**
    * Trình diễn áp dụng quy trình chuẩn cho endpoint Permission: chạy test kiểm tra danh sách quyền đang chờ duyệt (`ui/permission/pending`) và cấu hình tham số quy tắc (`ui/permission/rule - config`).
  * **Demo 3: Git Branching & Quy trình triển khai CI/CD:**
    * Trình diễn quy ước đặt tên branch độc lập theo từng endpoint (`<branch-name>-<endpoint>`) giúp PR gọn gàng và cô lập phạm vi kiểm thử.

## Knowledge Sharing:

* Pick ra 1 topic trong feature mình đã làm để sharing knowledge (UI):

  * **Transfer tool manage permission & Instructions:**
    * **Chủ đề lựa chọn:** Xử lý triệt để bẫy cờ `PENDING_APPROVAL` trên Jenkins và Chiến lược phân quyền kiểm thử cho tính năng Retry Failed Transfer.
    * **1. Bài toán thực tế & Hướng xử lý (Giải quyết lỗi Flaky Test trên Jenkins):**
      * **Vấn đề:** Khi chạy test tự động trên Jenkins cho file `transfer_tool.feature`, các test case mong đợi trạng thái hoàn tất (`SUCCESS`) thỉnh thoảng bị dừng ở trạng thái `PENDING_APPROVAL`, khiến build bị fail bất ngờ.
      * **Nguyên nhân:** Trên môi trường QA dùng chung, các thao tác test thủ công hoặc người dùng khác vô tình bật cờ yêu cầu duyệt (`approval_required = true`), làm thay đổi luồng xử lý mặc định của lệnh chuyển tiền.
      * **Giải pháp của QA:** Thiết lập các hook pre-test setup để chủ động reset và ép cấu hình approval về đúng trạng thái kỳ vọng của từng scenario trước khi chạy, sau đó có bước teardown dọn dẹp để đảm bảo kết quả test luôn ổn định, chính xác.
    * **2. Kiểm thử tính năng Dev Enhancement (`QA-6880` - Restrict Retry of Failed Transfer):**
      * **Những gì đã thay đổi:**
        1. Phân quyền: Chỉ duy nhất người dùng có vai trò Ops (`Ops role`) mới được phép retry các lệnh chuyển tiền bị lỗi (`FAILED`).
        2. Bỏ cửa sổ thời gian: Loại bỏ điều kiện giới hạn thời gian (time-window) từng chặn người dùng không được retry sau một khoảng thời gian nhất định.
      * **Những điểm QA cần xác minh (Test Scenarios):**
        * *Trường hợp tích cực (Positive):* Ops user có thể kích hoạt retry thành công trên bất kỳ lệnh `FAILED` nào dù lệnh đó đã fail từ lâu.
        * *Trường hợp tiêu cực (Negative):* Người dùng không phải Ops (user thường, viewer) sẽ không nhìn thấy nút retry hoặc nhận mã lỗi `403 Forbidden` khi cố tình gọi API.
        * *Bảo vệ trạng thái (State guards):* Đảm bảo hệ thống không cho phép retry trên các trạng thái khác (`INITIATED`, `QUEUED`, `SUCCESS`).
      * **Xác định phạm vi Regression (Regression Scope):**
        * *Vùng cần test lại:* Luồng tạo lệnh bình thường (normal transfer flow), luồng hủy lệnh (`ABORTED`), và audit log lịch sử giao dịch (đảm bảo ghi nhận chính xác người thực hiện retry).
        * *Lý do bao gồm:* Bộ xử lý retry dùng chung logic chuyển trạng thái cốt lõi với luồng thực thi thông thường, do đó phải chắc chắn các luồng lệnh chuẩn không bị ảnh hưởng.
        * *Vùng loại trừ:* Các luồng nạp tiền (deposit) hoặc indexer blockchain bên ngoài, vì thay đổi này được cô lập bên trong bộ phân quyền và chuyển trạng thái của Transfer Coordinator.

* Cách apply AI trong công việc:

  * **Quy trình ứng dụng thực chiến:** **Input → AI Hỗ trợ → QA Đánh giá & Rà soát → Kết quả cuối cùng**
    1. **Input:** Link Jira ticket, tài liệu Confluence PRD/spec, git diff của PR và các đoạn thảo luận trên Slack.
    2. **AI Hỗ trợ:** Dùng prompt chuyên dụng để bóc tách nghiệp vụ phức tạp và chuyển đổi yêu cầu thô thành tài liệu Markdown có cấu trúc:
       * Tóm tắt phạm vi thay đổi (Scope breakdown).
       * Bảng kịch bản test API (`ID`, `Scenario`, `Expected`, `Actual`, `Status`).
       * Ma trận kiểm thử UI và vùng hồi quy (Regression matrix).
       * Tự động tạo Slash Command `/create-draft-test-execution` để cả team tái sử dụng.
    3. **QA Đánh giá & Rà soát:** QA rà soát lại các case biên (edge cases), bổ sung các điều kiện kiểm tra an toàn tiền tệ (money safety) và tinh chỉnh kỳ vọng.
    4. **Kết quả cuối cùng:** Đồng bộ trực tiếp lên Confluence dưới Epic cha `QA-3614: Transfer Tools Enhancement` với nhãn `Test Artifact:`, sẵn sàng để Dev review trước khi deploy.

* Cách test regression tests và scope cần test trong regression tests:

  * **Mô hình 3 tầng xác định phạm vi Regression cho Ticket Enhancement:**
    * **Tầng 1 - Phạm vi ảnh hưởng trực tiếp (Direct Impact Scope):** Các hàm, quyền hạn và tham số bị thay đổi trực tiếp bởi tính năng mới (ví dụ: xác thực quyền của Ops role khi retry và kiểm tra không còn bộ đếm timeout).
    * **Tầng 2 - Phạm vi biên & Tiêu cực (Boundary & Negative Scope):** Các role không có quyền và trạng thái chuyển dịch không hợp lệ (ví dụ: non-Ops gọi endpoint retry, retry lệnh đang ở trạng thái `SUCCESS` hoặc `PENDING`).
    * **Tầng 3 - Phạm vi hồi quy mở rộng (Broader Regression Scope):** Toàn bộ các dịch vụ liên kết trong vòng đời của lệnh (ví dụ: đảm bảo lệnh chuyển tiền bình thường chạy suôn sẻ; lịch sử audit log ghi nhận đầy đủ).

Cách test ticket enhancement của dev và regression scope mình cần làm tương ứng.

Action items:

* Phối hợp với Dev xác nhận trạng thái deploy môi trường staging cho ticket `QA-6880` và thực thi toàn bộ kịch bản kiểm thử phân quyền RBAC.
* Tiếp tục triển khai các kịch bản automated test cho endpoint `GET /instruction/request/status` (`QA-6700`).
* Mở rộng độ bao phủ automation test cho các kịch bản biên và negative của `ui/permission/rule - config` (`QA-6703`).
* Áp dụng hook test setup reset approval trên toàn bộ feature files của Transfer Tool để triệt tiêu hoàn toàn lỗi false-negative trên Jenkins.
