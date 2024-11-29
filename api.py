from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = {"message": "Olá, mundo!"}

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET request"""
        if self.path == "/api":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.end_headers()

def run():
    server_address = ('', 8000) 
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    print("Iniciando o servidor na porta 8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
