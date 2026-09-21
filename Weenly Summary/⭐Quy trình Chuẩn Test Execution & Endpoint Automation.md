# ⭐ SỔ TAY TỔNG HỢP QUY TRÌNH CHUẨN: TEST EXECUTION & ENDPOINT AUTOMATION TESTING

Tài liệu này tổng hợp toàn diện, chi tiết và chuẩn hóa 100% hai quy trình kiểm thử cốt lõi trong dự án: **Quy trình Test Execution (Ticket Thường / UI-QA / Feature)** và **Quy trình Endpoint Automation Testing (API Backend)**.

---

## 📑 MỤC LỤC
1. [Bảng So Sánh & Nhận Diện Hai Quy Trình](#1-bảng-so-sánh--nhận-diện-hai-quy-trình)
2. [Quy Trình Chuẩn Test Execution (Workflow 2 - 8 Bước Chi Tiết)](#2-quy-trình-chuẩn-test-execution-workflow-2---8-bước-chi-tiết)
3. [Quy Trình Chuẩn Endpoint Automation Testing (Workflow 1 - 15 Bước Chi Tiết)](#3-quy-trình-chuẩn-endpoint-automation-testing-workflow-1---15-bước-chi-tiết)
4. [Sổ Tay Tra Cứu Nhanh Cấu Hình & Lưu Ý Nghiệp Vụ Trọng Yếu](#4-sổ-tay-tra-cứu-nhanh-cấu-hình--lưu-ý-nghiệp-vụ-trọng-yếu)

---

## 1. BẢNG SO SÁNH & NHẬN DIỆN HAI QUY TRÌNH

| Tiêu chí | Quy Trình Test Execution (Workflow 2) | Quy Trình Endpoint Automation (Workflow 1) |
| :--- | :--- | :--- |
| **Loại ticket áp dụng** | Ticket kiểm thử chức năng, UI, logic nghiệp vụ, APM, regression (`[TEST EXECUTION]`, `[UI-QA]`, `GTO-xxxx`). | Ticket viết test tự động cho API backend có endpoint cụ thể (`[API-QA]`, `endpoint`, `automation BE`). |
| **Tổng số bước** | **8 bước chuẩn** (từ Bước 0 đến Bước 7) | **15 bước chuẩn** (từ Bước 1 đến Bước 15) |
| **Hành động khởi đầu** | **Pre-check với Dastan trên Slack** (hỏi xem đã tạo draft ticket/test cases chưa để chống duplicate). | **Tạo Test Scenario Prompt** để AI phân tích API spec (sinh kịch bản 4 tầng logic). |
| **Công cụ sinh kịch bản** | Claude Slash Command: `/create-draft-test-execution` | AI Prompt đọc spec sinh Scenarios 4 tầng logic. |
| **Cấu hình Jira bắt buộc** | - Linked Work Items: Trạng thái **`tests`** ➔ Link tới **Request Ticket** (`GTO-xxxx`).<br>- Epic cha: **`QA-3614: Transfer Tools Enhancement and feedback`**. | Cập nhật các trạng thái: `In Project` ➔ `Under Review` ➔ `Done` ✅ sau khi merge code vào `main`. |
| **Đồng bộ Confluence** | Chạy lệnh `/create-test-artifact` ngay sau khi cập nhật Jira. | Không tạo Test Artifact riêng (kết quả lưu qua PR và TestRail). |
| **Quy tắc Nghiệm thu (Sign-off)** | Kiểm thử Staging Pass 100% ➔ **Sign-off Jira sang `Pass Test` ✅ TRƯỚC** ➔ Mới gửi Dev Review & UAT ➔ Mới làm TestRail. | Viết code, chạy local test suite Pass 100% ➔ Tạo PR gán Dastan review ➔ Merge `main` ➔ Chuyển sang `Done` ✅. |
| **Thông báo Review & UAT** | - Gửi Dev review xác nhận test section.<br>- Nhắn Slack cho Ops (**@tiffany.kao**, **@jento.chan**) nhờ test UAT. | Gán Dastan review PR, nhận feedback và resolve bằng `/resolve-pr`. |
| **Đồng bộ TestRail** | - Sau khi Dev review OK.<br>- `/Create-testrail-cases-from-confluence` ➔ `/Create-TR-Run-From-TR-Draft`. | - Trong quá trình code test script.<br>- `/create-testrail` ➔ `/sync-testrail` link trực tiếp vào Jira. |

---

## 2. QUY TRÌNH CHUẨN TEST EXECUTION (WORKFLOW 2 - 8 BƯỚC CHI TIẾT)

> [!NOTE]
> **Nhận diện ticket:** Áp dụng cho các ticket có tag `[TEST EXECUTION]`, `[UI-QA]`, hoặc các ticket chức năng/giao diện chung (`GTO-xxxx`).

### 🔹 Bước 0: Pre-check với Dastan (Bắt buộc - Chống Duplicate)
* **Thời điểm:** Trước khi bắt tay tạo draft hay làm bất cứ thao tác nào trên Jira / TestRail.
* **Mục đích:** Chống tạo trùng lặp ticket trên Jira, trùng kịch bản trên TestRail hoặc xung đột dữ liệu kiểm thử.
* **Thao tác:** Bắt buộc nhắn tin trực tiếp hỏi Dastan trên Slack xem anh ấy đã tạo draft ticket hoặc draft test cases cho ticket đó chưa.
  * Nếu Dastan đã tạo ➔ Tiếp nhận bản draft của Dastan để hoàn thiện tiếp.
  * Nếu Dastan xác nhận chưa tạo ➔ Bắt đầu tiến hành Bước 1.

> [!TIP]
> **Mẫu tin nhắn Slack chuẩn gửi Dastan:**  
> *"Hi Dastan, for ticket `<TICKET_ID>` (`<TICKET_NAME>`), have you created the draft ticket or test cases yet? If not, I will start creating the draft test execution."*

---

### 🔹 Bước 1: Khởi tạo Draft qua Claude (`/create-draft-test-execution`)
* **Thời điểm:** Sau khi Dastan xác nhận chưa tạo draft.
* **Thao tác:**
  * Thu thập đầy đủ tài liệu đặc tả: Jira Ticket yêu cầu, tài liệu Confluence spec, Pull Request (PR) diff của Dev.
  * Chạy slash command:
    ```bash
    /create-draft-test-execution
    ```
  * AI đọc tài liệu đặc tả và tự động sinh file markdown (`.md`) chứa kịch bản nháp.
  * Chuyển trạng thái ticket Jira sang **`In Progress`**.

---

### 🔹 Bước 2: Rà soát & Hoàn thiện kịch bản trên VS Code
* **Thời điểm:** Sau khi file markdown kịch bản nháp được sinh ra.
* **Thao tác:** Mở file markdown trực tiếp trên **Visual Studio Code (VS Code)** để rà soát chi tiết:
  * Kiểm tra tính logic và chặt chẽ của **Preconditions** (điều kiện tiên quyết), **Test Steps** (các bước thực hiện), **Expected Results** (kết quả mong đợi).
  * Bổ sung đầy đủ các phân tầng kiểm thử: Happy Path, Negative cases, Boundary (điều kiện biên), Phân quyền tài khoản (Roles/Grants), Xử lý lỗi hệ thống & timeout.

---

### 🔹 Bước 3: Chuẩn hóa Description, Bảng Kịch Bản & Liên Kết Ticket trên Jira
* **Thời điểm:** Sau khi kịch bản đã được rà soát hoàn chỉnh trên VS Code.
* **Thao tác:**
  1. **Dán nội dung kịch bản:** Đưa bảng Markdown chuẩn (`ID`, `Scenario`, `Precondition`, `Steps`, `Expected Results`) vào phần Description hoặc Test Section của Jira Ticket.
  2. **Ghi rõ Endpoint API:** Khi kịch bản có tương tác với API backend, **bắt buộc phải ghi rõ Endpoint** (`URL`, `Method`, `Payload`) để xác định chính xác endpoint được gọi và cơ chế thực thi.
  3. **Cấu hình Linked Work Items (Quy tắc bắt buộc):**
     * Trong mục **Linked Issues** / **Linked Work Items** trên Jira:
     * Chọn loại quan hệ (Link Type) là: **`tests`**.
     * Liên kết trực tiếp tới **Request Ticket** tương ứng (ví dụ: `QA-xxxx` **tests** `GTO-xxxx`).
  4. **Liên kết Epic cha (Bắt buộc):** Chỉnh sửa ticket và liên kết vào đúng Epic cha:
     * **`QA-3614: Transfer Tools Enhancement and feedback`**.
  5. **Cập nhật trạng thái Ticket Jira:** Chuyển trạng thái ticket Jira sang **`Designing`** để xác nhận kịch bản đã được đưa lên hệ thống và đang trong giai đoạn thiết kế hoàn tất.

> [!IMPORTANT]
> **Quy tắc vàng tại Bước 3:**
> * Chuyển trạng thái ticket Jira sang **`Designing`**.
> * Tuyệt đối không được quên cấu hình **Linked Work Items** (chọn mối quan hệ là `tests` trỏ vào Request Ticket) và gắn đúng **Epic cha** `QA-3614: Transfer Tools Enhancement and feedback`.
> * Bắt buộc ghi rõ **Endpoint API** (`URL`, `Method`, `Payload`) khi mô tả các API call.

---

### 🔹 Bước 4: Tạo Test Artifact sang Confluence (`/create-test-artifact`) & Đổi Trạng Thái Jira (`Testing` 🚀)
* **Thời điểm:** **Thực hiện ngay sau khi cập nhật xong nội dung Jira Ticket (Bước 3).**
* **Thao tác:**
  1. Chạy lệnh slash command:
     ```bash
     /create-test-artifact
     ```
  2. Tự động đồng bộ toàn bộ tài liệu đặc tả kiểm thử sang trang Confluence của dự án, phục vụ lưu trữ tập trung và đối soát kỹ thuật.
  3. **Chuyển trạng thái ticket Jira:** Cập nhật trạng thái ticket Jira sang **`Testing`** 🚀 để sẵn sàng cho việc thực thi kiểm thử trên môi trường test.
* **Mục đích:** Đồng bộ tài liệu sang Confluence và chuyển ticket sang trạng thái `Testing` để bắt đầu thực thi test.

---

### 🔹 Bước 5: Thực thi Kiểm thử trên Staging & Nghiệm thu (Sign-off) Hoàn tất Ticket Jira (`Pass Test` ✅)
* **Thời điểm:** Khi ticket đã ở trạng thái **`Testing`** 🚀 và Dev hoàn tất build/deploy bản test lên môi trường Staging.
* **Thao tác:**
  * Tiến hành thực thi kiểm thử thực tế trên Staging theo toàn bộ kịch bản đã chuẩn bị (bao gồm Functional test, UI, API, Polling/Trace và Regression test các vùng liên quan).
  * Chụp ảnh màn hình actual UI, lưu log response làm evidence.
  * **Nghiệm thu (Sign-off) & Hoàn tất Ticket Jira:**  
    Khi kiểm thử thực tế đạt kết quả 100% Passed ➔ Chuyển trạng thái ticket Jira sang **`Pass Test`** ✅ và tag các reviewer phụ trách (**Dastan**, **Mohit**, **Sandeep**).

> [!IMPORTANT]
> **Nguyên tắc Sign-off First:** Bắt buộc nghiệm thu ticket trên Jira sang **`Pass Test`** ✅ xong xuôi thì mới được chuyển sang làm Bước 6 (Gửi Review) và Bước 7 (Tạo TestRail).

---

### 🔹 Bước 6: Gửi Dev Review & Thông báo UAT Testing cho Ops (@tiffany.kao, @jento.chan) qua Slack
* **Thời điểm:** ⚠️ **Nghiệm thu (Sign-off) & Hoàn tất Ticket Jira (`Pass Test` ✅) trên môi trường QA xong xuôi mới thực hiện bước này.**
* **Thao tác gồm 2 phần:**
  1. **Gửi Dev Review:** Nhắn tin trên Slack cho Dev phụ trách thông báo ticket đã Pass Test và gửi kèm link Jira/Confluence để Dev review xác nhận:
     > 💬 *"Hi @<dev_name>, ticket `<TICKET_KEY>` has been tested and passed (Pass Test ✅). Here is the detailed test section: `<Jira_Link>`. Could you please help review? Thank you!"*
  2. **Thông báo UAT Testing cho Ops (`@tiffany.kao` & `@jento.chan`):**  
     Khi đã hoàn tất kiểm thử trên môi trường QA và tính năng đã được setup sẵn sàng trên môi trường UAT, gửi tin nhắn Slack tag đích danh **Ops** (**@tiffany.kao** và **@jento.chan**) nhờ test trên UAT theo mẫu:

> [!NOTE]
> **Mẫu tin nhắn Slack thông báo UAT Testing chuẩn (như ảnh thực tế):**  
> ```text
> hi @tiffany.kao , @jento.chan we have completed testing for <TICKET_KEY_AND_TITLE> on QA environment. And we already set it up on UAT environment, please help testing it on UAT. Thank you! 🙏
> UAT UI deployed at: web-reports.uat-gp.galaxydigital.io/fund_transfer_tool
> ```
> *(Đính kèm thẻ preview Jira Cloud của ticket tương ứng, ví dụ: Task `GTO-16167`)*

* **Mục đích:** Dev xác nhận review OK kết quả test thực tế và Ops (@tiffany.kao, @jento.chan) tiến hành kiểm thử nghiệm thu trên môi trường UAT.

---

### 🔹 Bước 7: Tạo Test Case & Test Run trên TestRail (`/Create-testrail-cases-from-confluence` & `/Create-TR-Run-From-TR-Draft`)
* **Thời điểm:** ⚠️ **Sau khi Dev đã review OK xong xuôi, lúc này mới bắt đầu làm bước 7 (TestRail).**
* **Cấu hình TestRail:** Project ID `30`, chọn đúng Suite ID:
  * `Suite ID API`: **945**
  * `Suite ID UI`: **946**
  * `Suite ID E2E`: **947**
* **Thao tác 2 công đoạn bắt buộc (Theo đúng trình tự):**
  1. **Công đoạn 1 - Sinh Markdown Draft Test Cases:** Chạy lệnh:
     ```bash
     /Create-testrail-cases-from-confluence
     ```
     AI đọc tài liệu Confluence spec & Jira ticket để sinh file markdown (`.md`) chứa draft test cases chuẩn format TestRail.
  2. **Công đoạn 2 - Tạo Test Run & Import Cases Chính Thức:** Sau khi đã có file draft `.md`, chạy tiếp lệnh:
     ```bash
     /Create-TR-Run-From-TR-Draft
     ```
     Lệnh này tự động import toàn bộ test cases vào TestRail theo đúng Suite ID tương ứng, khởi tạo Test Run chính thức và đính kèm evidence kết quả kiểm thử (All Passed ✅).

---

## 3. QUY TRÌNH CHUẨN ENDPOINT AUTOMATION TESTING (WORKFLOW 1 - 15 BƯỚC CHI TIẾT)

> [!NOTE]
> **Nhận diện ticket:** Áp dụng cho mọi ticket có tag `[API-QA]`, `endpoint`, `automation BE`.  
> ⚙️ **Testing endpoint = sửa in project** (triển khai mã nguồn kiểm thử tự động trực tiếp trong repository project).

### 🔹 Bước 1: Tạo Prompt Sinh Kịch Bản Kiểm Thử (Create Test Scenario Prompt)
* **Thời điểm:** Ngay khi tiếp nhận ticket API-QA và tài liệu đặc tả endpoint.
* **Mục đích:** Khai thác AI đọc hiểu toàn diện API spec, Swagger/Postman collection và requirement để sinh bộ kịch bản đầy đủ, chống bỏ sót trường hợp.
* **Thao tác:** Soạn prompt đưa vào Claude/AI phân tích tài liệu đặc tả và sinh bộ Scenarios đầy đủ 4 tầng logic:
  * **Happy Path:** Kiểm tra mã trạng thái `200 OK`, response time tối ưu, schema dữ liệu đầy đủ, đúng logic nghiệp vụ.
  * **Negative Cases:** Kiểm tra xử lý lỗi client (`400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`).
  * **Boundary Conditions:** Kiểm tra độ dài chuỗi tối đa/tối thiểu, giá trị số âm/0/cực đại, định dạng ngày tháng ISO 8601.
  * **Adverse / Edge Cases:** Payload rỗng, thiếu header bắt buộc (`Authorization`, `Content-Type`), ký tự đặc biệt, SQL/Script Injection pattern.

---

### 🔹 Bước 2: Khởi Tạo Nhánh Mới Độc Lập Từ Nhánh Main (Create New Branch)
* **Thời điểm:** Sau khi đã có bộ Scenarios ban đầu từ AI.
* **Mục đích:** Đảm bảo mã nguồn được cách ly hoàn toàn, độc lập phát triển và tránh xung đột code.
* **Thao tác:**
  * Kéo mã nguồn mới nhất từ nhánh `main`.
  * Tạo branch mới độc lập theo quy tắc định danh: `<branch-name>-<endpoint>` (ví dụ: `QA-6700-instruction-by-step-ref`).
  * Cập nhật trạng thái ticket trên Jira sang **`In Project`**.
* **Quy tắc bất biến:** **1 branch chỉ phục vụ duy nhất 1 endpoint**, tuyệt đối không gộp chung nhiều endpoint vào một branch.

---

### 🔹 Bước 3: Hoàn Thiện Kịch Bản Kiểm Thử Chi Tiết (Complete Scenario)
* **Thời điểm:** Trước khi bắt tay viết code kiểm thử tự động.
* **Mục đích:** Đảm bảo kịch bản đạt độ chính xác 100%, rõ ràng từng tham số truyền vào và kết quả mong đợi.
* **Thao tác:** Rà soát và hoàn thiện chi tiết từng Scenario:
  * Xác định rõ `URL`, `HTTP Method` (`GET`, `POST`, `PUT`, `DELETE`).
  * Chuẩn bị đầy đủ `Query Parameters`, `Path Parameters`, `Request Headers`, `Request Body (Payload)`.
  * Liệt kê chi tiết các điều kiện xác thực: Assertions cho Status Code, Response Body Fields, Error Messages, Schema Type.

---

### 🔹 Bước 4: Tự Rà Soát Mã Nguồn & Cấu Hình Kết Nối (Review Code)
* **Thời điểm:** Sau khi viết xong kịch bản test script và các hàm hỗ trợ (helper).
* **Mục đích:** Kiểm soát chất lượng code, bảo mật thông tin xác thực và tính toàn vẹn của môi trường test.
* **Thao tác:**
  * Tự rà soát cấu trúc test script, fixtures, authentication tokens/headers.
  * Kiểm tra tính đóng gói và tái sử dụng của các hàm helper.

> [!IMPORTANT]
> **Hai lưu ý kỹ thuật bắt buộc tại Bước 4:**
> 1. **Nạp biến môi trường Database:** Nếu test script có tương tác trực tiếp với Database, bắt buộc phải import và gọi hàm `load_dotenv()` ở đầu file test để nạp cấu hình (`DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_PORT`) từ file `.env`.
> 2. **Quy tắc OMS Scope:** Tuân thủ quy tắc **Không tạo file trong `database/oms`** (vì phạm vi dự án hiện tại là Transfer Tool / Gateway, tránh tạo file rác/orphan code làm bẩn repository).

---

### 🔹 Bước 5: Thực Thi Chạy Toàn Bộ Test Suite Cục Bộ (Run Code)
* **Thời điểm:** Sau khi hoàn thành code và tự review.
* **Mục đích:** Xác minh chất lượng thực tế của endpoint và độ ổn định của bộ kiểm thử tự động.
* **Thao tác:**
  * Thực thi chạy toàn bộ bộ test suite automation cục bộ trên máy.
  * Kiểm tra từng test case để đảm bảo toàn bộ bộ test đạt kết quả **Pass 100%**.
* **Quy chuẩn tài liệu:** Không cần ghi câu lệnh CLI run test cụ thể.

---

### 🔹 Bước 6: Khắc Phục Lỗi Mã Nguồn & Tinh Chỉnh Assertions (Fix Code)
* **Thời điểm:** Khi có bất kỳ test case nào bị Fail hoặc phát sinh lỗi trong Bước 5.
* **Mục đích:** Sửa triệt để mọi lỗi logic, assertion sai lệch hoặc xử lý dữ liệu động không tương thích.
* **Thao tác:**
  * Phân tích nguyên nhân: do assertion quá cứng nhắc, sai lệch kiểu dữ liệu (`int` vs `str`), thiếu field từ backend, hay do backend trả lỗi thực tế.
  * Cập nhật lại test script hoặc tinh chỉnh response parser cho khớp chính xác.
  * Chạy lại test case vừa sửa để đảm bảo kết quả chuyển sang Pass.

---

### 🔹 Bước 7: Khởi Tạo Test Cases & Đồng Bộ ID Lên Jira (Create TestRail & Sync Jira)
* **Thời điểm:** Khi code test đã chạy ổn định và đạt Pass cục bộ.
* **Mục đích:** Quản lý tập trung các trường hợp kiểm thử tự động trên TestRail và liên kết minh bạch trên Jira.
* **Thao tác:**
  1. Chạy lệnh slash command `/create-testrail` để tự động tạo mới các test cases trên hệ thống TestRail (đúng Suite và Section).
  2. Chạy lệnh `/sync-testrail` để đồng bộ mã ID của các test case từ TestRail trực tiếp vào Jira Ticket.

---

### 🔹 Bước 8: Chạy Lại Bộ Test Đảm Bảo Không Bị Regression (Run Review Code)
* **Thời điểm:** Ngay sau khi đã liên kết TestRail IDs vào test scripts.
* **Mục đích:** Đảm bảo việc thêm annotation/ID của TestRail không gây ảnh hưởng hoặc hồi quy mã nguồn.
* **Thao tác:** Chạy lại toàn bộ test suite cục bộ một lần nữa; đảm bảo kết quả duy trì **Pass 100%**.

---

### 🔹 Bước 9: Quét & Dọn Dẹp Toàn Bộ Hàm Mồ Côi (Check Orphan Functions)
* **Thời điểm:** Trước khi chuẩn bị commit và đóng gói mã nguồn.
* **Mục đích:** Giữ gìn codebase luôn sạch sẽ, không có mã thừa thãi hoặc code rác gây khó khăn cho review.
* **Thao tác:**
  * Chạy slash command:
    ```bash
    /review-code
    ```
  * AI tự động rà soát toàn bộ branch để phát hiện các orphan functions (hàm mồ côi không được gọi), biến không dùng, log debug thừa và import dư thừa.
  * Tiến hành xóa bỏ và dọn dẹp sạch sẽ.

---

### 🔹 Bước 10: Rà Soát & Đối Chiếu Model Pydantic (Kiểm Tra Model Pydantic)
* **Thời điểm:** Sau khi hoàn thành code và dọn dẹp hàm thừa.
* **Mục đích:** Chống lỗi type mismatch hoặc crash runtime do schema thay đổi đột ngột từ backend.
* **Thao tác:**
  * Rà soát kỹ lưỡng toàn bộ các class và schema Pydantic được định nghĩa trong thư mục model/schema.
  * Đối chiếu 100% từng field, kiểu dữ liệu (`str`, `int`, `float`, `bool`, `Optional[...]`, `List[...]`) với response payload thực tế từ API.

---

### 🔹 Bước 11: Commit & Push Code Lên GitHub Remote (Commit and Push Code)
* **Thời điểm:** Khi code đã đạt chuẩn chất lượng, clean và pass 100%.
* **Mục đích:** Lưu trữ phiên bản code lên máy chủ Git từ xa và chuẩn bị cho giai đoạn mở PR.
* **Thao tác:**
  * Thực hiện git commit với thông điệp rõ ràng theo đúng chuẩn convention của dự án (ví dụ: `feat(api-qa): implement test suite for <endpoint>`).
  * Thực hiện push nhánh code lên remote repository trên GitHub.

---

### 🔹 Bước 12: Tự Động Soạn Thảo Bản Tóm Tắt PR (Create PR Summary)
* **Thời điểm:** Sau khi đã push nhánh code lên GitHub remote.
* **Mục đích:** Chuẩn bị nội dung tóm tắt chuyên nghiệp, mạch lạc và đầy đủ thông tin để reviewer dễ dàng nắm bắt phạm vi thay đổi.
* **Thao tác:**
  * Chạy slash command:
    ```bash
    /pr summary
    ```
  * AI tự động đọc git diff của branch so với nhánh `main` và sinh ra bản tóm tắt PR chuẩn cấu trúc (Scope of changes, Test Coverage, Evidence, Endpoints tested).

---

### 🔹 Bước 13: Mở Pull Request Trên GitHub Vào Nhánh Main (Create Pull Request)
* **Thời điểm:** Khi đã có bản PR Summary hoàn chỉnh.
* **Mục đích:** Đề xuất đưa code test mới vào nhánh chính của repository dự án.
* **Thao tác:**
  * Tạo Pull Request (PR) mới từ branch của ticket vào nhánh `main`.
  * Dán toàn bộ nội dung PR Summary đã chuẩn bị vào phần mô tả PR.
  * Đính kèm evidence kết quả chạy test cục bộ đạt Pass 100%.
  * Gán reviewer chính phụ trách duyệt code là **Dastan**.

---

### 🔹 Bước 14: Cập Nhật Trạng Thái Ticket Jira Sang Under Review (Update Review Status)
* **Thời điểm:** Ngay sau khi đã tạo xong Pull Request trên GitHub.
* **Mục đích:** Cập nhật tiến độ minh bạch cho cả team và Stakeholders trên Jira Board.
* **Thao tác:**
  * Chuyển trạng thái ticket trên Jira sang **`Under Review`**.
  * Dán đường dẫn liên kết của Pull Request vào mục tương ứng trong ticket Jira.

---

### 🔹 Bước 15: Nhắn Dastan Review, Xử Lý Feedback & Merge Code (Request Review & Merge ➔ Done ✅)
* **Thời điểm:** Sau khi ticket đã ở trạng thái `Under Review`.
* **Mục đích:** Nhận phê duyệt chính thức từ reviewer, xử lý dứt điểm phản hồi kỹ thuật và hoàn tất vòng đời ticket.
* **Thao tác:**
  1. **Nhắn tin cho Dastan:** Gửi tin nhắn trên Slack cho **Dastan** nhờ anh ấy review Pull Request:
     > 💬 *"Hi Dastan, I have created PR for ticket `<TICKET_ID>` (`<ENDPOINT>`): `<PR_LINK>`. All tests passed 100%. Could you please help review it? Thank you!"*
  2. **Xử lý feedback qua AI:** Khi Dastan có nhận xét hoặc yêu cầu chỉnh sửa, chạy lệnh:
     ```bash
     /resolve-pr
     ```
     để AI tự động đọc feedback và hỗ trợ cập nhật code chuẩn xác.
  3. **Merge & Hoàn tất Ticket:** Sau khi Dastan phê duyệt (Approved) ➔ Tiến hành merge code vào nhánh `main` và chuyển trạng thái ticket Jira sang **`Done`** ✅.

---

## 4. SỔ TAY TRA CỨU NHANH CẤU HÌNH & LƯU Ý NGHIỆP VỤ TRỌNG YẾU

### 🎯 1. Cấu hình TestRail Suite (Project ID 30)
| Suite Name | Suite ID | Mục đích sử dụng |
| :--- | :---: | :--- |
| **API** | **945** | Chứa các kịch bản kiểm thử API Backend, Endpoints, Schema, Status Codes. |
| **UI** | **946** | Chứa các kịch bản kiểm thử giao diện người dùng, components, flow thao tác trên web. |
| **E2E** | **947** | Chứa các kịch bản kiểm thử tích hợp xuyên suốt từ UI qua Gateway tới Database/Services. |

---

### 🔗 2. Cấu hình Jira Ticket cho Test Execution
* **Mối quan hệ (Link Type):** Chọn **`tests`**.
* **Liên kết trực tiếp tới:** Request Ticket tương ứng (ví dụ: `QA-xxxx` tests `GTO-xxxx`).
* **Epic cha liên kết:** **`QA-3614: Transfer Tools Enhancement and feedback`**.

---

### 💬 3. Mẫu Tin Nhắn Slack Chuẩn

#### 🔸 Mẫu 1: Pre-check với Dastan (Bước 0 - Chống duplicate)
> *"Hi Dastan, for ticket `<TICKET_ID>` (`<TICKET_NAME>`), have you created the draft ticket or test cases yet? If not, I will start creating the draft test execution."*

#### 🔸 Mẫu 2: Gửi Dev Review (Bước 6)
> *"Hi @<dev_name>, ticket `<TICKET_KEY>` has been tested and passed (Pass Test ✅). Here is the detailed test section: `<Jira_Link>`. Could you please help review? Thank you!"*

#### 🔸 Mẫu 3: Thông báo UAT Testing cho Ops (Bước 6)
> *"hi @tiffany.kao , @jento.chan we have completed testing for `<TICKET_KEY_AND_TITLE>` on QA environment. And we already set it up on UAT environment, please help testing it on UAT. Thank you! 🙏*  
> *UAT UI deployed at: web-reports.uat-gp.galaxydigital.io/fund_transfer_tool"*

---

### ⚙️ 4. Lưu ý Kỹ thuật Cốt Lõi
* **Không tạo file trong `database/oms`:** Phạm vi ticket thuộc Transfer Tool / Gateway, không đụng chạm đến phân hệ Order Management System (OMS). Tránh tạo file thừa để không bị tính là orphan code khi Dastan review PR.
* **Nạp biến môi trường Database:** Khi viết test query trực tiếp Database, bắt buộc gọi hàm `load_dotenv()` ở đầu file test để nạp cấu hình kết nối từ file `.env`.
* **Tuyệt đối không vẽ sơ đồ / diagram:** Toàn bộ ghi chú, báo cáo tuần và tài liệu tuân thủ chuẩn text thuần, bảng Markdown và danh sách đánh số.
