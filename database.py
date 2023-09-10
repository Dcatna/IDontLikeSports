import mysql.connector

myDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Vaprak08!",
    database = "testdatabase"
    
)

myCurser = myDB.cursor()

table1 = "CREATE TABLE Event (sport_nice varchar PRIMARY KEY NOT NULL )"
myCurser.execute(table1)
table2 = "CREATE TABLE SportNice (sport_name varchar PRIMARY KEY, FORIEGN KEY(sport_name) REFERENCES Event(sport_nice), commence_time varchar NOT NULL, odds list NOT NULL, teams list NOT NULL)"
myCurser.execute(table2)
class dataInsertion():
    #Returns all events from Event Table
    def getAllEventTable():
        return myCurser.execute("SELECT * FROM Event")

    #Returns the Event of a given sport name
    def getEventTable(sport_nice):
        return myCurser.execute("SELECT * FROM Event WHERE sport_nice = $sport_nice")
    
    #adds given event to the Event Table
    def addToEventTable(sport_nice):
        myCurser.execute("INSERT INTO Event (sport_nice) VALUES(%s, %s)", sport_nice)
        myDB.commit()

print(myDB)