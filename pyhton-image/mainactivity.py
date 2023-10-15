
import requests
import json
from testJson import MainCollection
from database import DataInsertion
from database import BettingDatabase
# An api key is emailed to you when you sign up to a plan
#my key 'ba7e6e8faf2f023cea41e73e8089e9d0'
#ethans key 'e6d25e5095f904c5ed3a729152a5f57d'
API_KEY = 'e6d25e5095f904c5ed3a729152a5f57d'

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



def pushGameID(odds_json, scores_json):
    collection = MainCollection(odds_json, scores_json)
    collection.pushAll()


#pushInfoToDB(odds_json)
#pushScoresToDB(scores_json)
#print(odds_json)
pushGameID(odds_json, scores_json)
inserter = DataInsertion()

x = BettingDatabase.cursor()
x.execute("SELECT * FROM GameIDs")


print(x.fetchone()[1])
    
    #print(json.loads(str(i)))



   