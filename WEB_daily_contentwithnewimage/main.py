import streamlit as st
import requests

# NASA API KEY
api_key = "QumO0ALhqSIvVTINNpTmdhMEBtGkPMu908JRiycW"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"
response1 = requests.get(url)
data = response1.json()

title = data['title']
explanation = data['explanation']
img_url = data['url']

image_name = 'img.jpg'
response2 = requests.get(img_url)
image = response2.content

with open(image_name, "wb") as file:
	img = file.write(image)

st.title(title)
st.image(image_name)
st.text(explanation)
