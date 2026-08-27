@echo off
chcp 65001 >nul
echo ========================================================
echo   CAI DAT TU DONG TAO GHI CHU DAILY ^& REPORT ^& SUMMARY
echo ========================================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0register_tasks.ps1"

if %errorlevel% equ 0 (
    echo.
    echo ========================================================
    echo [THANH CONG] Da dang ky 2 lich tu dong tren Windows!
    echo ========================================================
    echo 1. Buoi sang (08:00 AM): Tu dong tao file Ghi chu Daily moi.
    echo 2. Cuoi gio (17:35 PM / 5:35 PM): Tu dong doc note va xuat Daily Report tieng Anh!
    echo 3. Cuoi tuan (T7 - CN): Tu dong tong ket Summary toan bo tuan!
) else (
    echo.
    echo [LUU Y] Neu gap loi ve quyen, ban hay chuot phai vao file nay va chon 'Run as administrator'.
)

echo.
pause
