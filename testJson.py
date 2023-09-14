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
                sport_id = dataSet['id']

                #should make so can get all the odds from all the sites
                #print(dataSet['sites'][0]['site_nice'])
                for sites in dataSet['sites']:
                    site = sites['site_nice']
                    odds = sites['odds']['h2h']
                     #Getting rid of soccer for now
                    if(len(odds) >= 3):
                        continue
                    time = dataSet['commence_time']

                    #this is overwritign need to fix
                    if(tuple(teams) in newData):
                        
                        newData[tuple(teams)] += tuple([(sport_name, sport_id, odds, time, site)])
                    else:
                        newData[tuple(teams)] = tuple([(sport_name, sport_id, odds, time, site)])
                
        #print(newData)
        print(newData)
        self.data = newData
    
    #pushed to the DB !!!!!takes a list of tuples if u want just the tuple take out the exevutemany()
    def pushToDatabase(self, sportList):
        dataInserdter = DataInsertion()
        dataInserdter.testInsertion(sportList)
    
    #gets the specific info from data into a list
    def getListOfInfo(self):
        #list of all the possible sites the api can reach to accesss alllltheoddss
        returnLis = []
        print("hi")
        print(self.data)
        for info in self.data.keys():
            temp = self.data[info] 
            #IMAFUCGINIDIOT
            sportTable = (temp[0], temp[3], temp[2][0], temp[2][1], info[0], info[1], temp[4])
            returnLis.append(sportTable)

        return returnLis


#PUTTING INFO INTO THE DATABASE

#DataInserter.testInsertion(sportName, sportTable)

test = MainCollection(json_object)
temp1 = test.collectCurrentSportsInfo()
temp = test.getListOfInfo()
#test.collectCurrentSportsInfo()

print()
#print(json_object['data'])
print()
#print(data)
