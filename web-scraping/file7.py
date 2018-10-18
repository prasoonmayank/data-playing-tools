from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://duckduckgo.com/?q=fun+thing&ia=web')

browser.maximize_window()

content = browser.find_element_by_css_selector('h2.result__title')
print "Content text printed\n"
print content.text

all_bubbles = browser.find_elements_by_css_selector('h2.result__title')
print "Length of all bubbles printed \n"
print len(all_bubbles)
print "Final printed\n"
for bubble in all_bubbles:
	print bubble.text


