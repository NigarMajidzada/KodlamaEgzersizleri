# import selenium
import  requests
from bs4 import  BeautifulSoup

url="https://www.alixaprodev.com/"
response=requests.get(url)

# print(response)
html_icerigi=response.content

soup=BeautifulSoup(html_icerigi,"html.parser")

# print(soup.prettify())



for link in soup.find_all("a"):
    print(link)
    print("**************************************************************************")

# print(soup.find_all('div',{'class':'yp-poi-box-2'}))
