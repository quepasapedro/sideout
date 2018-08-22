import requests as r 
from bs4 import BeautifulSoup as bs 
from fetch_player_ids import get_players


def get_player_data(player_id): 
	raw_html = r.get('http://www.bvbinfo.com/player.asp?ID={}'.format(player_id)).text

	text_table = bs(raw_html, "lxml")

	PAGE_SECTIONS = [label.text for label in text_table.findAll(attrs={"class":"clsPlayerTable"})[0].findAll(attrs={"class":"clsPlayerHeader"})]
	TABLE_COLUMNS = [label.text for label in text_table.find(attrs={"class":"clsPlayerDataHeader"}).stripped_strings]
	
	return


def __main__():
	VALID_PLAYER_IDS = get_players()
	for pair in VALID_PLAYER_IDS.items():
		get_player_data(pair[0])