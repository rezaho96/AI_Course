from mysql.connector import connect , Error
# Create table
try: 
    with connect(host="localhost",user="root",password="962013058",database="dblibarary") as db:
        myCursor=db.cursor()
        q1='''
        create table t_books(
            BookId int primary key auto_increment,
            Title varchar(400) NOT NULL,
            Author varchar(100) NOT NULL,
            Publisher varchar(100) NOT NULL
        )
        '''
        myCursor.execute(q1)
        db.commit()
except Error as error:
    print(error)
# ////////////////////////////////////////////////////////////////////
while(1):
    print("-----------------------------")
    print("1)Add book \n2)Delete book \n3)Search book \n4)Show books")
    print("-----------------------------")
    click=int(input("Enter number :"))
    match click:
        case 1:
            try: 
                with connect(host="localhost",user="root",password="962013058",database="dblibarary") as db:
                    myCursor=db.cursor()        
                    title=input("Enter title :")
                    author=input("Enter author :")
                    publisher=input("Enter publisher :")
                    val=(title,author,publisher)
                    myCursor.execute("insert into t_books(Title,Author,Publisher)values(%s,%s,%s)",val)
                    db.commit()
            except Error as error:
                print(error)
        case 2:
            try: 
                with connect(host="localhost",user="root",password="962013058",database="dblibarary") as db:
                    myCursor=db.cursor()        
                    bookId=int(input("Enter bookId for delete :"))
                    val=(bookId,)
                    myCursor.execute("Delete From t_books Where bookid=%s",val)
                    db.commit()
            except Error as error:
                print(error)

        case 3:
            try: 
                with connect(host="localhost",user="root",password="962013058",database="dblibarary") as db:
                    myCursor=db.cursor()        
                    bookId=int(input("Enter bookId for select :"))
                    val=(bookId,)
                    myCursor.execute("Select * From t_books Where bookid=%s",val)
                    book=myCursor.fetchall()
                    print(book)
                    db.commit()
            except Error as error:
                print(error)
        case 4:
            try: 
                with connect(host="localhost",user="root",password="962013058",database="dblibarary") as db:
                    myCursor=db.cursor()        
                    myCursor.execute("Select * From t_books")
                    books=myCursor.fetchall()
                    for book in books:
                        print(book)
                    db.commit()
            except Error as error:
                print(error)