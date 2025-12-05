import mysql.connector
import random
from enum import Enum

#code notes :
# entering "0" results in moving back one step
# only 2 types of login accounts

# connection to MySQL server
connection = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "LostReadersDatabase",
	database = "Library_Database_Phase3"
)

mycursor = connection.cursor()

def login():
	id_exists = 0
	#choose type: librarian or patron
	id_type = input("Please enter '1' for Patron Login or '2' for Librarian Login: ")
	while id_exists == 0:
		id = input("Please enter your ID (enter '0' to quit): ")
		if id == '0':
			quit()
		if id_type == '1':
			mycursor.execute("SELECT * FROM Patron WHERE Member_id = (%s)", (id,))
			for x in mycursor:
				id_exists += 1

		if id_type == '2':
			mycursor.execute("SELECT * FROM Librarian WHERE Admin_id = (%s)", (id,))
			for x in mycursor:
				id_exists += 1
		if id_exists == 0:
			print("ID does not exist. Please enter valid ID.")
	#now check password
	pswd_check = 0
	while pswd_check == 0:
		pswd = input("Please enter your password (enter 0 to quit): ")
		if pswd == '0':
			quit()
		if id_type == '1':
			mycursor.execute("SELECT * FROM Patron WHERE Member_id = (%s) AND Patron_password = (%s)", (id, pswd))
			for x in mycursor:
				pswd_check += 1
		if id_type == '2':
			mycursor.execute("SELECT * FROM Librarian WHERE Admin_id = (%s) AND Librarian_password = (%s)", (id, pswd))
			for x in mycursor:
				pswd_check += 1
		if pswd_check == '0':
			print("Password is inncorrect. Please try again. ")



def show_database():
	print("Showing Database Tables: ")

#printing Librarian table
	print("Librarian:")
	table = mycursor.execute("""
		select *
		from Librarian;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
	print(row)

#printing Patron table
	print("\nPatron:")
	table = mycursor.execute("""
		select *
		from Patron;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

#printing Media table
	print("\nMedia:")
	table = mycursor.execute("""
		select *
		from Media;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)
#printing Media_book table
	print("\nMedia_book:")
	table = mycursor.execute("""
		select *
		from Media_book;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

#printing Media_dvd table
	print("\nMedia_dvd:")
	table = mycursor.execute("""
		select *
		from Media_dvd;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

#printing Media_item table
	print("\nMedia_item:")
	table = mycursor.execute("""
		select *
		from Media_item;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)
#printing Location table
	print("\nLocation:")
	table = mycursor.execute("""
		select *
		from Location;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

#printing Edit table
	print("\nEdit:")
	table = mycursor.execute("""
		select *
		from Edit;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

#printing Overdue_flag table
	print("\nOverdue_flag:")
	table = mycursor.execute("""
		select *
		from Overdue_flag;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

#printing Waitlist table
	print("\nWaitlist:")
	table = mycursor.execute("""
		select *
		from Waitlist;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

def show_patrons():
	print("Patrons:")
	table = mycursor.execute("""
		select Patron_name, Member_id, Wishlist
		from Patron;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

def show_librarians():
	print("Librarians:")
	table = mycursor.execute("""
		select Librarian_name, Admin_id
		from Librarian;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

def show_media():
	print("Showing Media by Type:")

# printing table of books
	print("Books:")
	table = mycursor.execute("""
		select Media_book.Dewey_decimal_code, Media.Media_name, Media_book.Author, Media_book.Genre, Media.Availability, Medi$
		from Media, Media_book
		where Media.Dewey_decimal_code = Media_book.Dewey_decimal_code;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

# printing table of dvds
	print("Dvds:")
	table = mycursor.execute("""
		select Media_dvd.Dewey_decimal_code, Media.Media_name, Media_dvd.Director, Media_dvd.Genre, Media.Availability, Media$
		from Media, Media_dvd
		where Media.Dewey_decimal_code = Media_dvd.Dewey_decimal_code;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

# printing table of items
	print("Items:")
	table = mycursor.execute("""
		select Media_item.Dewey_decimal_code, Media.Media_name, Media.Availability, Media.Copies
		from Media, Media_item
		where Media.Dewey_decimal_code = Media_item.Dewey_decimal_code;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

def show_attributes(table_name):
	mycursor.execute("SHOW COLUMNS FROM {}".format(table_name))
	print("Attributes")
	for x in mycursor:
		print(x)

#do we even need this? it is techically the search fuction



def show_wishlist():
#needs done

def show_waitlist():
	print("Waitlist:")
	table = mycursor.execute("""
		select Media.Dewey_decimal_code, Media.Media_name, Patron.Patron_name, Patron.Member_id, Media.Due_date
		from Media, Patron, Waitlist
		where Media.Dewey_decimal_code = Waitlist.Dewey_decimal_code and Patron.Member_id = Waitlist.Patron_id
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

        
def overdue_flag():
#needs done

def add_media(DDC, Summary, Media_name, Availability, Copies, Due_date, Member_id):
#needs done

def add_patron(Member_id, Patron_password, Patron_name, Wishlist):
#needs done

def add_librarian(Admin_id, Librarian_password, Librarian_name):
#needs done

def reserve_media():
#needs done


def checkout_media():
	dewey_decimal_code = input("Please enter the Dewey decimal code of the item you would like to check out: ")
#checking if item exists
	mycursor.execute("""
		select Dewey_decimal_code
		from Media
		where Media.Dewey_decimal_code = %s""", (dewey_decimal_code,))
	table = mycursor.fetchall()
	if not table:
		print("Item not found")
		return
#checking if item is available
	mycursor.execute("""
		select Availability
		from Media
		where Media.Dewey_decimal_code = %s""", (dewey_decimal_code,))
	availability = mycursor.fetchone()[0]
	if availability == 1:
		member_id = input("Please enter your Member ID: ")
#validating member id
		mycursor.execute("""
			select Member_id
			from Patron
			where Patron.Member_id = %s""", (member_id,))
		id = mycursor.fetchall()
		if not id:
			print("Member ID not found.")
			return
		today = date.today()
		due = today + timedelta(days = 21)
		mycursor.execute("""
			update Media
			set Availability = 0, Due_date = %s, Member_id = %s
			where Dewey_decimal_code = %s""", (due, member_id, dewey_decimal_code))
		connection.commit()
		mycursor.execute("""
			select Dewey_decimal_code, Media_name, Due_date, Member_id
			from Media
			where Media.Dewey_decimal_code = %s""", (dewey_decimal_code,))
		table_info = mycursor.fetchall()
		for row in table_info:
			print(row)
		print("Is this the item you want to check out?")
		option = input("(y - Yes, n - No)") 
if (option == "y") or (option == "Y"):
			print("You checked out: ")
			for row in table_info:
				print(row)
			print("This item will be due:", due)
		else:
			return

	else:	   
		print("Sorry, this item is not available for checkout at this time. Would you like to reserve this item?")
		reserve_media() #not finished



def return_media():
#needs done


def edit_password():
#needs done


def edit_location():
#needs done


def edit_waitlist():
#needs done


def edit_wishlist():
#needs done


def delete_media(condition : str):
#needs done


def delete_patron(condition : str):
	try:
		mycursor.execute("DELETE FROM Patron WHERE {}".format(condition))
		db.commit()
	except mysql.connector.errors.IntegrityError or mysql.connector.errors.ProgrammingError as err:
		print(err)
		end = input("Press Enter to continue..." )
		return err
	mycursor.execute("SELECT * FROM Librarian")
	for x in mycursor:
		print(x)
	del_finished = input("Database updated. Press Enter to continue... ")



def delete_librarian():
#needs done

        
#aggregate functions below
#media_type is 1, 2, or 3. 1 = book, 2 = dvd, and 3 = item
def get_sum_media_type(media_type):
# sum of books
	if media_type == 1:
		table = mycursor.execute("""
			select sum(copies)
			from Media, Media_book
			where Media.Dewey_decimal_code = Media_book.Dewey_decimal_code;
			""")
		result = mycursor.fetchone()[0]

# sum of dvds
	elif media_type == 2:
		table = mycursor.execute("""
			select sum(copies)
			from Media, Media_dvd
			where Media.Dewey_decimal_code = Media_dvd.Dewey_decimal_code;
			""")
		result = mycursor.fetchone()[0]

# sum of items
	elif media_type == 3:
		table = mycursor.execute("""
			select sum(copies)
			from Media, Media_item
			where Media.Dewey_decimal_code = Media_item.Dewey_decimal_code;
			""")
		result = mycursor.fetchone()[0]
	return result

def get_sum_media():
	sum_books = get_sum_media_type(1)
	sum_dvds = get_sum_media_type(2)
	sum_items = get_sum_media_type(3)
	total = sum_books + sum_dvds + sum_items
	print("The total number of media (books/dvds/items) in the library is:", total)

def get_sum_available():
	table = mycursor.execute("""
		select sum(Availability)
		from Media;
		""")
	total = mycursor.fetchone()[0]
	print("The total number of media (books/dvds/items) available for checkout in the library is:", total)


def locate_media(media_info, dewey_decimal_index):
	dewey_decimal_code = media_info[dewey_decimal_index]
	media_location_table = mycursor.execute("""
		select Media.Dewey_decimal_code, Location.Shelf_number, Location.Shelf_row, Location.Cardinal_direction
		from Media, Location
		where Media.Dewey_decimal_code = Location.Media_dewey_decimal_code and Media.Dewey_decimal_code = %s""", (dewey_decimal_code,))
	location_info = mycursor.fetchall()
	print("Location is: ", location_info)

def search_media():
	correct = "0" #to be used in input validation later
	print("What would you like to search by? \nSearch Menu: \n1 - Dewey Decimal Code \n2 - Title/Name \n3 - Genre (Book and Dvd only) \n4 - Author/Director (Book and Dvd only) \n5 - Quit (or press any key)")
	option = input("Please enter the number of the search method you would like to use: ")
#searching by dewey decimal code
	if option == "1":
		Dewey_decimal_code = input("Please enter the Dewey decimal code of the media you are searching for: ")
		print("Searching by Dewey decimal code:")
		table = mycursor.execute("""
			select Dewey_decimal_code, Media_name, Availability, Copies, Summary
			from Media
			where Media.Dewey_decimal_code = %s""", (Dewey_decimal_code,))
		table_info = mycursor.fetchall()
		if not table_info:
			print("Item not found. Please ensure the Dewey decimal code was entered correctly.")
		else:
			for row in table_info:
				print(row)

		while (correct != "y") and (correct != "n") and (correct != "Y") and (correct != "N"):
			correct = input("Is this the media you were looking for? (y - Yes, n - No) ")
		if (correct == "y") or (correct == "Y"):
			locate_media(table_info[0], 0)
		else:
			print("Returning to search menu...\n")
			search_media()
#searching by title
	elif option == "2":
		media_name = input("Please enter the title/name of the media you are searching for: ")
		print("Searching by title:")
		table = mycursor.execute("""
			select Dewey_decimal_code, Media_name, Availability, Copies, Summary
			from Media
			where Media_name = %s""", (media_name,))
		table_info = mycursor.fetchall()
		if not table_info:
			print("Item not found. Please ensure the title/name was entered correctly.")
		else:
			num = 1
			for row in table_info:
				print(num, row)
				num += 1
		selection = 1
		if len(table_info) > 1:
			while True:
				try:
					selection = int(input("Please enter the number of the media you want to know the location of: "))
					break
				except ValueError:
					print("Invalid input")
			print(table_info[selection - 1])
					
		while (correct != "y") and (correct != "n") and (correct != "Y") and (correct != "N"):
			correct = input("Is this the media you were looking for? (y - Yes, n - No) ")
		if (correct == "y") or (correct == "Y"):
			locate_media(table_info[selection - 1], 0)
		else:
			print("Returning to search menu...\n")
			search_media()
				
			
#searching by genre
	elif option == "3":
		media_type = input("Please enter the type of media you are searching for (1 = Book, 2 = Dvd): ")
		print("Searching by genre: ")
#searching books
		if media_type == "1":
			genre =  input("Please enter the genre you are looking for: ")
			table = mycursor.execute("""
				select Media_book.Genre, Media.Dewey_decimal_code, Media.Media_name, Media.Availability, Media.Copies, Media.Summary
				from Media_book, Media
				where Media_book.Dewey_decimal_code = Media.Dewey_decimal_code and Media_book.Genre = %s""", (genre,))
			table_info = mycursor.fetchall()
			if not table_info:
				print("Item not found. Please ensure the genre was entered correctly.")
			else:
				num = 1
				for row in table_info:
					print(num, row)
					num += 1
			
#searching dvds
		elif media_type == "2":
			genre = input("Please enter the genre you are looking for: ")
			table =  mycursor.execute("""
				select Media_dvd.Genre, Media.Dewey_decimal_code, Media.Media_name, Media.Availability, Media.Copies, Media.Summary
				from Media_dvd, Media
				where Media.Dewey_decimal_code = Media_dvd.Dewey_decimal_code and Media_dvd.Genre = %s""", (genre,))
			table_info = mycursor.fetchall()
			if not table_info:
				print("Item not found. Please ensure the genre was entered correctly.")
			else:
				num = 1
				for row in table_info:
					print(num, row)
					num += 1
			
		else:
			print("Invalid input")
				
		selection = 1
		if len(table_info) > 1:   
			while True:
				try:
					selection = int(input("Please enter the number of the media you want to know the location of: "))
					break
				except ValueError:
					print("Invalid input")
			print(table_info[selection - 1])
		while (correct != "y") and (correct != "n") and (correct != "Y") and (correct != "N"):
			correct = input("Is this the media you were looking for? (y - Yes, n - No) ")
		if (correct == "y") or (correct == "Y"):
			locate_media(table_info[selection - 1], 1)
		else:
			print("Returning to search menu...\n")
			search_media()
			
#searching by author/director
	elif option == "4":  
		media_type = input("Please enter the type of media you are searching for (1 = Book, 2 = Dvd): ")
#searching books
		if media_type == "1":
			author = input("Please enter the author you are looking for: ")
			table = mycursor.execute("""
				select Media_book.Author, Media.Dewey_decimal_code, Media.Media_name, Media.Availability, Media.Copies, Media.Summary
				from Media_book, Media
				where Media_book.Dewey_decimal_code = Media.Dewey_decimal_code and Media_book.Author = %s""", (author,))
			table_info = mycursor.fetchall()
			if not table_info:
				print("Item not found. Please ensure the author name was entered correctly.")
			else:
				num = 1
				for row in table_info:
					print(num, row)
					num += 1
#searching dvds
		elif media_type == "2":
			author = input("Please enter the director you are looking for: ")
			table = mycursor.execute("""
				select Media_dvd.Director, Media.Dewey_decimal_code, Media.Media_name, Media.Availability, Media.Copies, Media.Summary
				from Media_dvd, Media
				where Media_dvd.Dewey_decimal_code = Media.Dewey_decimal_code and Media_dvd.Director = %s""", (author,))
			table_info = mycursor.fetchall()
			if not table_info:
				print("Item not found. Please ensure the director name was entered correctly.")
			else:
				num = 1
				for row in table_info:
					print(num, row)
					num += 1
		else:	   
			print("Invalid input")

		selection = 1   
		if len(table_info) > 1:
			while True:
				try:
					selection = int(input("Please enter the number of the media you want to know the location of: "))
					break
				except ValueError:
					print("Invalid input")
			print(table_info[selection - 1])
			
		while (correct != "y") and (correct != "n") and (correct != "Y") and (correct != "N"):
			correct = input("Is this the media you were looking for? (y - Yes, n - No) ")
		if (correct == "y") or (correct == "Y"):
			locate_media(table_info[selection - 1], 1)
		else:   
			print("Returning to search menu...\n")
			search_media()
			
	elif option == "5":     
		return
					
		     






