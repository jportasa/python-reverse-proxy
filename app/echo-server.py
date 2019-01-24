#!/usr/bin/env python

import http.server
from urllib.parse import urlparse

PORT = 3000

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        url_parsed_path = urlparse(self.path).path.split('/',1)[1]
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(format(url_parsed_path).encode('utf8'))

server = http.server.HTTPServer(('', PORT), MyHandler)
print('Started http server')
server.serve_forever()

