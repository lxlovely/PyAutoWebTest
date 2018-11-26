# !usr/bin/env python
# -*- coding:utf-8 _*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time

browser = webdriver.Firefox()
browser.get("http://www.inziqi.com/")

def change_windows():
    # 切换到新开页面窗口
    time.sleep(3)  # 休眠3秒
    browser.switch_to_window(browser.window_handles[1])
    # 关闭新开窗口
    browser.close()
    # 因为刚才执行了窗口切换，故需要切换回最初的窗口时继续执行操作
    browser.switch_to_window(browser.window_handles[0])



#滑动查看案例展示
browser.implicitly_wait(10)
Caseshow = browser.find_element_by_xpath('//*[@id="topage"]').click()
time.sleep(3)

#查看最新资讯全文
browser.implicitly_wait(10)
lateset_news = browser.find_element_by_class_name('seeAll').click()
time.sleep(3)
browser.back()

#进入更多资讯
browser.implicitly_wait(10)
more_news = browser.find_element_by_class_name('fz18').click()
time.sleep(3)
browser.back()

#业务咨询


# elements element 的区别，获取多个元素和单个元素
# xpathelements = browser.find_elements_by_xpath('//*[@id="app"]/div/div[7]/div/div[2]/form/input')
# xpathelements[0] =
# xpathelements[1]
#


dict={'company_name':'','person_name':'','tel':'','wexin_num':'','title':'','content':''}

#1，输入公司名字company_name
dict['company_name']= browser.find_element_by_xpath('//*[@id="app"]/div/div[7]/div/div[2]/form/input[1]').send_keys('成都子奇有限公司')
#2.输入姓名person_name
dict['person_name'] = browser.find_element_by_xpath('//*[@id="app"]/div/div[7]/div/div[2]/form/input[2]').send_keys('test')
#3.输入联系电话tel
dict['tel'] = browser.find_element_by_xpath('//*[@id="app"]/div/div[7]/div/div[2]/form/input[3]').send_keys('1008611')
#4输入微信号wexin_num
dict['wexin_num']= browser.find_element_by_xpath('//*[@id="app"]/div/div[7]/div/div[2]/form/input[4]').send_keys('1008611')
#5.输入标题title
dict['title']= browser.find_element_by_xpath('//*[@id="app"]/div/div[7]/div/div[2]/form/input[5]').send_keys('title')
#6.输入咨询内容content
dict['content'] = browser.find_element_by_xpath('//*[@id="app"]/div/div[7]/div/div[2]/form/textarea').send_keys('hhhhhhhhhh')
time.sleep(3)

if (dict !=None):

    send = browser.find_element_by_class_name('pointer').click()
    print("咨询发送成功")
    time.sleep(3)
else:
    print("请保证所有必填项已经填写")

#查看合作伙伴

# 点击 合作伙伴 亚马逊
aws = browser.find_element_by_xpath('//*[@id="app"]/div/div[8]/div/div[2]/dl/dd/span[1]/a').click()
browser.back()

# 切换到新开页面窗口
browser.switch_to_window(browser.window_handles[1])
# 关闭新开窗口
browser.close()
# 因为刚才执行了窗口切换，故需要切换回最初的窗口时继续执行操作
browser.switch_to_window(browser.window_handles[0])


# 点击 合作伙伴
suoduoduo = browser.find_element_by_xpath('//*[@id="app"]/div/div[8]/div/div[2]/dl/dd/span[2]/a').click()
time.sleep(3)
change_windows()

btc =browser.find_element_by_xpath('//*[@id="app"]/div/div[8]/div/div[2]/dl/dd/span[3]/a').click()
time.sleep(3)
change_windows()

jinse = browser.find_element_by_xpath('//*[@id="app"]/div/div[8]/div/div[2]/dl/dd/span[3]/a').click()
time.sleep(3)
change_windows()

huobi =browser.find_element_by_xpath('//*[@id="app"]/div/div[8]/div/div[2]/dl/dd/span[5]/a').click()
change_windows()
browser.implicitly_wait(10)
huobi_url = browser.find_element_by_xpath('//*[@id="app"]/div/div[8]/div/div[2]/dl/dd/span[5]/a').get_attribute("href")
print("货币的网页：",huobi_url )
time.sleep(3)

aliyun =browser.find_element_by_xpath('//*[@id="app"]/div/div[8]/div/div[2]/dl/dd/span[6]/a').click()
time.sleep(3)
change_windows()

okex = browser.find_element_by_xpath('//*[@id="app"]/div/div[8]/div/div[2]/dl/dd/span[7]/a').click()
time.sleep(3)
change_windows()

kyber = browser.find_element_by_xpath('//*[@id="app"]/div/div[8]/div/div[2]/dl/dd/span[8]').click()
time.sleep(3)
change_windows()
browser.implicitly_wait(10)
kyber_url = browser.find_element_by_xpath('//*[@id="app"]/div/div[8]/div/div[2]/dl/dd/span[8]').get_attribute("href")
print("kyber的网页：",kyber_url)


browser.close()











