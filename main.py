#third part library
#useful when you want to browse the api
import requests
from send_email import send_email

api_key="81eaadf604134ab297c47f8a80ea6bd3"

url = "https://newsapi.org/v2/everything?q=tesla&"\
    "from=2025-08-01&sortBy=publishedAt&apiKey=" \
    "81eaadf604134ab297c47f8a80ea6bd3"

#Make request
request =requests.get(url)

#Get a dictionary with date
content = request.json()

#Access the article title and description
body= ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"]+ "\n"+ article["description"]+2*"\n"

#correct the error
body=body.encode("utf-8")
send_email(message=body)