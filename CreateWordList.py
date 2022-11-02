from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import subprocess

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def find(xpath):
    return driver.find_element(by = By.XPATH, value = xpath)
EXTENSION_PATH = "C:/Users/Acer/AppData/Local/Google/Chrome/User Data/Default/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/10.20.0_0.crx"
while True:
    try:
        opt = webdriver.ChromeOptions()
        opt.add_extension(EXTENSION_PATH)
        driver = webdriver.Chrome(chrome_options=opt)
        time.sleep(1)

        #switch tabs
        driver.switch_to.window(driver.window_handles[0])

        #CLICK THROUGH BUTTONS:
        #btn1
        time.sleep(2)
        find('/html/body/div[1]/div/div[2]/div/div/div/button').click()

        #btn_recuse
        time.sleep(1)
        find('/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]').click()

        #btn2
        time.sleep(1)
        find('/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/button').click()

        #CLICK ON TEXTFIELD
        copy2clip('123456789')

        time.sleep(0.5)
        elem = find('/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div/input')
        elem.send_keys(Keys.CONTROL + 'v')

        elem = find('/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[2]/div/input')
        elem.send_keys(Keys.CONTROL + 'v')

        find('/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[3]/div').click();

        find('/html/body/div[1]/div/div[2]/div/div/div[2]/form/button').click()

        time.sleep(3.5)
        find('/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/button').click()

        time.sleep(1)
        find('/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[5]/div[2]').click()

        time.sleep(1)
        text = find('/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[5]/div').text
        driver.close()
        with open('wordList.txt', 'a') as f:
            f.write(text)
            f.write('\n')
    except:
        driver.close()