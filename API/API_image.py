import requests

url = "https://wii.gov.in/images//images/documents/images_2024/cheetah_landscapa_2024.jpg"

response = requests.get(url)
image = response.content

# open and read binary content as image
with open("image.jpg", "wb") as file:
	file.write(image)
