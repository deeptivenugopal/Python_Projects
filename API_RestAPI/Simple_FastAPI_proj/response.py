import requests
from PIL import Image
import io

# resp = requests.get("http://localhost:8000/plot-iris")
# file = io.BytesIO(resp.content)
# im = Image.open(file)
# im.show()


#------------------
resp = requests.get("http://localhost:8000/my-first-api_req_arg?name=Deepti")
print(resp.text)