* [Vsee - Galaxy] Weekly Summary + Demo

Attendees: Brian Pham Hau Duong (Hầu Dương) Huy Nguyễn Pháp Huỳnh Quốc Thai Huynh

* Notes

Meeting sẽ chia ra làm các phần chính như sau:

## Summary:

* List ra trong tuần rồi đã / đang làm ticket nào, progress như thế nào rồi:

  * **`QA-GATEWAY-AUTO` - Nghiên cứu Gateway & Xây dựng Kịch bản Automation:**
    * **Đã làm:** 
      * Phân tích và nắm bắt cấu trúc kịch bản Smoke Test và Regression Test trong file kiểm thử cốt lõi `transfer_gateway.feature`.
      * Rà soát bảng dữ liệu `Examples` đối chiếu với version hiện tại để làm mới dữ liệu kiểm thử.
      * Sử dụng công cụ `Helper Script/check-new-apis` để quét danh sách các API mới được cập nhật và chạy lệnh cập nhật Roadmap dự án `./update-roadmap.sh`.
    * **Tiến độ hiện tại:** Hoàn thành nghiên cứu và cập nhật đầy đủ bộ dữ liệu kiểm thử cho Gateway.

  * **`QA-PROCESS-STD` - Sổ tay Quy trình QA & Chuẩn hóa Test Execution:**
    * **Đã làm:** 
      * Áp dụng **Quy trình kiểm thử Ticket thường (Standard Feature/UI Testing Workflow)** gồm 5 giai đoạn cho việc chuẩn hóa:
        1. **Read Request:** Đọc và phân tích kỹ yêu cầu kỹ thuật từ Spec, Ticket, công cụ Tester Tool và cấu hình User Group/Scope (`FBS:GDL:TSY`, `FBS:GTA:MOTC`).
        2. **Designing:** Chuyển status sang `Designing`, thiết lập quy ước đặt tên task (`[TEST EXECUTION]`, `[API-QA]`, `[UI-QA]`), chuẩn hóa lệnh tạo test case `/Create-Test-Cases-from-Confluent` với ProjectID: 30 và phân chia 3 suite (API: 945, UI: 946, E2E: 947).
        3. **Testing:** Chuyển status sang `Testing`, thực thi các bộ test, tạo Test Run trên TestRail bằng `/Create-TR-RUN-from-TR-Daraf` và xác nhận kết quả All Passed.
        4. **Pass Test:** Chuyển status sang `Pass Test` sau khi hoàn thành nghiệm thu, đánh dấu ✅.
        5. **Create PR:** Tạo PR và gửi request lấy Sign-off trên giao diện Visual từ các bên liên quan.
    * **Tiến độ hiện tại:** Hoàn thành ban hành sổ tay quy trình và áp dụng chuẩn hóa trong team.

  * **`QA-GIT-AI-FLOW` - Quy trình Git Branching & Chuẩn hóa Prompt AI Sinh Kịch bản Automation:**
    * **Đã làm:** 
      * Chuẩn hóa quy trình tạo branch từ `main` (`git pull origin main` ➔ `git checkout -b <branch-name>`).
      * Xây dựng câu prompt AI chuẩn mực yêu cầu AI đọc tài liệu endpoint và file `.feature` hiện tại để sinh các Scenarios bổ sung, bắt buộc phải có bước review kịch bản trước khi sửa đổi file code.
    * **Tiến độ hiện tại:** Hoàn thành thử nghiệm thành công và đưa vào áp dụng cho toàn bộ các ticket automation.

* Demo feature đã / đang làm:

  * **Demo 1: Quy trình AI sinh Kịch bản Automation & Rà soát Kịch bản:**
    * Trình diễn câu prompt AI chuẩn kết hợp tài liệu endpoint và file `.feature`, kiểm soát việc AI đề xuất scenarios và quy trình review kịch bản trước khi triển khai code.
  * **Demo 2: Đồng bộ Test Cases lên TestRail & Quản lý Bộ Suite IDs:**
    * Trình diễn tạo test cases tự động từ Confluence vào đúng các Suite chuyên biệt: API (945), UI (946), E2E (947) trên TestRail và kích hoạt Test Run All Passed.

## Knowledge Sharing:

* Pick ra 1 topic trong feature mình đã làm để sharing knowledge (UI):

  * **Quy chuẩn quản lý Test Cases TestRail & Tích hợp AI vào chu trình tạo Kịch bản Automation:**
    * **Chủ đề lựa chọn:** Thiết lập cấu trúc phân nhóm Test Suite (API, UI, E2E) trên TestRail và Quy trình 4 bước ứng dụng AI tạo kịch bản Scenario chuẩn mực.
    * **1. Cấu trúc định danh và quản lý TestRail:**
      * ProjectID chuẩn: **30**.
      * Phân định rõ ràng 3 Suite ID: **Suite API: 945**, **Suite UI: 946**, **Suite E2E: 947**.
      * Quy tắc cập nhật: Lệnh `/create-testrail` chỉ tạo case mới, trong khi `/sync-testrail` sẽ đồng bộ và cập nhật trực tiếp trạng thái lên Jira ticket.
    * **2. Bốn bước chuẩn mực khi dùng AI sinh Scenario:**
      * *Bước 1 (Chuẩn bị Log Step):* Thu thập đầy đủ câu query SQL, dữ liệu output, lệnh curl API và response JSON mẫu.
      * *Bước 2 (Prompt AI sinh Scenario):* Đưa context rõ ràng và yêu cầu AI sinh kịch bản dạng BDD Gherkin trước, không được tự ý sửa file code trực tiếp.
      * *Bước 3 (Review kịch bản):* QA rà soát tính bao phủ của kịch bản, đối chiếu các trường hợp Happy Path và Negative.
      * *Bước 4 (Implement & Cập nhật TestRail):* Sau khi duyệt kịch bản, tiến hành viết mã test và đồng bộ test case ID lên hệ thống.

* Cách apply AI trong công việc:

  * **Quy trình ứng dụng thực chiến:** **Input → AI Hỗ trợ → QA Đánh giá & Rà soát → Kết quả cuối cùng**
    1. **Input:** Tài liệu đặc tả endpoint mới và file `.feature` hiện tại của module.
    2. **AI Hỗ trợ:** Chạy prompt yêu cầu AI phân tích dữ liệu đầu vào và sinh kịch bản Scenario kiểm thử bao phủ các trường hợp biên và validation.
    3. **QA Đánh giá & Rà soát:** QA và Leader rà soát từng bước Gherkin, đảm bảo cú pháp tái sử dụng (reusable steps) và không làm hỏng các step định nghĩa trước đó.
    4. **Kết quả cuối cùng:** Kịch bản Scenario hoàn thiện, làm cơ sở để triển khai code automation chính xác và nhanh chóng.

* Cách test regression tests và scope cần test trong regression tests:

  * **Phương pháp xác định phạm vi Regression khi test ticket enhancement:**
    * **Xác định các điểm chạm dùng chung (Shared Seams):** Khi cập nhật file kịch bản dùng chung như `transfer_gateway.feature`, bắt buộc phải kiểm tra lại toàn bộ các scenario trong cùng file.
    * **Phân tách rõ vùng ảnh hưởng:** Tách bạch rõ giữa phạm vi kiểm thử API (Suite 945) và UI (Suite 946), chạy kiểm tra Smoke test trước khi chạy toàn bộ Regression Suite.
    * **Ngưỡng chặn hồi quy (Regression Gate):** Toàn bộ các test cases trong Test Run phải đạt trạng thái Passed 100% trước khi ký Sign-off bàn giao.

Cách test ticket enhancement của dev và regression scope mình cần làm tương ứng.

Action items:

* Triển khai bộ kịch bản automation cho các endpoint mới của Permission service (`QA-6702`).
* Áp dụng quy tắc mỗi branch một endpoint (`<branch-name>-<endpoint>`) cho tất cả các task phát triển test sắp tới.
* Đồng bộ đầy đủ các kịch bản kiểm thử mới lên TestRail và liên kết vào Jira tickets tương ứng.
