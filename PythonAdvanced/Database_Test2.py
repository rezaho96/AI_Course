from mysql.connector import connect , Error

try: 
    with connect(host="localhost",user="root",password="962013058",database="dbtest2") as db:
        myCursor=db.cursor()
        q1='''
        create table t_person(
            PersonId int primary key,
            Neme varchar(30),
            Family varchar(30),
            Age int,
            Avg decimal(4,2)
        )
        '''
        myCursor.execute(q1)
        db.commit()
except Error as error:
    print(error)