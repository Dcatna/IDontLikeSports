
from database import DataInsertion
from datetime import datetime
import pytz

class MainCollection():
    json_scores = {}
    json_object = {}
    json_players = {}
    inserter = DataInsertion()


    def __init__(self, json_object, json_scores, json_players):
            self.json_object = json_object
            self.json_scores = json_scores
            self.json_players = json_players


    def convert_utc_to_et(self, utc_time_str):
        # Parse the UTC time string to a datetime object
        utc_time = datetime.strptime(utc_time_str, '%Y-%m-%dT%H:%M:%SZ')

        # Define the UTC timezone
        utc = pytz.utc

        # Define the Eastern Time timezone
        eastern = pytz.timezone('America/New_York')

        # Localize the UTC datetime and convert it to Eastern Time
        eastern_time = utc.localize(utc_time).astimezone(eastern)
        formatted_time = eastern_time.strftime("%Y-%m-%d %I:%M:%S %p %Z")
        return formatted_time


    def pushAll(self):
        gamedic = {} #team, time, odds, id
        #putting the game_id and the dic in the db
        for dataSet in self.json_object:
            sum = 0
            count = 0
            bestoddwin = -10000000000000
            bestoddwinsite = ""
            bestoddlose = -10000000000000
            bestoddlosesite = ""
            leftteam = False
            print(str(dataSet) + "\n")
            if(dataSet['sites'] == []):
                continue
            else:
                game_id = dataSet['id']
                teams = dataSet['teams']
                utc_time = dataSet['commence_time']
                time = self.convert_utc_to_et(utc_time)
                game_info = {
                'game_id': game_id,
                'teams': teams,
                'commence_time': time,
                'odds': []
                }

        # Iterating over each site to gather odds
            for site in dataSet['sites']:
                sitename = site['site_nice']
                odds = site['odds']['h2h']
                
                # Adding site name and odds to the game_info
                game_info['odds'].append({'site': sitename, 'odds': odds})         
            #print(game_info)
            for game_odds in game_info['odds']:
                #print(game_odds)
                odd = game_odds['odds']
                #print(odd)
                if(int(odd[0]) > 0): #when +odds is on the left
                    sum += int(odd[0])
                    if(int(odd[1]) > bestoddwin):
                        bestoddwin = int(odd[1])
                        bestoddwinsite = game_odds['site']
                    else:
                        if(int(odd[0]) > bestoddlose):
                            bestoddlose = int(odd[0])
                            bestoddlosesite = game_odds['site']
                else :
                    leftteam = True
                    sum += int(odd[1])
                    if(int(odd[0]) > bestoddwin):
                        bestoddwin = int(odd[0])
                        bestoddwinsite = game_odds['site']
                    elif(int(odd[1]) > bestoddlose):
                        bestoddlose = int(odd[1])
                        bestoddlosesite = game_odds['site']
                       # print(str(bestoddlosesite) + "\n")
                count+=1
            
            avg = sum/count
            if(leftteam == False):
                winTeamOne = 100/(avg + 100)
                winTeamTwo = 1 - winTeamOne
                winTeamTwo, winTeamOne = (winTeamTwo * 100), (winTeamOne * 100)
            else:
                winTeamTwo = 100/(avg + 100)
                winTeamOne = 1 - winTeamTwo
                winTeamTwo, winTeamOne = (winTeamTwo * 100), (winTeamOne * 100)
           # print(winTeamOne, winTeamTwo)
           # print(bestoddwinsite + "             ", bestoddlosesite)
            print((game_id, time,(teams[0], winTeamOne), (teams[1], winTeamTwo), (bestoddwinsite, bestoddwin, bestoddlosesite, bestoddlose)))
            self.inserter.pushPercents(game_id, time, teams[0], winTeamOne, teams[1], winTeamTwo, bestoddwinsite, bestoddwin, bestoddlosesite, bestoddlose)
            

    def updateScores(self):
        #updating the scores of the game afterwards
        for scoreSet in self.json_scores:
            if(scoreSet['completed'] == False):
                continue
            else:
                game_id = scoreSet['id']
                self.inserter.updateGameIDS(game_id, scoreSet)

    def playerOdds(self):
        gamedic = {}
        teams = [self.json_players['home_team'], self.json_players['away_team']]
        commence_time = self.json_players['commence_time']
        for bookie in self.json_players['bookmakers']:
            market = bookie['markets']
            for playerodd in bookie['outcomes']:
                gamedic[playerodd['description']] += [playerodd['name'], playerodd['price']]
                pass
        pass



    #returning all the games whose odds are within a certain range
    def getRangeOfOdds(self, range1, range2):
        AllData = self.inserter.getAllGames()
        returnList = {}
        pass


