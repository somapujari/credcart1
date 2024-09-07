from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def setup():
    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.binary_location = r'C:\Users\Dell\AppData\Local\Google\Chrome\Application\chrome.exe'
    path = r'C:\Users\Dell\AppData\Local\Programs\Python\Python310\chromedriver.exe'
    service = Service(path)
    service.start()
    driver = webdriver.Chrome(service=service, options=chromeoptions)
    return driver
