import json
from database import DataInsertion

with open('data.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

class MainCollection():
    data = {}

    def clearData(self):
        self.data = {}

    #saves the desired data into the data dict
    def collectCurrentSportsInfo(self):
        newData = {}
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

                newData[tuple(teams)] = tuple([sport_name, sport_id, odds, time, sites])
        #print(newData)
        self.data = newData
    
    #pushed to the DB !!!!!takes a list of tuples if u want just the tuple take out the exevutemany()
    def pushToDatabase(idek, sportList):
        dataInserdter.testInsertion(sportList)
    
    #gets the specific info from data into a list
    def getListOfInfo(self):
        returnLis = []
        for info in self.data.keys():
            temp = self.data[info] 
            sportTable = (temp[0], temp[3], temp[2][0], temp[2][1], info[0], info[1], "FanDuel")
            returnLis.append(sportTable)

        return returnLis

dataInserdter = DataInsertion()
#PUTTING INFO INTO THE DATABASE

    #DataInserter.testInsertion(sportName, sportTable)


print()
#print(json_object['data'])
print()
#print(data)
