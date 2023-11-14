from mysql.connector import connect , Error

try: 
    with connect(host="localhost",user="root",password="962013058",database="dbtest2") as db:
        myCursor=db.cursor()
        # myCursor.execute("select * from dbtest2.t_person")
        # people=myCursor.fetchall()
        # for person in people:
        #     print(person)
        
        
        
        # myCursor.execute("select * from dbtest2.t_person where Age<26")
        # people=myCursor.fetchall()
        # for person in people:
        #     print(person)
        
        
        age =int(input("Enter number for limited age:"))
        myCursor.execute(f"select * from dbtest2.t_person where Age<{age}")
        people=myCursor.fetchall()
        for person in people:
            print(person)
except Error as error:
    print(error)