import requests as r 
from bs4 import BeautifulSoup as bs 
from fetch_player_ids import get_players, get_tournaments


def check_valid_combo(tournament_id, player_id_1, player_id_2):

	# Example url format:
	# http://50.21.56.50/TeamPreview?TournID=3076&ID1=13454&ID2=13453
	result_html = r.get('http://50.21.56.50/TeamPreview?TournID={}&ID1={}&ID2={}'.format(tournament_id, player_id_1, player_id_2)).text.encode('utf-8')
	combo_soup = bs(result_html, "lxml")

	if combo_soup.find(attrs={"id":"PlayerPersonalControl11_lblPlayerName"}).text == 'Label':
		return ('NULL')
	else:
		# tournament_teams[tournament_id] = {'player_1': player_id_1, 'player_2': player_id_2}
		return (tournament_id, player_id_1, player_id_2)
	

def __main__():

	tournament_teams = {}

	TOURNAMENT_IDS = get_tournaments()
	PLAYER_IDS = get_players()

	i = 0

	while i < 10:
		for tournament_id in TOURNAMENT_IDS.keys():
			for player_id_1 in PLAYER_IDS.keys():
				for player_id_2 in PLAYER_IDS.keys():
					team_response = check_valid_combo(tournament_id, player_id_1, player_id_2)
					if team_response == 'NULL':
						i += 1
						continue
					else:
						tournament_teams[team_response[0]] = {'player_1': team_response[1], 'player_2': team_response[2]}
						i += 1

	print(tournament_teams.items()[:10])


__main__()