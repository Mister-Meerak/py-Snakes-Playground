import time
import winsound
from selenium import webdriver
#Still work in progress

#Variables
outOfStock = '/html/body/div[1]/div/div[3]/producthero-component/div/div/div[3]/producthero-info/div/div[4]/div[2]'
addButton ='/html/body/div[1]/div/div[3]/producthero-component/div/div/div[3]/producthero-info/div/div[4]/button'
sleepInSeconds = 10
#enter the site
siteDigital = 'https://direct.playstation.com/en-us/consoles/console/playstation5-console.3005816'

def alertSound():
    duration=1000
    freq = 1500
    winsound.Beep(freq,duration)

def getInQueue():
    try:        
        driverIncognito.get(siteDigital)
        outOfStockElement = driverIncognito.find_element_by_xpath(outOfStock)
        if outOfStockElement.is_displayed():
            time.sleep(sleepInSeconds)
            driverIncognito.close
            print('Still Out of Stock')
            getInQueue()
        
        addButtonElement = driverIncognito.find_element_by_xpath(addButton)
        if addButtonElement.is_displayed():
            driverIncognito.close
            driver = webdriver.Chrome("c:/_DaCode/lib/chromedriver.exe", chrome_options=driverOptions)
            driver.get(siteDigital)
            addButtonElement = driver.find_element_by_xpath(addButton)
            addButtonElement.click()
            alertSound()
            print('Added to Cart')
            return

        print('nothing found.. we might be in the queue')
        #close incognito browser, relaunch in normal browser
        alertSound()
        driverIncognito.close
        driver = webdriver.Chrome("c:/_DaCode/lib/chromedriver.exe", chrome_options=driverOptions)
        driver.get(siteDigital)    

    except Exception as ex:        
        alertSound()
        print('something broke', ex)        
        driverIncognito.close
        driver = webdriver.Chrome("c:/_DaCode/lib/chromedriver.exe", chrome_options=driverOptions)
        driver.get(siteDigital) 
    
if __name__ == "__main__":
    driverOptions = webdriver.ChromeOptions()
    driverOptions.add_argument("--incognito")
    driverIncognito = webdriver.Chrome("c:/_DaCode/lib/chromedriver.exe", chrome_options=driverOptions)
    getInQueue()
    
