#!/usr/bin/python3
"""
Task: Build a basic HTTP server using http.server module.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = 'localhost'
PORT = 8000


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Custom handler to process GET requests on different endpoints."""

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

    # Optional: Log suppression
    def log_message(self, format, *args):
        return  # Disable default logging to clean output


def run_server():
    """Starts the HTTP server."""
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Starting server on http://{HOST}:{PORT}")
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()

