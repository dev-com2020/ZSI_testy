from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class Test_1:
    def test(self):
        driver = webdriver.Chrome()
        self.latitude = 42.1408845
        self.longitude = -72.5033907
        self.accuracy = 100

        driver.maximize_window()
        driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "accuracy": self.accuracy
        })

        driver.get("https://locations.dennys.com/search.html/")
        time.sleep(7)
        location_icon = driver.find_element(By.CSS_SELECTOR, ".icon-geolocate")
        time.sleep(7)
        location_icon.click()
        time.sleep(7)
        print("Test zakończony!")