import os
from selenium import webdriver

driver = webdriver.Remote(
    command_executor=os.environ["SELENIUM_URL"],
    options=webdriver.ChromeOptions(),
)

driver.get('https://www.amazon.co.jp/dp/480261179X')
driver.save_screenshot('amazon.png')
driver.quit()