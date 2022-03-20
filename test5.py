from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://helion.pl")

#driver.add_cookie({"name": "tomek", "value": "selenium"})
#driver.delete_all_cookies()
driver.delete_cookie("tomek")
#print(driver.get_cookie("name"))
print(driver.get_cookies())
