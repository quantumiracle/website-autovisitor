# encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
#使用谷歌浏览器，方便查看效果，如果追求速度可以用phantomJS
driver=webdriver.Chrome()
#调整最大窗口，否则某些元素无法显示
driver.maximize_window()
#使用淘宝找回密码界面做测试
driver.get('https://passport.taobao.com/ac/password_find.htm?spm=a2107.1.0.0.phBxhD&from_site=0')
time.sleep(5)#等待滑动模块和其他JS文件加载完毕！
while True:
    try:
   #定位滑块元素
        source=driver.find_element_by_xpath("//*[@id='nc_1_n1z']")  
   #定义鼠标拖放动作
        ActionChains(driver).drag_and_drop_by_offset(source,400,0).perform()
        #等待JS认证运行,如果不等待容易报错
        time.sleep(2)
        #查看是否认证成功，获取text值
        text=driver.find_element_by_xpath("//div[@id='nc_1__scale_text']/span")
        #目前只碰到3种情况：成功（请在在下方输入验证码,请点击图）；无响应（请按住滑块拖动)；失败（哎呀，失败了，请刷新）
        if text.text.startswith(u'请在下方'):
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
#退出浏览器，如果浏览器打开多个窗口，可以使用driver.close()关闭当前窗口而不是关闭浏览器
driver.quit()