from bs4 import BeautifulSoup
import urllib.request
import re
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
page = urllib.request.urlopen(url) # conntect to website
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
regex = re.compile('^tocsection-')
content_lis = soup.find_all('li', attrs={'class': regex})
content = []
content = []
for li in content_lis:
    content.append(li.getText().split('\n')[0])
for i in content:
  print(i)
