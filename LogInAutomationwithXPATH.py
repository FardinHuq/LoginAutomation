import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service=Service(r"C:\Drives\edgedriver_win64\msedgedriver.exe")
driver=webdriver.Edge(service=service)

driver.get("https://www.instagram.com")
driver.maximize_window()

#Absolute xpath
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[1]/div/label/input").send_keys("email@gmail.com")

#Relative xpath
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("password")

#or xpath
driver.find_element(By.XPATH, "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1' or @id='null' ]").click()
time.sleep(20)

driver.quit()
