import requests as r
from bs4 import BeautifulSoup as bs


def get_players():

  player_names = {}

  player_id = 0
  while player_id <= 20:

    player_html = r.get('http://www.bvbinfo.com/player.asp?ID={}'.format(player_id)).text.encode('utf-8')
    player_soup = bs(player_html, "lxml")

    if len(player_soup.findAll(attrs={"class":"clsErrorMsg"})) > 0:
      player_id += 1
    else:
      player_name = player_soup.findAll(attrs={"class":"clsPlayerName"})[0].string.encode('utf-8')
      
      player_names[player_id] = player_name.strip()
      player_id += 1 

  return player_names


def get_tournaments():
  
  tournament_names = {}

  tournament_id = 0
  while tournament_id <= 10:

    tournament_html = r.get('http://www.bvbinfo.com/Tournament.asp?ID={}'.format(tournament_id)).text.encode('utf-8')
    tournament_soup = bs(tournament_html, "lxml")
    
    if len(tournament_soup.findAll(attrs={"class":"clsErrorMsg"})) > 0:
      tournament_id += 1
    else:
      tournament_list = [x for x in tournament_soup.findAll(attrs={"class":"clsTournHeader"})[0].stripped_strings]
      tournament_names[tournament_id] = tournament_list[0]
      tournament_id += 1 

  return tournament_names


def get_matches():

  match_ids = {}

  match_id = 0
  while match_id < 20:

    match_html = r.get('http://50.21.56.50/MatchRecap?matchid={}'.format(match_id)).text.encode('utf-8')
    match_soup = bs(match_html, "lxml")

    if match_soup.find(attrs={"id":"PlayerPersonalControl11_lblPlayerName"}).text.encode('utf-8') == 'Label':
      match_id += 1
    else:
      match_ids[match_id] = {'tournament_name':match_soup.find(attrs={"class":"clsTournamentName"}).text.encode('utf-8'), 'match_name':match_soup.find(attrs={"class":"clsMatch"}).text.encode('utf-8')}
      match_id += 1

  return match_ids

get_players()
get_tournaments()
get_matches()