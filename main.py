# Lost Reader Database
# Main function execution
# CS2300 Final

import sql_query.py as sq
import time
import os

def Add_Tuples():
    clear()
    sq.Show_Database()
    table = int(input("Which table # would you like to add to? [0 to exit]: "))
    
    while table < 0 or table > 9:
        print("Please choose from the available table #")
        sq.Show_Database()
        table = int(input("Which table # would you like to see?: "))
    match table:
        case 0:
            return
        case 1:
            name = input("Please enter your name: ")
            password = input("Plase enter a password: ")
            if password != 0:
                authorization_no = 5
                count = 0
                for i in authorization_lists:
                    count +=1
                    print( "{}. ".format(count) + i)
                while authorization_no not in range(0,4):
                    authorization_no = int(input("Please enter ID number:"))
                
                sq.Add_Librarian(authorization_no,password,name)
		case 2:
            name = input("Please enter your name: ")
            password = input("Plase enter a password: ")
            if password != 0:
                authorization_no = 5
                count = 0
                for i in authorization_lists:
                    count +=1
                    print( "{}. ".format(count) + i)
                while authorization_no not in range(0,4):
                    authorization_no = int(input("Please enter ID number:"))
                
                sq.Add_Patron(authorization_no,password,name,null)
		case 3:
			id = input("Please enter your librarian ID: ")
            #if ID in librarian IDs
            Media_name = input("Plase enter a media's title/name: ")
			dewey_dec = input("Plase enter a media's dewey decimal code: ")
			summary = input("Plase enter a media's summary: ")
			copies = input("Plase enter number of copies of media that will be stocked: ")
            sq.Add_Media(dewey_dec,summary,Media_name,1,copies,null,null)
		case 4:
			id = input("Please enter your librarian ID: ")
            #if ID in librarian IDs
            Media_name = input("Plase enter a media's title/name: ")
			dewey_dec = input("Plase enter a media's dewey decimal code: ")
			summary = input("Plase enter a media's summary: ")
			copies = input("Plase enter number of copies of media that will be stocked: ")
            sq.Add_Media(dewey_dec,summary,Media_name,1,copies,null,null)
			Author = input("Plase enter the book's author: ")
			    Genre = input("Plase enter the book's genre: ")
			    sq.Add_Media_Book(Author,Genre,dewey_dec)
		case 5:
			id = input("Please enter your librarian ID: ")
            #if ID in librarian IDs
            Media_name = input("Plase enter a media's title/name: ")
			dewey_dec = input("Plase enter a media's dewey decimal code: ")
			summary = input("Plase enter a media's summary: ")
			copies = input("Plase enter number of copies of media that will be stocked: ")
            sq.Add_Media(dewey_dec,summary,Media_name,1,copies,null,null)
			Director = input("Plase enter the dvd's Director: ") 
				Genre = input("Plase enter the dvd's genre: ")
				sq.Add_Media_dvd(Director,Genre,dewey_dec)
		case 6:
			id = input("Please enter your librarian ID: ")
            #if ID in librarian IDs
            Media_name = input("Plase enter a media's title/name: ")
			dewey_dec = input("Plase enter a media's dewey decimal code: ")
			summary = input("Plase enter a media's summary: ")
			copies = input("Plase enter number of copies of media that will be stocked: ")
            sq.Add_Media(dewey_dec,summary,Media_name,1,copies,null,null)
			sq.Add_Media_item(dewey_dec)



def Show_Tables():
    clear()
    sq.Show_Database()
    table = int(input("Which table # would you like to see? (enter 0 to quit): "))

    while table < 0 or table > 4:
        print("Please choose from the available table #")
        sq.Show_Database()
        table = int(input("Which table # would you like to see? (enter 0 to quit): "))
    match table:
        case 0:
            clear(  )
            return
        case 1:
            sq.Show_Librarians()
            okay = input("press ENTER")
            Show_Tables()
        case 2:
            sq.Show_Patrons()
            okay = input("press ENTER")
            Show_Tables()
        case 3:
            sq.Show_Media()
            okay = input("press ENTER")
            Show_Tables()
        case 4:
            sq.Show_Media_Books()
            okay = input("press ENTER")
            Show_Tables()
		case 5:
            sq.Show_Media_dvds()
            okay = input("press ENTER")
            Show_Tables()
		case 6:
            sq.Show_Media_item()
            okay = input("press ENTER")
            Show_Tables()
		 case 7:
            sq.Show_Locations()
            okay = input("press ENTER")
            Show_Tables()
		 case 8:
            sq.Show_Overdue_flags()
            okay = input("press ENTER")
            Show_Tables()
		 case 9:
            sq.Show_Waitlists()
            okay = input("press ENTER")
            Show_Tables()
		
        case 0:
            return 0


def main():
	Menu()


if __name__ == "__main__":
	main()
