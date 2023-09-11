from CommonClass.CommonActions import send_keys, click, clear, get
from CommonActions import *
from CommonClass.CommonActions import *
import time


class LoginClass():
    def __init__(self, jsonObject):
        self.jsonObject = jsonObject
        self.user_name_text_box_xpath               = "//input[@name='email']"
        self.password_text_box_xpath                = "//input[@name='password']"
        self.submit_button_xpath                    = "//button[@type='submit']"
        self.time_button_xpath                      = "//a[text()='Time']"


    def Login(self):
        for i in range(len(self.jsonObject['userNameList'])):
            print(i)
            send_keys(self.user_name_text_box_xpath, self.jsonObject['userNameList'][i])
            send_keys(self.password_text_box_xpath, self.jsonObject['passwordList'][i])
            click(self.submit_button_xpath)
            print(self.jsonObject['userNameList'] + "Logged Successfully")
            time.sleep(2)