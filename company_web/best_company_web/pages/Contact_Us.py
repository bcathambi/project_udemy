import streamlit as st
from send_email import sent_email
import pandas
st.header('Contact Us')


df = pandas.read_csv('topics.csv')

with st.form(key='email_form'):
	email = st.text_input("Enter your email")
	option = st.selectbox('What topic do you want to discuss',
	                      df['topic'])
	raw_message = st.text_area("Enter your comments")
	message = f"""\
Subject: New mail - {email}

From: email {email} received
Topic: {option}
{raw_message}
"""
	submit = st.form_submit_button('Submit')
	if submit:
		sent_email(message)
		st.info('Your mail was sent successfully')
