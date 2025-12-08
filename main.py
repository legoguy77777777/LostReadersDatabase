# Lost Reader Database
# Main function execution
# CS2300 Final

import query2 as sq
import time
import os

authorization_lists = ('Patron', 'Admin')

def Add_Tuples():
	sq.show_database()
	table = int(input("Which table # would you like to add to? [0 to exit]: "))
	while table < 0 or table > 9:
		print("Please choose from the available table #")
		sq.show_database()
		table = int(input("Which table # would you like to see?: "))
	match table:
		case 0: #quit
			return
		case 1: #add librarian
			name = input("Please enter your name: ")
			password = input("Plase enter a password: ")
			if password == '0':
				quit()
			authorization_no = None
			count = 0
			for i in authorization_lists:
				count +=1
				#print( "{}. {}".format(count, i))
			while authorization_no in range(1, count + 1):
				try:
					authorization_no = int(input("Please enter ID number:"))
				except ValueError:
					print("Please enter valid number... ")
			sq.add_librarian(authorization_no,password,name)
		case 2: #add patron
			name = input("Please enter your name: ")
			password = input("Plase enter a password: ")
			if password != 0:
				authorization_no = 5
				count = 0
				for i in authorization_lists:
					count +=1
					#print( "{}. ".format(count) + i)
				while authorization_no in range(0,4):
					authorization_no = int(input("Please enter ID number:"))
				sq.add_patron(authorization_no,password,name,null)
		case 3: #add media
			id = input("Please enter your librarian ID: ")
			if(sq.validate_staff(id)):
				Media_name = input("Plase enter a media's title/name: ")
				dewey_dec = input("Plase enter a media's dewey decimal code: ")
				summary = input("Plase enter a media's summary: ")
				copies = input("Plase enter number of copies of media that will be stocked: ")
				sq.add_media(dewey_dec,summary,Media_name,1,copies)
		case 4: #add media_books (adds to media)
			id = input("Please enter your librarian ID: ")
			if(sq.validate_staff(id)):
				Media_name = input("Plase enter a media's title/name: ")
				dewey_dec = input("Plase enter a media's dewey decimal code: ")
				summary = input("Plase enter a media's summary: ")
				copies = input("Plase enter number of copies of media that will be stocked: ")
				sq.add_media(dewey_dec,summary,Media_name,1,copies,null,null)
				Author = input("Plase enter the book's author: ")
				Genre = input("Plase enter the book's genre: ")
				sq.add_media_book(Author,Genre,dewey_dec)
		case 5: #add media_dvds (adds to media)
			id = input("Please enter your librarian ID: ")
			if(sq.validate_staff(id)):
				Media_name = input("Plase enter a media's title/name: ")
				dewey_dec = input("Plase enter a media's dewey decimal code: ")
				summary = input("Plase enter a media's summary: ")
				copies = input("Plase enter number of copies of media that will be stocked: ")
				sq.add_media(dewey_dec,summary,Media_name,1,copies,null,null)
				Director = input("Plase enter the dvd's Director: ") 
				Genre = input("Plase enter the dvd's genre: ")
				sq.add_media_dvd(Director,Genre,dewey_dec)
		case 6: #add media_items (adds to media)
			id = input("Please enter your librarian ID: ")
			if(sq.validate_staff(id)):
				Media_name = input("Plase enter a media's title/name: ")
				dewey_dec = input("Plase enter a media's dewey decimal code: ")
				summary = input("Plase enter a media's summary: ")
				copies = input("Plase enter number of copies of media that will be stocked: ")
				sq.add_media(dewey_dec,summary,Media_name,1,copies,null,null)
				sq.add_media_item(dewey_dec)
		case 7: #add location
			id = input("Please enter your librarian ID: ")
			if(sq.validate_staff(id)):
				dewey_dec = input("Plase enter the media's dewey decimal code: ")
				Shelf_number  = input("Plase enter the shelf number the media is located: ")
				Shelf_row = input("Plase enter the shelf row the media is located: ")
				Cardinal_direction  = input("Plase enter the Cardinal direction the exposed part of the media is facing: ")
				sq.add_location(Shelf_number, dewey_dec,Shelf_row,Cardinal_direction)
		case 8: #add waitlist
			id = input("Please enter their patron ID: ")
			if(sq.validate_patron(id)):
				dewey_dec = input("Plase enter the media's dewey decimal code: ")
				due_date = input("Plase enter the media's due date: ")
				sq.add_waitlist(id, dewey_dec, due_date)



def Show_Tables():
	clear()
	sq.show_database()
	table = int(input("Which table # would you like to see? (enter 0 to quit): "))
	while table < 0 or table > 9:
		print("Please choose from the available table #")
		sq.show_database()
		table = int(input("Which table # would you like to see? (enter 0 to quit): "))
	match table:
		case 0: #quit
			return
		case 1: #show libraians
			sq.show_librarians()
			okay = input("press ENTER")
			Show_Tables()
		case 2: #show patrons
			sq.show_patrons()
			okay = input("press ENTER")
			Show_Tables()
		case 3:  #show media
			sq.show_media()
			okay = input("press ENTER")
			Show_Tables()
		case 4:  #show media
			sq.show_media()
			okay = input("press ENTER")
			Show_Tables()
		case 5:  #show media
			sq.show_media()
			okay = input("press ENTER")
			Show_Tables()
		case 6:  #show media
			sq.show_media()
			okay = input("press ENTER")
			Show_Tables()
		case 7: #show media locations
			sq.show_locations()
			okay = input("press ENTER")
			Show_Tables()
		case 8: #show overdue flags
			sq.show_overdue_flags()
			okay = input("press ENTER")
			Show_Tables()
		case 9: #show waitlist
			sq.show_waitlists()
			okay = input("press ENTER")
			Show_Tables()

def Delete_Tables():
	print("What would you like to delete? \nMenu: \n1 - Media information \n2 - Patron information \n3 - Librarian information \n0 - Quit")
	menuFunct = int(input("Please enter the number of the menu option you would like to use: "))
	while menuFunct < 0 or menuFunct > 3:
		print("Please choose from the available option #")
		print("What would you like to delete? \nMenu: \n1 - Media information \n2 - Patron information \n3 - Librarian information \n0 - Quit")
		menuFunct = int(input("Please enter the number of the menu option you would like to use: "))
	match menuFunct:
		case 0: #quit
			return
		case 1: #delete media
			dewey_dec = input("Plase enter the media's dewey decimal code: ")
			okay = input("Are you sure? (y/n): ")
			if(okay == "y"):
				sq.delete_media(dewey_dec)
		case 2: #delete patron
			id = input("Please enter the patron ID: ")
			okay = input("Are you sure? (y/n): ")
			if(okay == "y"):
				sq.delete_patron(id)
		case 3: #delete librarian
			id = input("Please enter the librarian ID: ")
			okay = input("Are you sure? (y/n): ")
			if(okay == "y"):
				sq.delete_librarian(id)



def main():
	cont = "y"
	innerCont = "y"
	while(cont == "y"):
		print("Are you a: \n1 - Patron \n2 - Librarian \n3 - New Patron \n4 - New Admin \n0 - Quit")
		menuFunct = int(input("Please enter the number of the menu option you would like to use: "))
		match menuFunct:
			case 0: #quit
				break
			case 1: #patron
				sq.login()
				innerCont == "y"
				while(innerCont == "y"):
					print("What would you like to do? \nPatron Menu: \n1 - Search media \n2 - Locate media \n3 - Reserve media \n4 - Checkout media \n5 - View waitlist \n6 - Delete item from waitlist \n7 - Edit password \n0 - Quit")
					patronFunct = int(input("Please enter the number of the menu option you would like to use: "))
					match patronFunct:
						case 0: #quit
							break
						case 1: #search media
							sq.search_media()
						case 2: #locate media
							dewey_dec = input("Plase enter a media's dewey decimal code: ")
							sq.locate_media(dewey_dec)
						case 3: #reserve media
							sq.reserve_media()
						case 4: #checkout media
							sq.checkout_media()
						case 5: #show waitlist
							id = input("Please enter your patron ID: ")
							if(validate_member(id)):
								sq.show_waitlist(id)
						case 6: #delete waitlist item
							id = input("Please enter your patron ID: ")
							if(validate_member(id)):
								dewey_dec = input("Plase enter the media's dewey decimal code: ")
								sq.delete_waitlist(dewey_dec)
						case 7: #edit password
							sq.edit_password()
					innerCont = input("Would you like to continue (y/n): ")
			case 2: #librarian
				sq.login()
				innerCont == "y"
				while(innerCont == "y"):
					print("What would you like to do? \nAdmin Menu: \n1 - Return media \n2 - Edit media location \n3 - Add media into system \n4 - Delete elements from system \n5 - View overdue book \n6 - View media inventory \n7 - Edit password \n0 - Quit")
					adminFunct = int(input("Please enter the number of the menu option you would like to use: "))
					match adminFunct:
						case 0: #quit
							break
						case 1: #log returned media
							sq.return_media()
						case 2: #edit media location
							sq.edit_location()
						case 3: #add to the system
							Add_Tuples()
						case 4: #delete from the system
							Delete_Tables()
						case 5: #view overdue flags
							sq.show_overdue_flags()
						case 6: #view library inventory numbers
							print(sq.get_sum_available())
							print(sq.get_sum_media())
							print("Would you like to see how many books(1), dvds(2), or other itmes(3) there are: ")
							type = int(input("Please enter the number of the menu option you would like to use: "))
							print(sq.get_sum_media_type(type))
						case 7: #edit password
							sq.edit_password()
					innerCont = input("Would you like to continue (y/n): ")
			case 3: #new patron
				name = input("Please enter your name: ")
				password = input("Plase enter a password: ")
				if password != 0:
					authorization_no = 5
					count = 0
					for i in authorization_lists:
						count +=1
						#print( "{}. ".format(count) + i)
					while authorization_no in range(0,4):
						authorization_no = int(input("Please enter ID number:"))
					sq.add_patron(authorization_no,password,name,"null")
			case 4: #new librarian
				name = input("Please enter your name: ")
				password = input("Plase enter a password: ")
				if password != 0:
					authorization_no = 5
					count = 0
					for i in authorization_lists:
						count +=1
						#print( "{}. ".format(count) + i)
					while authorization_no in range(0,4):
						authorization_no = int(input("Please enter ID number:"))
					sq.add_librarian(authorization_no,password,name)
		cont = input("Would you like to continue (y/n): ")
			

if __name__ == "__main__":
	main()
