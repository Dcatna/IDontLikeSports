import json
import requests
from database import DataInsertion

#with open('data.json', 'r') as openfile:
    # Reading from json file
    #json_object = json.load(openfile)

#print(json_object['data'])

class MainCollection():
    data = {}
    json_object = {}

    def __init__(self, json_object):
        self.json_object = json_object

    def clearData(self):
        self.data = {}
        

    #saves the desired data into the data dict
    def collectCurrentSportsInfo(self):
        newData = {}
        for dataSet in self.json_object:
            
            if(dataSet["bookmakers"] == []):
                continue
            elif(dataSet['bookmakers'][0] == []):
                continue
            else:
                #COLLECTING WANTED VALUES
                sport_name = dataSet['sport_title']
                team1 = dataSet['home_team']
                team2 = dataSet['away_team']
                teams = [team1, team2]
                sport_id = dataSet['id']

                #should make so can get all the odds from all the sites
                #print(dataSet['sites'][0]['site_nice'])
                for sites in dataSet['bookmakers']:
                    site = sites['title']
                    odds = []
                    for odd in sites['markets']:
                        #Getting rid of soccer for now
                        if(len(odds) >= 3):
                            continue
                        odd1 = odd['outcomes'][0]['price']
                        odd2 = odd['outcomes'][1]['price']
                        odds = [odd1, odd2]
                        #odds += odd['outcomes']['price']
                        
                    time = dataSet['commence_time']
                     

                    #this is overwritign need to fix
                    if(tuple(teams) in newData):
                        newData[tuple(teams)] += [sport_name, sport_id, odds, time, site]
                    else:
                        newData[tuple(teams)] = [sport_name, sport_id, odds, time, site]
                
        #print(newData)
        self.data = newData
    
    #pushed to the DB !!!!!takes a list of tuples if u want just the tuple take out the exevutemany()
    def pushToDatabase(self, sportList):
        dataInserdter = DataInsertion()
        dataInserdter.testInsertion(sportList)
    
    #gets the specific info from data into a list
    def getListOfInfo(self):
        #list of all the possible sites the api can reach to accesss alllltheoddss
        returnLis = []
        for info in self.data.keys():
            temp = self.data[info] 
            #IMAFUCGINIDIOT
            sportTable = (temp[0], temp[3], temp[2][0], temp[2][1], info[0], info[1], temp[4])
            returnLis.append(sportTable)

        return returnLis


#PUTTING INFO INTO THE DATABASE

#DataInserter.testInsertion(sportName, sportTable)



#test.collectCurrentSportsInfo()

print()
#print(json_object['data'])
print()
#print(data)
