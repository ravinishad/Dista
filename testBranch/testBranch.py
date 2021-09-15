from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://www.dista.ai/")
driver.maximize_window()
driver.find_element_by_link_text("Products").click()
wait = WebDriverWait(driver, 5)

driver.find_element_by_link_text("Dista Food").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# will wait 5 seconds to count Branches
Branches = int(wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@data-to-value='200']"))).text)
if(Branches >= 200):
    print("200 Branches")
else:
    print('Branches less than 200')
