# Lost Reader Database
# Main function execution
# CS2300 Final

import query2.py as sq
import time
import os

def Add_Tuples():
    clear()
    sq.show_database()
    table = int(input("Which table # would you like to add to? [0 to exit]: "))
    
    while table < 0 or table > 9:
        print("Please choose from the available table #")
        sq.show_database()
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
                
                sq.add_librarian(authorization_no,password,name)
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
                
                sq.add_patron(authorization_no,password,name,null)
		case 3:
			id = input("Please enter your librarian ID: ")
            if(validate_staff(id)):
              Media_name = input("Plase enter a media's title/name: ")
			  dewey_dec = input("Plase enter a media's dewey decimal code: ")
			  summary = input("Plase enter a media's summary: ")
			  copies = input("Plase enter number of copies of media that will be stocked: ")
              sq.add_media(dewey_dec,summary,Media_name,1,copies,null,null)
		case 4:
			id = input("Please enter your librarian ID: ")
            if(validate_staff(id)):
              Media_name = input("Plase enter a media's title/name: ")
			  dewey_dec = input("Plase enter a media's dewey decimal code: ")
			  summary = input("Plase enter a media's summary: ")
			  copies = input("Plase enter number of copies of media that will be stocked: ")
              sq.add_media(dewey_dec,summary,Media_name,1,copies,null,null)
			  Author = input("Plase enter the book's author: ")
			  Genre = input("Plase enter the book's genre: ")
			  sq.add_media_book(Author,Genre,dewey_dec)
		case 5:
			id = input("Please enter your librarian ID: ")
            if(validate_staff(id)):
              Media_name = input("Plase enter a media's title/name: ")
			  dewey_dec = input("Plase enter a media's dewey decimal code: ")
			  summary = input("Plase enter a media's summary: ")
			  copies = input("Plase enter number of copies of media that will be stocked: ")
              sq.add_media(dewey_dec,summary,Media_name,1,copies,null,null)
			  Director = input("Plase enter the dvd's Director: ") 
			  Genre = input("Plase enter the dvd's genre: ")
			  sq.add_media_dvd(Director,Genre,dewey_dec)
		case 6:
			id = input("Please enter your librarian ID: ")
            if(validate_staff(id)):
              Media_name = input("Plase enter a media's title/name: ")
			  dewey_dec = input("Plase enter a media's dewey decimal code: ")
			  summary = input("Plase enter a media's summary: ")
			  copies = input("Plase enter number of copies of media that will be stocked: ")
              sq.add_media(dewey_dec,summary,Media_name,1,copies,null,null)
			  sq.add_media_item(dewey_dec)
		case 7:
			id = input("Please enter your librarian ID: ")
            if(validate_staff(id)):
			  dewey_dec = input("Plase enter the media's dewey decimal code: ")
			  Shelf_number  = input("Plase enter the shelf number the media is located: ")
			  Shelf_row = input("Plase enter the shelf row the media is located: ")
			  Cardinal_direction  = input("Plase enter the Cardinal direction the exposed part of the media is facing: ")
			  sq.add_location(Shelf_number, Media_dewey_decimal_code,Shelf_row,Cardinal_direction)
		case 8:
			id = input("Please enter your librarian ID: ")
            if(validate_staff(id)):
				dewey_dec = input("Plase enter the media's dewey decimal code: ")
				due_date = input("Plase enter the media's due date: ")
				sq.add_waitlist(id, dewey_dec, due_date)
		case 9:
			id = input("Please enter your patron ID: ")
            if(validate_member(id)):
			  dewey_dec = input("Plase enter the media's dewey decimal code: ")
			  sq.add_waitlist(id, dewey_dec, 2026-01-01)



def Show_Tables():
    clear()
    sq.show_database()
    table = int(input("Which table # would you like to see? (enter 0 to quit): "))

    while table < 0 or table > 9:
        print("Please choose from the available table #")
        sq.show_database()
        table = int(input("Which table # would you like to see? (enter 0 to quit): "))
    match table:
        case 0:
            clear(  )
            return
        case 1:
            sq.show_librarians()
            okay = input("press ENTER")
            Show_Tables()
        case 2:
            sq.show_patrons()
            okay = input("press ENTER")
            Show_Tables()
        case 3:
            sq.show_media()
            okay = input("press ENTER")
            Show_Tables()
        case 4:
            sq.show_media()
            okay = input("press ENTER")
            Show_Tables()
		case 5:
            sq.show_media()
            okay = input("press ENTER")
            Show_Tables()
		case 6:
            sq.show_media()
            okay = input("press ENTER")
            Show_Tables()
		 case 7:
            sq.show_locations()
            okay = input("press ENTER")
            Show_Tables()
		 case 8:
            sq.show_overdue_flags()
            okay = input("press ENTER")
            Show_Tables()
		 case 9:
            sq.show_waitlists()
            okay = input("press ENTER")
            Show_Tables()


def main():
	Menu()


if __name__ == "__main__":
	main()
