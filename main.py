from db import *
import sys

#Functions for choosing the desired options

#1. Adding a user
def add_user():
    add = add_rem_User()
    add.addUser()

#2. Adding a new book
def add_book():
    add = add_rem_Book()
    add.addBook()

#3. Search for a book
def srch_book():
    srch = display()
    srch.search()

#4. Issue a book to an existing member
def issue_book():
    issue = transaction()
    issue.issueBook()

#5. Accepting the book
def accept_book():
    accept = transaction()
    accept.acceptBook()

#6. Display issuing history
def hist():
    disp = display()
    disp.get_hist()

#7. Display details of book
def details_books():
    disp = display()
    disp.show_db_books()

#8. Display details of user
def details_user():
    disp = display()
    disp.show_db_users()

#9. Remove a user
def rem_user():
    rem = add_rem_User()
    rem.remUser()

#10. Remove a book
def rem_book():
    rem = add_rem_Book()
    rem.remBook()

def end():
    sys.exit()

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
    10:rem_book,
    11:end
}

def switch(opt):
    o = options.get(opt, default)
    o()
    

#Various options of Library Management shown on Command Line when program starts

inp = 'y'
while inp == 'y':
    print("\nWelcome to the Library\n")

    print("1. {}Add a new user".format(' '))
    print("2. {}Add a new book".format(' '))
    print("3. {}Search for a book".format(' '))
    print("4. {}Issue a book to an existing customer".format(' '))
    print("5. {}Accept returned book from member".format(' '))
    print("6. {}Display issuing history of members".format(' '))
    print("7. {}Display details of books in database".format(' '))
    print("8. {}Display details of users in database".format(' '))
    print("9. {}Remove a user".format(' '))
    print("10. Remove a book")
    print("11. Exit")
   
    #Getting input from the user
    print("\nPress the desired option please :\n")

    opt = int(input())
    switch(opt)
    inp = input("Do you wish to continue? (y/n) : ")