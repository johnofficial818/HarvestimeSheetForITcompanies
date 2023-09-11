import json
from CommonClass.CommonActions import get
from CommonClass.CommonActions import *
from CommonClass.pages import *
from CommonClass.pages.e2e import E2EClass



with open("testdata/test_data.json") as jsonFile:    #Loading testdata
    jsonObject = json.load(jsonFile)
    jsonFile.close()

driver.implicitly_wait(10)   #implicit wait
get(jsonObject['url'])
driver.maximize_window()
# @pytest.mark.usefixtures("test_setup")
class test_harvest():
    def test_timesheetLogin():    
        E2EObj = E2EClass(jsonObject)
        E2EObj.e2e()           
    
