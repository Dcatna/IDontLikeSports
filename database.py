import mysql.connector

myDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Vaprak08!",
    database = "testdatabase"
    
)

myCurser = myDB.cursor()

#table1 = "CREATE TABLE Events (sport_nice VARCHAR(50) PRIMARY KEY NOT NULL, site VARCHAR(50) NOT NULL)"
#myCurser.execute(table1)
table2 = "CREATE TABLE SportsTablee (sport_name VARCHAR(50) PRIMARY KEY NOT NULL, commence_time VARCHAR(50) NOT NULL, odds_one int NOT NULL, odds_two int NOT NULL, teams1 VARCHAR(50) NOT NULL, teams2 VARCHAR(50), site VARCHAR(50) NOT NULL)"
#myCurser.execute(table2)

class dataInsertion():
    #Returns all events from Event Table
    def getAllEventTable():
        return myCurser.execute("SELECT * FROM SportsTablee")

    #Returns the Event of a given sport name
    def getEventTableForSport(sport_nice):
        return myCurser.execute("SELECT * FROM SportsTablee WHERE sport_nice = $sport_nice")
    
    #adds given event to the Event Table
    def addToEventTable(id, sports):
        insertSStatement = "INSERT INTO SportsTablee (sport_name, commence_time, odds_one, odds_two, teams1, teams2, site) VALUES(%s, %s, %s, %s, %s, %s, %s)"

        #commits all the info to the database
        myCurser.executemany(insertSStatement, sports)
        myDB.commit()
    


test = dataInsertion()
#odd= ([-130, 120])
#teams = (["jac", "dolp"])
#events = [("ass", "JERK")]
sportsTable = [("ass", "1111111", -120, 120, "beng", "jags", "JERK")]
#test.addToEventTable(sportsTable)

#myCurser.execute("DESCRIBE SportsTable")
myCurser.execute("SELECT * FROM SportsTablee")
for x in myCurser:
    print(x)
#print(myCurser.fetchall())
print(myDB)