from selenium import webdriver

from AutomationFramework.InvokeDrivers import StartChromeDriver, StartFirefoxDriver

#from AutomationFramework.WebTest import WebTest
#from AutomationFramework.Utilities.Utils import Utils

# def StartChromeDriver():
#     # WebTest.Driver=webdriver.Chrome(executable_path="D:/Drivers/ChromeDriver/chromedriver.exe")
#     WebTest.Driver = webdriver.Chrome(
#         executable_path=Utils.EnvVars.get("ChromeDriverPath"))
''''
    switch(BroowserName)
    {
        case "Chrome":
            System.setproperty("webdriver.chrome.driver",<PATH>)
            D=new ChromeDriver();    
        case "Firefox":
    
    }

    This BrowserDriverSwitcher is a Dictionary implemented to support swith
    statement.
    It has keys representing Cases in switch and functionames performing 
    required operations for a case,as values. 

'''

BrowserDriverSwitcher = {
    "Chrome": StartChromeDriver,
    "Firefox":StartFirefoxDriver

}
