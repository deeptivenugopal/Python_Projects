from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class APIHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/fruits':
			self.send_response(200)
			self.send_header('Content-Type','application/json')
			self.end_headers()
			fruits = ['apple','banana','mango']
			self.wfile.write(json.dumps(fruits).encode())
		else:
			self.send_response(404)
			
httpd = HTTPServer(('localhost',8000),APIHandler)
httpd.serve_forever()