from selenium.webdriver import Chrome
import time


broswer = Chrome()
broswer.get('http://www.porters.vip/features/webdriver.html')

script = 'Object.defineProperty(navigator,"webdriver",{get:() => false,});'
broswer.execute_script(script)
time.sleep(1)
broswer.find_element_by_css_selector('.btn.btn-primary.btn-lg').click()
elements = broswer.find_element_by_css_selector('#content')
time.sleep(1)
print(elements.text)
broswer.close()