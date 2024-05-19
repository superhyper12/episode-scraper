import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://en.wikipedia.org/wiki/Kaiju_No._8'

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

element1 = soup.find_all('td', class_='summary')
element2 = soup.find_all('span', class_='bday dtstart published updated itvstart')
element3 = soup.find_all('div', class_='shortSummaryText')

episode_title =  element1[-1].text
release_date = element2[-1].text
episode_description = element3[-1].text

date_obj = datetime.strptime(release_date, "%Y-%m-%d")
formatted_date = date_obj.strftime("%b %d, %Y")

print(f'New episode: {episode_title}')
print(f'Release date: {formatted_date}')
print(f'Description: {episode_description}')