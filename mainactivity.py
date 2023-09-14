import json
import requests
from testJson import MainCollection
from database import DataInsertion
from database import myDB

# An api key is emailed to you when you sign up to a plan
api_key = 'e6d25e5095f904c5ed3a729152a5f57d'


# First get a list of in-season sports
sport_key = 'upcoming'

odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params= {
    'api_key': api_key,
    'sport': sport_key,
    'region': 'us', # uk | us | eu | au
    'mkt': 'h2h', # h2h | spreads | totals
    "oddsFormat" : 'american', # decimal | american
    'dateFormat': 'iso',  # iso | unix
    
})

odds_json = json.loads(odds_response.text)

#print(odds_json['data'])
def pushInfoToDB(sport_json):
    if not sport_json['success']:
        print("WTFAREUDOING")
    else:

        collection = MainCollection(sport_json['data'])

        collection.collectCurrentSportsInfo()

        listOfInfo = collection.getListOfInfo()
        print(listOfInfo)
        collection.pushToDatabase(listOfInfo)
    
pushInfoToDB(odds_json)

inserter = DataInsertion()

#allData = sports_json['data']      
#print(sports_json)
for x in inserter.getAllEventTable():
    print(x)


   