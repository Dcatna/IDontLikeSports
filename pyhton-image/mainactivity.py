
import requests
import json
from testJson import MainCollection
from database import DataInsertion
from database import BettingDatabase
from flask import Flask
import os

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def trigger_function():
    # Here, you can call your main application logic
        
    # An api key is emailed to you when you sign up to a plan
    #my key 'ba7e6e8faf2f023cea41e73e8089e9d0'
    API_KEY = 'e6d25e5095f904c5ed3a729152a5f57d'
    #API_KEY = 'dc8cc9a10b3cbbbb7cf28290a2b23c4e'

    # First get a list of in-season sports
    SPORT = 'americanfootball_nfl' # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports
    SPORT2 = 'basketball_nba'
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
    scores_response2 = requests.get(
        f'https://api.the-odds-api.com/v4/sports/{SPORT}/scores/?apiKey={API_KEY}&daysFrom={3}&dateFormat={DATE_FORMAT}', 
        params={
            'apiKey': API_KEY,
            'sport' : SPORT2,
            'dateFormat' : DATE_FORMAT,
            'daysFrom' : 3,
        }
        
    )
    scores_json = scores_response.json()
    scores_json2 = scores_response2.json()
    #print(scores_json)

    odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params= {
    'api_key': API_KEY,
    'sport': SPORT,
    'region': 'us', # uk | us | eu | au
    'mkt': 'h2h', # h2h | spreads | totals
    "oddsFormat" : 'american', # decimal | american
    'dateFormat': 'iso',  # iso | unix
    
})
    odds_response2 = requests.get('https://api.the-odds-api.com/v3/odds', params= {
        'api_key': API_KEY,
        'sport': SPORT2,
        'region': 'us', # uk | us | eu | au
        'mkt': 'h2h', # h2h | spreads | totals
        "oddsFormat" : 'american', # decimal | american
        'dateFormat': 'iso',  # iso | unix,
        'daysFrom' : 1,
        
    })

    #odds_json = odds_response.json()
    #odds_json = odds_json['data']
    odds_json2 = odds_response2.json()
    #print(odds_json2)
    odds_json2 = odds_json2['data']
    #print(odds_json["data"])
    #print(odds_json)

    #try:
        #print(odds_json)
    #except:
        #None
    #print(odds_json)



    def pushGameID(odds_json, scores_json, player_json):
        collection = MainCollection(odds_json, scores_json, player_json)
        collection.pushAll()
        collection.updateScores()


    #pushInfoToDB(odds_json)
    #pushScoresToDB(scores_json)
    #print(odds_json)
    #pushGameID(odds_json, scores_json)
    #print(odds_json2)
    pushGameID(odds_json2, scores_json2, {})
    inserter = DataInsertion()

    x = BettingDatabase.cursor()
    x.execute("SELECT * FROM GamePercents")
    result = x.fetchall()
    print(result)
    


    player_markets = ['player_points', 'player_rebounds', 'player_assists', 'player_threes', 'player_double_double', 'player_blocks', 'player_steals', 'player_points_rebounds_assists']
    for market in player_markets:
        for ids in result:
            event_id = ids[0]
            url = f'https://api.the-odds-api.com/v4/sports/{SPORT2}/events/{event_id}/odds'
            params = {
                'apiKey': API_KEY,
                'regions': 'us',
                'markets': market,
                'dateFormat': 'iso',
                'oddsFormat': 'american'
            }
            response = requests.get(url, params=params)
        
            if response.status_code == 200:
                # Process the response
                data = response.json()
               # print(data)
                #save by teams, commencetime, player/overunder ma 

           # else:
                # Handle errors
                #print(f"Error: {response.status_code}")
                #print(response.text)
    res = []
        
        #print(json.loads(str(i)))
    
    return f'Operation completed successfully {res}!'
#93b978585bf0aa7cafb48cc3ef875fc9

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

#redeploy calls
#docker build -t gcr.io/[PROJECT-ID]/[IMAGE-NAME]:[NEW-TAG] .
#docker build -t gcr.io/lucky-coast-400516/pyhton-image-app:2 .

#docker push gcr.io/[PROJECT-ID]/[IMAGE-NAME]:[NEW-TAG]
#docker push gcr.io/lucky-coast-400516/pyhton-image-app:2
