from CommonClass.CommonActions import send_keys, click, clear, get
from CommonClass.CommonActions import *
from CommonClass.pages.login import LoginClass
from CommonClass.pages import *
import time


class E2EClass():
    def __init__(self, jsonObject):
        self.jsonObject = jsonObject
        self.user_name_text_box_xpath               = "//input[@name='email']"
        self.password_text_box_xpath                = "//input[@name='password']"
        self.submit_button_xpath                    = "//button[@type='submit']"
        self.time_button_xpath                      = "//a[text()='Time']"
        self.clickHolidayMonday_xpath               = "//tbody/tr[1]/td[2]/input[1]"
        self.sendHolidayMonday_xpath                = "//tbody/tr[1]/td[2]/input[1]"
        self.clickHolidayTuesday_xpath              = "//tbody/tr[1]/td[3]/input[1]"
        self.sendHolidayTuesday_xpath               = "//tbody/tr[1]/td[3]/input[1]"
        self.clickHolidayWednesday_xpath            = "//tbody/tr[1]/td[4]/input[1]"
        self.sendHolidayWednesday_xpath             = "//tbody/tr[1]/td[4]/input[1]"
        self.clickHolidayThursday_xpath             = "//tbody/tr[1]/td[5]/input[1]"
        self.sendHolidayThursday_xpath              = "//tbody/tr[1]/td[5]/input[1]"
        self.clickHolidayFriday_xpath               = "//tbody/tr[1]/td[6]/input[1]"
        self.sendHolidayFriday_xpath                = "//tbody/tr[1]/td[6]/input[1]"
        self.clickWorkingMonday_xpath               = "//tbody/tr[2]/td[2]/input[1]"
        self.sendWorkingMonday_xpath                = "//tbody/tr[2]/td[2]/input[1]"
        self.clickWorkingTuesday_xpath              = "//tbody/tr[2]/td[3]/input[1]"
        self.sendWorkingTuesday_xpath               = "//tbody/tr[2]/td[3]/input[1]"
        self.clickWorkingWednesday_xpath            = "//tbody/tr[2]/td[4]/input[1]"
        self.sendWorkingWednesday_xpath             = "//tbody/tr[2]/td[4]/input[1]"
        self.clickWorkingThursday_xpath             = "//tbody/tr[2]/td[5]/input[1]"
        self.sendWorkingThursday_xpath              = "//tbody/tr[2]/td[5]/input[1]"
        self.clickWorkingFriday_xpath               = "//tbody/tr[2]/td[6]/input[1]"
        self.sendWorkingFriday_xpath                = "//tbody/tr[2]/td[6]/input[1]"
        self.logoutProfile_xpath                    = "//button[@id='user-dropdown-toggle']"
        self.logoutButton_xpath                     = "(//a[text()='Sign out'])[1]"
        
        
        
        # self.specificLeave                          = "//tbody/tr[1]/td[6]/input[1]"


    def test_e2e(self):
        for i in range(len(self.jsonObject['userNameList'])):
            print(i)
            if self.jsonObject['userNameList'] == self.jsonObject['specificLeaveList']:    
                send_keys(self.user_name_text_box_xpath, self.jsonObject['userNameList'][i])
                send_keys(self.password_text_box_xpath, self.jsonObject['passwordList'][i])
                click(self.submit_button_xpath)
                # print(self.jsonObject['userNameList'])
                time.sleep(2)
                click(self.time_button_xpath)
                time.sleep(5)
                for j in range(len(self.jsonObject['specificLeaveList'])):  
                    # print(self.jsonObject['specificLeaveList'][j])     
                    k = self.jsonObject['specificLeaveList'][j]
                    # print(k)
                    print(self.jsonObject['userNameListwithData'][j][k]['holiday_monday'])
                    click(self.clickHolidayMonday_xpath )       
                    send_keys(self.sendHolidayMonday_xpath, self.jsonObject['userNameListwithData'][j][k]['holiday_monday'])
                    time.sleep(2)
                    click(self.clickHolidayTuesday_xpath )       
                    send_keys(self.sendHolidayTuesday_xpath, self.jsonObject['userNameListwithData'][j][k]['holiday_tuesday'])
                    time.sleep(2)
                    click(self.clickHolidayWednesday_xpath )       
                    send_keys(self.sendHolidayWednesday_xpath, self.jsonObject['userNameListwithData'][j][k]['holiday_wednesday'])
                    time.sleep(2)
                    click(self.clickHolidayThursday_xpath )       
                    send_keys(self.sendHolidayThursday_xpath, self.jsonObject['userNameListwithData'][j][k]['holiday_thursday'])
                    time.sleep(2)
                    click(self.clickHolidayFriday_xpath )       
                    send_keys(self.sendHolidayFriday_xpath, self.jsonObject['userNameListwithData'][j][k]['holiday_friday'])
                    
                    print("Holidays Successfully Updated")
                    
                    time.sleep(5)
                    click(self.clickWorkingMonday_xpath )      
                    clear(self.clickWorkingMonday_xpath ) 
                    send_keys(self.sendWorkingMonday_xpath, self.jsonObject['userNameListwithData'][j][k]['working_monday'])
                    time.sleep(2)
                    click(self.clickWorkingTuesday_xpath )  
                    clear(self.clickWorkingTuesday_xpath )    
                    send_keys(self.sendWorkingTuesday_xpath, self.jsonObject['userNameListwithData'][j][k]['working_tuesday'])
                    time.sleep(2)
                    click(self.clickWorkingWednesday_xpath )    
                    clear(self.clickWorkingWednesday_xpath )
                    send_keys(self.sendWorkingWednesday_xpath, self.jsonObject['userNameListwithData'][j][k]['working_wednesday'])
                    time.sleep(2)
                    click(self.clickWorkingThursday_xpath )  
                    click(self.clickWorkingThursday_xpath )     
                    send_keys(self.sendWorkingThursday_xpath, self.jsonObject['userNameListwithData'][j][k]['working_thursday'])
                    time.sleep(2)
                    click(self.clickWorkingFriday_xpath )  
                    clear(self.clickWorkingFriday_xpath )
                    send_keys(self.sendWorkingFriday_xpath, self.jsonObject['userNameListwithData'][j][k]['working_friday'])
                    time.sleep(5)
                    
                    print("Workingday Successfully Updated")
                    
                    click(self.logoutProfile_xpath)
                    time.sleep(2)
                    click(self.logoutButton_xpath)
                    time.sleep(3)
                    
                    print(self.jsonObject['userNameList'])
                    
                    time.sleep(1)
                    driver.refresh()
                    time.sleep(5)  
                 
            else:
                send_keys(self.user_name_text_box_xpath, self.jsonObject['userNameList'][i])
                send_keys(self.password_text_box_xpath, self.jsonObject['passwordList'][i])
                click(self.submit_button_xpath)
                
                print(self.jsonObject['userNameList'])
                
                time.sleep(2)
                click(self.time_button_xpath)
                time.sleep(5)
                click(self.clickHolidayMonday_xpath )       
                send_keys(self.sendHolidayMonday_xpath, self.jsonObject["holiday_monday"])
                time.sleep(2)
                click(self.clickHolidayTuesday_xpath )       
                send_keys(self.sendHolidayTuesday_xpath, self.jsonObject["holiday_tuesday"])
                time.sleep(2)
                click(self.clickHolidayWednesday_xpath )       
                send_keys(self.sendHolidayWednesday_xpath, self.jsonObject["holiday_wednesday"])
                time.sleep(2)
                click(self.clickHolidayThursday_xpath )       
                send_keys(self.sendHolidayThursday_xpath, self.jsonObject["holiday_thursday"])
                time.sleep(2)
                click(self.clickHolidayFriday_xpath )       
                send_keys(self.sendHolidayFriday_xpath, self.jsonObject["holiday_friday"])
                
                print("Holidays Successfully Updated")
                
                time.sleep(5)
                click(self.clickWorkingMonday_xpath )  
                clear((self.clickWorkingMonday_xpath ))
                send_keys(self.sendWorkingMonday_xpath, self.jsonObject["working_monday"])
                time.sleep(2)
                click(self.clickWorkingTuesday_xpath )    
                clear(self.clickWorkingTuesday_xpath )
                send_keys(self.sendWorkingTuesday_xpath, self.jsonObject["working_tuesday"])
                time.sleep(2)
                click(self.clickWorkingWednesday_xpath ) 
                clear(self.clickWorkingWednesday_xpath )
                send_keys(self.sendWorkingWednesday_xpath, self.jsonObject["working_wednesday"])
                time.sleep(2)
                click(self.clickWorkingThursday_xpath )      
                clear(self.clickWorkingThursday_xpath ) 
                send_keys(self.sendWorkingThursday_xpath, self.jsonObject["working_thursday"])
                time.sleep(2)
                click(self.clickWorkingFriday_xpath )    
                clear(self.clickWorkingFriday_xpath )   
                send_keys(self.sendWorkingFriday_xpath, self.jsonObject["working_friday"])
                time.sleep(5)
                
                print("Holidays Successfully Updated")
                
                click(self.logoutProfile_xpath)
                time.sleep(2)
                click(self.logoutButton_xpath)
                time.sleep(3)
                
                print(self.jsonObject['userNameList'])
                
                time.sleep(1)
                driver.refresh()
                time.sleep(5)