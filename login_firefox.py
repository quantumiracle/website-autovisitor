#-*- coding: UTF-8 -*-

import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import time
'''
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
'''
#firefoxdriver = "/usr/bin/geckodriver"
#os.environ["webdriver.firefox.driver"] = firefoxdriver
driver = webdriver.Firefox()

def login(uname, pwd):
    driver.get("https://www.taobao.com")
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click();
    time.sleep(0.1)
    if driver.find_element_by_link_text("密码登录"):
        driver.find_element_by_link_text("密码登录").click();
    time.sleep(0.1)
    if driver.find_element_by_name("TPL_username"):
        driver.find_element_by_name("TPL_username").send_keys(uname);
    time.sleep(0.1)
    if driver.find_element_by_name("TPL_password"):
        driver.find_element_by_name("TPL_password").send_keys(pwd);
    time.sleep(0.2)
    while True:
    #定位滑块元素
            #source=driver.find_element_by_xpath("//*[@id='nc_1_n1z']")
        if driver.find_element_by_xpath("//*[@id='nc_1_n1z']"):
            try:
                source = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")
                #source=driver.find_element_by_xpath("//*[@id='J_NcoToken']")
                #source=driver.find_element_by_id("nocaptcha")
                print("sour:",source)  
        #定义鼠标拖放动作
                ActionChains(driver).drag_and_drop_by_offset(source,400,0).perform()
                #等待JS认证运行,如果不等待容易报错
                time.sleep(1)
                #查看是否认证成功，获取text值
                text=driver.find_element_by_xpath("//div[@id='nc_1__scale_text']/span")
                #目前只碰到3种情况：成功（请在在下方输入验证码,请点击图）；无响应（请按住滑块拖动)；失败（哎呀，失败了，请刷新）
                if text.text.startswith(u'通过'):
                    print('成功滑动')
                    break
                if text.text.startswith(u'请点击'):
                    print('成功滑动')
                    break
                if text.text.startswith(u'请按住'):
                    continue
            
            except Exception as e:
            #这里定位失败后的刷新按钮，重新加载滑块模块
                driver.find_element_by_xpath("//div[@id='havana_nco']/div/span/a").click()
                print(e)  
        else:
                break
    if driver.find_element_by_id("J_SubmitStatic"):
        driver.find_element_by_id("J_SubmitStatic").click();
    time.sleep(1)
    '''
    driver.get("https://cart.taobao.com/cart.htm")
    if driver.find_element_by_id("J_SelectAll1"):
        driver.find_element_by_id("J_SelectAll1").click()
    time.sleep(3)
    
    if driver.find_element_by_link_text("结 算"):
        driver.find_element_by_link_text("结 算").click();
    now = datetime.datetime.now()
    '''
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))

def buy_on_time(buytime):
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            while True:
                try:
                    driver.find_element_by_link_text('提交订单').click()
                except:
                    time.sleep(1)
        time.sleep(0.1)
#中文账号的时候要给它编码一下，不然会出错
#login("中文账号".decode('utf-8'),'密码')
login("miracleddjj",'dzh042896')
#buy_on_time('2017-05-06 21:30:01')