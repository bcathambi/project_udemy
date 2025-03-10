import smtplib, ssl

def sendemail(message):
	port = 465
	host = "smt.gmail.com"

	username = 'nallathambibca11@gmail.com'
	password = 'moluaavvnxovunxn'

	receiver = "nallathambibca11@gmail.com"
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL(port, host, context=context) as server:
		print("Port", port)
		print("host", host)
		print("context; ", context)
		server.login(username, password)
		server.sendmail(username, receiver, message)