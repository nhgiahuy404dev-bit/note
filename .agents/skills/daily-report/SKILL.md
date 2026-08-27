---
name: daily-report
description: Tự động tổng hợp và tạo Daily Report cuối ngày bằng tiếng Anh chuẩn (What I’ve done, In Progress, Todo, Issues) từ file ghi chú daily.
---

# 📋 Skill: Daily Report Generator (English Standard)

Skill này kích hoạt khi người dùng gõ `/daily-report`, `/report`, hoặc yêu cầu tạo báo cáo cuối ngày từ file ghi chú daily hôm nay.

> [!IMPORTANT]
> **Ngôn ngữ báo cáo:** Luôn luôn xuất Daily Report bằng **tiếng Anh (English)** chuyên nghiệp, ngắn gọn và chuẩn chỉnh theo văn phong QA / Software Engineering.

---

## 🎯 Cấu Trúc Báo Cáo Chuẩn (Format)

```markdown
# 📋 DAILY REPORT - DD/MM/YYYY (Day of week)

What I’ve done:
- [Completed tasks, finished tickets [TEST EXECUTION], [API-QA], [UI-QA], studied topics...]

In Progress:
- [Ongoing tasks, tests or implementations currently in progress]

Todo:
- [Next planned tasks, pending checklist items [ ]]

Issues:
None
```

> [!NOTE]
> Mục **Issues** mặc định luôn ghi `None` (trừ khi file ghi chú có đề cập cụ thể đến lỗi/blocker).

---

## ⚙️ Quy Trình Thực Hiện

1. Đọc file ghi chú daily hôm nay trong thư mục tuần hiện tại (`Tuần XX (...)`).
2. Dịch và chuẩn hóa nội dung sang tiếng Anh:
   - **What I’ve done:** Các task `- [x]`, ticket `[TEST EXECUTION]`, các nội dung đã nghiên cứu/triển khai.
   - **In Progress:** Các công việc đang thực thi dở dang.
   - **Todo:** Các task checklist `- [ ]` còn lại cho ngày tiếp theo.
   - **Issues:** Mặc định `None`.
3. Tạo file `Daily Report DDMMYYYY.md` trong thư mục tuần và xuất ra màn hình chat cho người dùng tiện copy.
