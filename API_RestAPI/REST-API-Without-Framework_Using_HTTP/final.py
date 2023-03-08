#https://github.com/RahulYadav119/PYTHON-REST-API-Without-Framework-  - Didnot understand completely
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

#open json file and give it to data variable, in the form of dictionary
with open("db.json") as data_file:
	data = json.load(data_file)

print(data)
print(type(data))

#Defining a HTTP Request Handler class
class ServiceHandler(BaseHTTPRequestHandler):
	#sets basic headers for the server
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type','text/json')
		#reads the length of the headers
		length = int(self.headers['Content-Length'])
		#reads the content of the request
		content = self.rfile.read(length)
		temp = str(content).strip('b\'')
		self.end_headers()
		return temp
		
	######
	#LIST#
	######
	#GET Method definition
	def do_GET(self):
		#defining all the headers
		self.send_response(200)
		self.send_header('Content-type','text/json')
		self.end_headers()
		#prints all the keys and values of the json file
		self.wfile.write(json.dumps(data).encode())
		
	######
	#VIEW#
	######
	#View method definition
	def do_View(self):
		#dict var for pretty print
		display = {}
		temp = self._set_headers()
		#check if the key is present in the dictionary
		if temp in data:
			display[temp] = data[temp]
			#print the keys required from the json file
			self.wfile.write(json.dumps(display).encode())
		else:
			error = "NOT FOUND!"
			self.wfile.write(bytes(error,'utf-8'))
			self.send_response(404)
	
	######
	#CREATE#
	########
	#POST Method definition
	def do_POST(self):
		temp = self._set_headers()
		key = 0
		#getting key and value from data
		for key,value in data.items():
			pass
		index = int(key) + 1
		data[str(index)] = str(temp)
		#write changes to the json file
		with open("db.json",'w+') as file_data:
			json.dump(data,file_data)
		#self.wfile.write(json.dump(data[str(index)]).encode()
		
	
	########
	#UPDATE#
	########
	#PUT method Defination
	def do_PUT(self):
		temp = self._set_headers()
		#seprating input into key and value
		x = temp[:1]
		y = temp[2:]
		#check if key is in data
		if x in data:
			data[x] = y
			#write the changes to file
			with open("db.json",'w+') as file_data:
				json.dump(data,file_data)
			#self.wfile.write(json.dumps(data[str(x)]).encode())
		else:
			error = "NOT FOUND!"
			self.wfile.write(bytes(error,'utf-8'))
			self.send_response(404)
			
	########
	#DELETE#
	########
	#DELETE method defination	
	def do_DELETE(self):
		temp = self._set_headers()
		#check if the key is present in the dictionary
		if temp in data:
			del data[temp]
			#write the changes to json file
			with open("db.json",'w+') as file_data:
				json.dump(data,file_data)
		else:
			error = "NOT FOUND!"
			self.wfile.write(bytes(error,'utf-8'))
			self.send_response(404)
			
#Server Initialization
server = HTTPServer(('127.0.0.1',8080), ServiceHandler)
server.serve_forever()
print("Server Started at PORT = 8000")