Create a **[Vsee - Galaxy] Weekly Summary + Demo** based on the information I provide.

**IMPORTANT REQUIREMENTS:**

* Keep the **exact structure, section order, headings, and format** of the template below (matching `request.md`).
* Do not rename, remove, reorder, or add any main sections.
* The content inside the template must remain in the same structure.
* **BẮT BUỘC KẺ BẢNG TỔNG HỢP (TICKET SUMMARY):** Ở ngay đầu mục `## Summary:` (dưới dòng `* List ra trong tuần rồi đã / đang làm ticket nào, progress như thế nào rồi:`), bắt buộc kẻ bảng Markdown tóm tắt toàn bộ ticket trong tuần (`| STT | Ticket ID | Nội dung công việc | Phân loại | Thời gian | Trạng thái (Jira) | Ghi chú / Kết quả |`).
* **NGHIÊM CẤM TỰ Ý TÓM TẮT SƠ SÀI / KHÔNG ĐƯỢC TỰ Ý GỘP BƯỚC:** Khi liệt kê chi tiết từng ticket, **BẮT BUỘC** phải ghi đầy đủ các bước đánh số (Numbered Steps) theo đúng Workflow chuẩn của loại ticket đó. Tuyệt đối không viết vài gạch đầu dòng tóm tắt chung chung.
* Viết báo cáo bằng **tiếng Việt mạch lạc, dễ hiểu** cho các bước (steps), phần giải thích, mô tả quy trình để dễ đọc và thuyết trình trong meeting.
* Giữ nguyên **tiếng Anh chuẩn** cho các thuật ngữ kỹ thuật, tên ticket, API endpoints, status Jira (`Done`, `Pass Test`, `Under Review`, `Testing`, `In Progress`), lệnh command, code và tên tính năng sẵn có.
* Use actual information from my provided work only. Do not invent tickets, progress, features, or completed tasks.
* For each ticket, clearly describe what was done, the current progress, and what remains if applicable.
* For the Demo section, include features that I have actually worked on or am currently working on.
* For Knowledge Sharing, select **one relevant topic** from the features I worked on and explain it in a way that is easy to present to the team.
* For testing-related topics, focus on the QA perspective: test approach, test coverage, regression scope, and how to determine the appropriate regression scope.
* For Dev enhancement tickets, explain how QA should test the enhancement and how to identify the corresponding regression scope.
* For AI usage, describe practical ways AI can be applied in the QA workflow rather than giving generic AI explanations.
* Keep the final **Action items** clear and actionable, tích `[x]` các task đã hoàn thành và `- [ ]` cho các task tuần tới.

**Use the following template exactly as the presentation structure (from request.md):**

```
* [Vsee - Galaxy] Weekly Summary + Demo

Attendees: Brian Pham Hau Duong (Hầu Dương) Huy Nguyễn Pháp Huỳnh Quốc Thai Huynh

* Notes

Meeting sẽ chia ra làm các phần chính như sau:

## Summary:

* List ra trong tuần rồi đã / đang làm ticket nào, progress như thế nào rồi

* Demo feature đã / đang làm

## Knowledge Sharing:

* Pick ra 1 topic trong feature mình đã làm để sharing knowledge (UI)

* Example (Galaxy):

  * GET Whitelisting
  * G1
  * Kafka …
  * Settlement
  * Transfer tool manage permission
  * Transfer tool Instructions
  * On-Chain
  * ….

* Cách apply AI trong công việc,

* Cách test regression tests và scope cần test trong regression tests

Cách test ticket enhancement của dev và regression scope mình cần làm tương ứng.

Action items
```

**Content requirements for each section:**

1. **Summary**

   * **Bảng tổng hợp các Ticket trong tuần (Ticket Summary):**
     * Đặt ngay đầu mục `## Summary:` trước phần chi tiết.
     * Cột bảng bắt buộc: `| STT | Ticket ID | Nội dung công việc | Phân loại | Thời gian | Trạng thái (Jira) | Ghi chú / Kết quả |`
   * **Chi tiết từng ticket (Quy chuẩn bắt buộc đủ bước theo từng Workflow):**
     * **Workflow 1 - Endpoint Automation Testing (Bắt buộc ĐỦ 15 bước chuẩn):**
       Áp dụng cho các ticket tự động hóa endpoint API/Backend (`[API-QA]`, `endpoint`, `parsing`, `automation BE`):
       1. `Create Test Scenario Prompt`: Tạo prompt AI đọc test steps để tự động sinh Scenarios cho endpoints/logic cần test.
       2. `Create New Branch`: Tạo branch độc lập `<branch-name>` từ `main`, chuyển status Jira sang `In Project`.
       3. `Complete Scenario`: Rà soát và hoàn thiện kịch bản kiểm thử (Happy Path, Negative Cases, Schema validation, Adverse Responses) trước khi code.
       4. `Review Code`: Tự review code triển khai test script và các câu lệnh assertions.
       5. `Run Code`: Chạy test suite automation cục bộ (Pass 100%).
       6. `Fix Code`: Sửa các lỗi phát sinh về assertion và kiểu dữ liệu trả về (nếu có).
       7. `Create TestRail`: Tạo và cập nhật đầy đủ test cases lên hệ thống TestRail.
       8. `Run Review Code`: Chạy lại toàn bộ test suite sau khi tạo TestRail để đảm bảo không có regression (Pass 100%).
       9. `Check Orphan Functions`: Kiểm tra và dọn dẹp các orphan functions sau khi hoàn thành bằng lệnh `/review-code`.
       10. `Kiểm tra model Pydantic`: Rà soát lại toàn bộ model Pydantic đảm bảo khớp 100% với response schema thực tế, không bị thiếu trường hoặc crash type.
       11. `Commit and Push Code`: Commit với message chuẩn convention và push code lên remote branch.
       12. `Create PR Summary`: Soạn thảo bản tóm tắt nội dung thay đổi của PR.
       13. `Create Pull Request`: Tạo PR trên GitHub vào nhánh `main`.
       14. `Update Review Status`: Chuyển status ticket Jira sang **`Under Review`**.
       15. `Request Review & Merge`: Đưa cho **Dastan** review PR, nhận approval và merge vào nhánh chính; chuyển Jira sang **`Done`** ✅.
     * **Workflow 2 - Feature / UI / Test Execution (Bắt buộc ĐỦ các giai đoạn chuẩn):**
       Áp dụng cho các ticket kiểm thử chức năng, UI, enhancement, APM (`[TEST EXECUTION]`, `[UI-QA]`, `GTO-xxxx`):
       0. `Pre-check with Dastan (Bắt buộc - Chống duplicate)`: Trước khi làm ticket và tạo draft, **bắt buộc phải hỏi Dastan trên Slack** xem đã tạo draft ticket / test cases chưa để tránh bị duplicate (trùng lặp ticket/kịch bản trên Jira & TestRail). Nếu Dastan đã tạo thì kế thừa sử dụng, chưa có mới bắt đầu tạo draft.
       1. `Read Request & Create Draft`: Đọc và phân tích kỹ tài liệu yêu cầu Jira, Confluence spec, PR diff. Chạy lệnh `/create-draft-test-execution` để AI tự động sinh kịch bản nháp ➔ Cập nhật Jira sang **`In Progress`**.
       2. `Designing & Artifact`: Chuyển status Jira sang **`Designing`** ➔ Rà soát kịch bản trên VS Code, chuẩn hóa Description & Test Table trên Jira (**bắt buộc ghi rõ Endpoint API** `URL`, `Method`, `Payload`). Cấu hình mục **Linked Work Items** quan hệ **`tests`** liên kết tới Request Ticket tương ứng và gắn Epic cha **`QA-3614: Transfer Tools Enhancement and feedback`**. Chạy ngay lệnh `/create-test-artifact` để đồng bộ Confluence và chuyển status Jira sang **`Testing`** 🚀.
       3. `Testing on Staging & Sign-off Pass Test`: Chuyển status Jira sang **`Testing`** khi Dev deploy Staging ➔ Thực thi kiểm thử trực tiếp trên Staging toàn bộ test cases + regression test. Khi kiểm thử đạt 100% Passed ➔ **Nghiệm thu (Sign-off) & Hoàn tất Ticket Jira**: Chuyển trạng thái sang **`Pass Test`** ✅ và tag reviewers (**Dastan**, **Mohit**, **Sandeep**).
       4. `Dev Review & UAT Notification`: **Nghiệm thu (Sign-off) & Hoàn tất Ticket Jira (`Pass Test` ✅) trên môi trường QA xong mới gửi Dev review:** Nhắn tin Slack thông báo ticket đã Pass Test và gửi link để Dev review xác nhận. Đồng thời nhắn tin trên Slack nhờ Ops (**@tiffany.kao** và **@jento.chan**) test trên môi trường UAT (`web-reports.uat-gp.galaxydigital.io/fund_transfer_tool`).
       5. `Create TestRail`: **Sau khi Dev review OK xong, lúc này mới bắt đầu làm TestRail:** Phân loại Suite API `945`, UI `946`, E2E `947` - Project 30. Chạy `/Create-testrail-cases-from-confluence` sinh file markdown draft, sau đó chạy `/Create-TR-Run-From-TR-Draft` tạo Test Run và ghi nhận evidence.
     * **Workflow 3 - Code Enhancement / DevOps Fix (Bắt buộc ĐỦ 10 bước chuẩn):**
       Áp dụng cho sửa code logic, fix CI/CD Jenkins:
       1. Create New Branch ➔ 2. Modify Code ➔ 3. Review Code ➔ 4. Run Code/Test via CLI ➔ 5. Fix Code ➔ 6. Commit and Push ➔ 7. Create PR Summary ➔ 8. Create Pull Request ➔ 9. Update Review Status (`Under Review`) ➔ 10. Request Review & Merge ➔ **`Done`** ✅.

2. **Demo**
   * List the features that I have worked on or am currently working on.
   * Briefly explain what the feature does and what part can be demonstrated.
   * Do not include features that I have not actually worked on.

3. **Knowledge Sharing**
   * Select **one main topic** that is relevant to my work during the week.
   * Explain the topic from a practical QA perspective:
     * Challenges & Approach / Bài toán thực tế
     * Technical Deep Dive / Chi tiết kỹ thuật, cơ chế hoạt động
     * Testing Scoping & Test Matrix / Phân tầng kiểm thử & Quy tắc scoping
   * If the topic is related to testing, cover test approach, test cases, important validation points, regression testing & regression scope.
   * If the topic is a Dev enhancement, explain what was changed, what QA needs to verify, and how to determine the regression scope.

4. **Applying AI in Work**
   * Describe practical AI usage in the QA workflow:
     **Input → AI assistance → QA review → Final result**
   * Examples: sinh scenario qua `/create-draft-test-execution`, scan orphan functions qua `/review-code`, tạo artifact Confluence qua `/create-test-artifact`, tạo TestRail Run qua `/Create-TR-Run-From-TR-Draft`.

5. **Regression Scope**
   * Trình bày mô hình 3 tầng xác định Regression Scope cho ticket enhancement:
     * Tầng 1: Core Feature / Direct Impact Scope
     * Tầng 2: Boundary & Negative Scope / Legacy Cleanup
     * Tầng 3: Broader Regression Scope / Shared Seams (Global Nav, Gateway middleware, downstream services).

6. **Action items**
   * List các task cụ thể, rõ ràng, không chung chung.
   * Đánh dấu `- [x]` cho các việc đã nghiệm thu hoàn thành trong tuần và `- [ ]` cho các việc cần theo dõi hoặc tiếp tục trong tuần tới.

**Final output requirements:**
* Follow the template structure exactly (matching `request.md`).
* Keep the same section order.
* Do not create additional main sections.
* Do not change the attendee list.
* Keep the output concise enough for a weekly meeting.
* Sử dụng tiếng Việt tự nhiên, gãy gọn cho các bước mô tả để dễ thuyết trình trực tiếp trong meeting.
* Giữ nguyên tiếng Anh cho các thuật ngữ chuyên môn, mã ticket, status và code/command.
* If some information is missing, do not invent it. Mark it as `[Need input]` instead.
