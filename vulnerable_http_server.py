from http.server import BaseHTTPRequestHandler, HTTPServer

a=0

class VulnerableHTTPRequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		global a
		# Simulate a Long Processing time (2 seconds)
		import time
		time.sleep(2) # Simulate Processing Delay

		self.send_response(200)
		self.send_header("Content-type", "text/plain")
		self.end_headers()
		st=str(a)
		self.wfile.write(b"Hello Hacker" + st.encode("utf-8"))

def run(server_class=HTTPServer, handler_class=VulnerableHTTPRequestHandler, port=8000):
	server_address = ("127.0.0.1", port)
	httpd = server_class(server_address, handler_class)
	print(f"Starting httpd on port: {port} ....")
	httpd.serve_forever()

if __name__=="__main__":
	run()
