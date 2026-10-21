Set WshShell = CreateObject("WScript.Shell")
' Silently terminate process listening on port 5173
WshShell.Run "powershell -WindowStyle Hidden -Command ""Get-NetTCPConnection -LocalPort 5173 -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }""", 0, True
MsgBox "CampusSafe server has been stopped.", 64, "CampusSafe"
