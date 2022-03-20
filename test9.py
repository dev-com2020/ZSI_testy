from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.reddit.com")
browser.execute_script("window.open()")
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get("https://www.youtube.com")
time.sleep(2)
browser.switch_to.window(browser.window_handles[0])
browser.get("https://python.org")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
szerokosc = browser.get_window_size().get("width")
wysokosc = browser.get_window_size().get("height")

rozmiar = browser.get_window_size()
szer1 = rozmiar.get("width")
wys1 = rozmiar.get("height")
print(szer1,wys1)
browser.set_window_size(1024,768)
browser.maximize_window()