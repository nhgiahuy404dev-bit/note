# 📊 TỔNG KẾT TUẦN 36 (31.08 - 06.09.2026)

> 📅 **Thời gian tổng kết:** 05/09/2026 10:40:35  
> 📁 **Tổng số ngày làm việc ghi nhận:** 2 ngày

---

## 🗓️ 1. Nhật ký hoạt động trong tuần (Daily Breakdown)

| Ngày | Thứ | Chủ đề chính | File ghi chú |
| :--- | :--- | :--- | :--- |
| 03/09/2026 | Thứ Năm | ⭐ Kiểm thử Fiat Withdrawal UI & E2E | [⭐Ghi chú 03092026 - Kiểm thử Fiat Withdrawal UI & E2E.md](./%E2%AD%90Ghi%20ch%C3%BA%2003092026%20-%20Ki%E1%BB%83m%20th%E1%BB%AD%20Fiat%20Withdrawal%20UI%20%26%20E2E.md) |
| 04/09/2026 | Thứ Sáu | ⭐ Kiến trúc 5 Waves & Ma trận Test Backend Fiat Withdrawal | [⭐Ghi chú 04092026 - Kiến trúc 5 Waves & Ma trận Test Backend Fiat Withdrawal.md](./%E2%AD%90Ghi%20ch%C3%BA%2004092026%20-%20Ki%E1%BA%BFn%20tr%C3%BAc%205%20Waves%20%26%20Ma%20tr%E1%BA%ADn%20Test%20Backend%20Fiat%20Withdrawal.md) |

---

## ✅ 2. Những việc đã làm trong tuần (What I Did)

### 📌 Thứ Năm (03/09/2026) - 📝 Ghi chú ngày 03/09/2026 (Thứ Năm)
- 🖥️ **UI Testing:** Kiểm thử thủ công toàn diện giao diện rút tiền Fiat (Fiat withdrawal) trên Transfer Tool theo bộ kịch bản chi tiết (`UI-1` đến `UI-9`).
- 📅 **Test case Update ngày:** Thao tác kiểm tra trường ngày (Update date / Value date) và xác minh hiển thị dữ liệu lịch sử theo mốc ngày cập nhật trên UI.
- 🔄 **E2E Testing (UI through Backend):** Kiểm tra luồng End-to-End từ bước khởi tạo lệnh trên UI, phê duyệt Checker, chuyển trạng thái đến khi Settled (`E2E-1` đến `E2E-4`).
- 🛡️ **Xác minh hợp đồng dữ liệu & UI Guards:** Kiểm tra việc lược bỏ `blockchainNetworkId`, hiển thị dấu em dash (`—`), bảo vệ nút Copy không gây vỡ console, và kiểm tra bẫy validation ngầm (`UI-9`).
- **Kỳ vọng:** Sau khi cronjob đồng bộ (`REG-1` backend) ghi nhận ngân hàng thụ hưởng, mở form rút tiền fiat trên UI sẽ thấy ngay tài khoản thụ hưởng trong dropdown `To` và tạo được draft lệnh.

### 📌 Thứ Sáu (04/09/2026) - 📝 Ghi chú ngày 04/09/2026 (Thứ Sáu)
- 🔍 **Nghiên cứu tài liệu Backend & Kiến trúc hệ thống:** Phân tích tài liệu kỹ thuật Transfer Tool Phase 5 (`BE`) và cơ chế khởi tạo lệnh rút tiền Fiat (`Fiat withdrawal initiation`).
- 🏗️ **Khảo sát kiến trúc 5 Waves:** Nắm vững phạm vi thay đổi từ Database Migration (Wave 1) đến Venue E2E (Wave 5).
- 📋 **Xây dựng Ma trận kịch bản kiểm thử (Test Scenarios Matrix):** Thiết kế chi tiết các test cases Backend qua 7 nhóm chức năng (`MIG`, `REG`, `REF`, `CRD`, `STP`, `EXE`, `STA`).
- 🛡️ **Rà soát các bẫy an toàn tiền tệ & Money Safety:** Kiểm tra kỹ cơ chế chặn Double-payment, Idempotency, chặn Machine-channel và Fail-closed lookups.
- **Hôm nay (04/09):** `[QA-6741]` (GTO-15979) — Backend Initiation Layer & Test Scenarios Matrix (tập trung 5 Waves, API, Database, Step Handler, Execution Service & Money Safety).

---

## 💡 3. Kiến thức & Điểm nổi bật (Key Learnings & Highlights)

### 🌟 Thứ Năm (03/09/2026) - 📝 Ghi chú ngày 03/09/2026 (Thứ Năm)
#### 🔹 2. Kiểm thử [QA-6742] - GTO-16043: Fiat withdrawal UI + E2E (Transfer Tool)
> [!NOTE]
> **Phương pháp thực hiện thực tế:** Tập trung thực hiện kiểm thử thủ công (Manual Testing) trên giao diện Transfer Tool và luồng E2E qua UI; không thực hiện automation endpoint / viết kịch bản BDD scenario do ưu tiên xác minh hành vi giao diện người dùng và tính toàn vẹn luồng trước.
#### 🔹 A. Ma trận kịch bản kiểm thử giao diện Frontend (UI Matrix)
- Ma trận/Bảng dữ liệu: Đã xây dựng & bao phủ **9 kịch bản chi tiết** (xem chi tiết trong file ghi chú ngày).
#### 🔹 B. Luồng kiểm thử End-to-End (E2E — UI through Backend)
- **`E2E-1`: UI-initiated Fiat Withdrawal to Settled**
- **Thao tác:** Khởi tạo lệnh rút tiền Fiat từ giao diện đến tài khoản ngân hàng thụ hưởng đã whitelist -> Xác nhận Review -> Thẩm định/Duyệt lệnh (Maker-Checker) -> Dispatch thực thi và chờ poller kiểm tra trạng thái.
- **Kỳ vọng:**
#### 🔹 C. Kiểm tra chi tiết case Update ngày (Value Date / Update Date)
- Thao tác chọn và cập nhật trường ngày (Update date / Value date / Ngày hiệu lực) trên form tạo yêu cầu rút tiền.
- Kiểm tra tính tương thích khi đổi ngày: form tính toán lại thời gian xử lý, không bị crash form hoặc vỡ layout date picker.
- Xác minh hiển thị mốc ngày cập nhật chính xác trên trang Review, trang Details và danh sách History Grid.
#### 🧠 Ghi nhớ chính
- **Phân biệt rạch ròi 2 folder tài liệu:**
- Đối với trường trống trên UI fiat, luôn dùng dấu em dash (`—`) thay vì gạch ngang ngắn (`-`) hoặc để trống gây crash khi copy.

### 🌟 Thứ Sáu (04/09/2026) - 📝 Ghi chú ngày 04/09/2026 (Thứ Sáu)
#### 🔹 1. Tổng quan nghiệp vụ & Kiến trúc 5 Waves [QA-6741] (GTO-15979)
- **Mục tiêu bài toán:**
- Chuyển số dư tiền pháp định (Fiat) từ các tài khoản sàn giao dịch trực tiếp (Direct Exchange accounts) của Galaxy về tài khoản ngân hàng thụ hưởng đã được phê duyệt trong danh sách trắng (Whitelisted Bank Beneficiary) thông qua hệ thống **Transfer Tool**.
- **Phân rã kiến trúc 5 Waves:**
#### 🔹 2. Ma trận kịch bản kiểm thử chi tiết (Backend Test Scenarios Matrix)
- Ma trận/Bảng dữ liệu: Đã xây dựng & bao phủ **22 kịch bản chi tiết** (xem chi tiết trong file ghi chú ngày).
#### 🔹 3. Các điểm mấu chốt kỹ thuật & Bẫy rủi ro (Key Technical Highlights & Pitfalls)
- **Chặn kênh tự động (Machine-channel refusal):**
- Rút tiền Fiat bắt buộc phải có sự can thiệp và xác nhận của con người (Human-in-the-loop / Maker-Checker qua UI).
- Mọi nỗ lực gọi qua API tự động (Machine API / Service-to-Service bot) đều phải bị chặn cứng (`Refused`) ngay tại `transfer-coordinator`.
#### 🧠 Ghi nhớ chính
- **Phân biệt 2 Ticket:**
- Đọc kỹ tài liệu trong thư mục `BE` khi viết kịch bản chi tiết hoặc log bug backend.

---

## ⏳ 4. Việc còn tồn đọng & Kế hoạch tuần tới (Pending & Next Focus)

- [ ] `[04/09/2026]` **[TEST DESIGN / TEST MATRIX] - [QA-6741]:** GTO-15979 - Fiat withdrawal initiation (Transfer Tool) — Phase 5

### 🎯 Kế hoạch trọng tâm tuần tiếp theo:
- [ ] Triển khai kiểm thử End-to-End thực tế khi môi trường tích hợp hoàn tất (PR 8425 + BE Waves).
- [ ] Thực thi Regression Suite cho các luồng Crypto Fireblocks.
- [ ] Đồng bộ Test Cases lên TestRail và cập nhật trạng thái Jira.

---
*Tự động tổng kết lúc 10:40:35 - 05/09/2026*
