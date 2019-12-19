""" Authors: Jouya Mahmoudi  """

import csv

def extract_data():
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
            wanted_data.append(info)
            # new country
            if (info[1].lower() not in teams.keys()):
                teams[info[1].lower()] = 0
            
        if (int(row[0:4]) == 2014 and int(row[5:7]) == 5 and int(row[8:10]) > 11):
            break;
        
    return wanted_data 

def old_ranking():
    file = open("initial2010Rankings.csv", encoding="utf8")
    data = file.readlines()
    teams = {}
    for row in data:
        info = row.lstrip().rstrip().strip("\ufeff").split(",")
        
        teams[info[0].lower()] = info[1]
        
    
    return teams
    
def main():
    match_fixtures = extract_data()
    teams = old_ranking()
    print(match_fixtures)
    #print(teams)
    
    
    
main()
    
    
    
