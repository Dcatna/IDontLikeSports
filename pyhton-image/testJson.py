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
            if(dataSet["bookmakers"] == []):
                continue
            elif(dataSet['bookmakers'][0] == []):
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


    #gets the odds from all the sites for two specific teams
    def getOddsForTeam(self, team1, team2):
        teamOdds = {team1 : [], team2 : []}
        allData = self.inserter.getAllGames()

        for data in allData[1]:
            if(team1 in data and team2 in data):
                for sites in data[1]['bookmakers']:
                    if(sites['markets']['outcomes'][0]['name'] == team2):
                        team2Odds = sites['markets']['outcomes'][0]['price']
                        team1Odds = sites['markets']['outcomes'][1]['price']
                    else:
                        team1Odds = sites['markets']['outcomes'][0]['price']
                        team2Odds = sites['markets']['outcomes'][1]['price']

                    teamOdds[team1] += team1Odds
                    teamOdds[team2] += team2Odds 

        return teamOdds
    
    
    #gets the scores for two teams
    def getScoresForTeam(self, team1, team2):
        allData = self.inserter.getAllGames()
        team1Score = 0
        team2Score = 0
        for data in allData[2]:
            if(team1 in data and team2 in data):
                if(data['scores'][0]['name'] == team1):
                    team1Score = data['scores'][0]['score']
                    team2Score = data['scores'][1]['score']
                else:
                    team2Score = data['scores'][0]['score']
                    team1Score = data['scores'][1]['score']
        return [team1Score, team2Score]


    #returning all the games whose odds are within a certain range
    def getRangeOfOdds(self, range1, range2):
        AllData = self.inserter.getAllGames()
        returnList = {}
        pass


