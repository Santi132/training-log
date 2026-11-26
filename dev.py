"""Dev server with live reload. Stdlib only; not part of the app.

    python dev.py                      # http://127.0.0.1:8000/
    python dev.py --bind 192.168.0.13  # reachable from a phone on the LAN

Injects a tiny EventSource snippet into served HTML (index.html on disk is
untouched) and pushes a new version whenever a watched file changes, so open
pages reload themselves. Sends Cache-Control: no-store on everything.
On localhost use ?nosw so the service worker doesn't cache over your edits.
"""
import argparse
import http.server
import os
import time
from functools import partial

ROOT = os.path.dirname(os.path.abspath(__file__))
WATCH = {'.html', '.js', '.css', '.json', '.png', '.svg'}
SNIPPET = (b"<script>(()=>{let v;const es=new EventSource('/__reload');"
           b"es.onmessage=e=>{if(v&&e.data!==v)location.reload();v=e.data;};})();</script>")


def version():
    latest = 0
    for dirpath, dirnames, files in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for f in files:
            if os.path.splitext(f)[1] in WATCH:
                try:
                    latest = max(latest, os.stat(os.path.join(dirpath, f)).st_mtime_ns)
                except OSError:
                    pass
    return str(latest)


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def do_GET(self):
        path = self.path.split('?', 1)[0]
        if path == '/__reload':
            return self.stream()
        fs = self.translate_path(path)
        if path.endswith('/') and os.path.isdir(fs):
            fs = os.path.join(fs, 'index.html')
        if fs.endswith('.html') and os.path.isfile(fs):
            with open(fs, 'rb') as fh:
                body = fh.read().replace(b'</body>', SNIPPET + b'</body>', 1)
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def stream(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/event-stream')
        self.end_headers()
        last, idle = None, 0.0
        try:
            while True:
                v = version()
                if v != last:
                    self.wfile.write(f'data: {v}\n\n'.encode())
                    last, idle = v, 0.0
                elif idle >= 15:
                    self.wfile.write(b': ping\n\n')  # keeps idle connections open
                    idle = 0.0
                self.wfile.flush()
                time.sleep(0.4)
                idle += 0.4
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
            pass

    def log_message(self, fmt, *args):
        if '/__reload' not in self.path:
            super().log_message(fmt, *args)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--bind', default='127.0.0.1')
    ap.add_argument('--port', type=int, default=8000)
    a = ap.parse_args()
    srv = http.server.ThreadingHTTPServer((a.bind, a.port), partial(Handler, directory=ROOT))
    srv.daemon_threads = True
    print(f'Serving {ROOT} at http://{a.bind}:{a.port}/ with live reload', flush=True)
    srv.serve_forever()
