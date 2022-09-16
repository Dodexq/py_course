import requests
from bs4 import BeautifulSoup

url = 'https://www.webucator.com/course-demos/python/hrleaders.cfm'
r = requests.get(url, headers={'user-agent': 'my-app/0.0.1'})
content = r.text

soup = BeautifulSoup(content, 'lxml')

trs = soup('tr')
tds = soup('td')
first_row = trs[0]
print(first_row('th'))

print(soup.find('tr', 'steroids-era'))
print(ruths := soup.find_all('td', text='Babe Ruth'))
first_ruths_row = ruths[0].parent
print(first_ruths_row)

ruth_birth_day = first_ruths_row.find_all('td')[-1].text
print(ruth_birth_day)