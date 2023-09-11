from CommonClass.CommonActions import send_keys, click, clear, get
from CommonClass.CommonActions import *


class HolidayClass():
    def __init__(self, jsonObject):
        self.jsonObject = jsonObject
        self.clickHolidayMonday_xpath        = "//tbody/tr[1]/td[2]/input[1]"
        self.sendHolidayMonday_xpath         = "//tbody/tr[1]/td[2]/input[1]"
        self.clickHolidayTuesday_xpath       = "//tbody/tr[1]/td[3]/input[1]"
        self.sendHolidayTuesday_xpath        = "//tbody/tr[1]/td[3]/input[1]"
        self.clickHolidayWednesday_xpath     = "//tbody/tr[1]/td[4]/input[1]"
        self.sendHolidayWednesday_xpath      = "//tbody/tr[1]/td[4]/input[1]"
        self.clickHolidayThursday_xpath      = "//tbody/tr[1]/td[5]/input[1]"
        self.sendHolidayThursday_xpath       = "//tbody/tr[1]/td[5]/input[1]"
        self.clickHolidayFriday_xpath        = "//tbody/tr[1]/td[6]/input[1]"
        self.sendHolidayFriday_xpath         = "//tbody/tr[1]/td[6]/input[1]"
        
    def holiday(self):       
        click(self.clickHolidayMonday_xpath )       
        send_keys(self.sendHolidayMonday_xpath, self.jsonObject["holiday_monday"])
        click(self.clickHolidayTuesday_xpath )       
        send_keys(self.sendHolidayTuesday_xpath, self.jsonObject["holiday_tuesday"])
        click(self.clickHolidayWednesday_xpath )       
        send_keys(self.sendHolidayWednesday_xpath, self.jsonObject["holiday_wednesday"])
        click(self.clickHolidayThursday_xpath )       
        send_keys(self.sendHolidayThursday_xpath, self.jsonObject["holiday_thursday"])
        click(self.clickHolidayFriday_xpath )       
        send_keys(self.sendHolidayFriday_xpath, self.jsonObject["holiday_friday"])

        
        
    # def holiday(self):
    #     send_keys(self.clickMonday_xpath, self.jsonObject["username"])
    #     
    #     click(send.Monday_xpath)
    #     send_keys(self.sendMonday_xpath, self.jsonObject["password"])
    #     click(sendMonday_xpath)
    #     send_keys(self.sendTuesday_xpath, self.jsonObject["password"])
    #     click(send.Tuesday_xpath)
    #     send_keys(selfsendMonday_xpath, self.jsonObject["password"])
    #     click(sendMonday_xpath)
    #     send_keys(selfsendMonday_xpath, self.jsonObject["password"])
    #     click(sendMonday_xpath)
    #     send_keys(selfsendMonday_xpath, self.jsonObject["password"])
        

