import csv
def old_model():
    return None

def new_model():
    return None


def data_extract():
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
            wanted_data.append(row)
            info = row.split(",")
            # new country
            if (info[1].lower() not in teams.keys()):
                teams[info[1].lower()] = 0
            
        if (int(row[0:4]) == 2014 and int(row[5:7]) == 5 and int(row[8:10]) > 11):
            break;

    return wanted_data 

def old_ranking():
    
    
def main():
    wanted_data = data_extract()
    teams = old_ranking()
    
    
    
main()
    
    
    
