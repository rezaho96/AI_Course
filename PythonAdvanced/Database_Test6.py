from mysql.connector import connect , Error

try: 
    with connect(host="localhost",user="root",password="962013058",database="dbtest2") as db:
        myCursor=db.cursor()
        q1='''
        update t_person
        set avg=avg+1
        where age<25
        '''
        myCursor.execute(q1)
        db.commit()
except Error as error:
    print(error)