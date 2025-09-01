#third part library
#useful when you want to browse the api
import requests

api_key="81eaadf604134ab297c47f8a80ea6bd3"

url = "https://newsapi.org/v2/everything?q=tesla&"\
    "from=2025-08-01&sortBy=publishedAt&apiKey=" \
    "81eaadf604134ab297c47f8a80ea6bd3"

#Make request
request =requests.get(url)

#Get a dictionary with date
content = request.json()

#Access the article title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])