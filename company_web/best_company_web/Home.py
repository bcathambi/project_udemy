import streamlit as st
import pandas

st.set_page_config(layout='wide')
st.title('The Best Company')

content = """
	As you can see on my profile, company profiles go beyond a regular About page. My profile details how I started, 
	why I create content, and my journey to finally starting the blog. A simple About page would typically only include 
	a brief overview of who the company is and a point of contact.Your company profile would show your company's 
	beginnings and why you continue to serve customers. Essentially, it humanizes your brand.
"""
st.write(content)

st.header('Our Team')

col1, col2, col3 = st.columns(3)

dt = pandas.read_csv('data.csv')

with col1:
	for index, row in dt[:4].iterrows():
		st.write(f"{row['first name'].title()} {row['last name'].title()}")
		st.write(row['role'])
		st.image('images/'+ row['image'])

with col2:
	for index, row in dt[4:8].iterrows():
		st.write(f"{row['first name'].title()} {row['last name'].title()}")
		st.write(row['role'])
		st.image('images/'+ row['image'])

with col3:
	for index, row in dt[8:].iterrows():
		st.write(f"{row['first name'].title()} {row['last name'].title()}")
		st.write(row['role'])
		st.image('images/'+ row['image'])