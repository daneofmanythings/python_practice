'''https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html'''

# Use the BeautifulSoup and requests Python packages to print out a list
# of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.nytimes.com/')
soup = BeautifulSoup(r.text, 'lxml')
for item in soup.select('h3') :  # At the time of writing, this is the best way I could find to isolate story titles.
    print(item.text)