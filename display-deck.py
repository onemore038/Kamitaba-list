import streamlit as st
import requests
from bs4 import BeautifulSoup

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
    if extra_cards_div:
        extra_cards = extra_cards_div.find_all('img')
        for card in extra_cards:
            card_name = card.get('alt').strip()
            if card_name:
                extra_deck.append(card_name)

    return main_deck, extra_deck


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
            main_card = main_card.find("font").get_text()
            main_point.append(main_card)
    
    for card in extra:
        url = "https://yugioh-list.com/searches/result?keyword=" + card + "&keyword1=0&keyword1=1&keyword2=0&keyword2=1&keyword3=0&keyword3=1&effect=&kind_id1=&kind_id2=&type_id=&attribute_id=&level_f=&level_t=&level1=0&level1=1&level2=0&level2=1&p_blue_f=&p_blue_t=&p_red_f=&p_red_t=&link_num_f=&link_num_t=&link1=0&link2=0&link3=0&link4=0&link5=0&link6=0&link7=0&link8=0&atk_f=&atk_t=&atk_h=&dif_f=&dif_t=&dif_h=&limit_id=&limit_id%5B%5D=1&limit_id%5B%5D=2&limit_id%5B%5D=3&limit_id%5B%5D=4&avg_point_f=&avg_point_t="

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # メインデッキのカードを取得
        extra_cards_div = soup.find('table', class_='tableList')
        #print(main_cards_div)
        if extra_cards_div:
            extra_card = extra_cards_div.find('td',class_="rightyose")
            #print(extra_card)
            #extra_card = extra_card.find("font").get_text()
            #print(extra)
            extra_point.append(extra_point)

    return main_card, extra_card


# ユーザーにURLを入力してもらう
st.title("Webスクレイパー")
url = st.text_input("スクレイピングするURLを入力してください:")

if url:
    # URLの内容をリクエスト
    try:
        main, extra = scrape_deck(url)
        main_point, extra_point = scrape_point(main,extra)

        # タイトルの表示
        st.title("Yu-Gi-Oh! デッキリスト")

        # メインデッキの表示
        st.header("メインデッキ")
        st.write(f"カードの枚数: {len(main)}")
        
        for (card,point) in zip(main,main_point):
            st.write(f"- {card} - {point}")

        for card in main:
            st.write(f"- {card}")


        # エクストラデッキの表示
        st.header("エクストラデッキ")
        st.write(f"カードの枚数: {len(extra)}")
        for (card,point) in zip(extra,extra_point):
            st.write(f"- {card} - {point}")
        
        for card in extra:
            st.write(f"- {card}")
        

        st.write(f"合計点数 - {sum(extra_point) + sum(main_point)}")

        

    except requests.exceptions.RequestException as e:
        st.error(f"URLの読み込みに失敗しました: {e}")