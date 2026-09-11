@echo off
chcp 65001 >nul
echo ========================================================
echo   DAILY NOTE ^& REPORT ^& WEEKLY SUMMARY MANAGER
echo ========================================================
echo.
echo [1] Tao ghi chu Daily hom nay (Tu dong Summary neu la cuoi tuan)
echo [2] Tao Daily Report cuoi ngay (17:35) tu ghi chu hom nay
echo [3] Tao / Cap nhat Summary tuan nay ngay lap tuc
echo [4] Tong ket Summary tat ca cac tuan
echo.
set /p choice="Nhap lua chon cua ban (Nhan Enter de chon 1): "

if "%choice%"=="2" (
    echo.
    python "%~dp0create_daily_note.py" --report
) else if "%choice%"=="3" (
    echo.
    python "%~dp0create_daily_note.py" --summary
) else if "%choice%"=="4" (
    echo.
    python "%~dp0create_daily_note.py" --all-summaries
) else (
    echo.
    python "%~dp0create_daily_note.py"
)

echo.
pause
