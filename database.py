import mysql.connector

myDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Vaprak08!",
    database = "testdatabase"
    
)

myCurser = myDB.cursor()

#USE THIS LATER
"FOREIGN KEY(sport_name) REFERENCES Events(sport_nice)"
#

#table1 = "CREATE TABLE EventsTest (sport_nice VARCHAR(50) PRIMARY KEY NOT NULL)"
#myCurser.execute(table1)

#NEED TO MAKE PRIMARY KEY THE ID OF THE MATCH
#table2 = "CREATE TABLE SportsTest3 (sport_nice VARCHAR(50) PRIMARY KEY NOT NULL, commence_time VARCHAR(50) NOT NULL, odds_one int NOT NULL, odds_two int NOT NULL, teams1 VARCHAR(50) NOT NULL, teams2 VARCHAR(50), site VARCHAR(50) NOT NULL, FOREIGN KEY(sport_nice) REFERENCES EventsTest(sport_nice))"
#myCurser.execute(table2)


realTableHopefully = "CREATE TABLE SportsInfo (id int PRIMARY KEY AUTO_INCREMENT, sport_nice VARCHAR(50) NOT NULL, commence_time VARCHAR(50) NOT NULL, odds_one int NOT NULL, odds_two int NOT NULL, teams_one VARCHAR(50) NOT NULL, teams_two VARCHAR(50) NOT NULL, site VARCHAR(50) NOT NULL)"
#myCurser.execute(realTableHopefully)

class dataInsertion():
    #Returns all events from Event Table
    def getAllEventTable():
        return myCurser.execute("SELECT * FROM SportsTablee")

    #Returns the Event of a given sport name
    def getEventTableForSport(idek, sport_nice):
        return myCurser.execute("SELECT * FROM SportsTablee WHERE sport_nice = '%s'" , sport_nice)
    
    def testInsertion(thing, eventsPlug, SportsPlug):
        sata = "INSERT INTO EventsTest (sport_nice) VALUES(%s)"
        #print(eventsPlug)
        #myCurser.executemany(sata, eventsPlug)

        myCurser.executemany("INSERT INTO SportsInfo (sport_nice, commence_time, odds_one, odds_two, teams_one, teams_two, site) VALUES(%s, %s, %s, %s, %s, %s, %s)", SportsPlug)
        myDB.commit()
    

test = dataInsertion()
sporttist = [('assss', )]
sportsTable = [("assss", "1111111", -120, 120, "beng", "jags", "JERK")]

#test.testInsertion(sporttist, sportsTable)
#myCurser.execute("DESCRIBE SportsTable")
myCurser.execute("SELECT * FROM SportsInfo WHERE sport_nice = 'NFL'")
for x in myCurser:
    print(x)
#print(myCurser.fetchall())
print(myDB)