import json
from database import dataInsertion

with open('data.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)


data = {}
count = 0
#saves the desired data into the data dict
for dataSet in json_object['data']:
    if(dataSet["sites"] == []):
        continue
    elif(dataSet['sites'][0] == []):
        continue
    else:
        #COLLECTING WANTED VALUES
        sport_name = dataSet['sport_nice']
        teams = dataSet['teams']
        odds = dataSet['sites'][0]['odds']['h2h']
        time = dataSet['commence_time']
        sites = dataSet['sites']
        sport_id = dataSet['id']

        #Getting rid of soccer for now
        if(len(odds) >= 3):
            continue

        data[tuple(teams)] = tuple([sport_name, sport_id, odds, time, sites])


dataInserter = dataInsertion()
#PUTTING INFO INTO THE DATABASE
for info in data.keys():
    temp = data[info] 
    #print((tuple(temp[0]), temp[2], temp[1][0], temp[1][1], info[0], info[1], "FanDuel"))
    sportName = [(temp[0])]
    sportTable = [(temp[0], temp[3], temp[2][0], temp[2][1], info[0], info[1], "FanDuel")]
    #dataInserter.testInsertion(sportName, sportTable)


print()
#print(json_object['data'])
print()
#print(data)
