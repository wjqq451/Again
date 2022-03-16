from selenium import webdriver
from selenium.webdriver.common.by import By
import time

wd = webdriver.Chrome(r"D:\software\Chrome\chromedriver.exe")
wd.get('http://192.168.1.110:18685/private-admin/#/')
wd.implicitly_wait(10)

wd.add_cookie({'name':'token','value':'35e4273986e682aac1cedecbb9f182d2'})
wd.refresh()

jichu = wd.find_element(By.XPATH,'//span[text()="基础数据"]')
jichu.click()

haoma = wd.find_element(By.XPATH,'//span[text()="号码管理"]')
haoma.click()

from selenium.webdriver.common.action_chains import ActionChains
ac = ActionChains(wd)
xuanfu = wd.find_element(By.XPATH,'//i[@class="el-icon-arrow-down"]')
ac.move_to_element(xuanfu).perform()

guanbi = wd.find_element(By.XPATH,'//li[text()="关闭当前标签"]')
guanbi.click()

time.sleep(10)