from selenium import webdriver
from selenium.webdriver.common.by import By
import time

wd = webdriver.Chrome(r'D:\software\Chrome\chromedriver.exe')
wd.implicitly_wait(10)
wd.get('')

cookie = {'name':'token','value':'5ce5868f625af3a2d7959aa9f9f6d909'}
wd.add_cookie(cookie)
wd.refresh()

jichu = wd.find_element(By.XPATH,'')
jichu.click()
haoma = wd.find_element(By.XPATH,'')
haoma.click()

#模拟鼠标放在下拉框上
from selenium.webdriver.common.action_chains import ActionChains
ac = ActionChains(wd)
element = wd.find_element(By.XPATH,'')
ac.move_to_element(element).perform()
#点击下拉框的某个按钮
click1 = wd.find_element(By.XPATH,'')
click1.click()
# element1 = wd.find_element(By.XPATH,'')

# element1.send_keys('wj')

# element2 = wd.find_element(By.XPATH,'')

# element2.send_keys('123')


time.sleep(50)