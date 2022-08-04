def tournamentWinner(competitions, results):
	max_wins = -1
	max_win_lang = None
	win_count_dict = dict()
	for i,result in enumerate(results):
		if result == 1:
			win_team = competitions[i][0]
		else:
			win_team = competitions[i][1]
		win_count = win_count_dict.get(win_team,0)+1
		win_count_dict[win_team] = win_count
		if win_count > max_wins:
			max_wins = win_count
			max_win_lang = win_team
	return max_win_lang