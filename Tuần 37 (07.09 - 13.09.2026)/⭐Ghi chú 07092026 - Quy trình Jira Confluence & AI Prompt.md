# 📝 Ghi chú ngày 07/09/2026 (Thứ Hai) - Quy trình Jira Confluence & AI Prompt

---

## 🎯 Mục tiêu trong ngày
- [ ] **Tạo ticket Jira và tài liệu Confluence:** Chuẩn bị tài liệu test execution cho ticket và đồng bộ tài liệu liên quan.
- [ ] **[UI-QA] - [GTO-16168]:** Split Fireblocks section into Vault and Whitelisted Address sub-heading in permissions account picker.

---

## 📝 Ghi chú công việc / Study

### 📋 Quy trình chuẩn bị & Phân tích yêu cầu
- **Thu thập tài liệu nguồn:** Link Jira ticket, Confluence spec, Git PR và Slack threads liên quan.
- **Phân tích phạm vi:** Xác định rõ Scope thay đổi và thiết lập bộ kịch bản kiểm thử (API / UI / Regression).
- **Thiết kế tài liệu:** Soạn thảo test execution draft và phối hợp với các bên liên quan.

---

## ⚙️ Quy trình thực hiện & Mẫu AI Prompt chuẩn

### 🤖 1. Prompt tạo Draft Test Execution & Slash Command từ Jira / Confluence (BÂY GIỜ ĐÃ CÓ COMMAD /create-draft-test-execution)
> [!TIP]
> Sử dụng mẫu prompt dưới đây để yêu cầu AI đọc tổng thể ticket Jira, tài liệu Confluence, GitHub PR và Slack thread; từ đó tổng hợp thành file Markdown đặc tả Test Execution và tự động sinh Slash Command phục vụ tự động hóa.

```markdown
Read this ticket: <link_requirement>
- And related Confluence / Git PR to have a full understanding of this ticket. Also, please check the Slack thread inside the ticket to understand the requirements, ticket description, and implementation details.

Then create for me a markdown (.md) file saved to:
`Users/vpham/Documents/draft-ticket/test-executions`

For the file name, use the ticket ID (e.g., GTO-xxxx) from the URL as the prefix, followed by the Jira ticket title (e.g., `GTO-xxxx - Title.md`).

The document should include the following sections:
1. Documentation: List all related tickets, documentation links, and Slack threads.
2. Scope: Summary of what has changed.
3. Changes Description Table: Detail the changes (e.g., endpoints added/updated, scope of changes) with columns:
   - `#` | `Title` | `Status` | `Description`
4. Test Sections:
   - API Tests: Group tests by endpoint sections. Each endpoint must have a Test Table with columns:
     - `ID` | `Scenario` | `Expected` | `Actual` | `Status`
   - UI Tests: List UI test cases in tables (separate tables if there are multiple pages or scopes).
5. Regression Tests: Identify scopes that may be affected by the ticket and create a Regression Test table for related scopes.

Finally, please create a slash command `/create-draft-test-execution` that accepts a list of Jira ticket URLs / Confluence URLs as the knowledge base to execute the workflow described above.
```

---

### 📋 2. Prompt tạo tài liệu hướng dẫn sử dụng Slash Command
> Sau khi tạo lệnh slash command xong, dùng prompt này để yêu cầu AI xuất bảng tóm tắt hướng dẫn sử dụng kèm các ví dụ tham số khác nhau:

```markdown
Show me the summary of how to use this slash command (in a table with different parameter inputs).
Save it to the `test-executions` folder as a guide.
```

---

### 🔄 3. Các bước phối hợp Jira ➔ Dev Review ➔ Confluence

| Bước | Hành động | Chi tiết thao tác & Lưu ý |
| :---: | :--- | :--- |
| **1** | **Tạo Ticket Jira** | Tạo ticket mới trong danh sách Jira, chọn Status ban đầu là **`Designing`**. |
| **2** | **Cập nhật nội dung** | Dán toàn bộ nội dung kịch bản test vừa được AI tạo vào phần mô tả của Ticket. |
| **3** | **Gửi Dev Review** | Nhắn tin/trao đổi trực tiếp với Dev phụ trách để cùng review các Test Cases đã thiết kế. |
| **4** | **Liên kết Epic / Ticket cha** | Nhớ chỉnh sửa ticket và liên kết vào: **`QA-3614: Transfer Tools Enhancement`**. |
| **5** | **Đồng bộ sang Confluence** | Đưa tài liệu sang Confluence. Trong Ticket Jira, dán liên kết trang Confluence với caption: **`Test Artifact:`**. |
| **6** | **Chuyển dữ liệu bằng AI** | Chạy prompt AI để chuyển dữ liệu từ Jira sang Confluence với lệnh: *"Fill out the section above Test Execution section"* hoặc điều chỉnh thủ công theo template trang. |
| **7** | **Xác nhận Deploy** | Chủ động hỏi Dev xác nhận xem code đã được deploy lên môi trường test chưa để bắt đầu thực thi. |

---

## 💡 Ghi nhớ / Ideas
- Luôn kiểm tra kỹ các section trên Confluence để đảm bảo template không bị vỡ sau khi paste dữ liệu từ Jira.
- Chủ động nắm bắt trạng thái deploy của backend/frontend trước khi tiến hành test execution.

---
*Cập nhật và chuẩn hóa vào lúc 08:14:00 - 11/09/2026*
