import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="password", database="lms")
mycursor = mydb.cursor()

# 1&9 Add and Remove a user
class add_rem_User:
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


    def remUser(self):
        usr_id = int(input("Enter the id of the user :"))


        query = ("delete from user where id = %s")
        val = (usr_id,)

        mycursor.execute(query, val)
        mydb.commit()
        
        print(mycursor.rowcount, "User deleted")



# 2&10 Add and Remove a book
class add_rem_Book:
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

    def remBook(self):
        isbn = int(input("Enter the isbn of book to be removed :"))
        

        query = ("delete from books where isbn = %s")
        val = (isbn,)
        
        mycursor.execute(query, val)
        mydb.commit()

        print(mycursor.rowcount, "Record Deleted")



# 7&8 Display Details of Books Available
class display:

    def show_db_books(self):

        mycursor.execute("select * from books")

        myresult = mycursor.fetchall()

        for book in myresult:
            print(book)

    def show_db_users(self):

        mycursor.execute("select * from user")

        myresult = mycursor.fetchall()

        for user in myresult:
            print(user)