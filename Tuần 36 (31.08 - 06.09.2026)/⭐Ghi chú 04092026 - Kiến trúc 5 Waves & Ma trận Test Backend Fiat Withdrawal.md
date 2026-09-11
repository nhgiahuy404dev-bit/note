# 📝 Ghi chú ngày 04/09/2026 (Thứ Sáu)

---

## 🎯 Mục tiêu trong ngày
- [ ] **[TEST DESIGN / TEST MATRIX] - [QA-6741]:** GTO-15979 - Fiat withdrawal initiation (Transfer Tool) — Phase 5
  - 🔍 **Nghiên cứu tài liệu Backend & Kiến trúc hệ thống:** Phân tích tài liệu kỹ thuật Transfer Tool Phase 5 (`BE`) và cơ chế khởi tạo lệnh rút tiền Fiat (`Fiat withdrawal initiation`).
  - 🏗️ **Khảo sát kiến trúc 5 Waves:** Nắm vững phạm vi thay đổi từ Database Migration (Wave 1) đến Venue E2E (Wave 5).
  - 📋 **Xây dựng Ma trận kịch bản kiểm thử (Test Scenarios Matrix):** Thiết kế chi tiết các test cases Backend qua 7 nhóm chức năng (`MIG`, `REG`, `REF`, `CRD`, `STP`, `EXE`, `STA`).
  - 🛡️ **Rà soát các bẫy an toàn tiền tệ & Money Safety:** Kiểm tra kỹ cơ chế chặn Double-payment, Idempotency, chặn Machine-channel và Fail-closed lookups.

---

## 📝 Ghi chú công việc / Study

### 🏛️ 1. Tổng quan nghiệp vụ & Kiến trúc 5 Waves [QA-6741] (GTO-15979)

- **Mục tiêu bài toán:**
  - Chuyển số dư tiền pháp định (Fiat) từ các tài khoản sàn giao dịch trực tiếp (Direct Exchange accounts) của Galaxy về tài khoản ngân hàng thụ hưởng đã được phê duyệt trong danh sách trắng (Whitelisted Bank Beneficiary) thông qua hệ thống **Transfer Tool**.
  - **Phụ thuộc cốt lõi:** Phụ thuộc vào `GTO-15470` (Mô hình danh sách trắng tài khoản sàn giao dịch - Exchange Account Whitelist Model).

- **Phân rã kiến trúc 5 Waves:**
  1. **Wave 1: Migration & Seed (Database & Reference Data)**
     - Khôi phục 3 account classes: `FB_EXTERNAL_ADDR`, `EXCHANGE_WD_FIAT`, `EXCHANGE_WD_CRYPTO`.
     - Áp dụng mô hình Asset Option C: `reference.t_source_system_supported_asset`, view `v_source_system_supported_asset`, loại bỏ bảng `t_venue_asset_mapping`.
     - Seed tối thiểu 22 dòng dữ liệu (10 fiat qua 4 sàn: Bitstamp, Bullish, Coinbase, Kraken + 12 crypto LMAX).
     - Ràng buộc duy nhất: `NULLS NOT DISTINCT` trên `t_account_supported_asset` và `t_fireblocks_supported_asset`.
     - Bổ sung Step Type mới: `DIRECT_EXCHANGE -> FIAT_BANK`.
  2. **Wave 2: Registry & Reference Service**
     - `transfer-tool-account-registry`: Adapter đăng ký điểm đến fiat thành tài khoản Transfer Tool (`s_address` và `s_memo` là `null`; đảm bảo tính `Idempotent` khi reconcile).
     - `transfer-tool-reference-service`: Query tài sản trả về fiat với thuộc tính `network = null`; API endpoint: `GET /internal/accounts/{ttAccountId}?include=fiatDestination` trả về thông tin chi tiết ngân hàng thụ hưởng (`bankName`, `accountNumber`, `iban`, `swift`,...).
  3. **Wave 3: Coordinator & Step Handler**
     - `transfer-coordinator`: Validation dữ liệu fiat; từ chối kênh máy móc (`machine channel` bị chặn hoàn toàn, chỉ cho phép UI/User); loại bỏ điều kiện bắt buộc có `network_id` khi tài sản là fiat; kiểm tra khớp loại tiền (currency match).
     - `transfer-step-handler`: Rẽ nhánh định tuyến (route branch) phía trước guard exchange-to-exchange; builder tạo bước `DIRECT_EXCHANGE -> FIAT_BANK`; response execute mang theo symbol sàn và thông tin ngân hàng thụ hưởng (không lưu thông tin nhạy cảm vào DB).
  4. **Wave 4: Execution Service**
     - `transfer-execution-service`: Đảo ngược cơ chế dispatch (trước đây Fireblocks là mặc định, nay direct exchange được định tuyến riêng qua bảng map base-URL theo từng venue code).
     - Xây dựng Payload Builder và Response Handler riêng cho 4 sàn: **Kraken (MMAS2)**, **Coinbase**, **Bullish**, **Bitstamp**.
     - Xử lý mã tiền tệ đặc thù (ví dụ: `ZUSD` vs `USD` đối với sàn Kraken).
  5. **Wave 5: Lifecycle & Venue E2E**
     - Vòng đời giao dịch hoàn chỉnh và kiểm thử tích hợp trực tiếp với từng sàn (ưu tiên triển khai Kraken MMAS2 đầu tiên, sau đó đến Coinbase, Bullish, Bitstamp).

---

### 🧪 2. Ma trận kịch bản kiểm thử chi tiết (Backend Test Scenarios Matrix)

| Nhóm kiểm thử | Mã kịch bản | Tên kịch bản | Phạm vi & Điều kiện kiểm tra | Kết quả kỳ vọng |
| :--- | :--- | :--- | :--- | :--- |
| **Migration & Seed** | `MIG-1` | DDL & Constraints Verification | Kiểm tra schema DB sau migration: kiểm tra 3 account classes và ràng buộc `NULLS NOT DISTINCT`. | Ràng buộc DB hoạt động chuẩn xác, ngăn chặn duplicate với giá trị null. |
| | `MIG-2` | Reference Seed Integrity | Xác minh dữ liệu seed cho `EXCHANGE_WD_FIAT`, `EXCHANGE_WD_CRYPTO`, `FB_EXTERNAL_ADDR`. | Dữ liệu tham chiếu tồn tại đầy đủ, metadata chính xác. |
| | `MIG-3` | Asset Seed Verification | Kiểm tra 22 rows seed tối thiểu (10 fiat qua 4 sàn + 12 LMAX crypto) qua view `v_source_system_supported_asset`. | Asset map đúng venue, không bị thiếu symbol nào. |
| **Account Registry** | `REG-1` | Whitelist Beneficiary ➔ TT Account | Sync tài khoản ngân hàng thụ hưởng đã whitelist từ Core sang Transfer Tool. | Tài khoản TT được tạo với class `EXCHANGE_WD_FIAT`, `s_address` = null, `s_memo` = null. |
| | `REG-2` | Reconcile Idempotency | Kích hoạt job reconcile nhiều lần liên tiếp với cùng một tập dữ liệu nguồn. | Không tạo bản ghi trùng lặp, cập nhật timestamp đúng chuẩn. |
| | `REG-3` | Skip Invalid Paths | Gặp bản ghi chưa duyệt whitelist hoặc dữ liệu ngân hàng bị thiếu/sai format. | Cleanly skip, ghi log cảnh báo chi tiết, không crash service. |
| **Reference Service** | `REF-1` | Currency Picker Fiat Network Null | Gọi API lấy danh sách tiền tệ hỗ trợ cho tài khoản nguồn fiat. | Trả về tài sản fiat (USD, EUR,...) với trường `network = null`. |
| | `REF-2` | G3 Default Mismatch Handling | Kiểm tra logic lọc tài sản mặc định để tránh trùng lặp. | Trả về danh sách duy nhất, không duplicate currency options. |
| | `REF-3` | Beneficiary Bank Detail Opt-in | Gọi `GET /internal/accounts/{id}?include=fiatDestination`. | Trả về đúng payload object `fiatDestination` gồm bank name, account number, SWIFT/IBAN. |
| **Transfer Coordinator** | `CRD-1` | Draft Creation & Park for Review | Tạo yêu cầu rút tiền fiat từ UI với đủ thông tin hợp lệ. | Tạo Draft thành công, chuyển sang trạng thái `PENDING_APPROVAL`. |
| | `CRD-2` | Idempotency & Asset Mismatch Refusal | **Case 1:** Call create UI 2 lần cho cùng 1 `instructionId` không sinh instruction mới.<br>**Case 2:** Chọn `to address` khác asset (VD: USD chọn to address EUR) phải trả lỗi 400. | Đảm bảo tính Idempotent không duplicate lệnh, từ chối lệch asset và không ghi DB rác. |
| | `CRD-3` | Permissions Default Deny | User không có quyền `EXCHANGE_WD_FIAT` cố tình khởi tạo lệnh rút tiền. | Bị từ chối truy cập (403 Forbidden / Access Denied). |
| **Step Handler** | `STP-1` | Fiat Leg Planning | Lập kế hoạch bước chuyển (step planning) cho luồng `DIRECT_EXCHANGE -> FIAT_BANK`. | Rẽ nhánh thành công trước guard exchange-to-exchange thông thường. |
| | `STP-2` | Self-Addressed Step Refusal | Tạo lệnh với tài khoản đích trùng với tài khoản nguồn. | Bị từ chối, không sinh step tự chuyển cho chính mình. |
| | `STP-3` | Execute Response Completeness | Step Handler trả response về cho Execution Service. | Đầy đủ venue symbol và thông tin ngân hàng trong memory, không persist thông tin nhạy cảm vào DB. |
| **Execution Service** | `EXE-1` | Inverted Dispatch Routing | Dispatch lệnh rút tiền direct exchange. | Route thẳng đến Exchange Adapter tương ứng, không gửi sang Fireblocks. |
| | `EXE-2` | Per-Venue Payload Matrix | Kiểm tra payload build cho 4 sàn: Kraken (MMAS2), Coinbase, Bullish, Bitstamp. | Định dạng JSON và trường dữ liệu khớp chuẩn API từng sàn (Kraken map `ZUSD`). |
| | `EXE-3` | Missing Mandatory Data Refusal | Thiếu trường bắt buộc của sàn (ví dụ thiếu mã Bank Wire ID). | Bị từ chối ở bước pre-dispatch, không gửi request lỗi lên sàn. |
| **State Lifecycle & Safety** | `STA-1` | Happy Path Lifecycle | Theo dõi luồng trạng thái từ đầu đến cuối của giao dịch hợp lệ. | `DRAFT` ➔ `PENDING_APPROVAL` ➔ `QUEUED` ➔ `INITIATED` ➔ `SUCCESS`. |
| | `STA-2` | Terminal States Before Dispatch | Lệnh bị từ chối duyệt (`REJECTED`) hoặc bị hủy (`ABORTED`). | Chuyển trạng thái terminal đúng, giải phóng các lock tài nguyên. |
| | `STA-3` | Double-Payment Guards | Gửi trùng request hoặc trigger webhook lặp (replay). | Idempotency guard kích hoạt, ngăn chặn tuyệt đối việc rút tiền 2 lần. |
| | `STA-4` | Adverse Venue Replies | Sàn trả về lỗi HTTP 4xx, 5xx hoặc HTTP 200 kèm error message trong body. | Bắt đúng lỗi, cập nhật trạng thái `FAILED`, không tự ý retry với các lỗi non-idempotent. |

---

### 🛡️ 3. Các điểm mấu chốt kỹ thuật & Bẫy rủi ro (Key Technical Highlights & Pitfalls)

1. **Chặn kênh tự động (Machine-channel refusal):**
   - Rút tiền Fiat bắt buộc phải có sự can thiệp và xác nhận của con người (Human-in-the-loop / Maker-Checker qua UI).
   - Mọi nỗ lực gọi qua API tự động (Machine API / Service-to-Service bot) đều phải bị chặn cứng (`Refused`) ngay tại `transfer-coordinator`.

2. **Cơ chế Fail-closed Lookups:**
   - Trong quá trình phân giải tài khoản hoặc thông tin ngân hàng thụ hưởng, nếu dữ liệu bị thiếu hoặc không khớp 100%, hệ thống phải dừng lại ngay lập tức (`Fail-closed`), tuyệt đối không được dùng giá trị mặc định (fallback default).

3. **Tính Idempotency & An toàn tiền tệ (Money Safety):**
   - Việc rút tiền fiat trực tiếp từ sàn tiềm ẩn rủi ro chuyển tiền thật ra khỏi sàn về tài khoản ngân hàng.
   - Phải kiểm tra chặt chẽ khóa chống trùng lệnh (`Idempotency Key`) ở cả phía Transfer Tool lẫn khi gọi sang sàn đối tác.
   - Xử lý chính xác các trường hợp sàn trả về HTTP 200 nhưng payload bên trong báo lỗi (`HTTP 200 OK with error payload`).

4. **Xử lý mã tiền tệ sàn (Venue Symbol Mapping):**
   - Lưu ý đặc thù sàn Kraken sử dụng mã tiền tệ nội bộ (ví dụ: `ZUSD` cho USD). Service phải chuyển đổi chính xác giữa mã chuẩn quốc tế và mã riêng của venue trước khi gửi request dispatch.

---

## 💡 Ghi nhớ / Ideas
- **Phân biệt 2 Ticket:**
  - **Hôm qua (03/09):** `[QA-6742]` (GTO-16043) — Manual UI + E2E testing (tập trung giao diện, form nhập liệu, case Update ngày).
  - **Hôm nay (04/09):** `[QA-6741]` (GTO-15979) — Backend Initiation Layer & Test Scenarios Matrix (tập trung 5 Waves, API, Database, Step Handler, Execution Service & Money Safety).
- Đọc kỹ tài liệu trong thư mục `BE` khi viết kịch bản chi tiết hoặc log bug backend.
- Chú ý các case bảo vệ tiền tệ (Money Safety): Replay attack, Double-payment, Chặn machine channel.

---
*Cập nhật vào lúc 10:30:00 - 04/09/2026*
