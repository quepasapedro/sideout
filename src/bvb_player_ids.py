import requests as r
from bs4 import BeautifulSoup as bs


def get_players():
  player_names = {}

  player_id = 0
  while player_id <= 10:
    player_html = r.get('http://www.bvbinfo.com/player.asp?ID={}'.format(player_id)).text
    player_soup = bs(player_html, "lxml")
    if len(player_soup.findAll(attrs={"class":"clsErrorMsg"})) > 0:
      player_id += 1
    else:
      player_name = player_soup.findAll(attrs={"class":"clsPlayerName"})[0].string
      player_names[player_id] = player_name.strip()
      player_id += 1 

  return player_names

player_mapping = get_players()
print(player_mapping.items())


def get_tournaments():
  tournament_names = {}

  tournament_id = 0
  while tournament_id <= 10:
    tournament_html = r.get('http://www.bvbinfo.com/Tournament.asp?ID={}'.format(tournament_id)).text
    tournament_soup = bs(tournament_html, "lxml")
    if len(tournament_soup.findAll(attrs={"class":"clsErrorMsg"})) > 0:
      tournament_id += 1
    else:
      tournament_list = [x for x in tournament_soup.findAll(attrs={"class":"clsTournHeader"})[0].stripped_strings]
      tournament_names[tournament_id] = tournament_list[0]
      tournament_id += 1 

  return tournament_names

tourn_mapping = get_tournaments()
print(tourn_mapping.items())