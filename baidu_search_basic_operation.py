from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://baidu.com')
# 找到一个按钮，然后点击
hao = driver.find_element_by_name('tj_trhao123')
hao.click()

# 回到上一个界面
driver.back()

# 填写一些东西
baidu_search = driver.find_element_by_id("kw")
baidu_search.send_keys('beijing one day trip')
baidu_button = driver.find_element_by_id('su')
baidu_button.click()

time.sleep(3)  # 强制等待3秒再执行下一步

# scroll to the bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(2)

# generate a screen shot
driver.save_screenshot('screenshot.png')

# print(driver.current_url)
driver.quit()

