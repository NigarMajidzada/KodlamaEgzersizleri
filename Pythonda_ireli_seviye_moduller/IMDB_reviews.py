from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from tqdm import tqdm
import pandas as pd


driver=webdriver.Chrome()
driver.get('https://www.imdb.com/title/tt0111161/reviews?ref_=tt_urv')

soup= BeautifulSoup(driver.page_source,'html.parser')

review_count=int(soup.find('div',{'class':'header'}).span.text.split(' ')[0].replace(',',''))

iterations = int (review_count/25)

for i in tqdm(range(5)):
    button=driver.find_element(By.ID,'load-more-trigger')
    button.click()
    time.sleep(5)

soup= BeautifulSoup(driver.page_source,'html.parser')

review_list=soup.find_all('div',{'class':'lister-item-content'})
review_list[0]

titles=[]
users=[]
dates=[]
descs=[]

for review in review_list:
    title = review.a.text.strip()
    titles.append(title)
    user = review.find('span', {'class': 'display-name-link'}).text.strip()
    users.append(user)
    date = review.find('span', {'class': 'review-date'}).text.strip()
    dates.append(date)
    desc = review.find('div', {'class': 'content'}).text.strip()
    descs.append(desc)

Data=pd.DataFrame({'Titles':titles,'Users':users,'Dates':dates,'Desc':descs})
Data.to_csv('IMDB Reviews.csv')
