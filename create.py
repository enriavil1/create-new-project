import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


path= "/Users/enriavil1/Desktop/project/Python/"
try:
    browser= webdriver.Safari()

except Exception:
    browser= webdriver.Chrome()

browser.get("https://github.com/login")
enter_key= u'\ue007'

def create():

    name = str(sys.argv[1])
    username= str(os.environ["username"])
    password= str(os.environ["password"])

    os.mkdir(path + name)

    #putting your username in
    button= browser.find_elements_by_xpath("//*[@id='login_field']")[0]

    try:
        button.send_keys(username)
    
    except Exception:
        print("no username inputed")

    #putting your password in
    button= browser.find_elements_by_xpath("//*[@id='password']")[0]

    try:
        button.send_keys(password)
    
    except Exception:
        print("no password inputed")
    
    #login in
    button= browser.find_elements_by_xpath("//input[@name= 'commit']")[0]
    button.send_keys(enter_key)

    time.sleep(3)
    browser.get("https://github.com/new")


    #putting new repo name
    button= WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='repository_name']")))
    button.send_keys(name)

    #pressing creating repo"//*[@id='new_repository']/div[3]/button"
    time.sleep(2)
    button= browser.find_element_by_xpath("//*[@id='new_repository']/div[3]/button")
    button.send_keys(enter_key)
    browser.close()

    







if __name__ == "__main__":
    create()


