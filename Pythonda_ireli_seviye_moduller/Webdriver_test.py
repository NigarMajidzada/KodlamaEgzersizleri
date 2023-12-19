from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# WebDriver'ı başlat
chrome_path = "path/to/chromedriver"  # chromedriver'ın dizinini belirtin
chrome_options = Options()
chrome_options.add_argument("--headless")  # Arka planda çalıştırmak için
chrome_service = ChromeService(executable_path=chrome_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

url = "https://yellowpages.com.tr/"

# Sayfayı aç
driver.get(url)

# Sayfanın tam yüklenmesini bekle (gerekirse süreyi ayarlayabilirsiniz)
driver.implicitly_wait(5)

# Sayfanın tam içeriğini al
html_content = driver.page_source

# WebDriver'ı kapat
driver.quit()

# BeautifulSoup ile işlem yapabilirsiniz
soup = BeautifulSoup(html_content, "html.parser")

# Örneğin tüm "a" etiketlerini bulabilirsiniz
print(soup.find_all("a"))
