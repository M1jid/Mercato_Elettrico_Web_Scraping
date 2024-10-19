from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

# Chrome web driver options
options = Options()
options.headless = True  # Run in headless mode (no browser window)

# Set up chromedriver service
service = Service(executable_path='Z:/web_scraping/chromedriver.exe')

driver = webdriver.Chrome(service=service, options=options)

# Access the website
driver.get('https://www.mercatoelettrico.org/en-us/Home/Results/Electricity/MI/MI-A1/Results/ZonalPrices')
time.sleep(5)

# Click the checkboxes
policy = driver.find_element(By.XPATH, "//span[@id='spanCB1']")
policy.click()

policy2 = driver.find_element(By.XPATH, "//span[@id='spanCB2']")
policy2.click()

# Click the button to show more options
policy3 = driver.find_element(By.XPATH, "//button[@type='button']")
policy3.click()

# Open dropdown for data export
data_select = driver.find_element(By.XPATH, "//button[@class='graph-buttons dropdown-toggle']")
data_select.click()
time.sleep(1)

# Click on "Export all zones XLSX"
data_downloader = driver.find_element(By.XPATH, "//a[contains(text(), 'Export all zones XLSX')]")
data_downloader.click()
time.sleep(3)

# Wait for the download to complete
driver.get('https://www.mercatoelettrico.org/en-us/Home/Results/Electricity/MI/MI-A1/Results/Volumes')
time.sleep(3)

volumes = driver.find_element(By.XPATH, "//button[@class='graph-buttons dropdown-toggle']")
volumes.click()

volume_downloader = driver.find_element(By.XPATH, "//a[contains(text(), 'Export all zones XLSX')]")
volume_downloader.click()
time.sleep(3)

# Close the browser
driver.quit()
