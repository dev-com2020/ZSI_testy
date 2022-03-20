from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://helion.pl")
driver.find_element(By.LINK_TEXT, "Videokursy").click()
driver.back()
driver.forward()
driver.refresh()



