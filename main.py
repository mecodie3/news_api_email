#third part library
#useful when you want to browse the api
import requests
from send_email import send_email


topic ="tesla"
api_key="81eaadf604134ab297c47f8a80ea6bd3"

url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&"\
    "from=2025-08-01&"\
      "sortBy=publishedAt&"\
      "apiKey=81eaadf604134ab297c47f8a80ea6bd3&language=en"

#Make request
request =requests.get(url)

#Get a dictionary with date
content = request.json()

#Access the article title and description, articles are limited to 20
body = "Subject: Today's news\n\n"

for article in content["articles"][:20]:
    title = article.get("title", "")
    description = article.get("description", "")
    url = article.get("url", "")

    body += (
        f"{title}\n"
        f"{description}\n"
        f"{url}\n\n"
    )
#correct the error
body=body.encode("utf-8")
send_email(message=body)