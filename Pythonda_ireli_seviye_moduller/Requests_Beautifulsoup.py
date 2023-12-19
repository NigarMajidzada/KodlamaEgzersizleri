# import selenium
import  requests
from bs4 import  BeautifulSoup

url="https://www.alixaprodev.com/"
response=requests.get(url)

# print(response)
html_icerigi=response.content

soup=BeautifulSoup(html_icerigi,"html.parser")

# print(soup.prettify())

all_link=soup.findAll('a')

for link in all_link:
    print(link.text)
    print("**************************************************************************")

# print(soup.find_all('div',{'class':'yp-poi-box-2'}))
