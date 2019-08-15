#!/usr/bin/python3

from selenium import webdriver

from time import sleep
from random import randint

webdriver.DesiredCapabilities.CHROME["unexpectedAlertBehaviour"] = "accept"
driver = webdriver.Chrome()

driver.get("http://minesweeperonline.com/#beginner")

sleep(3)

buttonByID = driver.find_element_by_id('4_4')
buttonsByClass = driver.find_elements_by_xpath("//*[contains(@class, 'blank')]")
gamecount = 0
gamewon = False
while not gamewon:
    gamecount+=1
    start = driver.find_element_by_id('face')
    start.click()
    for i in range(80):
        buttonsByClass = driver.find_elements_by_xpath("//*[contains(@class, 'blank') and not(contains(@style,'display: none;'))]")
        squaresLeft = len(buttonsByClass)
        #print(squaresLeft)
        if squaresLeft > 10:
            buttonsByClass[randint(0,squaresLeft-1)].click()
        else:
            gamewon = True
            break
        if len(driver.find_elements_by_xpath("//*[contains(@class, 'bombdeath')]")) > 0:
                                             break
                                            
    print("{0} \t {1}".format(gamecount,squaresLeft-10))
print("You Won! After {} games".format(gamecount))        
#buttonByID.click()

sleep(10)