import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pyderman

driverpath = pyderman.install(browser=pyderman.chrome)
driver = webdriver.Chrome(driverpath)

driver.maximize_window()
weburl = "https://www.youtube.com"
driver.get(weburl)

wait = ui.WebDriverWait(driver, 3000)

while True:
    try:
        if EC.presence_of_element_located((By.XPATH,".//div/div/div/div/div/span/button/div[contains(text(),'Skip Ad')]")):
            button = driver.find_element(By.XPATH, ".//div/div/div/div/div/span/button/div[contains(text(),'Skip Ad')]")
            driver.execute_script("arguments[0].click();", button)
            print("ad skipped")
            time.sleep(2)
        else:
            continue

    except NoSuchElementException:
        print("no element detected")
        time.sleep(2)
