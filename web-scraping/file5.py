from lxml import html

page = html.parse('http://www.enoughproject.org/take_action')
root = page.getroot()

ta_divs = root.cssselect('div.view-row')

print ta_divs

all_data = []

for ta in ta_divs:
	data_dict = {}
	title = ta.cssselect('h2')[0]
	data_dict['title'] = title.text_content()
	data_dict['link'] = title.find('a').get('href')
	data_dict['about'] = [p.text_content() for p in ta.cssselect('p')]
	all_data.append(data_dict)

print all_data

print root.find('div')
print root.find('head')
print root.find('head').findall('script')
print root.cssselect('div')
print root.cssselect('head script')
