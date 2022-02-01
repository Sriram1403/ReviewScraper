import time

import selenium.webdriver
from lxml import html
from selenium.webdriver.common.keys import Keys


driver = selenium.webdriver.Chrome(executable_path="C:\\Users\\DELL\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")

driver.get('https://www.flipkart.com/')

driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()

driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input"). \
    send_keys(input("enter the product :"))

driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input"). \
    send_keys(Keys.ENTER)

time.sleep(3)

source = html.fromstring(driver.page_source)

prod_xpath = ['//div[@class="_4rR01T"]/text()', '//a[@class="s1Q9rs"]/text()', '//a[@class="s1Q9rs"]/text()', '//div[@class="_1W9f5C"]/div/text()']
# //div[@class="_2WkVRV"]/text()
product_name = []
product_review = []

try:
    for i in prod_xpath:
        product_name = source.xpath(i)
        if len(product_name) != 0:
            break
    if len(product_name) == 0:
        print('xpath not detected')
        # exit(-1)
    product_review = source.xpath('//div[@class="_3LWZlK"]/text()')
except:
    raise Exception("Source not found")


try:
    print(product_name)
    print(product_review)
    print(len(product_name), ' ', len(product_review))
    product_name = product_name[len(product_review)-len(product_name):]
    for i in range(len(product_name)):
        print(product_name[i], "   ", product_review[i])
except:
    print('Not found')



# //div[@class="_4rR01T"]/text()
# input('Enter your product name : ')