# import requests
# import io
# from PIL import Image

# url = 'http://127.0.0.1:5000/upload?key=YourApiKey&mode=label'

# payload = {'image': open('car.jpg','rb')}

# response = requests.post(url, files = payload)

# image_bytes = io.BytesIO(response.content)

# img = Image.open(image_bytes)
# img = img.resize((1024,720))
# img.show('figure')

import requests

url = "http://127.0.0.1:5000/upload?key=YourApiKey&mode=label"

payload={}
files=[
  ('image',('car.jpg',open('/home/yigit/Documents/project/api/car.jpg','rb'),'image/jpeg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)