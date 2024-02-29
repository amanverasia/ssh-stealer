import http.server
import socketserver

PORT = 8000 

class WebhookHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)  # Read the data

        # Write the received data to a file
        with open("received_data.txt", "wb") as f:  # Use wb for binary mode
            f.write(data)

        print(f"Received data written to 'received_data.txt'")
        self.send_response(200)

with socketserver.TCPServer(("", PORT), WebhookHandler) as httpd:
    print("Webhook server listening on port", PORT)
    httpd.serve_forever()