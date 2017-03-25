import sqlite3

class Interface:
    """Each instance should create a user interface that manages the sqlite3 commands for the user
    """
    def __init__(self, database):
        self.database=database
    
    #retrieve the names of the tables available, present to user...


if __name__=='__main__':

    connection = sqlite3.connect("chinook.db")
    cursor = connection.cursor()
    
    print("The options appear in the mess below that I'll clean up later.")
    cursor.execute("PRAGMA table_info(employees)")
    result = cursor.fetchall()
    for r in result:
        print(r)

    option=raw_input("What data would you like to view?")

    cursor.execute("SELECT "+ option+ " FROM employees")
    print("fetchall:")
    result = cursor.fetchall()
    for r in result:
        print(r)

    option2=raw_input("Would you like to insert data into this set?")
    if option2=="yes":
        print("sorry, that resource hasn't been coded yet.")

    raw_input("press return")
    print("Here's a join of the name and title columns of the artists and albums tables.")
    
    cursor.execute("SELECT Name, Title FROM artists INNER JOIN albums ON albums.Artistid=artists.ArtistId")
    res=cursor.fetchall()
    for r in res:
        print(r)
