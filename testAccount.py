from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import subprocess

f = open('save.txt', 'r')

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

EXTENSION_PATH = "C:/Users/Acer/AppData/Local/Google/Chrome/User Data/Default/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/10.20.0_0.crx"

opt = webdriver.ChromeOptions()
opt.add_extension(EXTENSION_PATH)

for line in f:
    try:
        driver = webdriver.Chrome(chrome_options=opt)
        time.sleep(0.5)

        #switch tabs
        driver.switch_to.window(driver.window_handles[0])

        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase')
        time.sleep(0.5)
        
        copy2clip(line)
        elem = driver.find_element(by = By.XPATH, value= '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[1]/div/input')
        elem.send_keys(Keys.CONTROL + 'v')

        time.sleep(0.5)

        elem = driver.find_element(by = By.XPATH, value= '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[2]/div[1]/div/input')
        elem.send_keys('123456789')

        elem = driver.find_element(by = By.XPATH, value= '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[2]/div[2]/div/input')
        elem.send_keys('123456789')

        driver.find_element(by = By.XPATH, value= '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[3]/input').click()

        driver.find_element(by = By.XPATH, value= '/html/body/div[1]/div/div[2]/div/div/div[2]/form/button').click()
        time.sleep(6)
        driver.find_element(by = By.XPATH, value= '/html/body/div[1]/div/div[2]/div/div/button').click()
        val = driver.find_element(by = By.XPATH, value= '/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div/span[2]').text
        print(val)
        if(int(val) > 0):
            print(line)
            with open('withBalance.txt', 'a') as f:
                f.write(line)
                f.write('\n')
    except Exception as e:
        print("\n")
    driver.close()