# 📝 Ghi chú ngày 03/09/2026 (Thứ Năm)

---

## 🎯 Mục tiêu trong ngày
- [x] **[TEST EXECUTION] - [QA-6742]:** GTO-16043 - Fiat withdrawal UI + E2E (Transfer Tool)
  - 🖥️ **UI Testing:** Kiểm thử thủ công toàn diện giao diện rút tiền Fiat (Fiat withdrawal) trên Transfer Tool theo bộ kịch bản chi tiết (`UI-1` đến `UI-9`).
  - 📅 **Test case Update ngày:** Thao tác kiểm tra trường ngày (Update date / Value date) và xác minh hiển thị dữ liệu lịch sử theo mốc ngày cập nhật trên UI.
  - 🔄 **E2E Testing (UI through Backend):** Kiểm tra luồng End-to-End từ bước khởi tạo lệnh trên UI, phê duyệt Checker, chuyển trạng thái đến khi Settled (`E2E-1` đến `E2E-4`).
  - 🛡️ **Xác minh hợp đồng dữ liệu & UI Guards:** Kiểm tra việc lược bỏ `blockchainNetworkId`, hiển thị dấu em dash (`—`), bảo vệ nút Copy không gây vỡ console, và kiểm tra bẫy validation ngầm (`UI-9`).

---

## 📝 Ghi chú công việc / Study

### 🌿 1. Công thức tạo 1 branch mới trong Git
- **Tạo và chuyển sang nhánh mới luôn:**
  ```bash
  git checkout -b <ten-nhanh>
  # hoặc
  git switch -c <ten-nhanh>
  ```
- **Chỉ tạo nhánh mới:**
  ```bash
  git branch <ten-nhanh>
  ```
- **Đẩy nhánh mới lên remote (lần đầu):**
  ```bash
  git push -u origin <ten-nhanh>
  ```

---

### 🧪 2. Kiểm thử [QA-6742] - GTO-16043: Fiat withdrawal UI + E2E (Transfer Tool)

> [!NOTE]
> **Phương pháp thực hiện thực tế:** Tập trung thực hiện kiểm thử thủ công (Manual Testing) trên giao diện Transfer Tool và luồng E2E qua UI; không thực hiện automation endpoint / viết kịch bản BDD scenario do ưu tiên xác minh hành vi giao diện người dùng và tính toàn vẹn luồng trước.

#### 📋 A. Ma trận kịch bản kiểm thử giao diện Frontend (UI Matrix)

| Mã test | Tên kịch bản | Thao tác thực hiện (Action) | Kết quả kỳ vọng (Expected Result) |
| :--- | :--- | :--- | :--- |
| `UI-1` | **Blockchain Network Placeholder** | Chọn loại tài sản là Fiat (USD, EUR,...). | Trường chọn mạng Blockchain được ẩn hoặc vô hiệu hóa, giữ lại placeholder hiển thị thích hợp (`<Blockchain Network> placeholder left rendered`). |
| `UI-2` | **Destination Eligibility & Network-less** | Khi chọn fiat, mở dropdown `To`. Sau đó chọn tài sản crypto có cùng `currencyId` rồi mở lại dropdown `To`. Kiểm tra network request `ui/accountsWithVenue`. | - **Với Fiat:** Chỉ hiển thị các địa chỉ ngân hàng thụ hưởng (Whitelisted Bank Beneficiary) hợp lệ có `network = null`. Tuyệt đối không hiện ví/vault crypto.<br>- **Với Crypto:** Không được hiển thị tài khoản ngân hàng fiat.<br>- *Hai nhóm network-less và networked không bao giờ được lẫn lộn.* |
| `UI-3` | **Balances Fetched for Fiat** | Chọn tài sản fiat, mở dropdown `From`. Nhập số tiền lớn hơn số dư khả dụng. | - Danh sách tài khoản nguồn hiển thị đúng số dư khả dụng (không bị báo "Balance Unavailable").<br>- Danh sách sắp xếp giảm dần theo số dư.<br>- Hiển thị đúng footer `Balance as of ...`.<br>- Cảnh báo `"Amount exceeds the last polled balance"` khi nhập vượt số dư. |
| `UI-4` | **Draft Payload Omits Network Key** | Bật tab Network devtools, nhấn Review lệnh rút tiền fiat. Kiểm tra payload `instruction/create/draft` và màn hình Review. | - Payload gửi đi **hoàn toàn không có key** `blockchainNetworkId` (omitted hoàn toàn, không phải `null`, không phải `0`, không phải chuỗi rỗng).<br>- Tại màn hình Review, trường Blockchain Network hiển thị dấu gạch ngang dài em dash (`—`). |
| `UI-5` | **Details Page & Copy Guard** | Mở trang chi tiết lệnh (`ui/instruction/details/{id}`). Nhấn icon Copy ở trường có dữ liệu và trường trống. Mở browser console. | - Màn hình render bình thường dù thiếu network keys.<br>- Blockchain Network hiển thị em dash (`—`) và **không có** icon copy bên cạnh.<br>- Các trường trống (`Initiated By`, `Venue`) hiển thị em dash (`—`).<br>- **Không bị crash console:** Đã fix lỗi `value.toString()` khi click copy ở các ô trống. |
| `UI-6` | **History Grid & Pending Card** | Tìm lệnh fiat trên bảng lịch sử (History Grid) và thẻ chờ duyệt (Pending Card). Kiểm tra filter cột Network. | - Ô Blockchain Network để trống cho các dòng fiat (hành vi chủ đích, không phải lỗi).<br>- Bộ lọc cột Network có thêm lựa chọn ô trống (blank entry).<br>- Thẻ Pending Card hiển thị em dash (`—`) cho dòng Network. |
| `UI-7` | **Clone a Fiat Instruction** | Từ trang chi tiết lệnh fiat, nhấn nút **Clone**. Kiểm tra form pre-fill và nhấn Review. | - Form tự động điền đúng asset, tài khoản gửi/nhận, số tiền và loại chuyển tiền.<br>- Submit Review thành công, payload của bản draft clone cũng lược bỏ key `blockchainNetworkId`. |
| `UI-8` | **Crypto is Unaffected** | Thực hiện tạo và clone lệnh với tiền mã hóa (BTC, ETH). | Các luồng crypto hoạt động bình thường như cũ: hiển thị tên mạng, câu tóm tắt có mệnh đề `on <network>`, và payload vẫn gửi kèm `blockchainNetworkId`. |
| `UI-9` | **Known Trap - Silent Nested Validation** | Kích hoạt lỗi validation ở một trường dữ liệu lồng sâu (nested field - không phải top-level) rồi nhấn Review. | Nút submit bị chặn mà không hiện thông báo lỗi trực quan (do FormField chỉ đọc lỗi cấp cao nhất). Đây là hành vi tồn tại từ trước (pre-existing), ghi nhận lại để theo dõi chứ không log bug mới. |

---

#### 🔄 B. Luồng kiểm thử End-to-End (E2E — UI through Backend)
*(Điều kiện chạy: Môi trường triển khai đồng bộ PR 8425 của FE và các Wave backend của GTO-15979)*

1. **`E2E-1`: UI-initiated Fiat Withdrawal to Settled**
   - **Thao tác:** Khởi tạo lệnh rút tiền Fiat từ giao diện đến tài khoản ngân hàng thụ hưởng đã whitelist -> Xác nhận Review -> Thẩm định/Duyệt lệnh (Maker-Checker) -> Dispatch thực thi và chờ poller kiểm tra trạng thái.
   - **Kỳ vọng:**
     - Backend Coordinator chấp nhận payload không có `blockchainNetworkId`.
     - Trạng thái lệnh tiến triển tuần tự trên UI: `DRAFT` ➔ `PENDING_APPROVAL` ➔ `QUEUED` ➔ `INITIATED` ➔ `SUCCESS`.
     - Mã tham chiếu `s_unique_ref` từ venue được gắn chuẩn xác, poller phân giải trạng thái thành công và phản ánh lên UI.
2. **`E2E-2`: Hợp đồng dữ liệu Null vs Undefined (Contract Validation)**
   - **Kỳ vọng:**
     - `ui/currenciesWithBlockchainNetworks` & `ui/accountsWithVenue`: Trả về `null` rõ ràng cho network của fiat (không trả về synthetic network ID giả mạo để tránh làm vỡ logic lọc dropdown).
     - `ui/instruction/details/{id}`: Lược bỏ key network (nhận vào dạng `undefined`).
     - Outbound Draft Request: Không chứa trường `blockchainNetworkId`.
3. **`E2E-3`: Hiển thị tài khoản thụ hưởng Whitelist (Selectable Beneficiary)**
   - **Kỳ vọng:** Sau khi cronjob đồng bộ (`REG-1` backend) ghi nhận ngân hàng thụ hưởng, mở form rút tiền fiat trên UI sẽ thấy ngay tài khoản thụ hưởng trong dropdown `To` và tạo được draft lệnh.
4. **`E2E-4`: Xử lý các nhánh từ chối và hủy lệnh (Refusal & Abort Paths)**
   - **Kỳ vọng:**
     - Checker từ chối duyệt ➔ Lệnh chuyển `REJECTED` ngay trên UI.
     - Người dùng bấm Abort khi lệnh đang ở `QUEUED` ➔ Chuyển `ABORTED`.
     - Cố tình Abort khi lệnh đã ở `INITIATED` ➔ Bị từ chối với thông báo cảnh báo rõ ràng trên UI (không chạy ngầm vô hiệu khiến user tưởng nhầm là đã hủy).
     - Sàn trả về lỗi nghiệp vụ dạng HTTP 200 ➔ UI hiển thị trạng thái `FAILED` kèm nội dung thông báo từ sàn, tuyệt đối không hiển thị thành công.

---

#### 📅 C. Kiểm tra chi tiết case Update ngày (Value Date / Update Date)
- Thao tác chọn và cập nhật trường ngày (Update date / Value date / Ngày hiệu lực) trên form tạo yêu cầu rút tiền.
- Kiểm tra tính tương thích khi đổi ngày: form tính toán lại thời gian xử lý, không bị crash form hoặc vỡ layout date picker.
- Xác minh hiển thị mốc ngày cập nhật chính xác trên trang Review, trang Details và danh sách History Grid.

---

#### 🎯 D. Tiêu chí ký duyệt hoàn thành (Sign-off Criteria)
- [x] **UI-2 Green (2 chiều):** Beneficiary ngân hàng chọn được khi rút fiat; không bị lẫn lộn giữa tài sản fiat và crypto.
- [x] **UI-4 & E2E-2 Green:** Lược bỏ sạch `blockchainNetworkId` ở outbound payload, hiển thị dấu em dash (`—`) trên màn hình review, cấu trúc API khớp đúng hợp đồng null/undefined.
- [x] **UI-5 Green (Clean Console):** Không crash `value.toString()` khi copy ô trống; hiển thị em dash (`—`) thay vì để khoảng trắng lỗi.
- [x] **E2E-1 Green:** Chứng minh thành công tối thiểu 1 luồng rút tiền fiat hoàn chỉnh từ bước tạo trên UI đến khi poller xác nhận hoàn tất.

---

## 💡 Ghi nhớ / Ideas
- **Phân biệt rạch ròi 2 folder tài liệu:**
  - **Folder `FE`:** Phục vụ ticket `[QA-6742]` (GTO-16043) — Giao diện Transfer Tool, form nhập liệu, validation, case Update ngày và kiểm thử E2E qua UI.
  - **Folder `BE`:** Phục vụ ticket `[QA-6741]` (GTO-15979) — Khởi tạo tầng Backend, 5 Waves kiến trúc, Database migration, Step handler, Execution payload 4 sàn và Money safety.
- Nhớ lưu ý bẫy `UI-9`: validation ở trường con bị ẩn lỗi, không phải bug mới mà là cơ chế cũ của component FormField.
- Đối với trường trống trên UI fiat, luôn dùng dấu em dash (`—`) thay vì gạch ngang ngắn (`-`) hoặc để trống gây crash khi copy.

---
*Cập nhật bổ sung nội dung FE vào lúc 10:38:00 - 04/09/2026*
