import requests
from bs4 import BeautifulSoup

def scrape_point(main,extra):

    main_point = []
    extra_point = []
    for card in main:
        url = "https://yugioh-list.com/searches/result?keyword=" + card + "&keyword1=0&keyword1=1&keyword2=0&keyword2=1&keyword3=0&keyword3=1&effect=&kind_id1=&kind_id2=&type_id=&attribute_id=&level_f=&level_t=&level1=0&level1=1&level2=0&level2=1&p_blue_f=&p_blue_t=&p_red_f=&p_red_t=&link_num_f=&link_num_t=&link1=0&link2=0&link3=0&link4=0&link5=0&link6=0&link7=0&link8=0&atk_f=&atk_t=&atk_h=&dif_f=&dif_t=&dif_h=&limit_id=&limit_id%5B%5D=1&limit_id%5B%5D=2&limit_id%5B%5D=3&limit_id%5B%5D=4&avg_point_f=&avg_point_t="

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # メインデッキのカードを取得
        main_cards_div = soup.find('table', class_='tableList')
        #print(main_cards_div)
        if main_cards_div:
            main_card = main_cards_div.find('td',class_="rightyose")
            try:
                main_card = main_card.find("font").get_text()
                main_point.append([card,main_card])
            except:
                extra_point.append([card,0])
    
    for card in extra:
        url = "https://yugioh-list.com/searches/result?keyword=" + card + "&keyword1=0&keyword1=1&keyword2=0&keyword2=1&keyword3=0&keyword3=1&effect=&kind_id1=&kind_id2=&type_id=&attribute_id=&level_f=&level_t=&level1=0&level1=1&level2=0&level2=1&p_blue_f=&p_blue_t=&p_red_f=&p_red_t=&link_num_f=&link_num_t=&link1=0&link2=0&link3=0&link4=0&link5=0&link6=0&link7=0&link8=0&atk_f=&atk_t=&atk_h=&dif_f=&dif_t=&dif_h=&limit_id=&limit_id%5B%5D=1&limit_id%5B%5D=2&limit_id%5B%5D=3&limit_id%5B%5D=4&avg_point_f=&avg_point_t="

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # メインデッキのカードを取得
        extra_cards_div = soup.find('table', class_='tableList')
        #print(main_cards_div)
        if extra_cards_div:
            #print(card)
            extra_card = extra_cards_div.find('td',class_="rightyose")
            try:
                extra_card = extra_card.find("font").get_text()
                extra_point.append([card,extra_card])
            except:
                extra_point.append([card,0])
                

    return main_point, extra_point

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

url = "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=fa08c8e750b16b29682b4a63d5defe6f&dno=16&request_locale=ja"
main, extra = scrape_deck(url)
#print(main,extra)
main_point, extra_point = scrape_point(main,extra)
print(main,main_point)
print(extra,extra_point)