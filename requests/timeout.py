import requests
from requests.exceptions import Timeout

try:
    response = requests.get('https://api.github.com', timeout=0.35)
except Timeout:
    print('The request timed out ')
else:
    print('The request did not time out.')
