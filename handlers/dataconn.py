import mysql.connector
from mysql.connector import Error
import json

def connect_to_db():
    try: 
        # USING RAILWAY
        print("Connecting...")
        BettingDatabase = mysql.connector.connect(
                port = 7892,
                host = "containers-us-west-201.railway.app",
                password = "afsTDjDtfErxDRlnCcVU",
                database = "railway",
                user = 'root'
            )

        if BettingDatabase.is_connected():
            print("Successful Connection")
            return BettingDatabase, BettingDatabase.cursor(buffered=True)#huge play buffer stops data being lost aswell as reseting cursor

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None, None

BettingDatabase, myCurser = connect_to_db()

class CollectData():

    #returns the odds and sites for a given pair of teams
    def getOddsByName(self, team1, team2):
        oddsList = []
        myCurser.execute("SELECT * FROM GameIDs")
        for data in myCurser.fetchall():
            data = data[1]
            data = eval(data) #convert the stirng back to a dictonary

            if(team1 in data['teams'] and team2 in data['teams']):
                teams = data['teams']
                oddsList.append((teams))
                for odds in data['sites']:
                    oddsList += ((odds['site_nice'], odds['odds']['h2h']))

        return oddsList  
    
    def getRangeOfOdds(self, oddslist):
        low, high = 0, 0

        for odds in oddslist[1::]:
            if(type(odds) == list):

                if(low > odds[1]):
                    low = odds[0]
                
                if(high < odds[0]):
                    high = odds[1]
                    
        return [low, high]

rah = CollectData()
fd = rah.getOddsByName('Arizona Cardinals', 'Cleveland Browns')
print(fd)
rang = rah.getRangeOfOdds(fd)
print(rang)

