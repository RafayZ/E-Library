#Exercise 3
print("Exercise 3")
print("Welcome to the digital library of Rafay!! ")

import csv
from multiprocessing.sharedctypes import Value
from re import T

BOOK_DATA = []

name = input("Enter the file name to open it: ")
def import_csv_data(name):
    try:
        f = open(name, "r")
    except UnboundLocalError:
        print(f"Unable to find a file named: {name}")
        exit()
    except FileNotFoundError:
        print(f"Unable to find a file named: {name}")
        exit()
    else:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            id = int(row[0].strip())
            title = row[1].strip()
            author = row[2].strip()
            isbn = int(row[3].strip())
            year = row[4].strip()

            BOOK_DATA.append((id, title, author, isbn, year))
        f.close()


import_csv_data(name)

ISBN = [i[3] for i in BOOK_DATA]

def Menu():
    print("\n")
    inp = input("Welcome to the navigation Menu! Please select a valid option \n 1. Display the Library \n 2. Adding a book \n 3. Searching for a book \n 4. Sorting books \n 5. Updating books \n 6. Quit \n Please select:  ")
    if inp == "1":
        print(Display_Data())
    elif inp == "2":
        print(Add_Book())
    elif inp == "3":
        print(Search_Book())
    elif inp == "4":
        print(Sort_Book())
    elif inp == "5":
        print(Update_Book())
    elif inp == "6":
        pass
    else:
        print("Please choose a suitable option.")
        Menu()


#Displaying all the data
def Display_Data():
    print("\n")
    access = "Access Mode"
    B_t = "Book-Title"
    A_Ln = "Author-LastName"
    ISBn = "ISBN"
    P_d = "Publication-Date"
    print('{:30} {:47} {:15} {:17} {:>11}'.format(A_Ln, B_t, ISBn, P_d, access))
    for i in BOOK_DATA:
        print('{:25} {:51} {:6} {:>20} {:13}'.format(i[2], i[1], i[3], i[4], i[0]))
    print("\n")
    Menu()

#Adding a book
def  Add_Book():
    while True:
        inp_ISBN = input("Please enter the unique ISBN (5 digit) to check for duplicate books before adding one: ")
        if len(inp_ISBN) != 5:
            print("Please enter a valid ISBN.")
            temp_var = input("Enter 1 to retry and any other key to Menu: ")
            if temp_var == '1':
                Add_Book()
            else:
                Menu()
        else:
            try:
                inp_ISBN = int(inp_ISBN)
            except ValueError:
                print("Please use digits!")
                continue
            else:
                if int(inp_ISBN) in ISBN:
                    print("The ISBN already exists in the database.")
                    Menu()
                else:
                    while True:
                        A_last = input("Please enter the Author's last name:\t" + "(Should be less then 10 characters)\n-->")
                        if len(A_last) > 10:
                            print("You have entered more then 10 characters! ")
                            continue
                        if not A_last.isalpha():
                            print("Please enter only alphabets!")
                            continue
                        break
                    while True:
                        B_title = input("Please enter the Book title:\t" + "(Should be under 50 characters)\n-->")
                        if len(B_title) > 50:
                            print("You have entered more then 50 characters!")
                            continue
                        break
                    while True:
                        P_date = input("Please enter the publishing date:\t" + "(Should contain 4 digits)\n-->")
                        if len(P_date) != 4:
                            print("Your input is more or less then 4 digits!")
                            continue
                        try:
                            P_date = int(P_date)
                            break
                        except ValueError:
                            print("Please only use digits!")
                    while True:
                        A_mode = input("Please enter the access mode where 1 is Editable and 0 is Can't be edited:\n-->")
                        try:
                            A_mode = int(A_mode)
                        except ValueError:
                            print("Please only enter digits!")
                        else:
                            if A_mode not in [1,0]:
                                print("Please enter only 1 or 0!")
                                continue
                            break
        break
    tuple_create = (A_mode, B_title, A_last, int(inp_ISBN), str(P_date))
    BOOK_DATA.append(tuple_create)
    print('{:30} {:47} {:15} {:17} {:>11}'.format("Author-LastName", "Book-Title", "ISBN", "Publishing-Date", "Access Mode"))
    print('{:25} {:51} {:6} {:>20} {:13}'.format(A_last, B_title, inp_ISBN, P_date, A_mode))
    print("\n")
    print("Book sucessfully added!")

    Menu()

#Searching for a  book
def Search_Book():
    while True:
        input_ISBN = input("Please enter the unique ISBN to search for the book: ")
        if len(str(input_ISBN)) != 5:
            print("Please enter a valid ISBN")
            continue
        break
    try:
        input_ISBN = int(input_ISBN)
    except ValueError:
        print("Please enter only digits!")
        Search_Book()
    else:
        for i in BOOK_DATA:
            if input_ISBN == i[3]:
                print(i)
                print("Your search result ^^^")
                break
        else:
            print("The book linked to that ISBN does not exist in this library!")
            temp_var = input("Enter 1 to retry and any other key to Menu: ")
            if temp_var == "1":
                Search_Book()
            else:
                Menu()
    Menu()        

#Sorting books
def Sort_Book():
    length = len(BOOK_DATA)
    while True:
        upper_year = input("Please enter the upper limit(year): ")
        lower_year = input("Please enter the lower limit(year): ")
        try:
            if len(upper_year) != 4:
                print("Please enter a valid year!")
                continue
            if len(lower_year) != 4:
                print("Please enter a valid year!")
                continue
            upper_year = int(upper_year)
            lower_year = int(lower_year)
            if lower_year > upper_year:
                print("Starting year is more then ending year!")
                continue
        except ValueError:
            print("Please use only digits in your input!")
        else:
            temp_list = []
            for element in range(upper_year, lower_year-1,-1):
                element=str(element)
                for tuples in range(length):
                    if element == BOOK_DATA[tuples][4]:
                        print(BOOK_DATA[tuples])
                        temp_list = [1]
            if len(temp_list) == 0:
                print("No books in sorting range were found")
            break
            

    Menu()

#Updating books
def Update_Book():
    ISBN = [i[3] for i in BOOK_DATA]
    while True:
        input_ISBN = input("Please enter the unique ISBN for the book to be updated: ").strip()
        if len(input_ISBN) != 5:
            print("Please enter a valid ISBN")
            continue
        break
    try:
        input_ISBN = int(input_ISBN)
    except ValueError:
        print("Please only enter digits!")
    else:
        if int(input_ISBN) in ISBN:
            for element in BOOK_DATA:
                if int(input_ISBN) == element[3]:
                    record = element
                    if element[0] == 0:
                        print("Access denied! The contents of this book can not be edited.")
                        temp_var = input("Enter 1 to retry and any other key to Menu: ")
                        if temp_var == "1":
                            Update_Book()
                        else:
                            Menu()
                    elif element[0] == 1:
                        while True:
                            A_last = input("Please enter the Author's last name:\t" + "(Should be less then 10 characters)\n-->")
                            if len(A_last) > 10:
                                print("You have entered more then 10 characters! ")
                                continue
                            if not A_last.isalpha():
                                print("Please enter only alphabets!")
                                continue
                            break
                        while True:
                            B_title = input("Please enter the Book title:\t" + "(Should be under 50 characters)\n-->")
                            if len(B_title) > 50:
                                print("You have entered more then 50 characters!")
                                continue
                            break
                        while True:
                            P_date = input("Please enter the publishing date:\t" + "(Should contain 4 digits)\n-->")
                            if len(P_date) != 4:
                                print("Your input is more or less then 4 digits!")
                                continue
                            try:
                                P_date = int(P_date)
                                break
                            except ValueError:
                                print("Please only use digits!")
                        temp_tuple = (1, B_title, A_last, input_ISBN, P_date)
                        index = BOOK_DATA.index(element)
                        BOOK_DATA[index] = temp_tuple
                        print("Book details updated sucessfully! ")
        else:
            print("ISBN was not found in database.")
    Menu()
#Quitting the program
def Quit():
    print("Thank you for using the program!!")
    quit=True

while True:
    Menu()
    print("Thank you for using this program!!")
    break
