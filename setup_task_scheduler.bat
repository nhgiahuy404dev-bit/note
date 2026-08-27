@echo off
chcp 65001 >nul
echo ========================================================
echo   CAI DAT TU DONG TAO GHI CHU DAILY VA SUMMARY
echo ========================================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -Command "$action = New-ScheduledTaskAction -Execute 'python.exe' -Argument '\"%~dp0create_daily_note.py\"'; $trigger = New-ScheduledTaskTrigger -Daily -At 8:00AM; Register-ScheduledTask -TaskName 'DailyNoteAutoCreate' -Action $action -Trigger $trigger -Force"

if %errorlevel% equ 0 (
    echo.
    echo [THANH CONG] Da dang ky lich tu dong chay vao luc 08:00 sang hang ngay!
    echo - Hang ngay (T2 - T6): Tu dong tao ghi chu Daily moi.
    echo - Cuoi tuan (T7 - CN): Tu dong tao Daily note VA tong ket Summary tuan!
) else (
    echo.
    echo [LUU Y] Neu gap loi, ban hay chuot phai vao file nay va chon 'Run as administrator'.
)

echo.
pause
