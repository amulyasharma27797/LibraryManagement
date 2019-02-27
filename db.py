from datetime import datetime, timedelta
import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="password", database="lms")
mycursor = mydb.cursor()

# global due 
due = datetime.now().date() + timedelta(days=7)


#4 & 5 Issue and Accept a Book
class transaction():
    # global due 
    #Issuing a book   
    def issueBook(self):
        isbn = int(input("Enter the ISBN of the book : "))
        user_id = str(input("Enter the id of the user :  "))
        issue = datetime.now().date()
        
        # global due 
        # due = datetime.now().date() + timedelta(days=7)

        #Getting and updating count of books available in the database
        query0 = ("select books_count from books where isbn = %s")
        val0 = (isbn,)
        mycursor.execute(query0, val0)
        myresult = mycursor.fetchall()
        get_count = myresult[0][0]
        # print(get_count)
        if get_count > 0:
            get_count = get_count - 1 
            query = ("update books set books_count = %s where isbn = %s")
            val = (get_count,isbn)
            mycursor.execute(query, val)
            mydb.commit()
        else:
            print("Book not available")

        #Issuing the book to the user and maintaining the log
        query = ("insert into history(isbn, userid, issue_date, due_date) values(%s, %s, %s, %s)")
        val = (isbn, user_id, issue, due)

        mycursor.execute(query, val)
        mydb.commit()

        print(mycursor.rowcount, "Book issued")

    #Accepting a book
    def acceptBook(self):
        isbn = int(input("Enter the ISBN of the book : "))
        user_id = str(input("Enter the id of the user :  "))


        #Getting and updating count of books available in the database
        query0 = ("select books_count from books where isbn = %s")
        val0 = (isbn,)
        mycursor.execute(query0, val0)
        myresult = mycursor.fetchall()
        get_count = myresult[0][0]

        get_count = get_count + 1 
        query = ("update books set books_count = %s where isbn = %s")
        val = (get_count,isbn)
        mycursor.execute(query, val)
        mydb.commit()

        #Calculation of fine
        return_date = datetime.now().date()
        
        # return_date = datetime.now().date()
        if return_date > due:
            days = return_date - due
            fine = days.day * 5
            print("Your fine is :" + fine)
        else:
            print("Thanks for returning")
        
        #Deleting history from the database
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
        
        #Searching by book name
        def book_name():
            bookName = str(input("Enter the name of the book : "))
            query = ("select * from books where name = %s")
            val = (bookName,)

            mycursor.execute(query, val)
            myresult = mycursor.fetchall()

            for book in myresult:
                print(book)

        #Searching through ISBN
        def isbn():
            number = int(input("Enter the isbn number :"))
            query = ("select * from books where isbn = %s")
            val = (number,)

            mycursor.execute(query, val)
            myresult = mycursor.fetchall()

            for book in myresult:
                print(book)

        #Searching by author's name
        def author():
            author_name = str(input("Enter the name of author : "))
            query = ("select * from books where author = %s")
            val = (author_name,)

            mycursor.execute(query, val)
            myresult = mycursor.fetchall()

            for book in myresult:
                print(book)

        #Incorrect Input
        def default():
            print("Enter a valid option please")

        #Dict used for search referencing
        book_dict = {1:book_name, 2:isbn, 3:author}


        def switch(get_inp):
            opt = book_dict.get(get_inp, default)
            opt()

        print("Search a Book\n")
        print("1. Search by Book Name")
        print("2. Search by ISBN\n")
        print("3. Search by Author\n")
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