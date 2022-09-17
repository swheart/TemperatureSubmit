# -*- coding:utf-8 -*-
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import os
import random




chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver)


url = r'http://got.goermicro.com:8089/got/temperature/attend.html'
driver.get(url)

print("访问页面成功")

username = driver.find_element(by='id', value='employeeNumber')
StudentID = '9002370'
username.send_keys(StudentID)

print("填入员工号成功")

secretKey = driver.find_element(by='id', value='numId')
KeyNum = '041815'
secretKey.send_keys(KeyNum)

print("填入身份证成功")

logbtn = driver.find_element(by='id', value='sub')
logbtn.click()

print("提交员工信息成功")
time.sleep(2)

logbtn = driver.find_element(by='id', value='agreement')
logbtn.click()

print("同意协议")


time.sleep(2)


driver.get('http://got.goermicro.com:8089/got/temperature/to_temperature.html')

print("进入体温填报页面成功")

time.sleep(2)

secretKey = driver.find_element(by='id', value='afternoon')
<<<<<<< HEAD
def rands():
    b = '{:.1f}'.format(random.uniform(36.2, 36.7))
    return b
secretKey.send_keys(rands())
=======
KeyNum = '36.6'
secretKey.send_keys(KeyNum)
>>>>>>> 0f2b6d856a034fc6b1f82f3e1b1979c58d68d905

print("填入下午体温成功")

logbtn = driver.find_element(by='id', value='sub')
logbtn.click()

print("提交下午体温成功")
print(driver.title)



