* [Vsee - Galaxy] Weekly Summary + Demo

Attendees: Brian Pham Hau Duong (Hầu Dương) Huy Nguyễn Pháp Huỳnh Quốc Thai Huynh

* Notes

Meeting sẽ chia ra làm các phần chính như sau:

## Summary:

* List ra trong tuần rồi đã / đang làm ticket nào, progress như thế nào rồi:

  * **`ONBOARD-W33` - Thiết lập Main Workspace & Cấu hình Môi trường Kiểm thử:**
    * **Đã làm:** 
      * Hoàn thành thiết lập toàn bộ môi trường làm việc kỹ thuật: Kết nối cơ sở dữ liệu giữa 2 môi trường **QA** và **UAT**, cấu hình bộ request API trên **Postman** (`My Collection`).
      * Làm quen và thiết lập các repository trên GitHub (Repo chính kiểm thử API và Repo UI), cấu hình trang quản trị nội bộ **Fortool** (Internal Button mở 2 trang QA và Operation).
      * Thiết lập quy trình tạo **Test Artifact** cung cấp actual data khi User Group yêu cầu và chuẩn hóa quy trình quản lý task trên Jira/Todo.
    * **Tiến độ hiện tại:** Hoàn thành 100% thiết lập môi trường và sẵn sàng nhận task kiểm thử.

  * **`QA-FUNDAMENTALS` - Chuẩn hóa Nền tảng Lý thuyết & Quy trình Kiểm thử Chất lượng:**
    * **Đã làm:** 
      * Hệ thống hóa và chuẩn hóa toàn bộ các định nghĩa cốt lõi trong quy trình kiểm thử phần mềm: Phân biệt rõ ràng giữa **Error (Sai sót con người)**, **Defect / Bug (Lỗi phần mềm)**, và **Failure (Sự cố vận hành)**.
      * Xây dựng ma trận phân biệt mục tiêu và câu hỏi cốt lõi của 4 cấp độ kiểm thử: **Smoke Test**, **Sanity Test**, **Retest (Verification Testing)** và **Regression Test**.
      * Định nghĩa rõ ràng ranh giới giữa **Verification (Xác minh - Bug Prevention)** và **Validation (Xác thực - Bug Detection)**, chuẩn hóa chu trình kiểm thử: `Deploy Build mới` ➔ `Smoke Test` ➔ `Sanity / Functional Test` ➔ `Retest Bug` ➔ `Regression Test` ➔ `Release`.
    * **Tiến độ hiện tại:** Hoàn thành tài liệu hóa và lưu vào sổ tay nghiệp vụ QA của team.

* Demo feature đã / đang làm:

  * **Demo 1: Thiết lập Không gian làm việc & Kết nối Môi trường (Main Workspace):**
    * Trình diễn luồng kết nối cơ sở dữ liệu đa môi trường (QA & UAT), quản lý tập trung các bộ API request trên Postman và tương tác với trang quản trị nội bộ Fortool.
  * **Demo 2: Ma trận Phân loại Lỗi & Chiến lược Cấp độ Kiểm thử (QA Fundamentals):**
    * Trình diễn cách ứng dụng vòng đời kiểm thử chuẩn từ khâu Smoke test chặn build lỗi, Sanity test vùng chức năng thay đổi, đến khâu Retest xác nhận fix bug và Regression test đảm bảo an toàn toàn hệ thống.

## Knowledge Sharing:

* Pick ra 1 topic trong feature mình đã làm để sharing knowledge (UI):

  * **Chiến lược phân tầng kiểm thử & Quy trình quản lý vòng đời lỗi phần mềm:**
    * **Chủ đề lựa chọn:** Phân biệt bản chất Error - Defect - Failure và Ứng dụng chu trình 4 cấp độ test (Smoke, Sanity, Retest, Regression) trong các sprint dự án Galaxy.
    * **1. Phân biệt Error - Defect/Bug - Failure:**
      * **Error:** Sai sót do con người (Dev code nhầm logic, BA ghi sai requirement).
      * **Defect / Bug:** Khiếm khuyết kỹ thuật làm kết quả thực tế (Actual) khác với mong đợi (Expected).
      * **Failure:** Sự cố vận hành xảy ra trên môi trường thực tế khi người dùng thao tác.
    * **2. Bốn cấp độ kiểm thử thiết yếu:**
      * *Smoke Test:* Trả lời câu hỏi *"Version này có đủ ổn định để tiếp tục test không?"* (Chặn đứng build lỗi ngay từ cổng vào).
      * *Sanity Test:* Trả lời câu hỏi *"Phân hệ / chức năng vừa được sửa có hoạt động ổn định không?"* (Kiểm tra sâu vào vùng vừa thay đổi).
      * *Retest:* Trả lời câu hỏi *"Lỗi cụ thể này đã thực sự được sửa triệt để chưa?"* (Xác minh bug và quyết định Close hay Reopen).
      * *Regression Test:* Trả lời câu hỏi *"Việc sửa đổi mới có làm hỏng các chức năng cũ đang chạy không?"*.
    * **3. Verification vs Validation:**
      * *Verification (Static Testing):* Đánh giá tài liệu, review code, phòng ngừa lỗi (Bug Prevention).
      * *Validation (Dynamic Testing):* Chạy ứng dụng thực tế, đối soát với nhu cầu người dùng (Bug Detection).

* Cách apply AI trong công việc:

  * **Quy trình ứng dụng thực chiến:** **Input → AI Hỗ trợ → QA Đánh giá & Rà soát → Kết quả cuối cùng**
    1. **Input:** Yêu cầu nghiệp vụ hoặc mô tả lỗi từ người dùng/sản phẩm.
    2. **AI Hỗ trợ:** Dùng AI hỗ trợ phân tích nguyên nhân gốc rễ (Root Cause Analysis), phân loại lỗi chính xác (Error vs Defect), và gợi ý kịch bản Smoke/Sanity test tương ứng.
    3. **QA Đánh giá & Rà soát:** QA rà soát tính khả thi trên hệ thống thực tế và môi trường QA/UAT của Galaxy.
    4. **Kết quả cuối cùng:** Kịch bản kiểm thử rõ ràng, tránh sót case và tối ưu thời gian test.

* Cách test regression tests và scope cần test trong regression tests:

  * **Phương pháp xác định phạm vi Regression khi test ticket enhancement:**
    * **Xác định các điểm chạm dùng chung (Shared Seams):** Kiểm tra các API, service hoặc dữ liệu dùng chung chịu ảnh hưởng bởi code thay đổi.
    * **Phân tách rõ vùng ảnh hưởng:** Luôn thực hiện Smoke Test trước để đảm bảo hệ thống không bị crash diện rộng, sau đó tập trung khoanh vùng các luồng nghiệp vụ lân cận.
    * **Ngưỡng chặn hồi quy (Regression Gate):** Toàn bộ các test cases thuộc luồng nghiệp vụ cốt lõi phải Pass 100% trước khi ký duyệt bàn giao sang môi trường UAT.

Cách test ticket enhancement của dev và regression scope mình cần làm tương ứng.

Action items:

* Tiếp tục làm quen sâu với các luồng nghiệp vụ của hệ thống Transfer Tool và cơ sở dữ liệu Galaxy.
* Chuẩn hóa quy trình tạo test case từ tài liệu Confluence và đồng bộ lên TestRail.
* Áp dụng chu trình Smoke Test và Regression Test vào các task kiểm thử thực tế của tuần tiếp theo.
