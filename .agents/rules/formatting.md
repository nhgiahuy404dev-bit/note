# Quy tắc định dạng tài liệu (Formatting Rule)

Khi người dùng gọi `/formating` hoặc `/formatting` (hoặc yêu cầu format một file/nội dung), hãy tự động kích hoạt skill `formating`:

1. **Chuẩn hóa cấu trúc**:
   - Sử dụng Tiêu đề cấp 1 `#` duy nhất kèm emoji phù hợp.
   - Chia các phần cấp 2 `##` bằng emoji (🎯, 📋, ⚙️, 🚀, 📌, 💡, ⚠️, ✅) và phân tách bằng đường kẻ `---`.
   - Chuyển đổi dữ liệu đối chiếu/cấu hình/tham số thành bảng Markdown (`| Cột 1 | Cột 2 |`).
   - Chuẩn hóa checklist công việc dạng `- [ ]` / `- [x]`.
   - Bao bọc lệnh, query SQL, kịch bản BDD/Feature trong đúng code blocks có syntax highlighting (`bash`, `sql`, `gherkin`, `python`, v.v.).
   - Sử dụng Callout (`> [!NOTE]`, `> [!IMPORTANT]`, `> [!TIP]`, `> [!WARNING]`) cho các lưu ý trọng tâm.

2. **Bảo toàn thông tin**:
   - Giữ nguyên 100% nội dung kỹ thuật, link, ID, code, không tự ý xóa bỏ chi tiết quan trọng.
   - Sửa lỗi chính tả và hành văn cho súc tích, mạch lạc.

3. **Tự động cập nhật file**:
   - Nếu file nằm trong workspace hoặc người dùng chỉ định đường dẫn, ghi đè trực tiếp nội dung đã format vào file.
