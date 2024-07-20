import requests
from bs4 import BeautifulSoup

def scrape_deck(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    main_deck = []
    extra_deck = []

    # メインデッキのカードを取得
    main_cards_div = soup.find('div', id='main', class_='card_set')
    #print(main_cards_div)
    if main_cards_div:
        main_cards = main_cards_div.find_all('img')
        #print(main_cards)
        for card in main_cards:
            #print(card)
            card_name = card.get('alt').strip()
            #print(card_name)
            if card_name:
                main_deck.append(card_name)

    # エクストラデッキのカードを取得
    extra_cards_div = soup.find('div', id='extra', class_='card_set')
    #print(extra_cards_div)
    if extra_cards_div:
        extra_cards = extra_cards_div.find_all('img')
        for card in extra_cards:
            card_name = card.get('alt').strip()
            #print(card_name)
            if card_name:
                extra_deck.append(card_name)

    return main_deck, extra_deck

url = "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?ope=1&wname=MemberDeck&ytkn=c453734b4fe1559b118a05e9f8d26fb5e275b6dfe0b95071625ff8d3bcbf491b&cgid=bea9ee95592a8073b38bb8e7a7daa9ba&dno=17&request_locale=ja"
main, extra = scrape_deck(url)
#print(main,extra)