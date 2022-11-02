from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import subprocess

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def nextPermutation( arr):
        bPoint, n = -1, len(arr)
        for i in range(n-2,-1,-1):
            if arr[i] >= arr[i+1]: continue                   # Skip the non-increasing sequence
            bPoint = i                                        # Got our breakpoint
            for j in range(n-1,i,-1):                         # again traverse from end
                if arr[j] > arr[bPoint]:                      # Search an element greater the element present at the breakPoint.
                    arr[j], arr[bPoint] = arr[bPoint], arr[j] # Swap it
                    break                                     # We just need to swap once
            break                                             # Break this loop too
        arr[bPoint+1:] = reversed(arr[bPoint+1:])
        return arr

f = open('wordList.txt', 'r')

words = f.readline().replace('\n', '').split(' ')

words = {
    1: words[0],
    2: words[1],
    3: words[2],
    4: words[3],
    5: words[4],
    6: words[5],
    7: words[6],
    8: words[7],
    9: words[8],
    10: words[9],
    11: words[10],
    12: words[11],
}

EXTENSION_PATH = "C:/Users/Acer/AppData/Local/Google/Chrome/User Data/Default/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/10.20.0_0.crx"

opt = webdriver.ChromeOptions()
opt.add_extension(EXTENSION_PATH)
driver = webdriver.Chrome(chrome_options=opt)
time.sleep(1)

#switch tabs
driver.switch_to.window(driver.window_handles[0])


#CLICK THROUGH BUTTONS:
#btn1
time.sleep(2)
elem = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/div/div/button').click()

#btn_recuse
time.sleep(1)
elem = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]').click()

#btn2
time.sleep(1)
elem = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()

arr = [1,2,3,4,5,6,7,8,9,10,11,12]
currentLine = 0
for line in f:
    currentLine += 1
    if currentLine == 1:
        continue
    for i in list(range(1, 13)):
        #CREATE KEYWORD STRING
        count = 0
        s = ''
        for e in words:
            s += " " + words[e]
        s.strip()

        #COPY STRING TO CLIPBOARD:
        copy2clip(s)

        #CLICK ON TEXTFIELD
        time.sleep(2)
        elem = driver.find_element(by = By.XPATH, value= '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[1]/div/input')

        #PASTE CLIPBOARD TO TEXTFIELD
        elem.send_keys(Keys.CONTROL + 'v')
        time.sleep(2)

        looper = True

        while looper:
            try:
                elem = driver.find_element(by = By.XPATH, value= '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[4]/div')
                count += 1
                s = ''
                arr = nextPermutation(arr)

                for e in arr:
                    s += " " + words[e]
                s.strip()

                #COPY STRING TO CLIPBOARD:
                copy2clip(s)
                #click on textfield
                elem = driver.find_element(by = By.XPATH, value= '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[1]/div/input')
                #PASTE CLIPBOARD TO TEXTFIELD
                elem.send_keys(Keys.CONTROL + 'v')

                # print(s)
            except:
                looper = False
                print("DONE!!!" , s)
                with open('save.txt', 'a') as f:
                    f.write(s + '\n')
        words[i] = line.replace('\n', '').split(' ')[i-1]
        print(line.replace('\n', '').split(' ')[i-1])
