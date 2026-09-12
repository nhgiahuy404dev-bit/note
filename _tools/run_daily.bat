@echo off
chcp 65001 >nul
echo ========================================================
echo   DAILY NOTE ^& REPORT ^& WEEKLY SUMMARY MANAGER
echo ========================================================
echo.
echo [1] Tao ghi chu Daily hom nay (Tu dong Summary neu la cuoi tuan)
echo [2] Tao Daily Report cuoi ngay (17:35) tu ghi chu hom nay
echo [3] Tao / Cap nhat Weekly Summary vao folder 'Weenly Summary'
echo [4] Tong ket Weekly Summary tat ca cac tuan vao 'Weenly Summary'
echo [5] Kiem tra va tao bu cac ngay con thieu file ghi chu trong tuan
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
) else if "%choice%"=="5" (
    echo.
    python "%~dp0create_daily_note.py" --fill-missing
) else (
    echo.
    python "%~dp0create_daily_note.py"
)

echo.
pause
