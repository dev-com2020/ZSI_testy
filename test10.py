from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://helion.pl")
el = driver.find_element(By.CLASS_NAME,'promotion-book')

el.screenshot('promocja1.png')

#driver.maximize_window()
#driver.save_screenshot('zrzut2.png')