from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write(json.dumps({'message': 'hello world'}))

if __name__ == "__main__":
    hostName = ''
    port = 8080
    webServer = HTTPServer((hostName, port), MyServer)
    print("Server started http://%s:%s" % (hostName, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
