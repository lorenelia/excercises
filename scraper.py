import shutil
import requests
from tinypng import shrink_file
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()
response=requests.get("your url here")
soup = BeautifulSoup(response.text, 'html.parser')
images = soup.find_all("img")

counter = 1
api_key = "tinypng key here"
for image in images:
	image_source = image.get("src")
	if image_source.endswith (".png"):
		response=requests.get(image_source, stream=True)
		

		image_name = "results/" + str(counter) + ".png"
		with open(image_name, "wb") as f:
			response.raw.decode_contet = True
			shutil.copyfileobj(response.raw, f)
			print image_source
			print image_name

		compressed_image_name =  "compressed/"+ str(counter) + ".png"	

		shrink_info = shrink_file(
			image_name,
    		api_key=api_key,
    		out_filepath=compressed_image_name)

		counter = counter + 1
