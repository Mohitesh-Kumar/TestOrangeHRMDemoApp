import csv
class Utils:
    #EnvVars is a class type of dictionary variable,storing env vars
    #in Key-value pair
    EnvVars={}
    #classmethod is a static method which can be called without creating object of class
    #To define classmethod we have to annotate method with @classmethod
    @classmethod
    def InitialiseEnvVars(cls):
        #Opening a csv file in Readmode using open function
        with open('D:\\SDET_Training\\TestOrangeHRMDemoApp\\EnvVars.csv') as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            #Using this for loop we are reading the contents of EnvVars file row by row
            for row in csv_reader:
                #for the 1st iteraation of loop:row=ChromeDriverPath,D:\\XoriantPythonSeleniumPostmanTraining\\Drivers\\chromedriver.exe
                #row(ChromeDriverPath,D:\\XoriantPythonSeleniumPostmanTraining\\Drivers\\chromedriver.exe)
                Utils.EnvVars[row[0]]=row[1]

    @classmethod
    def ReadLoginTestData(cls):
        LoginDataList=[]
        i=0
        # Opening a csv file in Readmode using open function
        #with open(Utils.EnvVars["DataFilesPath"]+'\\LoginTestData.csv') as csv_file:
        with open('D:\\SDET_Training\\TestOrangeHRMDemoApp\\DataFiles\\LoginTestData.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # Using this for loop we are reading the contents of EnvVars file row by row
            #csv_reader.next()
            for row in csv_reader:
                # for the 1st iteraation of loop:row=ChromeDriverPath,D:\\XoriantPythonSeleniumPostmanTraining\\Drivers\\chromedriver.exe
                # row(ChromeDriverPath,D:\\XoriantPythonSeleniumPostmanTraining\\Drivers\\chromedriver.exe)
                #{"UserName":"Admin","Password":"","Error":"Password cannot be empty"}
                LoginData = {}
                LoginData["UserName"]=row[0]
                LoginData["Password"]=row[1]
                LoginData["Error"]=row[2]
                LoginDataList.append(LoginData)
                i=i+1

        return LoginDataList