# PyNano.py

import http.server
import socketserver
import requests
import os
import threading

class PyServer:
    def __init__(self, directory, port):
        self.directory = directory
        self.port = port
        self.httpd = None
        self.server_thread = None

    def start_server(self):
        os.chdir(self.directory)
        handler = http.server.SimpleHTTPRequestHandler
        self.httpd = socketserver.TCPServer(("", self.port), handler)
        print(f"Serving at http://localhost:{self.port}/")
        self.server_thread = threading.Thread(target=self.httpd.serve_forever)
        self.server_thread.start()

    def stop_server(self):
        if self.httpd:
            self.httpd.shutdown()

    def send_get(self):
        url = f"http://localhost:{self.port}"
        response = requests.get(url)
        print("Response code from local server:", response.status_code)
