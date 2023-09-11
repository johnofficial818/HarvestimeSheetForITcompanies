from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service_object = Service("C:/Users/Johnbabu/PycharmProjects/harvestTimesheet/driver/chromedriver.exe")
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def click(xpath):
    return driver.find_element(By.XPATH, xpath).click()


def get(url):
    return driver.get(url)


def maximize_window():
    return driver.maximize_window()


def clear(xpath):
    return driver.find_element(By.XPATH, xpath).clear


def send_keys(xpath, keys):
    return driver.find_element(By.XPATH, xpath).send_keys(keys)

#Author : Johnbabu
