import requests
from sendemail import sendemail
api_key = "890603a55bfa47048e4490069ebee18c"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=890603a55bfa47048e4490069ebee18c"

request = requests.get(url)
content = request.json()

body = ""
for article in content['articles']:
	if article['title'] is not None:
		body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode('utf-8')
sendemail(message=body)



