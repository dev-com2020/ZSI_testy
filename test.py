import time
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_is
from webdriver_manager import ChromeDriverManager

# https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html?highlight=expected
# pip install webriver-manager

#driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())


print("Rozpoczynam test nr 1")
print("Otwieram stronę...")
driver.implicitly_wait(5)
driver.get(url='https://helion.pl/')
print("Strona otwarta")
print("Wpisuje w wyszukiwarkę...")
driver.find_element(By.ID, 'inputSearch').send_keys('Python' + Keys.ENTER)
print("Wpisano słowo 'Python'")
print("Klikam w zgodę...")
driver.find_element(By.ID, 'rodo-ok').click()
print("Kliknięcie udane")
print("Odnajduje książkę o Pythonie...")
WebDriverWait(driver, timeout=5).until(
    title_is('"Python" - Wyniki wyszukiwania - Wydawnictwo Helion, księgarnia helion.pl'))
print("Czekam na tytuł - Python - Wyniki wyszukiwania...")
WebDriverWait(driver, timeout=5, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException]).until(
    lambda x: x.find_element(By.CLASS_NAME, 'pytmie-link'))
print("Poszukuje elementu 'pytmie-link'")
driver.find_element(By.CLASS_NAME, 'pytmie-link').click()
print("Książka odnaleziona!")
print("Zaglądam do książki...")

zajrzyj = driver.find_element(By.ID, 'zajrzyj')
#webdriver.ActionChains(driver).click_and_hold(zajrzyj).perform()
#webdriver.ActionChains(driver).context_click(zajrzyj).perform()
webdriver.ActionChains(driver).double_click(zajrzyj).perform()
print("Test nr 1 wykonany prawidłowo!")
print("KONIEC")
