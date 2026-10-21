@echo off
title CAMPUSSAFE - Smart Campus Safety Platform
color 0B
cls
cd /d "%~dp0"

echo ==============================================================================
echo       CAMPUSSAFE : A Smart Campus Safety & Incident Response Platform        
echo   Bharati Vidyapeeth (Deemed to be University) College of Engineering, Pune   
echo ==============================================================================
echo.

:: Check Node / npm availability
where npm >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [1/3] Node.js and npm detected.
    echo [2/3] Launching Browser at http://localhost:5173/ ...
    start http://localhost:5173/
    echo [3/3] Starting CampusSafe Vite Dev Server...
    echo.
    echo ------------------------------------------------------------------------------
    echo   * Main Landing Page     : http://localhost:5173/
    echo   * Student Safety Portal : http://localhost:5173/student
    echo   * Security Command Hub  : http://localhost:5173/security
    echo ------------------------------------------------------------------------------
    echo Press CTRL+C to stop the server.
    echo.
    npm run dev
    goto :end
)

:: If npm is not found, check for Python to serve the pre-built dist
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [1/3] Node.js not detected in PATH; using Python to serve built application.
    echo [2/3] Launching Browser at http://localhost:5173/ ...
    start http://localhost:5173/
    echo [3/3] Starting CampusSafe Web Server (Python SPA mode)...
    echo.
    echo ------------------------------------------------------------------------------
    echo   * Main Landing Page     : http://localhost:5173/
    echo   * Student Safety Portal : http://localhost:5173/student
    echo   * Security Command Hub  : http://localhost:5173/security
    echo ------------------------------------------------------------------------------
    echo Press CTRL+C to stop the server.
    echo.
    python serve_dist.py
    goto :end
)

echo [ERROR] Neither Node.js (npm) nor Python were found in your PATH.
echo Please install Node.js (https://nodejs.org/) or Python (https://www.python.org/)
echo to launch the CampusSafe platform.
echo.
pause

:end
