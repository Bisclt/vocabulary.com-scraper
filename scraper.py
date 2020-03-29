from bs4 import BeautifulSoup
import requests

url_prefix = 'https://www.vocabulary.com/dictionary/'

fp = open('vocab_list.txt', 'r', encoding='UTF-8')

while True:

    # vocab = 'master'
    vocab = fp.readline().strip('\n')

    # print(vocab)
    if not vocab:
        break

    url = url_prefix+vocab
    # print(url)

    source = requests.get(url).text

    # print(source)

    soup = BeautifulSoup(source, 'html5lib')

    if soup.html.head.title.text == 'Page Not Found : Vocabulary.com':
        # print(url+"not found.\n")
        continue

    try:
        WANTED = soup.html.body.div.find(
            'div', class_='page', id='page').div.div.div

        word = WANTED.h1.text

        definitions = WANTED.find(
            'div', class_='definitionsContainer').div.div

        # print(definitions)

        short_def = definitions.find('p', class_='short').text
        long_def = definitions.find('p', class_='long').text
        # definition = soup.html.div.div.div.div.div.div.div.div

        # print(word)
        # print(definition)

        print('## ' + word)
        print()
        print('> ' + short_def)
        print()
        print('> ' + long_def)
        print('\n\n')
    except:
        # print(vocab + ' failed')
        pass
