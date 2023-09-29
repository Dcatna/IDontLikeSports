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
    scores = {}
    json_scores = {}

    def __init__(self, json_object, json_scores):
            self.json_object = json_object
            self.json_scores = json_scores

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
                    time = dataSet['commence_time']
                    for odd in sites['markets']:
                        #Getting rid of soccer for now
                        if(len(odds) >= 3):
                            continue
                        odd1 = odd['outcomes'][0]['price']
                        odd2 = odd['outcomes'][1]['price']
                        odds = [odd1, odd2]
                        #odds += odd['outcomes']['price']
                        

                        #this is overwritign need to fix
                        if(tuple(teams) in newData):
                            newData[tuple(teams)] += [(sport_id, sport_name, odd1, odd2, time, site)]
                        else:
                            newData[tuple(teams)] = [(sport_id, sport_name, odd1, odd2, time, site)]
                
        #print(newData)
        self.data = newData

     #gets the specific info from data into a list
    def getListOfInfo(self):
        #DONEDITTLYDONR
        returnLis = []
        for info in self.data.keys():
            temp = self.data[info] 
           # print(temp)
            #IMAFUCGINIDIOT
            
            for stats in temp:
                #print(stats)
                sportTable = (stats[0], stats[1], stats[4], stats[2], stats[3], info[0], info[1], stats[5])
            
                returnLis.append(sportTable)

        return returnLis
    
    def collectScoresInfo(self):
        #same idea as the other collector
        newScores = {}
        for scoreInfo in self.json_scores:
            if(scoreInfo['completed'] == False):
                continue
            else:
                sport_title = scoreInfo['sport_title']
                game_id = scoreInfo['id']
                team1 = scoreInfo['home_team']
                team2 = scoreInfo['away_team']
                commence_time = scoreInfo['commence_time']
                team1_score = scoreInfo['scores'][1]['score']
                team2_score = scoreInfo['scores'][0]['score']

                newScores[game_id] = [sport_title, team1, team2, commence_time, team1_score, team2_score]
        self.scores = newScores

    def getListOfScores(self):
        #yadada
        returnLis = []

        for score in self.scores.keys():
            temp = self.scores[score]
            scoreTable = (score, temp[3], temp[0], temp[4], temp[5], temp[1], temp[2])
            returnLis.append(scoreTable)

        return returnLis
    
    def pushScoresToDB(self, scoresList):
        dataInserter = DataInsertion()
        dataInserter.insertScore(scoresList)

    #pushed to the DB !!!!!takes a list of tuples if u want just the tuple take out the exevutemany()
    def pushToDatabase(self, sportList):
        dataInserdter = DataInsertion()
        dataInserdter.testInsertion(sportList)
    
   


#PUTTING INFO INTO THE DATABASE

#DataInserter.testInsertion(sportName, sportTable)



#test.collectCurrentSportsInfo()

print()
#print(json_object['data'])
print()
#print(data)
