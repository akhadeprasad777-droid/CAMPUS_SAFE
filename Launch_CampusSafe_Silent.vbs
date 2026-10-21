Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
strDir = fso.GetParentFolderName(WScript.ScriptFullName)

' Find pythonw executable
strPythonw = "pythonw"
If fso.FileExists("C:\Program Files\Python314\pythonw.exe") Then
    strPythonw = """C:\Program Files\Python314\pythonw.exe"""
End If

' Run multithreaded server silently in background
WshShell.Run strPythonw & " """ & strDir & "\serve_dist.py""", 0, False

' Brief wait for server binding
WScript.Sleep 600

' Open CampusSafe in default web browser
WshShell.Run "http://localhost:5173/"
