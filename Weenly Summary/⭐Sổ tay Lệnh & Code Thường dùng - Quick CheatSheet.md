# ⭐ Sổ Tay Lệnh & Code Thường Dùng (Quick Commands Cheat Sheet)

Tài liệu này tổng hợp toàn bộ các chuỗi câu lệnh Git, câu lệnh Terminal, Slash Commands và mẫu tin nhắn thường xuyên sử dụng trong công việc QA hàng ngày.

---

## 🌿 1. Chuỗi Câu Lệnh Git Thường Dùng

### 🔹 1.1. Tạo nhánh mới cho Endpoint / Feature (Yêu cầu chuẩn)
Áp dụng mỗi khi bắt đầu một ticket Endpoint Automation mới:

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
> **Quy ước đặt tên nhánh:** Luôn gắn liền ID ticket Jira và định danh endpoint cụ thể (ví dụ: `QA-6700-instruction-by-step-ref`).

---

### 🔹 1.2. Đồng bộ code mới nhất từ `main` về nhánh đang làm (Sync Code Flow)
Chuẩn hóa luồng lấy code mới nhất về nhánh endpoint để tránh xung đột:

```bash
# Luồng chuẩn theo AGENTS.md:
git switch main
git pull
git fetch origin
git switch main
git pull origin main
git switch <endpoint>
git pull
git pull origin main
```

Hoặc cách gộp nhanh bằng `merge`:
```bash
git switch <endpoint>
git fetch origin
git merge origin/main
```

---

### 🔹 1.3. Commit, Push và Tạo Pull Request
```bash
# 1. Kiểm tra trạng thái các file đã sửa
git status

# 2. Đưa toàn bộ thay đổi vào staging
git add .

# 3. Commit theo format chuẩn (gắn ticket ID)
git commit -m "feat(QA-xxxx): <mô tả nội dung thay đổi>"

# 4. Push nhánh lên GitHub remote
git push -u origin <branch-name>-<endpoint>
```

---

### 🔹 1.4. Xử lý sự cố Git & Dọn dẹp cục bộ
```bash
# Hủy các thay đổi chưa commit trên working tree
git restore .

# Xóa triệt để các file/thư mục rác mới sinh ra (untracked)
git clean -fd

# Xem 5 commit gần nhất trên 1 dòng
git log --oneline -n 5
```

---

## ⚡ 2. Danh Sách Slash Commands Thường Dùng (Claude / Antigravity AI)

| Lệnh Slash | Mục đích sử dụng | Workflow áp dụng |
| :--- | :--- | :---: |
| `/create-draft-test-execution` | Sinh kịch bản kiểm thử nháp từ Jira / Confluence spec / PR diff | Workflow 2 (Bước 1) |
| `/create-test-artifact` | Tự động đồng bộ kịch bản kiểm thử từ Jira sang Confluence | Workflow 2 (Bước 4) |
| `/Create-testrail-cases-from-confluence` | Đọc Confluence sinh file markdown draft test cases chuẩn TestRail | Workflow 2 (Bước 7 - Chưa có case) |
| `/Create-TR-Run-From-TR-Draft` | Import test cases vào TestRail, tạo Test Run và đính kèm evidence Pass | Workflow 2 (Bước 7 - Chưa có case) |
| `/create-testrail-test-run-from-confluence` | Tạo ngay Test Run ghi nhận Pass khi **ĐÃ CÓ SẴN** cases trên TestRail | Workflow 2 (Bước 7 - Đã có case) |
| `/create-testrail` & `/sync-testrail` | Khởi tạo test cases mới trên TestRail và đồng bộ ID lên Jira ticket | Workflow 1 (Bước 7) |
| `/review-code` | Quét kiểm tra chất lượng code và dọn dẹp orphan functions | Workflow 1 (Bước 9) |
| `/pr summary` | Tự động trích xuất nội dung tóm tắt PR phục vụ mở Pull Request | Workflow 1 (Bước 12) |
| `/resolve-pr` | Xử lý phản hồi review của Dastan trên PR | Workflow 1 (Bước 15) |

---

## 🛠️ 3. Scripts Hỗ Trợ & Tác Vụ Tự Động Hóa Workspace

### 🔹 3.1. Tool quản lý Ghi chú Daily & Báo cáo (Python CLI)
Thực thi tại thư mục `DOCUMENT`:

```powershell
# 1. Kiểm tra và tự động tạo bù file ghi chú còn thiếu trong tuần
python "d:\Workspace\main\Study_GALAXY\DOCUMENT\Ghi chú daily\_tools\create_daily_note.py" --fill-missing

# 2. Tạo Daily Report cuối ngày bằng tiếng Anh chuẩn (ngày hôm nay)
python "d:\Workspace\main\Study_GALAXY\DOCUMENT\Ghi chú daily\_tools\create_daily_note.py" --report

# 3. Tạo Daily Report cho một ngày cụ thể (ví dụ ngày 23/09/2026)
python "d:\Workspace\main\Study_GALAXY\DOCUMENT\Ghi chú daily\_tools\create_daily_note.py" --report 23092026

# 4. Tạo hoặc cập nhật Weekly Summary cho tuần hiện tại
python "d:\Workspace\main\Study_GALAXY\DOCUMENT\Ghi chú daily\_tools\create_daily_note.py" --summary
```

### 🔹 3.2. Helper Scripts trong Repository
```bash
# Kiểm tra danh sách API mới phát sinh
./Helper\ Script/check-new-apis

# Cập nhật lộ trình dự án (Roadmap)
./update-roadmap.sh
```

---

## 🚀 4. Lệnh DevOps & Atlantis (Terraform Secrets)

Áp dụng khi thêm secret mới cho Jenkins trên repository `terraform`:

```bash
# Gõ bình luận trực tiếp trên GitHub Pull Request sau khi nhận Approval từ SRE-ONCALL:
atlantis apply
```

> [!WARNING]
> **Quy tắc đặt Key trên Terraform:** Bắt buộc phải **thêm dấu sao (`*`) vào sau cùng của key** (suffix `*`, ví dụ: `<secret_key_name>*`) để đảm bảo match đúng phạm vi phân quyền.
> Tuyệt đối **không merge PR** khi `atlantis apply` chưa chạy thành công 100%.

---

## 💬 5. Mẫu Tin Nhắn Slack Chuẩn Dùng Hàng Ngày

### 🔹 5.1. Hỏi Dastan trước khi làm ticket (Chống Duplicate - Bắt buộc)
> 💬 `"Hi Dastan, for ticket <TICKET_ID> (<TICKET_NAME>), have you created the draft ticket or test cases yet? If not, I will start creating the draft test execution."`

### 🔹 5.2. Nhờ Dev Review sau khi hoàn tất kiểm thử (`Pass Test` ✅)
> 💬 `"Hi @dev, ticket <TICKET_KEY> has been tested and passed (Pass Test ✅). Here is the detailed test section: <Jira_Link>. Could you please help review? Thank you!"`

### 🔹 5.3. Nhắn tin bàn giao UAT Testing cho Ops (@tiffany.kao, @jento.chan)
> 💬 `"hi @tiffany.kao , @jento.chan we have completed testing for <TICKET_KEY_AND_TITLE> on QA environment. And we already set it up on UAT environment, please help testing it on UAT. Thank you! 🙏"`  
> `"UAT UI deployed at: web-reports.uat-gp.galaxydigital.io/fund_transfer_tool"`

### 🔹 5.4. Mẫu Email UAT Sign-off gửi Tiffany Kao & Ops Team
* **To:** `tiffany.kao@galaxydigital.io`, `jento.chan@galaxydigital.io`
* **Subject:** `[UAT Sign-off Request] <RELEASE_NAME> - <TICKET_KEY_AND_TITLE>`
* **Nội dung:**
  > *"Hi Tiffany & Ops team,*  
  >  
  > *QA has completed testing for **<TICKET_KEY> (<TICKET_TITLE>)** on QA environment with 100% Passed.*  
  > *The release is now deployed and ready for your UAT testing:*  
  > *- **UAT URL:** `web-reports.uat-gp.galaxydigital.io/fund_transfer_tool`*  
  > *- **Jira Ticket:** `<TICKET_KEY>`*  
  > *- **Key Scope:** <Phạm vi test chính đã pass trên QA>*  
  >  
  > *Please help test and provide your **UAT Sign-off** via this email thread once completed. Thank you! 🙏"*

---

## 📌 6. Thông Số Cố Định Cần Nhớ (Quick Specs Cheat Sheet)

* **Epic cha bắt buộc:** `QA-3614: Transfer Tools Enhancement and feedback`
* **Quan hệ Linked Work Items trên Jira:** Type `tests` trỏ vào Request Ticket (`GTO-xxxx` / `RM-xxxx`).
* **TestRail Project ID:** `30`
  * **Suite API:** `945`
  * **Suite UI:** `946`
  * **Suite E2E:** `947`
* **Môi trường UAT:** `web-reports.uat-gp.galaxydigital.io/fund_transfer_tool`
