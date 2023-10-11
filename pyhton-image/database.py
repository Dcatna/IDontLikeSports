import mysql.connector

BettingDatabase = mysql.connector.connect(
        port = '3306',
        host = "db",
        password = "root",
        database = "db",
        user = 'root'
    )
print('mydb')
myCurser = BettingDatabase.cursor()

scoresTable = "CREATE TABLE IF NOT EXISTS ScoreInfos(game_id VARCHAR(100) PRIMARY KEY NOT NULL, commence_time VARCHAR(50) NOT NULL, sport_title VARCHAR(50) NOT NULL, score_one int NOT NULL, score_two int NOT NULL, team_one VARCHAR(50) NOT NULL, team_two VARCHAR(50) NOT NULL)"
realTableHopefully = "CREATE TABLE IF NOT EXISTS SportInfos(game_id VARCHAR(100) PRIMARY KEY NOT NULL, sport_nice VARCHAR(50) NOT NULL, commence_time VARCHAR(50) NOT NULL, odds_one int NOT NULL, odds_two int NOT NULL, teams_one VARCHAR(50) NOT NULL, teams_two VARCHAR(50) NOT NULL, site VARCHAR(50) NOT NULL)"

myCurser.execute(realTableHopefully)
myCurser.execute(scoresTable)

class DataInsertion():
   #Returns all scores from the scorestable

    def getAllScoretable(self):
        myCurser.execute("SELECT * FROM ScoreInfo")
        return myCurser.fetchall()
    
    #inserts new info into scoretable
    def insertScore(self, scoreInfo):
        myCurser.executemany("REPLACE INTO ScoreInfos (game_id, commence_time, sport_title, score_one, score_two, team_one, team_two) VALUES(%s, %s, %s, %s, %s, %s, %s)", scoreInfo)
        BettingDatabase.commit()

    #Returns all events from Event Table
    def getAllEventTable(self):
        myCurser.execute("SELECT * FROM SportInfos")
        return myCurser.fetchall()

    #Returns the Event of a given sport name
    def getEventTableForSport(self, sport_nice):
        myCurser.execute("SELECT * FROM SportInfos WHERE sport_nice = (%s)" , sport_nice)
        return myCurser.fetchall()
    
    def testInsertion(self, SportsPlug):
        #replace removes dups
        myCurser.executemany("REPLACE INTO SportInfos (game_id , sport_nice, commence_time, odds_one, odds_two, teams_one, teams_two, site) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", SportsPlug)
        BettingDatabase.commit()

    #gets odds and teams for a specific game id
    def getOddsTeams(self, sport_id):
        myCurser.execute("SELECT odds_one, odds_two, teams_one, teams_two FROM SportInfos WHERE sport_id = (%s)", sport_id)
        return myCurser.fetchall()
    

test = DataInsertion()
sporttist = [('assss', )]
sportsTable = [("assss", "1111111", -120, 120, "beng", "jags", "JERK")]

#test.testInsertion(sporttist, sportsTable)
#myCurser.execute("DESCRIBE SportsTable")
#lis = test.getEventTableForSport(('WNBA', ))

#myCurser.execute("SELECT * FROM SportsInfo WHERE sport_nice = 'NFL'")
#for x in lis:
 #   print(x)
#print(myCurser.fetchall())
#print(myDB)