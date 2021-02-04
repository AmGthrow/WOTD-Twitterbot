import bs4, requests, pyperclip, lxml
from datetime import date

res = requests.get('https://www.merriam-webster.com/word-of-the-day')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')


message = f'''{soup.select('span.w-a-title.margin-lr-0.margin-tb-1875em')[0].text.split(':')[1][1:]}

{soup.select('div.word-and-pronunciation h1')[0].text.upper()}
{soup.select('span.main-attr')[0].text} | {soup.select('span.word-syllables')[0].text}

{soup.select('div.wod-definition-container h2')[0].text.capitalize()}
'''
definitionList = soup.select('div.wod-definition-container > p')
for definition in definitionList:
    message = message + '\n' + definition.text

pyperclip.copy(message)