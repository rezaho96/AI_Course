from mysql.connector import connect , Error

try: 
    with connect(host="localhost",user="root",password="962013058") as db:
        myCursor=db.cursor()
        myCursor.execute("show databases")
        for database in myCursor: 
            print(database)
        
        q1="create DaTabase dbtest2"
        myCursor.execute(q1)
except Error as error:
    print(error)