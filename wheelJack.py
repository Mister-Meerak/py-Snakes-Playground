import time
import smtplib
from selenium import webdriver
#Still work in progress
#TODO: code currently forces me to answer pages to prove im not a bot.. gotta figure that out
#TODO: code needs to alert out if we are redirect to the queue/ send out a tweet or email or text


#Variables
outOfStock = '/html/body/div[1]/div/div[3]/producthero-component/div/div/div[3]/producthero-info/div/div[4]/div[2]'
#PS5 Disc
site = 'https://direct.playstation.com/en-us/consoles/console/playstation5-console.3005816'

def getInQueue():
    try:        
        driverIncognito.get(site)
        driverIncognito.find_element_by_xpath(outOfStock)
        print("not there. try again")
        #print(driver.find_element_by_xpath(outOfStock))
        time.sleep(5)
        #driver.refresh()
        driverIncognito.close
        getInQueue()
    except Exception as ex:
        print("failed")
        print(ex)
    

print("hello")
if __name__ == "__main__":
    driverOptions = webdriver.ChromeOptions()
    driverOptions.add_argument("--incognito")
    driverIncognito = webdriver.Chrome("c:/_DaCode/lib/chromedriver.exe", chrome_options=driverOptions)
    
    getInQueue()
