from db import * 
# show_db_books, add_rem_Book

#Functions for choosing the desired options

#Adding a user
def add_user():
    add = add_rem_User()
    add.addUser()

#Adding a new book
def add_book():
    add = add_rem_Book()
    add.addBook()

#Search for a book
def srch_book():
    pass

#Issue a book to an existing member
def issue_book():
    pass

#Accepting the book
def accept_book():
    pass

#Display issuing history
def hist():
    pass

#Display details of book
def details_books():
    disp = display()
    disp.show_db_books()

#Display details of user
def details_user():
    disp = display()
    disp.show_db_users()

#Remove a user
def rem_user():
    rem = add_rem_User()
    rem.remUser()

#Remove a book
def rem_book():
    rem = add_rem_Book()
    rem.remBook()

#Incorrect Input
def default():
    print("Incorrect Option")

options = {
    1:add_user,
    2:add_book,
    3:srch_book,
    4:issue_book,
    5:accept_book,
    6:hist,
    7:details_books,
    8:details_user, 
    9:rem_user,
    10:rem_book
}

def switch(opt):
    o = options.get(opt, default)
    o()
    



#Various options of Library Management shown on Command Line when program starts

inp = 'y'
while inp == 'y':
    print("\nWelcome to the Library\n")

    print("1. Add a new user")
    print("2. Add a new book")
    print("3. Search for a book")
    print("4. Issue a book to an existing customer")
    print("5. Accept returned book from member")
    print("6. Display issuing history of members")
    print("7. Display details of books in database")
    print("8. Display details of users in database")
    print("9. Remove a user")
    print("10. Remove a book")
    #Getting input from the user
    print("\nPress the desired option please :\n")

    opt = int(input())
    switch(opt)
    inp = input("Do you wish to continue? (y/n) : ")

