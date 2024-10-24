from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Added import for Keys
import allure
import selenium
from allure_commons.types import AttachmentType
import time
from pathlib import Path
import pyautogui

#Create a webdriver object. Here we use Firefox, but you can choose other browsers like Chrome, Edge, etc.
def testPythonSelenium(driver):
    with allure.step("Step 1"):
        # Navigate to the GeeksforGeeks website
        driver.get("https://www.geeksforgeeks.org/")
        # Maximize the browser window
        driver.maximize_window()
        # Locate the search icon element using XPath
        searchIcon = driver.find_element(By.XPATH, "//span[@class='flexR gs-toggle-icon']")
        # Click on the Search Icon to activate the search field
        searchIcon.click()
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name="None", attachment_type=AttachmentType.PNG)
        # Locate the input field for search text using XPath
        enterText = driver.find_element(By.XPATH, "//input[@class='gs-input']")
        
        # Enter the search query "Data Structure" into the input field
        enterText.send_keys("Data Structure")
        time.sleep(2)
        
        enterText.send_keys(Keys.RETURN)
