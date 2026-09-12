---
name: create-ghi-chu
description: Tự động kiểm tra và tạo bù các file ghi chú daily còn thiếu trong tuần (hoặc tạo file ghi chú hôm nay nếu chưa có) khi người dùng gõ /create-ghi-chu.
---

# 📝 Skill: Create Ghi Chú Daily & Tự Động Tạo Bù Ngày Thiếu

Skill này được kích hoạt khi người dùng gõ `/create-ghi-chu`, `/tao-ghi-chu`, `/create-note`, hoặc yêu cầu kiểm tra/tạo bù các file ghi chú daily còn thiếu trong tuần.

---

## ⚙️ Quy Trình Thực Hiện

Khi nhận được lệnh `/create-ghi-chu`:

1. **Xác định tuần làm việc:**
   - Xác định ngày hiện tại và thư mục tuần tương ứng (ví dụ: `Tuần 37 (07.09 - 13.09.2026)`).
   - Nếu người dùng chỉ định một tuần cụ thể, chuyển sang thư mục tuần đó.

2. **Cách 1: Thực thi qua Script tự động (Khuyến nghị):**
   - Chạy lệnh Terminal:
     ```powershell
     python "d:\Workspace\main\Study_GALAXY\DOCUMENT\Ghi chú daily\_tools\create_daily_note.py" --fill-missing
     ```
   - Script sẽ tự động quét từ Thứ 2 đến ngày hiện tại (bao gồm Thứ 7 nếu đang là Thứ 7), phát hiện ngày nào chưa có file ghi chú và tự động tạo file `Ghi chú DDMMYYYY.md` tương ứng.

3. **Cách 2: Agent tự động kiểm tra và tạo bù trực tiếp:**
   - Quét danh sách file trong thư mục tuần.
   - Nhận diện các ngày làm việc:
     - Thứ 2: `start_of_week`
     - Thứ 3: `start_of_week + 1 day`
     - ...
     - Thứ 6: `start_of_week + 4 days`
     - Thứ 7: `start_of_week + 5 days` (nếu hôm nay là Thứ 7 hoặc người dùng yêu cầu).
   - Nếu ngày nào chưa có file `.md` chứa mã ngày `DDMMYYYY` (ví dụ `08092026`), tiến hành tạo file mới với cấu trúc chuẩn:

```markdown
# Ghi chú ngày DD/MM/YYYY (Thứ ...)

## 🎯 Mục tiêu trong ngày
- [ ] 

## 📝 Ghi chú công việc / Study
- 

## 💡 Ghi nhớ / Ideas
- 

---
*Tạo tự động vào lúc HH:MM:SS*
```

4. **Báo cáo kết quả rõ ràng:**
   - Xuất bảng tổng kết trạng thái từng ngày trong tuần (Ngày nào đã có sẵn, ngày nào vừa được tạo bù).
