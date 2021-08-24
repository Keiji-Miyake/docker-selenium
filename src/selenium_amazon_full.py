import os
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Remote(
    command_executor=os.environ["SELENIUM_URL"],
    options=options,
)

driver.get('https://www.amazon.co.jp/dp/480261179X')
page_width = driver.execute_script(
    'return document.body.scrollWidth'
)
page_height = driver.execute_script(
    'return document.body.scrollHeight'
)
driver.set_window_size(page_width, page_height)
driver.save_screenshot('amazon_full.png')
driver.quit()