import json
import requests
from testJson import MainCollection
from database import DataInsertion
from database import myDB
import datetime
# An api key is emailed to you when you sign up to a plan
API_KEY = 'ba7e6e8faf2f023cea41e73e8089e9d0'

# First get a list of in-season sports
SPORT = 'americanfootball_nfl' # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports

REGIONS = 'us' # uk | us | eu | au. Multiple can be specified if comma delimited

MARKETS = 'h2h,spreads' # h2h | spreads | totals. Multiple can be specified if comma delimited

ODDS_FORMAT = 'american' # decimal | american

DATE_FORMAT = 'iso' # iso | unix

scores_response = requests.get(
    f'https://api.the-odds-api.com/v4/sports/{SPORT}/scores/?apiKey={API_KEY}&daysFrom={3}&dateFormat={DATE_FORMAT}', 
    params={
        'apiKey': API_KEY,
        'sport' : SPORT,
        'dateFormat' : DATE_FORMAT,
        'daysFrom' : 3,
    }
    
)

scores_json = scores_response.json()
#print(scores_json)

odds_response = requests.get(
    f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds/?apiKey={API_KEY}&regions={REGIONS}&markets={MARKETS}',
    params={
        'api_key': API_KEY,
        'sport' : SPORT,
        'regions': REGIONS,
        'markets': MARKETS,
        'oddsFormat': ODDS_FORMAT,
        'dateFormat': DATE_FORMAT,
    }
)


odds_json = odds_response.json()
#print(odds_json)

#try:
    #print(odds_json)
#except:
    #None
#print(odds_json)


def pushInfoToDB(sport_json):
        
    collection = MainCollection(sport_json, {})

    collection.collectCurrentSportsInfo()

    listOfInfo = collection.getListOfInfo()
    #print(listOfInfo)
    collection.pushToDatabase(listOfInfo)

def pushScoresToDB(scores_json):
    collection = MainCollection({}, scores_json)

    collection.collectScoresInfo()
    listOfInfo = collection.getListOfScores()
    #print(listOfInfo)
    collection.pushScoresToDB(listOfInfo)


pushInfoToDB(odds_json)
#pushScoresToDB(scores_json)

inserter = DataInsertion()

x = myDB.cursor()
x.execute("SELECT * FROM ScoreInfo")

for i in x.fetchall():
    try:
        print(i)
    except:
        print(Exception )



   