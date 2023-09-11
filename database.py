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

table1 = "CREATE TABLE EventsTest (id int PRIMARY KEY AUTO_INCREMENT, sport_nice VARCHAR(50) NOT NULL)"
#myCurser.execute(table1)

#NEED TO MAKE PRIMARY KEY THE ID OF THE MATCH
table2 = "CREATE TABLE SportsTest2 (sport_id int PRIMARY KEY, FOREIGN KEY(sport_id) REFERENCES EventsTest(id), sport_name VARCHAR(50) NOT NULL, sport_id VARCHAR(50) NOT NULL, commence_time VARCHAR(50) NOT NULL, odds_one int NOT NULL, odds_two int NOT NULL, teams1 VARCHAR(50) NOT NULL, teams2 VARCHAR(50), site VARCHAR(50) NOT NULL)"
#myCurser.execute(table2)

class dataInsertion():
    #Returns all events from Event Table
    def getAllEventTable():
        return myCurser.execute("SELECT * FROM SportsTablee")

    #Returns the Event of a given sport name
    def getEventTableForSport(sport_nice):
        return myCurser.execute("SELECT * FROM SportsTablee WHERE sport_nice = $sport_nice")
    
    def testInsertion(thing, eventsPlug, SportsPlug):
        sata = "INSERT INTO EventsTest (sport_nice) VALUES(%s)"
        #print(eventsPlug)
        myCurser.executemany(sata, eventsPlug)

        myCurser.executemany("INSERT INTO SportsTest2 (sport_name, sport_id, commence_time, odds_one, odds_two, teams1, teams2, site) VALUES(%s, %s,%s, %s, %s, %s, %s, %s)", SportsPlug)
        myDB.commit()
    
    #adds given event to the Event Table
    def addToEventTable(id, sports):
        #HAVE TO FIX THE IGNORE
        insertSStatement = "INSERT IGNORE INTO SportsTablee (sport_name, commence_time, odds_one, odds_two, teams1, teams2, site) VALUES(%s, %s, %s, %s, %s, %s, %s)"

        #commits all the info to the database
        myCurser.executemany(insertSStatement, sports)
        myDB.commit()
    

test = dataInsertion()
sporttist = [('ass', )]
sportsTable = [("ass", "@#$^&*FGHJK", "1111111", -120, 120, "beng", "jags", "JERK")]

#test.testInsertion(sporttist, sportsTable)
#myCurser.execute("DESCRIBE SportsTable")
myCurser.execute("SELECT * FROM SportsTest2")
for x in myCurser:
    print(x)
#print(myCurser.fetchall())
print(myDB)