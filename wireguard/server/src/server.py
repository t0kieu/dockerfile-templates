#!/usr/bin/env python3
import http.server
import socketserver
import os

server_port = os.environ.get('PORT', '8888')
handler = http.server.SimpleHTTPRequestHandler


with socketserver.TCPServer(("", int(server_port)), handler) as httpd:
    httpd.serve_forever()
