import json
import mysql.connector

try: 
    BettingDatabase = mysql.connector.connect(
            port = 3306,
            host = "db",
            password = "root",
            database = "db"
        )
    
    if(BettingDatabase.is_connected):
        print("Succesful Connection")

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
    

print('mydb')
myCurser = BettingDatabase.cursor()
gameIDTable = "CREATE TABLE IF NOT EXISTS GameIDs (game_id VARCHAR(50) PRIMARY KEY NOT NULL, response TEXT NOT NULL, scores TEXT)"
scoresTable = "CREATE TABLE IF NOT EXISTS ScoreInfos(game_id VARCHAR(100) PRIMARY KEY NOT NULL, commence_time VARCHAR(50) NOT NULL, sport_title VARCHAR(50) NOT NULL, score_one int NOT NULL, score_two int NOT NULL, team_one VARCHAR(50) NOT NULL, team_two VARCHAR(50) NOT NULL)"
realTableHopefully = "CREATE TABLE IF NOT EXISTS SportInfos(game_id VARCHAR(100) PRIMARY KEY NOT NULL, sport_nice VARCHAR(50) NOT NULL, commence_time VARCHAR(50) NOT NULL, odds_one int NOT NULL, odds_two int NOT NULL, teams_one VARCHAR(50) NOT NULL, teams_two VARCHAR(50) NOT NULL, site VARCHAR(50) NOT NULL)"

myCurser.execute(realTableHopefully)
myCurser.execute(scoresTable)
myCurser.execute(gameIDTable)

class DataInsertion():
    #pushes initial odds for game without score bc it hasnt played yet
    def pushGameID(self, game_id, response):
        myCurser.execute("REPLACE INTO GameIDs(game_id, response) VALUES(%s, %s)", (game_id, str(response)))
        BettingDatabase.commit()

    #pushes the scores to the game after played by game_id
    def updateGameIDS(self, game_id, scores): #uhuh
        myCurser.execute("UPDATE GameIDs SET scores = %s WHERE game_id = %s", (str(scores), game_id))

    def getAllGames(self):
        myCurser.execute("SELECT * FROM GameIDs")
        return myCurser.fetchall()
    

#test.testInsertion(sporttist, sportsTable)
#myCurser.execute("DESCRIBE SportsTable")
#lis = test.getEventTableForSport(('WNBA', ))

#myCurser.execute("SELECT * FROM SportsInfo WHERE sport_nice = 'NFL'")
#for x in lis:
 #   print(x)
#print(myCurser.fetchall())
#print(myDB)