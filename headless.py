import timeit
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

start = timeit.default_timer()

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

service = Service("chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://helion.pl")
driver.maximize_window()

driver.find_element(By.ID, 'inputSearch').send_keys("Selenium")

stop = timeit.default_timer()
print('Czas wykonania: ', stop - start)
