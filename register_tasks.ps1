$scriptPath = Join-Path $PSScriptRoot "create_daily_note.py"
$workingDir = $PSScriptRoot

# Tìm đường dẫn tuyệt đối của python.exe
$pythonExe = (Get-Command python.exe -ErrorAction SilentlyContinue).Source
if (-not $pythonExe -or $pythonExe.EndsWith(".bat")) {
    if (Test-Path "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe") {
        $pythonExe = "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe"
    } elseif (Test-Path "C:\Python311\python.exe") {
        $pythonExe = "C:\Python311\python.exe"
    } else {
        $pythonExe = "python.exe"
    }
}

Write-Host "Su dung Python tai: $pythonExe"

# 1. Task tạo note buổi sáng lúc 08:00
$actionMorning = New-ScheduledTaskAction -Execute $pythonExe -Argument "`"$scriptPath`"" -WorkingDirectory $workingDir
$triggerMorning = New-ScheduledTaskTrigger -Daily -At 8:00AM
Register-ScheduledTask -TaskName "DailyNoteAutoCreate" -Action $actionMorning -Trigger $triggerMorning -Force

# 2. Task tạo Daily Report buổi chiều lúc 17:35 (5:35 PM)
$actionReport = New-ScheduledTaskAction -Execute $pythonExe -Argument "`"$scriptPath`" --report" -WorkingDirectory $workingDir
$triggerReport = New-ScheduledTaskTrigger -Daily -At 5:35PM
Register-ScheduledTask -TaskName "DailyReportAutoCreate" -Action $actionReport -Trigger $triggerReport -Force

Write-Host "SUCCESS: Da dang ky thanh cong cac task vao Task Scheduler!"
Get-ScheduledTask -TaskName "DailyNoteAutoCreate", "DailyReportAutoCreate" | Select-Object TaskName, State
