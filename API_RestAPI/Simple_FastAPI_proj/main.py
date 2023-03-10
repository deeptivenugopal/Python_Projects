#Basic API
#Used 3 different endpoints to explain the working of endpoint,parameters
'''
How to create an API in Python
https://anderfernandez.com/en/blog/how-to-create-api-python/
'''

from fastapi import FastAPI
app = FastAPI()

@app.get("/my-first-api")
def hello():
	return {"Hello World"}
	
'''
Output:
Browser: http://localhost:8000/my-first-api
["Hello World"]
'''

#Passing of required/mandatory arguments or parameters to the function to add in the endpoint
@app.get("/my-first-api_req_arg")	
def hello_req_arg(name:str):
	return {'Hello '+name+'!'}
	
'''
Output
Browser : http://localhost:8000/my-first-api_req_arg?name=Deepti
["Hello Deepti!"]
'''

#Passing optional arguments with help of None
@app.get("/my_first_api_opt_arg")
def hello_opt_arg(name=None):
	if name is None:
		text = 'Hello'
	else:
		text = 'Hello dear '+name+'!'
	return text

'''
Output
Browser: http://localhost:8000/my_first_api_opt_arg
"Hello"

Browser: http://localhost:8000/my_first_api_opt_arg?name=Deepti
"Hello dear Deepti!"
'''

#Return different data types with FastAPI--Using iris data
@app.get("/get-iris")
def get_iris():
	import pandas as pd
	url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv"
	iris = pd.read_csv(url)
	return iris
	
#resp.text

'''
Output
Browser: http://localhost:8000/get-iris
{"sepal_length":{"0":5.1,"1":4.9,"2":4.7,"3":4.6,"4":5.0,"5":5.4,"6":4.6,"7":5.0,"8":4.4,"9":4.9,"10":5.4,"11":4.8,"12":4.8,"13":4.3,"14":5.8,"15":5.7,"16":5.4,"17":5.1,"18":5.7,"19":5.1,"20":5.4,"21":5.1,"22":4.6,"23":5.1,"24":4.8,"25":5.0,"26":5.0,"27":5.2,"28":5.2,"29":4.7,"30":4.8,"31":5.4,"32":5.2,"33":5.5,"34":4.9,"35":5.0,"36":5.5,"37":4.9,"38":4.4,"39":5.1,"40":5.0,"41":4.5,"42":4.4,"43":5.0,"44":5.1,"45":4.8,"46":5.1,"47":4.6,"48":5.3,"49":5.0,"50":7.0,"51":6.4,"52":6.9,"53":5.5,"54":6.5,"55":5.7,"56":6.3,"57":4.9,"58":6.6,"59":5.2,"60":5.0,"61":5.9,"62":6.0,"63":6.1,"64":5.6,"65":6.7,"66":5.6,"67":5.8,"68":6.2,"69":5.6,"70":5.9,"71":6.1,"72":6.3,"73":6.1,"74":6.4,"75":6.6,"76":6.8,"77":6.7,"78":6.0,"79":5.7,"80":5.5,"81":5.5,"82":5.8,"83":6.0,"84":5.4,"85":6.0,"86":6.7,"87":6.3,"88":5.6,"89":5.5,"90":5.5,"91":6.1,"92":5.8,"93":5.0,"94":5.6,"95":5.7,"96":5.7,"97":6.2,"98":5.1,"99":5.7,"100":6.3,"101":5.8,"102":7.1,"103":6.3,"104":6.5,"105":7.6,"106":4.9,"107":7.3,"108":6.7,"109":7.2,"110":6.5,"111":6.4,"112":6.8,"113":5.7,"114":5.8,"115":6.4,"116":6.5,"117":7.7,"118":7.7,"119":6.0,"120":6.9,"121":5.6,"122":7.7,"123":6.3,"124":6.7,"125":7.2,"126":6.2,"127":6.1,"128":6.4,"129":7.2,"130":7.4,"131":7.9,"132":6.4,"133":6.3,"134":6.1,"135":7.7,"136":6.3,"137":6.4,"138":6.0,"139":6.9,"140":6.7,"141":6.9,"142":5.8,"143":6.8,"144":6.7,"145":6.7,"146":6.3,"147":6.5,"148":6.2,"149":5.9},"sepal_width":{"0":3.5,"1":3.0,"2":3.2,"3":3.1,"4":3.6,"5":3.9,"6":3.4,"7":3.4,"8":2.9,"9":3.1,"10":3.7,"11":3.4,"12":3.0,"13":3.0,"14":4.0,"15":4.4,"16":3.9,"17":3.5,"18":3.8,"19":3.8,"20":3.4,"21":3.7,"22":3.6,"23":3.3,"24":3.4,"25":3.0,"26":3.4,"27":3.5,"28":3.4,"29":3.2,"30":3.1,"31":3.4,"32":4.1,"33":4.2,"34":3.1,"35":3.2,"36":3.5,"37":3.1,"38":3.0,"39":3.4,"40":3.5,"41":2.3,"42":3.2,"43":3.5,"44":3.8,"45":3.0,"46":3.8,"47":3.2,"48":3.7,"49":3.3,"50":3.2,"51":3.2,"52":3.1,"53":2.3,"54":2.8,"55":2.8,"56":3.3,"57":2.4,"58":2.9,"59":2.7,"60":2.0,"61":3.0,"62":2.2,"63":2.9,"64":2.9,"65":3.1,"66":3.0,"67":2.7,"68":2.2,"69":2.5,"70":3.2,"71":2.8,"72":2.5,"73":2.8,"74":2.9,"75":3.0,"76":2.8,"77":3.0,"78":2.9,"79":2.6,"80":2.4,"81":2.4,"82":2.7,"83":2.7,"84":3.0,"85":3.4,"86":3.1,"87":2.3,"88":3.0,"89":2.5,"90":2.6,"91":3.0,"92":2.6,"93":2.3,"94":2.7,"95":3.0,"96":2.9,"97":2.9,"98":2.5,"99":2.8,"100":3.3,"101":2.7,"102":3.0,"103":2.9,"104":3.0,"105":3.0,"106":2.5,"107":2.9,"108":2.5,"109":3.6,"110":3.2,"111":2.7,"112":3.0,"113":2.5,"114":2.8,"115":3.2,"116":3.0,"117":3.8,"118":2.6,"119":2.2,"120":3.2,"121":2.8,"122":2.8,"123":2.7,"124":3.3,"125":3.2,"126":2.8,"127":3.0,"128":2.8,"129":3.0,"130":2.8,"131":3.8,"132":2.8,"133":2.8,"134":2.6,"135":3.0,"136":3.4,"137":3.1,"138":3.0,"139":3.1,"140":3.1,"141":3.1,"
'''

#IMAGES/PLOTS
#StreamingResponse gave NameError in the command line and hence tried with FileResponse by importing
# from fastapi.responses import FileResponse
# from fastapi.responses import StreamingResponse
# @app.get("/plot-iris")
# def plot_iris():
	
	# import pandas as pd
	# import matplotlib.pyplot as plt
	
	# url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv"
	# iris = pd.read_csv(url)
	
	# plt.scatter(iris['sepal_length'],iris['sepal_width'])
	# plt.savefig('iris.png')
	# file = open('iris.png',mode="rb")
	
	# #return StreamingResponse(file, media_type="image/png")
	# return FileResponse('iris.png')
	
# '''
# Output
# Browser: http://localhost:8000/plot-iris
# Gave plot image
# '''


# import requests
# from PIL import Image
# import io

# resp = requests.get("http://localhost:8000/plot-iris")
# file = io.BytesIO(resp.content)
# im = Image.open(file)
# im.show()
