from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://justfreetemplates.com/wordpress-themes/preview/3505.html')

iframe = browser.find_element_by_xpath('//iframe')

new_url = iframe.get_attribute('src')
browser.get(new_url)

