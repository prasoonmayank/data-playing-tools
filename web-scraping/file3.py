from bs4 import BeautifulSoup
import requests

page = requests.get('http://www.enoughproject.org/take_action')

bs = BeautifulSoup(page.content)

print bs.title

print bs.find_all('a')
print bs.find_all('p')

header_children = [c for c in bs.head.children]

print header_children

navigation_bar = bs.find(id='globalNavigation')

for d in navigation_bar.descendents:
	print d

for s in d.previous_siblings:
	print s
