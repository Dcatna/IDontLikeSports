import json
import requests
from database import DataInsertion

class MainCollection():
    json_scores = {}
    json_object = {}
    inserter = DataInsertion()


    def __init__(self, json_object, json_scores):
            self.json_object = json_object
            self.json_scores = json_scores

    def pushAll(self):
        
        #putting the game_id and the dic in the db
        for dataSet in self.json_object:
            if(dataSet['sites'] == []):
                continue
            else:
                game_id = dataSet['id']
                self.inserter.pushGameID(game_id, dataSet)
            
    

    def updateScores(self):
        #updating the scores of the game afterwards
        for scoreSet in self.json_scores:
            if(scoreSet['completed'] == False):
                continue
            else:
                game_id = scoreSet['id']
                self.inserter.updateGameIDS(game_id, scoreSet)


    #returning all the games whose odds are within a certain range
    def getRangeOfOdds(self, range1, range2):
        AllData = self.inserter.getAllGames()
        returnList = {}
        pass


