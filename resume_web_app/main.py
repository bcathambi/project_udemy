import streamlit as sg
import pandas

sg.set_page_config(layout='wide')

col1, col2 = sg.columns(2)

with col1:
	sg.image("images/photo.png")

with col2:
	sg.title('Nallathambi L')
	content ='''
	Having a 3.5 years of hands-on experience in manual testing within the automotive sector, I’ve mastered the art of ensuring the seamless performance and quality of automotive systems. My career began at Ford, where I gained invaluable experience working on modules such as Multimedia, Audio, SiriusXM, Radio, OOM, IVIS, OTA, IZT. Having experience in real world In-Vehicle drive test.

Current Role: NVH (Noise, Vibration, and Harshness) Module Testing
	'''
	sg.info(content)

content2 = '''Below you can find some of the apps I have build in python. Feel free to contact me'''
sg.write(content2)

tb = pandas.read_csv('data.csv', sep=';')
col3, empty_col, col4 = sg.columns([1.5, 0.5, 1.5])

with col3:
	for index, row in tb[:10].iterrows():
		sg.header(row['title'])
		sg.write(row['description'])
		sg.image('images/'+row['image'])
		sg.write(f"[Source Code]({row['url']})")

with col4:
	for index, row in tb[10:].iterrows():
		sg.header(row['title'])
		sg.write(row['description'])
		sg.image('images/' + row['image'])
		sg.write(f"[Source Code]({row['url']})")