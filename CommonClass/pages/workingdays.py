from CommonClass.CommonActions import send_keys, click, clear, get
from CommonClass.CommonActions import *


class WorkingdayClass():
    def __init__(self, jsonObject):
        self.jsonObject = jsonObject
        self.clickWorkingMonday_xpath               = "//tbody/tr[2]/td[2]/input[1]"
        self.sendWorkingMonday_xpath                = "//tbody/tr[2]/td[2]/input[1]"
        self.clickWorkingWorkingTuesday_xpath       = "//tbody/tr[2]/td[3]/input[1]"
        self.sendWorkingTuesday_xpath               = "//tbody/tr[2]/td[3]/input[1]"
        self.clickWorkingWednesday_xpath            = "//tbody/tr[2]/td[4]/input[1]"
        self.sendWorkingWednesday_xpath             = "//tbody/tr[2]/td[4]/input[1]"
        self.clickWorkingThursday_xpath             = "//tbody/tr[2]/td[5]/input[1]"
        self.sendWorkingThursday_xpath              = "//tbody/tr[2]/td[5]/input[1]"
        self.clickWorkingFriday_xpath               = "//tbody/tr[2]/td[6]/input[1]"
        self.sendWorkingFriday_xpath                = "//tbody/tr[2]/td[6]/input[1]"
        
    def workingday(self):       
        click(self.clickWorkingMonday_xpath )       
        send_keys(self.sendWorkingMonday_xpath, self.jsonObject["holiday_monday"])
        click(self.clickWorkingTuesday_xpath )       
        send_keys(self.sendWorkingTuesday_xpath, self.jsonObject["holiday_tuesday"])
        click(self.clickWorkingWednesday_xpath )       
        send_keys(self.sendWorkingWednesday_xpath, self.jsonObject["holiday_wednesday"])
        click(self.clickWorkingThursday_xpath )       
        send_keys(self.sendWorkingThursday_xpath, self.jsonObject["holiday_thursday"])
        click(self.clickWorkingFriday_xpath )       
        send_keys(self.sendWorkingFriday_xpath, self.jsonObject["holiday_friday"])

        
      