import bs4, requests, pyperclip, lxml
from datetime import date

res = requests.get('https://www.merriam-webster.com/word-of-the-day')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')


message = f'''{soup.select_one('.w-a-title').text.split(':')[1][1:]} 

{soup.h1.text.upper()} 
{soup.select_one('.main-attr').text} | {soup.select_one('.word-syllables').text}

{soup.select_one('.wod-definition-container h2').text.capitalize()}
'''

definitionList = soup.select('.wod-definition-container > p')
for definition in definitionList:
    message = message + '\n' + definition.text

pyperclip.copy(message)