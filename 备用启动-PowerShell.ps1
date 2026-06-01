Set-Location -Path $PSScriptRoot
$python = Get-Command py -ErrorAction SilentlyContinue
if ($python) {
  py -3 start_server.py
  exit
}
$python2 = Get-Command python -ErrorAction SilentlyContinue
if ($python2) {
  python start_server.py
  exit
}
Write-Host "未检测到 Python。请安装 Python 3，或使用 VS Code Live Server。"
Read-Host "按回车退出"
