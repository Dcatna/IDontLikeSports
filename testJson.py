import json
from database import DataInsertion

with open('data.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

#print(json_object['data'])

class MainCollection():
    data = {}
    json_object
    
    def __init__(self, json_object):
        self.json_object = json_object

    def clearData(self, json_object):
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
                sport_id = dataSet['id']

                #should make so can get all the odds from all the sites
                for site in dataSet['sites']['site_nice']:
                    odds = dataSet['sites'][site]['odds']['h2h']
                     #Getting rid of soccer for now
                    if(len(odds) >= 3):
                        continue
                    time = dataSet['commence_time']
                    newData[tuple(teams)] = tuple([sport_name, sport_id, odds, time, site])
                
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
            sportTable = (temp[0], temp[3], temp[2][0], temp[2][1], info[0], info[1], "FanDuel")
            returnLis.append(sportTable)

        return returnLis


#PUTTING INFO INTO THE DATABASE

    #DataInserter.testInsertion(sportName, sportTable)


print()
#print(json_object['data'])
print()
#print(data)
