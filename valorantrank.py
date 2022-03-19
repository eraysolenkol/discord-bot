import requests,json

def change(a):
    a_int = int(a)
    a = round(a,2)
    a_str = str(a)
    a_str_2 = a_str[3:5]
    a_int_2 = int(a_str_2)
    a_100_60 = (a_int_2*60)//100
    last_a = str(a_int) +"."+str(a_100_60)
    return last_a


valorant_agent_images = {"Astra":"https://images-ext-2.discordapp.net/external/Sy8ujb1EbYRBUUBP3HgQ1PVLI0EizbHQlE8oAME8lRU/%3Fcb%3D20210302170140/https/static.wikia.nocookie.net/valorant/images/8/8a/Astra_artwork.png/revision/latest?width=245&height=375",
"Breach":"https://static.wikia.nocookie.net/valorant/images/5/5c/Breach_artwork.png/revision/latest?cb=20200602020225",
"Brimstone":"https://static.wikia.nocookie.net/valorant/images/3/37/Brimstone_artwork.png/revision/latest?cb=20200602020239",
"Chamber":"https://static.wikia.nocookie.net/valorant/images/5/5d/Chamber_artwork.png/revision/latest?cb=20211031124636",
"Cypher":"https://static.wikia.nocookie.net/valorant/images/b/bb/Cypher_artwork.png/revision/latest?cb=20200602020329",
"Jett":"https://static.wikia.nocookie.net/valorant/images/7/79/Jett_artwork.png/revision/latest?cb=20200602020209",
"KAY/O":"https://static.wikia.nocookie.net/valorant/images/a/a9/KAYO_artwork.png/revision/latest?cb=20210622163116",
"Killjoy":"https://static.wikia.nocookie.net/valorant/images/6/6b/Killjoy_artwork.png/revision/latest?cb=20200729134445",
"Neon":"https://static.wikia.nocookie.net/valorant/images/a/ad/Neon_artwork.png/revision/latest?cb=20220112155550",
"Omen":"https://static.wikia.nocookie.net/valorant/images/0/06/Omen_artwork.png/revision/latest?cb=20200602020233",
"Phoenix":"https://static.wikia.nocookie.net/valorant/images/f/fa/Phoenix_artwork.png/revision/latest?cb=20200602020246",
"Raze":"https://static.wikia.nocookie.net/valorant/images/c/c4/Raze_artwork.png/revision/latest?cb=20200602020217",
"Reyna":"https://static.wikia.nocookie.net/valorant/images/4/41/Reyna_artwork.png/revision/latest/scale-to-width-down/587?cb=20200602020340",
"Sage":"https://static.wikia.nocookie.net/valorant/images/1/1e/Sage_artwork.png/revision/latest?cb=20200602020306",
"Skye":"https://static.wikia.nocookie.net/valorant/images/d/d6/Skye_artwork.png/revision/latest?cb=20201013182515",
"Sova":"https://static.wikia.nocookie.net/valorant/images/6/61/Sova_artwork.png/revision/latest?cb=20200602020314",
"Viper":"https://static.wikia.nocookie.net/valorant/images/9/91/Viper_artwork.png/revision/latest?cb=20200602020322",
"Yoru":"https://static.wikia.nocookie.net/valorant/images/1/1a/Yoru_artwork.png/revision/latest?cb=20210112180407"
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}

def getSTATS(name,match):
    a = 0
    last_games = []
    response = requests.get(f"https://api.henrikdev.xyz/valorant/v1/account/{name[0]}/{name[1]}",headers=headers)

    datas = json.loads(response.text)
    puuid = datas['data']['puuid']
    region = datas['data']['region']
    name_nn = datas['data']['name']

    if match != "hepsi":
        response2 = requests.get(f"https://api.henrikdev.xyz/valorant/v3/by-puuid/matches/{region}/{puuid}?filter={match}",headers=headers)
    else:
        response2 = requests.get(f"https://api.henrikdev.xyz/valorant/v3/by-puuid/matches/{region}/{puuid}",headers=headers)


    
    last_games_data = json.loads(response2.text)
    kd_ratio = []
    total_win = 0
    game_time_list = []
    player_team_result_list =[]
    game_kdas = []
    while a <5:
        first_game_data = last_games_data['data'][a]
        game_map = first_game_data['metadata']['map']
        game_server = first_game_data['metadata']['cluster']
        game_time = first_game_data['metadata']['game_start_patched']
        game_date = first_game_data['metadata']['game_start']
        game_time_ms = first_game_data['metadata']['game_length']
        game_time_minutes = game_time_ms*(1.66666667 / 100000)
        game_time_minutes_patched = change(game_time_minutes)
        game_time_list.append(game_time_minutes_patched)
        game_players = first_game_data['players']['all_players']
        game_mode = first_game_data['metadata']['mode'].lower()
        player_names = []
        player_scores = []
        players_total = 10
        if match == 'deathmatch':
            players_total = 12
        i = 0
        while i < players_total:
            player_score = game_players[i]['stats']['score']
            player_scores.append(player_score)
            for x,y in game_players[i].items():
                if x == "name":
                    player_names.append(y)


            i = i + 1

        index = player_names.index(name_nn)
        my_player_score = player_scores[index]
        player_scores.sort(reverse=True)
        my_player_place = player_scores.index(my_player_score) + 1
        player_info = game_players[index]
        player_agent = player_info['character']
        player_team = player_info['team']
        player_stats = player_info['stats']
        player_kills = player_stats['kills']
        player_deaths = player_stats['deaths']
        kd_ratio.append(player_kills/player_deaths)
        player_assists = player_stats['assists']

        player_headshots = player_stats['headshots']
        player_bodyshots = player_stats['bodyshots']
        player_legshots = player_stats['legshots']
        
        try:
            player_team_score = first_game_data['teams'][player_team.lower()]
            player_team_result = "win"
            if player_team_score['has_won'] == False:
                player_team_result = "lose"
            if player_team_result == "win":
                total_win += 1
            player_team_win = player_team_score['rounds_won']
            player_team_lose = player_team_score['rounds_lost']
            player_team_result_list.append(player_team_result)
            game_result = f"{player_team_win} - {player_team_lose} - {game_map} - {player_agent}"
        
        except:
            print('deathmatch stats')

        if match == 'deathmatch':
            player_headshots = 1
            player_bodyshots = 1
            player_legshots = 1
            game_result = f"{game_map} - {player_agent}"
            if  player_kills == 40:
                player_team_result_list.append('win')
                total_win +=1
            else:
                player_team_result_list.append('lose')
        

        
        if type(player_headshots) == type(None):
            player_headshots = 0
        if type(player_bodyshots) == type(None):
            player_bodyshots = 0
        if type(player_legshots) == type(None):
            player_legshots = 0

        player_headshots_percentage = round((player_headshots *100) / (player_bodyshots + player_legshots + player_headshots),2)

        game_kda = f"{player_kills} / {player_deaths} / {player_assists}"
        game_kdas.append(game_kda)

        last_games.append((game_result,game_kda,player_agent,player_headshots_percentage,game_mode,game_server,my_player_place,game_date))

        a = a + 1
    return last_games,kd_ratio,total_win,game_time_list,player_team_result_list,game_kdas

