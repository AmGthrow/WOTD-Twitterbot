from bs4 import BeautifulSoup
import requests
import lxml

def get_word():
    res = requests.get('https://www.merriam-webster.com/word-of-the-day')
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    # Why doesn't soup.find() work for date??? I'd prefer .find() over .select_one(), gross
    date = soup.select_one('.w-a-title').text.split(':')[1][1:]
    word = soup.h1.text.upper()
    part_of_speech = soup.select_one('.main-attr').text
    pronunciation = soup.select_one('.word-syllables').text
    definitionList = soup.select('.wod-definition-container > p')

    message = f'{date}\n\n{word}\n\n{part_of_speech} | {pronunciation}\n\nDefinition'

    for definition in definitionList:
        message = message + '\n' + definition.text

    return message

if __name__ == "__main__":
    print(get_word())