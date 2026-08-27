# 📝 SỔ TAY QUY TRÌNH QA & AUTOMATION
**Ngày cập nhật:** 21/08/2026

---

## 1. QUY ƯỚC TẠO TASK (CẤU TRÚC ĐẶT TÊN)
*(Lưu ý: Luôn chủ động tuân thủ cấu trúc chuẩn khi tạo task)*

| Loại công việc | Định dạng tiêu đề task |
| :--- | :--- |
| **Chạy test execution** | `[TEST EXECUTION] - [ID__TICKET] TITLE` |
| **Làm task cho API-QA** | `[API-QA] - [ID__TICKET] TITLE` |
| **Làm task cho UI-QA** | `[UI-QA] - [ID__TICKET] TITLE` |

---

## 2. QUY TRÌNH QUẢN LÝ TESTRAIL

### 2.1. Tạo Test Cases
* **Lệnh thực hiện:** `/Create-Test-Cases-from-Confluent`
* **Thiết lập dự án:** 
  * `ProjectID`: **30**
  * Nếu project trong **GTO** và **QA** chứa cả 3 suite (UI, API, E2E) thì gọi cả 3.
* **Xử lý file lớn (Large Files):**
  * *Vấn đề:* Tránh dùng file local vì có thể lệch với file live, gây sai dữ liệu.
  * *Giải pháp:* Sử dụng lệnh `Current:disable-run`.
  * *Thao tác:* Create ➔ Copy ➔ Replace.
* **Phân loại & Tổng hợp:**
  * Sắp xếp Test Cases vào đúng nhóm: **API / UI / E2E**.
  * Yêu cầu hiển thị tóm tắt: *"Show Summary and API group"*.
* **Cập nhật hệ thống:**
  * Lấy ID dán vào **Jira** và **GTO**.
  * Chuyển trạng thái Automation thành **Candidate** (sẵn sàng tự động hóa).

### 2.2. Tạo Test Run
* **Lệnh thực hiện:** `/Create-TR-RUN-from-TR-Daraf` + Đánh dấu dự án **All Passed**.
* **Khởi tạo Run:**
  * Submit danh sách Test Case để estimate thời gian chạy.
  * Kiểm tra kỹ Project ID và Suite ID:
    * `ProjectID`: **30**
    * `Suite ID API`: **945**
    * `Suite ID UI`: **946**
    * `Suite ID E2E`: **947**
  * Kiểm tra lại toàn bộ status, đảm bảo tất cả đã chuyển sang **Passed**.

---

## 3. QUY TRÌNH ỨNG DỤNG AI TẠO SCENARIO (CHO AUTOMATION)
1. **Chuẩn bị dữ liệu (Check API):** Ghi chép đầy đủ log step:
   * Các đoạn code query SQL.
   * Dữ liệu xuất ra (output data).
   * Các câu lệnh API curl và response trả về.
   * Chi tiết dữ liệu đi kèm.
2. **Tổng hợp:** Chạy lệnh `/pr summary` (dùng AI tóm tắt lại).
3. **Tạo Scenario & Code:** Yêu cầu AI tạo Scenario, sau đó sinh code tương ứng cho từng class.
4. **Kiểm tra (Review):** Review kỹ mã nguồn và logic AI sinh ra.
5. **Cập nhật TestRail:** Tiến hành tạo test case trên TestRail.
6. **Báo cáo & Ghi nhận:**
   * Chạy lệnh `/pr summary`.
   * Dán nội dung báo cáo lên **GitHub**.
   * Vào **Confluence** dán link báo cáo (Hoàn thành phần nào, báo cáo dứt điểm phần đó).
   * Kiểm tra và set trạng thái cuối cùng.

---

## 4. QUY TRÌNH BÁO CÁO (DAILY REPORTING)
* **Lệnh thực hiện:** `/daily-report`
* **Quy tắc điền report:**
  * *Nếu có làm dự án:* Ghi rõ ràng, chi tiết tiến độ. Báo cáo dứt điểm theo từng phần (Ví dụ: hoàn tất việc của `api-qa`).
  * *Nếu không có thay đổi/không làm dự án:* Ghi chú: `"None cause not update anything on repos"`.
