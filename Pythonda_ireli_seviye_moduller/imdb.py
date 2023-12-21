from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd

driver=webdriver.Chrome()
driver.get("https://www.imdb.com/chart/top/")
button= driver.find_element(By.ID,'list-view-option-detailed')
button.click()

soup=BeautifulSoup(driver.page_source,'html.parser')

movie_list = soup.find_all ('li',{'class':'ipc-metadata-list-summary-item'})

titles=[]
images=[]
years=[]
durations=[]
imdb_ratings=[]
descs=[]


for movie in movie_list:
    title=movie.h3.text
    titles.append(title)
    image=movie.img['src']
    images.append(image)
    year=movie.find_all('span',{'class':'sc-43986a27-8 jHYIIK dli-title-metadata-item'})[0].text
    years.append(year)
    duration=movie.find_all('span',{'class':'sc-43986a27-8 jHYIIK dli-title-metadata-item'})[1].text
    durations.append(duration)
    imdb_rating=movie.find('span',{'class':'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating'}).text
    imdb_ratings.append(imdb_rating)
    desc=movie.find('div',{'class':'ipc-html-content-inner-div'}).text
    descs.append(desc)

Data = pd.DataFrame({'titles': titles, 'year': years, 'duration': durations, 'image': images, 'description': descs,
                         'imdb_rating': imdb_ratings})

Data.to_csv('IMDB top 250 Movies.csv')
