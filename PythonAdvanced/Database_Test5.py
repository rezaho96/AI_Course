from mysql.connector import connect , Error

try: 
    with connect(host="localhost",user="root",password="962013058",database="dbtest2") as db:
        myCursor=db.cursor()
        # id=int(input("Enter id for delete:"))
        # myCursor.execute(f"delete from t_person where PersonId={id}")
        
        
        id=int(input("Enter id for delete:"))
        myCursor.execute("delete from t_person where PersonId="+str(id))
        db.commit()
except Error as error:
    print(error)