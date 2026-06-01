@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Dreamy Xmas Hand Joint Tracking Server
echo ============================================================
echo Dreamy Xmas 手指关节追踪版 - 本地服务器启动器
echo ============================================================
echo.
echo 正在启动，请不要关闭此窗口。
echo 页面会自动打开；如果没有自动打开，请复制窗口中的地址。
echo.
where py >nul 2>nul
if %errorlevel%==0 (
    py -3 start_server.py
    goto end
)
where python >nul 2>nul
if %errorlevel%==0 (
    python start_server.py
    goto end
)
echo 未检测到 Python。
echo 请安装 Python 3，或在 VS Code 中使用 Live Server 打开 index.html。
echo 也可以尝试直接双击 index.html，但摄像头权限可能受浏览器限制。
:end
echo.
pause
