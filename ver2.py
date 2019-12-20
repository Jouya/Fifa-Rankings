""" Authors: Jouya Mahmoudi, Anam Shah, Drew, Roger  """

import csv
import random
import statistics
import datetime

CONFED = {'UEFA': (['albania', 'andorra', 'armenia', 'austria', 'austria', 'azerbaijan',
                 'belarus', 'belgium', 'bosnia and herzegovina', 'bulgaria', 
                 'croatia', 'cyprus', 'czech republic', 'denmark', 'england', 
                 'estonia', 'faroe islands', 'finland', 'france', 'georgia', 
                 'germany', 'gilbraltar', 'greece', 'hungary', 'iceland', 'israel',
                 'italy', 'kazakhstan', 'kosovo', 'latvia', 'liechtenstein', 
                 'lithuania', 'luxembourg', 'malta', 'moldova', 'montenegro', 
                 'netherlands', 'north macedonia', 'northern ireland', 'norway',
                 'poland', 'portugal', 'republic of ireland', 'romania', 'russia', 
                 'san marino', 'scotland', 'serbia', 'slovakia', 'slovenia', 
                 'spain', 'sweden', 'switzerland', 'turkey', 'ukraine', 'wales'], .99), 
          'CONMEBOL': (['argentina', 'bolivia', 'brazil', 'chile', 'colombia', 
                     'ecuador', 'paraguay', 'peru', 'uruguay', 'venezuela'], 1),
          'CONCACAF': (['anguilla', 'antigua and barbuda', 'aruba', 'bahamas', 
                     'barbados', 'belize', 'bermuda', 'british virgin islands', 
                     'canada', 'cayman islands', 'costa rica', 'cuba', 'curacao',
                     'dominica', 'dominican republic', 'el salvador', 'grenada',
                     'guatemala', 'guyana', 'haiti', 'honduras', 'jamaica', 
                     'mexico', 'montserrat', 'nicaragua', 'panama', 'puerto rico',
                     'st. kitts and nevis', 'st. lucia', 'st. vincent and the grenadlines',
                     'suriname', 'trinidad and tobago', 'turks and caicos islands',
                     'us virgin islands', 'usa'], .85), 
          'CAF': (['algeria', 'angola', 'benin', 'botswana', 'burkina faso', 'burundi',
                'cabo verde', 'cameroon', 'central african republic', 'chad', 
                'comoros', 'congo', 'congo dr', "cote d'ivoire", 'djibouti', 'egypt',
                'equatorial guinea', 'eritrea', 'eswatini', 'ethiopia', 'gabon', 
                'gambia', 'ghana', 'guinea', 'guinea-bissau', 'kenya', 'lesotho',
                'liberia', 'libya', 'madagascar', 'malawi', 'mali', 'mauritania',
                'mauritius', 'morocco', 'mozambique', 'namibia', 'niger', 
                'nigeria', 'rwanda', 'sao tome and principe', 'senegal', 
                'seychelles', 'sierra leone', 'somalia', 'south africa', 
                'south sudan', 'sudan', 'tanzania', 'togo', 'tunisia', 'uganda', 
                'zambia', 'zimbabwe'], .85),  
          'AFC': (['afghanistan', 'australia', 'bahrain', 'bangladesh', 'bhutan', 
                'bruinei darussalam', 'cambodia', 'china pr', 'chinese taipei', 
                'guam', 'hong kong', 'india', 'indonesia', 'iran', 'iraq',
                'japan', 'jordan', 'korea dpr', 'korea republic', 'kuwait', 
                'kyrgyz republic', 'kyrgyzstan', 'laos', 'lebanon', 'macau', 'malaysia', 
                'maldives', 'mongolia', 'myanmar', 'nepal', 'oman', 'pakistan', 
                'palestine', 'philippines', 'qatar', 'saudi arabia', 'singapore', 
                'sri lanka', 'syria', 'tajikistan', 'thailand', 'timor-leste', 
                'turkmenistan', 'united arab emirates', 'uzbekistan', 'vietnam', 
                'yemen'], .85),
          'OFC': (['american samoa', 'cook islands', 'fiji', 'new caledonia',
                'new zealand', 'papua new guinea', 'samoa', 'solomon islands', 
                'tahiti', 'tonga', 'vanuatu'], .85)}

def get_match_fixtures(countries):
    file = open("results.csv", encoding="utf8")
    data = file.readlines()
    # remove the header
    data.remove(data[0])
    wanted_data = []
    teams = {}
    record = False
    for row in data:
        # range of 2010 - 2014
        if (int(row[0:4]) == 2010 and int(row[5:7]) == 4 and int(row[8:10]) > 12):
            record = True       
        if (record):
            info = row.strip().split(",")
            if (info[1].lower() in countries and info[2].lower() in countries):
                wanted_data.append(info)
                # new country
                if (info[1].lower() not in teams.keys()):
                    teams[info[1].lower()] = 0
            
        if (int(row[0:4]) == 2014 and int(row[5:7]) == 5 and int(row[8:10]) > 11):
            break;
    file.close()
    return wanted_data 

def Data_from_2010():
    file = open("initial2010Rankings.csv", encoding="utf8")
    data = file.readlines()
    teams = {}
    positions = []
    for row in data:
        info = row.lstrip().rstrip().strip("\ufeff").split(",")
        positions.append(info[0].lower())
        #print(info)
        teams[info[0].lower()] = int(info[1])
        
    
    return teams, positions
    
def old_system(matches, ranking, teams):
    total = {}
    for key, val in teams.items():
        #total[key] = [int(val)]
        total[key] = []

    for game in matches:
        # result of a game
        m = [0]*2
        # importance of a game
        i = [0]*2
        # strength of opposing team
        t = [0]*2
        # region of the teams
        c = [0]*2
        
        winner = ''
        loser = ''
        draw = False
        
        # check to see if both sides have the same number of goals = draw
        if game[3] == game[4]:
            draw = True
            winner = game[1].lower()
            loser = game[2].lower()
        # home side wins
        elif game[3] > game[4]:
            winner = game[1].lower()
            loser = game[2].lower()
        # away side wins
        else: 
            winner = game[2].lower()
            loser = game[1].lower()            
            
        if winner == "south korea":
            winner = "korea republic"
        elif winner == "north korea":
            winner = "korea dpr"
        
        if loser == "south korea":
            loser = "korea republic"
        elif loser == "north korea":
            loser = "korea dpr"
        
        # Calculate M 
        penalty = (random.randint(0,100))/100
        if draw == False:  
            # calculated from data
            if penalty < .25:
                m[0] = 2
                if draw != True:
                    m[1] = 1
            # won a game normally
            else:
                m[0] = 3
                m[1] = 0
        # draw
        else:
            m[0] = 1
            m[1] = 1
        #print(m)
         
        #Calculate I (steal from the boys' work)
        if (game[5].lower() == "friendly"):
            i[0] = 1
            i[1] = 1
        elif (game[5].lower() == "fifa world Cup qualification"):
            i[0] = 2.5
            i[1] = 2.5
        # confedration cups
        else:
            i[0] = 3
            i[1] = 3
 
        
        #Calculate T 
        if ranking.index(winner) + 1 <= 50: t[0] = 50
        else: t[0] = 200 - ranking.index(winner) + 1
        if ranking.index(loser) + 1 <= 50: t[1] = 50
        else: t[1] = 200 - ranking.index(loser) + 1
        #print(t)
        
        #Calculate C 
        for key, value in CONFED.items():
            if winner in value[0]: 
                c[0] = value[1]
            if loser in value[0]:
                c[1] = value[1]
        #print(c)
    
        #Calculate 
        winner_points = m[0] * t[0] * c[0] * i[0]
        loser_points = m[1] * t[1] * c[1] * i[1]
        
        #Weight game by time played
        match_date = datetime.datetime.strptime(game[0],"%Y-%m-%d")
         
        year_two = [datetime.datetime.strptime('2012-06-12', "%Y-%m-%d"),
                    datetime.datetime.strptime('2013-06-11', "%Y-%m-%d")]
                    
        year_three = [datetime.datetime.strptime('2011-06-12', "%Y-%m-%d"),
                    datetime.datetime.strptime('2012-06-11', "%Y-%m-%d")]
        
        year_four = [datetime.datetime.strptime('2010-06-12', "%Y-%m-%d"),
                    datetime.datetime.strptime('2011-06-11', "%Y-%m-%d")]
        
        if year_two[0] <= match_date <= year_two[1]:
            winner_points *= 0.5
            loser_points *= 0.5
        elif year_three[0] <= match_date <= year_three[1]:
            winner_points *= 0.3
            loser_points *= 0.3
        elif year_four[0] <= match_date <= year_four[1]:
            winner_points *= 0.2
            loser_points *= 0.2   
        
        # P = M X I x T X C
        total[winner].append(winner_points)
        total[loser].append(loser_points)
    
    averages = {} 
    for country, points in total.items():
        if points != []:
            averages[country] = int(statistics.mean(points))
        
    return averages

def recalc_ranking(oldRankingA, oldRankingB, scoreA, scoreB, gameType, gameMonth):

    if scoreA > scoreB:
        matchResultA = 1
        matchResultB = 0
    elif scoreB > scoreA:
        matchResultA = 0
        matchResultB = 1
    else:
        matchResultA = 0.5
        matchResultB = 0.5

    matchImportance = 0
    nationsMatches = ["Cup", "Games", "Copa", "Nations", "Tournament"]
    confederationMatches = ["Championship", "AFC", "CAF", "CONCACAF", "CONMEBOL", "OFC", "UEFA"]
 
    
    if "Friendly" in gameType:
        if gameMonth in range(3,12):
            matchImportance = 10
        else:
            matchImportance = 5
    elif "qualification" in gameType:
        matchImportance = 25
    for nationString in nationsMatches:
        if nationString in gameType:
            matchImportance = 20
    for confederationString in confederationMatches:
        if confederationString in gameType:
            matchImportance = 37.5
    if matchImportance == 0:
        matchImportance = 15

    ratingDifferenceA = oldRankingA - oldRankingB
    expectedResultA = 1 / (10**(-1*ratingDifferenceA/400) + 1)
    ratingDifferenceB = oldRankingB - oldRankingA
    expectedResultB = 1 / (10**(-1*ratingDifferenceB/400) + 1)

    newRankingA = oldRankingA + matchImportance * (matchResultA - expectedResultA)
    newRankingB = oldRankingB + matchImportance * (matchResultB - expectedResultB)
    return int(newRankingA), int(newRankingB)


def main():
    teams, start_ranking = Data_from_2010()
    match_fixtures = get_match_fixtures(teams)
    points = old_system(match_fixtures, start_ranking, teams)
    
    # start off from each team's 2010 points/rankings
    new_model = teams
    games_played = {}
    for teams in new_model:
        #new_model[teams] = 0
        games_played[teams] = 0
    # apply the new 2018 scoring model to match_fixtures from 2010-2014
    for game in match_fixtures:
        home_team = game[1].lower()
        away_team = game[2].lower()
        # calcuate the resulting points from the given match
        home_score, away_score = recalc_ranking( new_model[home_team],new_model[away_team],game[3],game[4],game[5],game[0][5:7])
        # add/subtract to/from their score
        games_played[home_team] += 1
        games_played[away_team] += 1
        new_model[home_team] = home_score
        new_model[away_team] = away_score

      
    sort = {k: v for k, v in sorted(points.items(), key=lambda item: item[1], reverse=True)}
    sort2 = {k: v for k, v in sorted(new_model.items(), key=lambda item: item[1], reverse=True)}
    new_rankings = list(sort.items())
    #print("Old System", new_rankings)
    new_model = (sort2)
    
    print("New System:")
    counter = 1
    for team in new_model:
        print(str(counter) + ". " + team.capitalize()  + " = Points: " + str(new_model[team]) + ", Match Played: " + str(games_played[team]))
        counter += 1
    
    
    #print(start_ranking)
    #print(match_fixtures)
    #print(teams)
    
    
    
main()