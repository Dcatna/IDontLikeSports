import json
import requests
from testJson import MainCollection
from database import DataInsertion
from database import myDB

# An api key is emailed to you when you sign up to a plan
api_key = 'e6d25e5095f904c5ed3a729152a5f57d'

# First get a list of in-season sports
sports_response = requests.get('https://api.the-odds-api.com/v3/sports', params={
    'api_key': api_key
})

#sports_json = json.loads(sports_response.text)

def pushInfoToDB(sport_json):
    if not sport_json['success']:
        print("WTFAREUDOING")
    else:

        collection = MainCollection(sport_json)

        collection.collectCurrentSportsInfo()

        listOfInfo = collection.getListOfInfo()
        collection.pushToDatabase(listOfInfo)
    
#pushInfoToDB()

inserter = DataInsertion()

#allData = sports_json['data']      

for x in inserter.getAllEventTable():
    print(x)


   