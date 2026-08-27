# Ghi chú ngày 22/08/2026 (Thứ Bảy) - Quy trình Git Branch & Sử dụng AI Prompt

---

## 🌿 1. Quy trình Git Branch
1. Chuẩn bị trước câu lệnh Prompt trên file Document/Ghi chú.
2. Kiểm tra danh sách branch hiện tại:
   ```bash
   git branch | cat
   ```
3. Kéo code mới nhất từ nhánh chính về:
   ```bash
   git pull origin main
   ```
4. Tạo và chuyển sang branch mới để làm việc:
   ```bash
   git checkout -b <tên_branch_mới>
   ```

---

## 🤖 2. Quy trình làm việc với AI để sinh Scenario
1. Copy nội dung Prompt đã chuẩn bị sang Project chính.
2. Đính kèm file `.feature` và file tài liệu API/Endpoint.
3. Chạy lệnh Prompt chuẩn cho AI:
   ```text
   using new endpoint doc and generate scenarios to add on this one, please define and let me review first before making any changes on this feature file
   ```

---

## 👥 3. Review & Viết Automation Code
1. AI sinh kịch bản (Scenario) ➔ Gửi cho Leader/Anh hướng dẫn review.
2. Sau khi duyệt kịch bản (OK) ➔ Tiến hành viết code Automation hoàn thiện.
