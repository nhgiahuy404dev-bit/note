# 📝 Ghi chú ngày 10/09/2026 (Thứ Năm) - Restrict Retry Transfer & Automation Coordinator

---

## 🎯 Mục tiêu trong ngày
- [ ] **[TEST EXECUTION] - [QA-6880]:** `[GTO-16245]`, `[GTO-16246]` Restrict retry of a failed transfer to ops users only, and drop the retry time window *(In Progress)*
- [ ] **[API-QA] - [QA-6700]:** Implement automated tests for the missing Coordinator service endpoints `/instruction/by-step-ref/{uniqueRef}`

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

## 💡 Kế hoạch tiếp theo & Ghi nhớ
- **Kế hoạch tiếp theo:** `[API-QA]` - `[QA-6700]` Triển khai automated tests cho Coordinator service endpoints `/instruction/request/status` (dự kiến ngày mai).

---
*Tạo tự động vào lúc 08:00:02 - Cập nhật format vào lúc 08:16:30*
