# import pytest
# import os, re
# import json
# import logging,logging.config
# # import allure
# # import mysql.connector
# # import uuid
# # from CommonClass.api_utils.FrameworkConstants import Constants
# from selenium.webdriver.chrome.service import Service
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from CommonClass.CommonActions import *


# @pytest.fixture(scope='class')
# def test_setup(request):
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     request.cls.driver=driver
#     yield
#     driver.close()
#     driver.quit()
#     print("Test")