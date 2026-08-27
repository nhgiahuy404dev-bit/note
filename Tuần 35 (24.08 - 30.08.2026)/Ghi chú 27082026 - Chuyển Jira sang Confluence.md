# Ghi chú ngày 27/08/2026 (Thứ Năm) - Quy trình chuyển Jira sang Confluence

---

## 🎯 Mục tiêu
- Đồng bộ và cập nhật thông tin từ Jira Ticket sang trang tài liệu Confluence mà vẫn giữ nguyên cấu trúc (template) của Confluence.

-  [TEST EXECUTION]  GTO-16043 - Fiat withdrawal UI + E2E (Transfer Tool)
-  

---

## 📝 Quy trình thực hiện bằng AI Prompt
1. **Chuẩn bị liên kết:**
   - Link Jira Ticket: `[Link Jira]`
   - Link Confluence: `[Link Confluence]`

2. **Mẫu Prompt chuẩn sử dụng:**
   ```text
   Using this Jira ticket information:
   - Jira Ticket Link: <Link Jira>
   - Confluence Page Link: <Link Confluence>

   Please update the Confluence document while keeping the exact template of Confluence.
   Use the information from the Jira ticket to fill out details on Confluence, then copy the Test Table into the Test Section.
   ```

3. **Cập nhật & Kiểm tra:**
   - [ ] Kiểm tra bảng Test Table trong phần Test Section trên Confluence.
   - [ ] Đối chiếu dữ liệu giữa Jira và Confluence.
   - [ ] Lưu và xuất bản trang tài liệu.

# NOTE
- x-api-key của TEST-AUTOMATION: 802b1453-7149-as31-593530606dfa