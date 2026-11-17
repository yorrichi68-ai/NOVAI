#!/usr/bin/env python3
"""Local-only NOVA bridge: serves the UI and proxies API calls to ComfyUI."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COMFY = "http://127.0.0.1:8188"

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path.startswith("/api/"):
            self.proxy("GET")
        else:
            super().do_GET()

    def do_POST(self):
        if self.path.startswith("/api/"):
            self.proxy("POST")
        else:
            self.send_error(404)

    def proxy(self, method):
        path = self.path[len("/api"):]
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length) if length else None
        headers = {k: self.headers[k] for k in ("Content-Type", "Accept") if self.headers.get(k)}
        req = Request(COMFY + path, data=body, headers=headers, method=method)
        try:
            with urlopen(req, timeout=1800) as response:
                data = response.read()
                self.send_response(response.status)
                self.send_header("Content-Type", response.headers.get("Content-Type", "application/octet-stream"))
                self.send_header("Content-Length", str(len(data)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(data)
        except HTTPError as e:
            data = e.read()
            self.send_response(e.code)
            self.send_header("Content-Type", e.headers.get("Content-Type", "text/plain"))
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except (URLError, TimeoutError, OSError) as e:
            data = ("ComfyUI connection failed: " + str(e)).encode()
            self.send_response(502)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

    def log_message(self, fmt, *args):
        print("[NOVA] " + (fmt % args))

if __name__ == "__main__":
    print("NOVA AI running at http://127.0.0.1:8000")
    print("ComfyUI expected at " + COMFY)
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
