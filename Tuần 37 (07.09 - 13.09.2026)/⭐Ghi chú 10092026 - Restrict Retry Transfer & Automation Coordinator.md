# 📝 Ghi chú ngày 10/09/2026 (Thứ Năm) - Restrict Retry Transfer & Automation Coordinator

---

## 🎯 Mục tiêu trong ngày
- [x] **[TEST EXECUTION] - [QA-6880]:** `[GTO-16245]`, `[GTO-16246]` Restrict retry of a failed transfer to ops users only, and drop the retry time window *(In Progress)*
- [x] **[API-QA] - [QA-6700]:** Implement automated tests for the missing Coordinator service endpoints `/instruction/by-step-ref/{uniqueRef}`

---

## 🌿 Quy trình tạo nhánh Git (Flow Create Branch)

### 📋 1. Các bước thực hiện
1. **Lấy tên branch từ Jira:** Vào phần **Development** trên Jira ticket ➔ Nhấn **Create branch** ➔ Copy tên branch gợi ý.
2. **Chuẩn hóa tên nhánh:** Tinh chỉnh lại tên nhánh cho khớp với endpoint cần triển khai kiểm thử tự động (ví dụ: bổ sung thông tin endpoint cụ thể).
3. **Thực thi lệnh trên Terminal:** Tạo và chuyển sang branch mới để bắt đầu làm việc.

---

### 💻 2. Chuỗi câu lệnh Git chuẩn (Step-by-step Commands)

```bash
# 1. Điều hướng vào thư mục dự án
cd ~/Documents/Workspace/api-qa

# 2. Cập nhật thông tin các nhánh từ remote
git fetch origin

# 3. Chuyển về nhánh main và kéo code mới nhất
git switch main
git pull origin main

# 4. Tạo và chuyển sang nhánh mới cho endpoint cần làm
git checkout -b <branch-name>-<endpoint>
```

> [!TIP]
> **Quy ước đặt tên nhánh:** Luôn đảm bảo tên branch gắn liền với ID ticket Jira và định danh endpoint tương ứng (ví dụ: `QA-6700-instruction-by-step-ref`) để dễ dàng quản lý PR và trace code sau này.

---

## 🏗️ Tổng quan về Jenkins (CI/CD System)

> [!NOTE]
> **Bản chất:** Jenkins là một **Hệ thống CI/CD (Continuous Integration / Continuous Delivery)** hoàn chỉnh, **không chỉ dùng riêng cho việc chạy test (Run tests)** mà còn quản lý và tự động hóa toàn diện quy trình phát triển, tích hợp và triển khai phần mềm.

### 📋 Các ứng dụng phổ biến (Common Uses)

| STT | Trường hợp sử dụng | Mục đích & Chi tiết |
| :---: | :--- | :--- |
| 1 | **Run automated tests** | Tự động kích hoạt và thực thi các bộ kiểm thử (API, UI, Regression, Unit tests) |
| 2 | **Build applications** | Biên dịch mã nguồn, đóng gói ứng dụng và tạo build artifacts |
| 3 | **Deploy to servers** | Tự động triển khai phiên bản mới lên các máy chủ / môi trường (Dev, Staging, Production) |
| 4 | **Run scheduled jobs** | Thiết lập lịch trình tự động (cron jobs) chạy các tác vụ nền, batch jobs, báo cáo |
| 5 | **DevOps Integrations** | Tích hợp liền mạch với hệ sinh thái Git (**GitHub**, **GitLab**), **Docker**, **Kubernetes**, v.v. |

---

## 🔐 Quy trình thêm Secret mới cho Jenkins (Add New Secret to Jenkins)

### 📋 1. Ma trận triển khai & Phân quyền duyệt (Execution & Approval Matrix)

| Repository | Thứ tự thực hiện | Nhóm xét duyệt (Approval) | Kênh phối hợp / Ghi chú |
| :--- | :---: | :--- | :--- |
| **`terraform`** | **1 (Làm trước)** | **SRE-ONCALL** (Infra Team) | Kênh Slack `#production_assistance` |
| **`jenkins`** | **2 (Làm sau)** | **Team QA** | Phê duyệt nội bộ team QA |

---

### 🚀 2. Quy trình Apply & Merge trên Repo `terraform`

1. **Tạo Pull Request:** Khai báo secret mới trên repository `terraform`.
2. **Xin Approval:** Liên hệ **SRE-ONCALL** trên kênh Slack `#production_assistance` để được review và approve PR.
3. **Thực thi lệnh Atlantis:** Sau khi nhận được Approval, tại ô bình luận (Comment) của PR trên GitHub, gõ lệnh:
   ```bash
   atlantis apply
   ```
4. **Kiểm tra kết quả:** Chờ hệ thống Atlantis chạy và báo trạng thái apply thành công hoàn tất.
5. **Tiến hành Merge:** Chỉ nhấn **Merge PR** sau khi `atlantis apply` đã chạy thành công 100%.

> [!IMPORTANT]
> **Nguyên tắc Merge:** Tuyệt đối không merge PR khi `atlantis apply` chưa chạy xong hoặc bị lỗi.

---

### 📌 3. Lưu ý định dạng Key khi add vào `terraform` (Key Naming Rule)

> [!WARNING]
> **Quy tắc đặt Key:** Khi khai báo key secret trên **`terraform`**, bắt buộc phải **thêm dấu sao (`*`) vào sau cùng của key** (suffix `*`, ví dụ: `<secret_key_name>*`) để đảm bảo hệ thống match và phân quyền đúng phạm vi.

---

## 🛠️ Mẫu AI Prompt Cấu hình Test Setup & Teardown cho Helper

### 🤖 Prompt cấu hình Reset & Restore Approval State cho User Group
> [!TIP]
> **Mục đích:** Sử dụng prompt này để yêu cầu AI viết code hook `test setup` và `teardown` trong file helper; lưu lại cấu hình hiện tại của nhóm `TEST_AUTOMATION`, ép về chế độ không cần duyệt (`pending_approval = false`) trong suốt quá trình chạy test và tự động khôi phục lại trạng thái ban đầu sau khi hoàn tất để triệt tiêu lỗi Flaky Test trên Jenkins.

```markdown
Please take a look at this `<link_path_helpers>`.

I want to implement a test setup and teardown flow for user group settings:
1. **Setup:**
   - Get the current configuration of the `TEST_AUTOMATION` user group and remember/cache its initial state.
   - Update the `TEST_AUTOMATION` user group setting so that it does not require `pending_approval` (always).

2. **Teardown:**
   - Set the `TEST_AUTOMATION` user group back to its previous state recorded during setup.
```

> [!NOTE]
> **Tham số cần điền:**
> - `<link_path_helpers>`: Đường dẫn tới file helper cấu hình trong repo kiểm thử.

---

## 💡 Kế hoạch tiếp theo & Ghi nhớ
- **Kế hoạch tiếp theo:** `[API-QA]` - `[QA-6700]` Triển khai automated tests cho Coordinator service endpoints `/instruction/request/status` (dự kiến ngày mai).

---
*Tạo tự động vào lúc 08:00:02 - Cập nhật format vào lúc 17:18:00*
