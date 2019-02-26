import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="password", database="lms")
mycursor = mydb.cursor()


def issueBook():
   isbn = int(input("Enter the ISBN of the book : "))
   user_id = str(input("Enter the id of the user :  "))

   query = ("insert into history(isbn, userid) values(%s, %s)")
   val = (isbn, user_id)

   mycursor.execute(query, val)
   mydb.commit()

   print(mycursor.rowcount, "Book issued")


def acceptBook():
   isbn = int(input("Enter the ISBN of the book : "))
   user_id = str(input("Enter the id of the user :  "))

   query = ("delete from history where isbn = %s and userid = %s")
   val = (isbn, user_id)

   mycursor.execute(query, val)
   mydb.commit()

   print(mycursor.rowcount, "Book accepted")


# 1&9 Add and Remove a user
class add_rem_User:
    
    #1. Function for adding a user 
    def addUser(self):
        usr_id = int(input("Enter id :"))
        name = str(input("Enter the name :"))
        age = int(input("Enter the age :"))
        phn_no = int(input("Enter phone number : "))
        address = str(input("Enter address : "))

        query = ("insert into user (id, name, age, phn_no, address) values (%s, %s, %s, %s, %s)")
        val = (usr_id, name, age, phn_no, address)

        mycursor.execute(query, val)
        mydb.commit()

        print(mycursor.rowcount, "New user added")

    #9. Function for removing a user
    def remUser(self):
        usr_id = int(input("Enter the id of the user :"))


        query = ("delete from user where id = %s")
        val = (usr_id,)

        mycursor.execute(query, val)
        mydb.commit()
        
        print(mycursor.rowcount, "User deleted")



# 2&10 Add and Remove a book
class add_rem_Book:

    #2. Function for adding a book
    def addBook(self):
        book_id = int(input("Enter the book id : "))
        name = str(input("Enter the name of the book :"))
        books_count = int(input("Enter the number of books present :"))
        isbn = int(input("Enter the isbn number : "))
        author = str(input("Enter the author's name : "))


        query = ("insert into books (book_id, name, books_count, isbn, author) values (%s, %s, %s, %s, %s)")
        val = (book_id, name, books_count, isbn, author)

        mycursor.execute(query, val)
        mydb.commit()

        print(mycursor.rowcount, "Record Inserted")

    #10. Function for removing a book
    def remBook(self):
        isbn = int(input("Enter the isbn of book to be removed :"))
        

        query = ("delete from books where isbn = %s")
        val = (isbn,)
        
        mycursor.execute(query, val)
        mydb.commit()

        print(mycursor.rowcount, "Record Deleted")



# 3 & 6 & 7 & 8 Display Details
class display:

    #3. Function for searching the books in database
    def search(self):
        def book_name():
            bookName = str(input("Enter the name of the book : "))
            query = ("select * from books where name = %s")
            val = (bookName,)

            mycursor.execute(query, val)
            myresult = mycursor.fetchall()

            for book in myresult:
                print(book)

        def isbn():
            number = int(input("Enter the isbn number :"))
            query = ("select * from books where isbn = %s")
            val = (number,)

            mycursor.execute(query, val)
            myresult = mycursor.fetchall()

            for book in myresult:
                print(book)

        def default():
            print("Enter a valid option please")

        book_dict = {1:book_name, 2:isbn}

        def switch(get_inp):
            opt = book_dict.get(get_inp, default)
            opt()

        print("Search a Book\n")
        print("1. Search by Book Name")
        print("2. Search by ISBN\n")
        print("Enter your choice : \n")


        get_inp = int(input())
        switch(get_inp)

    #6. Function for getting history of all members in the databse
    def get_hist(self):
        mycursor.execute("select * from history")

        myresult = mycursor.fetchall()

        for user in myresult:
            print(user)


    #7. Function for displaying whole book database
    def show_db_books(self):

        mycursor.execute("select * from books order by book_id asc")

        myresult = mycursor.fetchall()

        for book in myresult:
            print(book)


    #8. Function for displaying whole user database
    def show_db_users(self):

        mycursor.execute("select * from user")

        myresult = mycursor.fetchall()

        for user in myresult:
            print(user)