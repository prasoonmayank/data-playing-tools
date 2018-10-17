from lxml import html
import requests

resp = requests.get('http://www.emoji-cheat-sheet.com/')
page = html.document_fromstring(resp.content)

body = page.find('body')
top_header = body.find('h2')

print top_header.text

headers_and_lists = [sib for sib in top_header.itersiblings()]

print headers_and_lists

proper_headers_and_lists = [s for s in top_header.itersiblings() if 
							s.tag in ['ul', 'h2', 'h3']]

print proper_headers_and_lists

