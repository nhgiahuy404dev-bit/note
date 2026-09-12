* [Vsee - Galaxy] Weekly Summary + Demo

Attendees: Brian Pham Hau Duong (Hầu Dương) Huy Nguyễn Pháp Huỳnh Quốc Thai Huynh

* Notes

Meeting sẽ chia ra làm các phần chính như sau:

## Summary:

* List ra trong tuần rồi đã / đang làm ticket nào, progress như thế nào rồi:

  * **`QA-6742` (GTO-16043) - Fiat withdrawal UI + E2E (Transfer Tool):**
    * **Đã làm:** Hoàn thành kiểm thử thủ công toàn diện giao diện rút tiền Fiat trên Transfer Tool theo ma trận từ `UI-1` đến `UI-9`. Kiểm tra kỹ tính năng cập nhật ngày (Value date / Update date) trên form nhập liệu và kiểm tra các luồng End-to-End (`E2E-1` đến `E2E-4`) từ giao diện Frontend xuống Backend.
    * **Tiến độ hiện tại:** Hoàn thành kiểm thử UI & E2E thủ công (Bao phủ 100% test cases UI, xác minh đầy đủ các UI guards và tính hợp lệ của form).

  * **`QA-6741` (GTO-15979) - Fiat withdrawal initiation (Transfer Tool) — Phase 5:**
    * **Đã làm:** Nghiên cứu kiến trúc Backend Initiation Layer qua 5 Waves. Xây dựng ma trận kiểm thử Backend (Backend Test Matrix) bao gồm 7 nhóm: `MIG`, `REG`, `REF`, `CRD`, `STP`, `EXE`, `STA`. Soạn thảo tài liệu đặc tả từng bước thực thi (Details Step) chi tiết kèm câu lệnh SQL query, mock curl và các điểm kiểm tra an toàn tiền tệ (Money Safety).
    * **Tiến độ hiện tại:** Hoàn thành thiết kế kịch bản kiểm thử (Sẵn sàng chạy test tích hợp khi môi trường deploy xong PR 8425 và các Backend waves).

* Demo feature đã / đang làm:

  * **Demo 1: Giao diện người dùng Rút tiền Fiat (`QA-6742`):**
    * **Lọc động điểm đến thụ hưởng (`UI-2`):** Trình diễn khi chọn tài sản Fiat (`USD`), dropdown `To` tự động lọc chỉ hiển thị các tài khoản ngân hàng thụ hưởng đã được Whitelist (`Whitelisted Bank Beneficiaries`), tuyệt đối không lẫn lộn với ví hay vault Crypto.
    * **Xử lý Date Picker & Thay đổi Value Date:** Thao tác chọn và thay đổi ngày giao dịch mượt mà, không gây vỡ layout và không làm crash form.
    * **Hợp đồng dữ liệu & UI Guards (`UI-4`, `UI-5`):** Bật tab Network trên DevTools chứng minh payload tạo draft lược bỏ hoàn toàn key `blockchainNetworkId` (omitted key). Màn hình Review hiển thị ký tự em dash (`—`) cho Network và nút Copy không còn bị lỗi văng `value.toString()`.
    * **Nhân bản lệnh (`UI-7`):** Thao tác Clone lệnh rút tiền Fiat tự động điền sẵn các trường thông tin chuẩn xác.
  * **Demo 2: Kịch bản kiểm thử Backend & An toàn dữ liệu (`QA-6741`):**
    * **Tính Idempotency khi tạo lệnh (`CRD-2` Case 1):** Gọi API `create UI` 2 lần liên tiếp cho cùng 1 `instructionId`, xác minh Database chỉ lưu duy nhất 1 bản ghi lệnh, không bị trùng lặp.
    * **Từ chối chọn lệch tài sản (`CRD-2` Case 2):** Trình diễn hệ thống trả về lỗi `400 Bad Request` ngay lập tức khi tạo lệnh rút USD nhưng lại chọn tài khoản ngân hàng thụ hưởng loại EUR.
    * **Chuỗi chuyển trạng thái lệnh (`STA-1`):** Theo dõi vòng đời lệnh: `DRAFT` ➔ `PENDING_APPROVAL` ➔ `QUEUED` ➔ `INITIATED` ➔ `SUCCESS`.

## Knowledge Sharing:

* Pick ra 1 topic trong feature mình đã làm để sharing knowledge (UI):

  * **Transfer Tool Instructions:**
    * **Chủ đề lựa chọn:** Kiểm thử chuyên sâu Giao diện (UI) luồng Lệnh rút Fiat & Quản lý Thụ hưởng Whitelist (`QA-6742`).
    * **1. Cơ chế lọc động điểm đến thụ hưởng (`UI-2`):**
      * Phân tách rạch ròi giữa chuyển tiền có mạng (Crypto - Networked) và không mạng (Fiat - Network-less).
      * Hợp đồng API bắt buộc phải trả về `network = null` cho tài sản Fiat; nếu gán nhầm ID giả sẽ làm UI ẩn toàn bộ tài khoản ngân hàng.
    * **2. Xử lý Form nhập liệu & Date Picker:**
      * Kiểm thử tính ổn định của date picker chọn Value Date, tránh crash form khi submit.
      * Truy vấn số dư động (Dynamic Balances) theo thời gian thực (`Balance as of <timestamp>`) và kích hoạt cảnh báo đỏ khi số tiền vượt quá số dư khả dụng.
    * **3. Quy tắc Omitted Key trong hợp đồng dữ liệu (`UI-4`):**
      * Payload gửi lên từ frontend bắt buộc phải lược bỏ hoàn toàn thuộc tính `blockchainNetworkId` (để ở dạng `undefined`), không gửi `null`, không gửi `0` hay chuỗi rỗng `""`.
    * **4. Chiến lược phòng vệ giao diện & Quy chuẩn hiển thị (`UI-5`, `UI-7`):**
      * Thống nhất hiển thị dấu gạch ngang dài em dash (`—`) cho các trường không áp dụng.
      * Thêm guard bọc nút Copy ngăn chặn lỗi `Uncaught TypeError` khi copy ô dữ liệu trống.
      * Đảm bảo tính toàn vẹn dữ liệu khi Clone lệnh đã có trong lịch sử.
    * **5. Bẫy lỗi ngầm khi validation form (`UI-9`):**
      * Component `FormField` dùng chung chỉ hiển thị lỗi chữ đỏ ở các thuộc tính cấp cao nhất; nếu lỗi xảy ra ở thuộc tính con lồng sâu (nested property), nút Review sẽ bị vô hiệu hóa (disabled) trong im lặng mà không có câu thông báo lỗi nào.

* Cách apply AI trong công việc:

  * **Quy trình ứng dụng thực chiến:** **Input → AI Hỗ trợ → QA Đánh giá & Rà soát → Kết quả cuối cùng**
    1. **Input:** Tài liệu Confluence PRD, ảnh chụp màn hình Jira và sơ đồ kiến trúc kỹ thuật.
    2. **AI Hỗ trợ:** Dùng AI bóc tách các ma trận nghiệp vụ đa tầng (ví dụ: bóc tách 5 Waves và 21 kịch bản kiểm thử cho GTO-15979), tạo ma trận test có caption tiếng Anh ngắn gọn và sinh hướng dẫn thực thi chi tiết kèm câu lệnh SQL, mock curl.
    3. **QA Đánh giá & Rà soát:** QA rà soát logic bảo vệ an toàn tiền tệ, phòng chống lỗi rút tiền 2 lần (double-payment) và thiếu cờ chống gửi trùng (idempotency).
    4. **Kết quả cuối cùng:** Hoàn thiện bộ tài liệu kiểm thử chất lượng cao, đồng bộ trực tiếp lên Jira ticket.

* Cách test regression tests và scope cần test trong regression tests:

  * **Phương pháp khoanh vùng Regression Scope khi kiểm thử Ticket Enhancement:**
    * **Xác định các điểm chạm dùng chung (Shared Seams):**
      * *Tầng Database:* Khi sửa bảng `t_account_supported_asset` thêm ràng buộc `NULLS NOT DISTINCT`, bắt buộc phải query lại 12 tài sản Crypto của sàn LMAX để đảm bảo không bị ảnh hưởng.
      * *Tầng Routing Service:* Khi đảo ngược luồng dispatch (`EXE-1`), phải test hồi quy 1 lệnh chuyển Crypto qua Fireblocks để đảm bảo không bị định tuyến nhầm sang Exchange Adapter.
    * **Nguyên tắc "Crypto is Unaffected" (`UI-8`):**
      * Khi sửa form cho Fiat, phải test song song với Crypto (BTC, ETH): dropdown Network vẫn bắt buộc chọn, câu tóm tắt vẫn giữ nguyên `on <network>`, và request gửi đi vẫn phải có `blockchainNetworkId`.
    * **Ngưỡng chặn hồi quy (Regression Gate):** Toàn bộ các test case cho luồng Crypto cũ phải Pass 100% trước khi ký duyệt nghiệm thu cho tính năng Fiat mới.

Cách test ticket enhancement của dev và regression scope mình cần làm tương ứng.

Action items:

* Theo dõi tiến độ deploy PR 8425 (Frontend) và các Waves Backend của GTO-15979 lên staging để kích hoạt chạy kiểm thử End-to-End thực tế (`E2E-1` đến `E2E-4`).
* Thực thi toàn bộ bộ test hồi quy (Regression Suite) cho các luồng chuyển tiền Crypto qua Fireblocks trên Transfer Tool.
* Đồng bộ 9 kịch bản UI và 21 kịch bản Backend lên TestRail và liên kết vào Jira ticket `QA-6741`, `QA-6742`.
* Phối hợp với Dev xử lý các trường hợp ngoại lệ của sàn Kraken MMAS2 liên quan đến mapping mã tiền tệ `ZUSD` và phản hồi HTTP 200 kèm error body.
