import http.server
import socketserver
import json
import random
import time
import os

PORT = 8000


class AIRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            try:
                data = json.loads(post_data.decode('utf-8'))
                user_message = data.get('message', '').lower()

                # Simple "AI" mock responses
                responses = [
                    "That's an interesting perspective! Tell me more.",
                    "I am ADHI AI, and my neural networks are processing your request.",
                    "I've analyzed your input. What would you like to explore next?",
                    "Fascinating. I can assist you further with that.",
                    "As an advanced artificial intelligence, I'm constantly learning from our interactions.",
                    "I understand. Let's delve deeper into this topic."
                ]

                response_text = random.choice(responses)

                # Keyword-based routing to make it feel smarter
                if "hello" in user_message or "hi" in user_message or "hey" in user_message:
                    response_text = "Hello! I am ADHI AI. How can I assist you today?"
                elif "name" in user_message:
                    response_text = "My name is ADHI AI. I function as a premium intelligent assistant designed to help you."
                elif "who are you" in user_message:
                    response_text = "I am ADHI AI, a cutting-edge artificial intelligence powered by advanced algorithms."
                elif "best" in user_message or "awesome" in user_message or "great" in user_message:
                    response_text = "Thank you! I strive to provide the absolute best experience and intelligence."
                elif "create" in user_message or "make" in user_message:
                    response_text = "I can help you create and build amazing things. Just let me know the details!"

                # Simulate thinking delay
                time.sleep(1.2)

                response_data = {
                    "reply": response_text
                }

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response_data).encode('utf-8'))

            except Exception as e:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()


# Set up to serve the current directory (where index.html will be)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("==============================================")
print("      ADHI AI SERVER INITIALIZATION           ")
print("==============================================")
print(f"Starting local server at: http://localhost:{PORT}")
print("Press Ctrl+C to stop the server.")

try:
    with socketserver.TCPServer(("", PORT), AIRequestHandler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
