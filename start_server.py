# -*- coding: utf-8 -*-
"""
Dreamy Xmas robust local server.
Double-click 一键启动.bat on Windows, or run: python start_server.py
"""
from __future__ import annotations

import functools
import http.server
import os
import socket
import socketserver
import sys
import threading
import time
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
START_PORT = 8765
MAX_TRIES = 30

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stdout.write("[%s] %s\n" % (self.log_date_time_string(), fmt % args))


def find_free_port(start: int = START_PORT) -> int:
    for port in range(start, start + MAX_TRIES):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind((HOST, port))
                return port
            except OSError:
                continue
    raise RuntimeError(f"No free port found from {start} to {start + MAX_TRIES - 1}.")


def open_browser_later(url: str):
    time.sleep(1.2)
    webbrowser.open(url)


def main():
    os.chdir(ROOT)
    port = find_free_port()
    url = f"http://{HOST}:{port}/index.html"
    handler = functools.partial(NoCacheHandler, directory=str(ROOT))

    with ReusableTCPServer((HOST, port), handler) as httpd:
        print("=" * 68)
        print("Dreamy Xmas · Hand Joint Tracking")
        print(f"Serving folder : {ROOT}")
        print(f"Open address   : {url}")
        print("Keep this window open while using the page.")
        print("If the browser does not open automatically, copy the address above.")
        print("=" * 68)
        threading.Thread(target=open_browser_later, args=(url,), daemon=True).start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("\n启动失败 / Failed to start server:")
        print(exc)
        print("\n请确认：1）已完整解压压缩包；2）电脑已安装 Python；3）没有安全软件拦截本地端口。")
        input("\nPress Enter to exit...")
