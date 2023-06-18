import requests
from bs4 import BeautifulSoup

url = "https://vettroesp.com"
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

images = html.find_all('img', 'data-src=""')


print(images)