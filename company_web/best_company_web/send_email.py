import smtplib, ssl


def sent_email(message):
	host = 'smtp.gmail.com'
	port = 465
	username = 'nallathambibca11@gmail.com'
	password = 'moluaavvnxovunxn'
	#password = os.getenv("PASSWORD")
	receiver = 'nallathambibca11@gmail.com'
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(host, port, context=context) as server:
		server.login(username, password)
		server.sendmail(username, receiver, message)
