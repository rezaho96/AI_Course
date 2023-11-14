from mysql.connector import connect , Error

try: 
    with connect(host="localhost",user="root",password="962013058",database="dbtest2") as db:
        myCursor=db.cursor()
        # q1='''
        # insert into t_person(PersonId,Neme,Family,Age,Avg)
        # values(4,"ahmad","jafari",26,14)
        
        # '''
        # myCursor.execute(q1)
        
        
        # myCursor.execute("insert into t_person(PersonId,Neme,Family,Age,Avg)values(6,'saeid','hamidi',18,16.32)")
        
        
        
        # personId=int(input("Enter personId :"))
        # name=input("Enter name :")
        # family=input("Enter family :")
        # age=int(input("Enter age :"))
        # avg=float(input("Enter average :"))
       
        # myCursor.execute(f"insert into t_person(PersonId,Neme,Family,Age,Avg)values({personId},'{name}','{family}',{age},{avg})")
        
        
        
        # personId=int(input("Enter personId :"))
        # name=input("Enter name :")
        # family=input("Enter family :")
        # age=int(input("Enter age :"))
        # avg=float(input("Enter average :"))
        # val=(personId,name,family,age,avg)
        # myCursor.execute("insert into t_person(PersonId,Neme,Family,Age,Avg)values(%s,%s,%s,%s,%s)",val)
        
        
        
        
        
        val=[(14,'hasan','mahmodi',36,17.2),(15,'jadem','khodarahmi',27,13.75)]
        myCursor.executemany("insert into t_person(PersonId,Neme,Family,Age,Avg)values(%s,%s,%s,%s,%s)",val)
        db.commit()
except Error as error:
    print(error)