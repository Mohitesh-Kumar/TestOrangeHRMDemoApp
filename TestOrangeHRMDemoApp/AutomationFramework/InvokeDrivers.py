from selenium import webdriver

from AutomationFramework.Utilities.Utils import Utils



def StartChromeDriver():
    # WebTest.Driver=webdriver.Chrome(executable_path="D:/Drivers/ChromeDriver/chromedriver.exe")
    from AutomationFramework.WebTest import WebTest
    WebTest.Driver = webdriver.Chrome(
        executable_path=Utils.EnvVars.get("ChromeDriverPath"))

def StartFirefoxDriver():
    pass