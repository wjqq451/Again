from selenium import webdriver
from selenium.webdriver.common.by import By
import time

wd = webdriver.Chrome(r'D:\software\Chrome\chromedriver.exe')
wd.get('')
wd.implicitly_wait(10)

wd.add_cookie({'name':'token','value':''})
wd.refresh()

jichu = wd.find_element(By.XPATH,'//span[text()=""]')
jichu.click()

qudao = wd.find_element(By.XPATH,'//span[text()=""]')
qudao.click()

qudao_new = wd.find_element(By.XPATH,'//*[@id="main-container"]/div[2]/div/div[2]/div/button[2]/span')
qudao_new.click()

bianma = wd.find_element(By.XPATH,'//input[@placeholder=""]')
jiancheng = wd.find_element(By.XPATH,'//input[@placeholder=""]')
quancheng = wd.find_element(By.XPATH,'//input[@placeholder=""]')
leixing = wd.find_element(By.XPATH,'//input[@placeholder=""]')
neibu = wd.find_element(By.XPATH,'//span[text()=""]')
tijiao = wd.find_element(By.XPATH,'//span[text()=""]')

bianma.send_keys('auto_test')
jiancheng.send_keys('自动化1')
quancheng.send_keys('自动化输入1')
leixing.click()
neibu.click()
tijiao.click()

time.sleep(10)