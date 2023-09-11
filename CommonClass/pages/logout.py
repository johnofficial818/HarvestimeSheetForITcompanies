from CommonClass.CommonActions import send_keys, click, clear, get
from CommonClass.CommonActions import *


class LogoutClass():
    def __init__(self, jsonObject):
        self.jsonObject = jsonObject
        self.logoutProfile_xpath      = "//button[@id='user-dropdown-toggle']"
        self.logoutButton_xpath       = "(//a[text()='Sign out'])[1]"
        

    def logout(self):
        click(self.logoutProfile_xpath)
        click(self.logoutButton_xpath)

