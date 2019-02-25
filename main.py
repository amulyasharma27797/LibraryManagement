from db import show_db

#Functions for choosing the desired options

#Adding a user
def add_user():
    pass

#Adding a new book
def add_book():
    pass 

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
def details():
    print(show_db())

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
    7:details
}

def switch(opt):
    print("in switch")
    
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

    #Getting input from the user
    print("\nPress the desired option please :\n")

    opt = int(input())
    switch(opt)
    inp = input("Do you wish to continue? (y/n) : ")

