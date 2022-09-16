import requests

url = 'https://www.webucator.com/course-demos/python/hrleaders.cfm'
r = requests.get(url, headers={'user-agent': 'my-app/0.0.1'})
content = r.text
print(content[:125]) # print first 125 characters