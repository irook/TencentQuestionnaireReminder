#解析问卷模块

from selenium import webdriver
import time

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
#你的问卷地址
main_url = "https://wj.qq.com/stat_recycle.html?id="
driver = webdriver.Safari()
driver.set_page_load_timeout(5)

def login():
    #获取界面
    driver.get(main_url)
    time.sleep(2)

    #进入登入界面
    qqLoginImg = driver.find_element_by_id("loginTabQQ")
    qqLoginImg.click()
    time.sleep(2)

    #寻找所在QQ
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="QQLoginIframe"]'))
    accountImg = driver.find_element_by_class_name("img_out")
    accountImg.click()
    time.sleep(4)

    #保存Cookie到会话中
    cookies = driver.get_cookies()
    for eachcookie in cookies:
        driver.add_cookie(eachcookie)

    driver.refresh()

    #进入收集界面
    questionImg = driver.find_element_by_xpath('//*[@id="survey_1491015"]/div[1]/img')
    questionImg.click()
    time.sleep(0.2)
    questionBtn = driver.find_element_by_xpath('//*[@id="survey_detail"]/div[2]/div/div[8]/a[1]')
    questionBtn.click()

def getNo():
    driver.refresh()
    time.sleep(2)
    no = driver.find_element_by_xpath('//*[@id="list"]/tr[1]/td[3]')
    print("The latest questionnaire number is: ", no)
    return no


def ana(ID):
    #你的问卷地址
    url = "https://wj.qq.com/stat_recycle_answer.html?id=#p1&" + ID
    driver.get(url)

    return driver.page_source
