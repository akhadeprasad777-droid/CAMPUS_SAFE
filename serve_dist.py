import http.server
import urllib.parse
import os
import sys
import socket
import mimetypes

PORT = 5173
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(BASE_DIR, "dist")
LOG_FILE = os.path.join(BASE_DIR, "server.log")

# Ensure proper MIME types for web assets
mimetypes.init()
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/javascript", ".js")
mimetypes.add_type("text/css", ".css")
mimetypes.add_type("image/svg+xml", ".svg")
mimetypes.add_type("application/json", ".json")

def log(msg):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{msg}\n")
    except Exception:
        pass

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex(("127.0.0.1", port)) == 0

class SPAHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIST_DIR, **kwargs)

    def log_message(self, format, *args):
        log(f"{self.address_string()} - {format % args}")

    def do_GET(self):
        # Strip query params and fragments to check disk file existence
        parsed_url = urllib.parse.urlparse(self.path)
        clean_path = parsed_url.path
        fs_path = self.translate_path(clean_path)

        # If file does not exist, route to /index.html for React Router SPA
        if not os.path.exists(fs_path) or (os.path.isdir(fs_path) and not os.path.exists(os.path.join(fs_path, "index.html"))):
            self.path = "/index.html"

        return super().do_GET()

    def do_HEAD(self):
        parsed_url = urllib.parse.urlparse(self.path)
        clean_path = parsed_url.path
        fs_path = self.translate_path(clean_path)

        if not os.path.exists(fs_path) or (os.path.isdir(fs_path) and not os.path.exists(os.path.join(fs_path, "index.html"))):
            self.path = "/index.html"

        return super().do_HEAD()

    def end_headers(self):
        # Prevent aggressive browser caching during dev/testing
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

if __name__ == "__main__":
    if not os.path.isdir(DIST_DIR):
        log(f"Error: dist folder not found at {DIST_DIR}")
        sys.exit(1)

    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except ValueError:
            pass

    if is_port_in_use(PORT):
        log(f"Server already running on port {PORT}")
        sys.exit(0)

    log(f"Starting ThreadingHTTPServer on port {PORT}")
    http.server.ThreadingHTTPServer.allow_reuse_address = True
    server = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), SPAHandler)
    server.daemon_threads = True

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        log("Server closed.")
