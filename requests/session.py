import requests
from getpass import getpass

#By using context manager, you can choose the resources used by
# the session will be released after use

with requests.Session() as session:
    session.auth = ('GeniusLearner', getpass())

    #instead of requests.get, you will use session.get
    response = session.get('https://api.github.com/user')
    response2 = session.get('https://api.github.com/user/repos')

# You can inspect the response just like before
print(response.headers)
print('This is my first repo!')
print(response.json())[0]['url']
