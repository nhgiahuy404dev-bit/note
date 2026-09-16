Create a **[Vsee - Galaxy] Weekly Summary + Demo** based on the information I provide.

**IMPORTANT REQUIREMENTS:**

* Keep the **exact structure, section order, headings, and format** of the template below.
* Do not rename, remove, reorder, or add any main sections.
* The content inside the template must remain in the same structure.
* Viết báo cáo bằng **tiếng Việt mạch lạc, dễ hiểu** cho các bước (steps), phần giải thích, mô tả quy trình để dễ đọc và thuyết trình trong meeting.
* Giữ nguyên **tiếng Anh chuẩn** cho các thuật ngữ kỹ thuật, tên ticket, API endpoints, status, lệnh command, code và tên tính năng sẵn có.
* Use actual information from my provided work only. Do not invent tickets, progress, features, or completed tasks.
* For each ticket, clearly describe what was done, the current progress, and what remains if applicable.
* For the Demo section, include features that I have actually worked on or am currently working on.
* For Knowledge Sharing, select **one relevant topic** from the features I worked on and explain it in a way that is easy to present to the team.
* For testing-related topics, focus on the QA perspective: test approach, test coverage, regression scope, and how to determine the appropriate regression scope.
* For Dev enhancement tickets, explain how QA should test the enhancement and how to identify the corresponding regression scope.
* For AI usage, describe practical ways AI can be applied in the QA workflow rather than giving generic AI explanations.
* Keep the final **Action items** clear and actionable.

**Use the following template exactly as the presentation structure:**

```
 * [Vsee - Galaxy] Weekly Summary + Demo

Attendees: Brian Pham Hau Duong (Hầu Dương) Huy Nguyễn Pháp Huỳnh Quốc Thai Huynh

* Notes

Meeting sẽ chia ra làm các phần chính như sau:

**## Summary:**

* List ra trong tuần rồi đã / đang làm ticket nào, progress như thế nào rồi

* Demo feature đã / đang làm

**## Knowledge Sharing:**

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

   * List all tickets I worked on during the week.
   * Clearly indicate the current progress of each ticket.
   * Distinguish between completed, in-progress, blocked, or pending work when applicable.
   * Keep each item concise and easy to explain verbally.
   * **Quy chuẩn ghi chép chi tiết theo 2 luồng công việc (Testing Workflows):**
     * **Workflow 1 - Endpoint Automation Testing (12 bước):** Áp dụng cho các ticket tự động hóa endpoint (như `QA-6700`, `QA-6703`), ghi rõ đủ 12 bước:
       1. `Create Test Scenario Prompt`: Tạo prompt cho AI đọc test steps và sinh Scenarios.
       2. `Create New Branch`: Tạo branch `<branch-name>-<endpoint>`, chuyển status sang `Testing`.
       3. `Complete Scenario`: Rà soát và hoàn thiện kịch bản trước khi code.
       4. `Review Code`: Review code test triển khai.
       5. `Run Code`: Chạy automated test cục bộ.
       6. `Fix Code`: Khắc phục lỗi phát sinh nếu có.
       7. `Create TestRail`: Tạo và cập nhật test cases trên TestRail.
       8. `Commit and Push Code`: Commit & push code lên remote.
       9. `Create PR Summary`: Soạn thảo nội dung PR summary.
       10. `Create Pull Request`: Mở PR trên GitHub.
       11. `Update Review Status`: Chuyển status ticket sang `Under Review` khi hoàn thành endpoint.
       12. `Request Review (Dastan)`: Đưa cho **Dastan** review PR và xử lý phản hồi.
     * **Workflow 2 - Feature / UI / Normal Ticket Testing (5 giai đoạn):** Áp dụng cho các ticket tính năng thường, UI, enhancement (như `GTO-16168`, `QA-6880`), ghi rõ 5 giai đoạn:
       1. `Read Request`: Đọc và phân tích yêu cầu kỹ thuật.
       2. `Designing`: Chuyển status sang `Designing`, thiết kế bộ test cases.
       3. `Testing`: Chuyển status sang `Testing`, thực thi test Endpoint/UI/Regression/E2E, đẩy test artifacts lên Confluence.
       4. `Pass Test`: Chuyển status sang `Pass Test` khi nghiệm thu xong, đánh dấu ✅.
       5. `Create PR`: Mở PR và gán các reviewer chính: **Mohit**, **Dastan**, và **Sandeep**.

2. **Demo**

   * List the features that I have worked on or am currently working on.
   * Briefly explain what the feature does and what part can be demonstrated.
   * Do not include features that I have not actually worked on.

3. **Knowledge Sharing**

   * Select **one main topic** that is relevant to my work during the week.
   * Explain the topic from a practical QA perspective.
   * If the topic is related to testing, cover:

     * Test approach
     * Test scenarios/cases
     * Important validation points
     * Regression testing
     * Regression scope
   * If the topic is a Dev enhancement, explain:

     * What was changed
     * What QA needs to verify
     * What related areas should be regression tested
     * How to determine the regression scope
     * Why those areas should or should not be included

4. **Applying AI in Work**

   * Describe practical AI usage in the QA workflow.
   * Examples may include:

     * Requirement analysis
     * Test scenario/test case generation
     * Test coverage review
     * API automation support
     * Log/response analysis
     * Regression scope identification
     * Test code/code review
   * Whenever possible, describe the workflow as:
     **Input → AI assistance → QA review → Final result**

5. **Action items**

   * List the tasks that need to be continued or completed after the meeting.
   * Keep each action item specific and actionable.
   * Do not use vague statements.

**Final output requirements:**

* Follow the template structure exactly.
* Keep the same section order.
* Do not create additional main sections.
* Do not change the attendee list.
* Keep the output concise enough for a weekly meeting.
* Sử dụng tiếng Việt tự nhiên, gãy gọn cho các bước mô tả để dễ thuyết trình trực tiếp trong meeting.
* Giữ nguyên tiếng Anh cho các thuật ngữ chuyên môn, mã ticket, status và code/command.
* If some information is missing, do not invent it. Mark it as `[Need input]` instead.
