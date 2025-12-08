import mysql.connector
import random
from datetime import date
from datetime import timedelta
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
	print("1 Librarian:")
	table = mycursor.execute("""
		select *
		from Librarian;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

#printing Patron table
	print("\n2 Patron:")
	table = mycursor.execute("""
		select *
		from Patron;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

#printing Media table
	print("\n3 Media:")
	table = mycursor.execute("""
		select *
		from Media;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

#printing Media_book table
	print("\n4 Media_book:")
	table = mycursor.execute("""
		select *
		from Media_book;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

#printing Media_dvd table
	print("\n5 Media_dvd:")
	table = mycursor.execute("""
		select *
		from Media_dvd;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

#printing Media_item table
	print("\n6 Media_item:")
	table = mycursor.execute("""
		select *
		from Media_item;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

#printing Location table
	print("\n7 Location:")
	table = mycursor.execute("""
		select *
		from Location;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

#printing Edit table
	print("\n8 Edit:")
	table = mycursor.execute("""
		select *
		from Edit;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

#printing Overdue_flag table
	print("\n9 Overdue_flag:")
	table = mycursor.execute("""
		select *
		from Overdue_flag;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

#printing Waitlist table
	print("\n10 Waitlist:")
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
		select Media_book.Dewey_decimal_code, Media.Media_name, Media_book.Author, Media_book.Genre, Media.Availability, Media.Copies
		from Media, Media_book

		where Media.Dewey_decimal_code = Media_book.Dewey_decimal_code;
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

# printing table of dvds
	print("Dvds:")
	table = mycursor.execute("""
		select Media_dvd.Dewey_decimal_code, Media.Media_name, Media_dvd.Director, Media_dvd.Genre, Media.Availability, Media.Copies
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
	for x in mycursor.fetchall():
		print(x)


def show_waitlists():
	print("Waitlist:")
	table = mycursor.execute("""
		select Media.Dewey_decimal_code, Media.Media_name, Patron.Patron_name, Patron.Member_id, Media.Due_date
		from Media, Patron, Waitlist
		where Media.Dewey_decimal_code = Waitlist.Dewey_decimal_code and Patron.Member_id = Waitlist.Patron_id
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

def show_patron_waitlist(id):
	print("Waitlist:")
	table = mycursor.execute("""
		select Media.Dewey_decimal_code, Media.Media_name, Patron.Patron_name, Patron.Member_id, Media.Due_date
		from Media, Patron, Waitlist
		where Media.Dewey_decimal_code = Waitlist.Dewey_decimal_code and Waitlist.Patron_id = id
		""")
	table_info = mycursor.fetchall()
	for row in table_info:
		print(row)

        
def show_overdue_flags():
        print("\nOverdue_flag:")
        table = mycursor.execute("""
                select *
                from Overdue_flag;
                """)
        table_info = mycursor.fetchall()
        for row in table_info:
                print(row)

def show_locations():
        print("\nLocation:")
        table = mycursor.execute("""
                select *
                from Location;
                """)
        table_info = mycursor.fetchall()
        for row in table_info:
                print(row)


#Add Funcs
def add_media_book(Author, Genre, DDC):
	try:
		mycursor.execute("INSERT Media_Book(Author, Genre, Dewey_decimal_code)VALUES(%s,%s,%s)", (Author, Genre, DDC))
		connection.commit()
	except mysql.connector.IntegrityError as err:
		print("Error: {}".format(err))
		return err
	
	print("New Media Book added!")
	print("New Media Book Table: ")
	mycursor.execute("SELECT * FROM Media_Book")
	for x in mycursor:
		print(x)
	ack = input("Database Updated [press ENTER to cont. ]")
	if ack == 1:
		connection.commit()


def add_media_dvd(director, genre, DDC):
        try:
                mycursor.execute("INSERT Media_Dvd(Director, Genre, Dewey_decimal_code)VALUES(%s,%s,%s)", (director, genre, DDC))
                connection.commit()
        except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return err

        print("New Media DVD added!")
        print("New Media DVD Table: ")
        mycursor.execute("SELECT * FROM Media_dvd")
        for x in mycursor:
                print(x)
        ack = input("Database Updated [press ENTER to cont. ]")
        if ack == 1:
                connection.commit()


def add_media_item(DDC):
        try:
                mycursor.execute("INSERT Media_item(Dewey_decimal_code)VALUES(%s)", (DDC,))
                connection.commit()
        except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return err
        print("New Media Item added!")
        print("New Media Item Table: ")
        mycursor.execute("SELECT * FROM Media_item")
        for x in mycursor:
                print(x)
        ack = input("Database Updated [press Enter to cont. ]")
        if ack == 1:
                connection.commit()


def add_media(DDC, Summary, Media_name, Availability, Copies):
        try:
                mycursor.execute("INSERT Media(Dewey_decimal_code, Summary, Media_name, Availability, Copies, Due_date, Member_id)VALUES(%s,%s,%s,%s,%s,null,null)", (DDC, Summary, Media_name, Availability, Copies))
                connection.commit()
        except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return err
        print("New Media added!")
        print("New Media Table: ")
        mycursor.execute("SELECT * FROM Media")
        for x in mycursor:
                print(x)
        ack = input("Database Updated [press Enter to cont. ]")
        if ack == 1:
                db.commit()



def add_patron(Member_id, Patron_password, Patron_name, Wishlist):
	try:
		mycursor.execute("INSERT Patron(Member_id, Patron_password, Patron_name, wishlist)VALUES(%s,%s,%s,%s)", (Member_id, Patron_password, Patron_name, Wishlist))
		connection.commit()
	except mysql.connector.IntegrityError as err:
		print("Error: {}".format(err))
		return err
	print("New Patron added!")
	print("New Patron Table: ")
	mycursor.execute("SELECT * FROM Patron WHERE Member_id = %s", (Member_id,))
	for x in mycursor:
		print(x)
	ack = input("Database Updated [press Enter to cont. ]")
	if ack == 1:
		connection.commit()


def add_librarian(Admin_id, Librarian_password, Librarian_name):
	try:
		mycursor.execute("INSERT Librarian(Admin_id, Librarian_password, Librarian_name)VALUES(%s,%s,%s)", (Admin_id, Librarian_password, Librarian_name))
		connection.commit()
	except mysql.connector.IntegrityError as err:
		print("Error: {}".format(err))
		return err
	
	print("New Librarian added!")
	print("New Librarian Table: ")
	mycursor.execute("SELECT * FROM Librarian WHERE Admin_id = %s", (Admin_id,))
	for x in mycursor:
		print(x)
	ack = input("Database Updated [press ENTER to cont. ]")
	if ack == 1:
		connection.commit()


def add_waitlist(id, DDC, date):
        try:
                mycursor.execute("INSERT Waitlist(Patron_id, Dewey_decimal_code, Due_date)VALUES(%s,%s,%s)", (id, DDC, date))
                connection.commit()
        except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return err
        print("New Waitlist added!")
        mycursor.execute("SELECT * From Waitlist Where Patron_id = %s and Dewey_decimal_code = %s", (id, DDC,))
        for x in mycursor:
            print(x)
        print("New Waitlist Table: ")
        mycursor.execute("SELECT * FROM Waitlist")
        for x in mycursor:
                print(x)
        ack = input("Database Updated [press Enter to cont. ]")
        if ack == 1:
                connection.commit()


def add_location(Shelf_number, Media_dewey_decimal_code, Shelf_row, Cardinal_direction):
        try:
                mycursor.execute("INSERT Location(Shelf_number, Media_dewey_decimal_code, Shelf_row, Cardinal_direction)VALUES(%s,%s,%s,%s)", (Shelf_number, Media_dewey_decimal_code, Shelf_row, Cardinal_direction))
        except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                return err
        print("New Location added!")
        mycursor.execute("select * from Location where Media_dewey_decimal_code = %s and Shelf_number = %s", (Media_dewey_decimal_code, Shelf_number,))
        for x in mycursor:
            print(x)
        print("New Location Table: ")
        mycursor.execute("SELECT * FROM Location")
        for x in mycursor:
                print(x)
        ack = input("Database Updated [press Enter to cont. ]")
        if ack == 1:
                connection.commit()


#not sure where is best to put this but for use in reserve and checkout functions
def validate_existance(DDC):
	mycursor.execute("""
		select Dewey_decimal_code
		from Media
		where Media.Dewey_decimal_code = %s""", (DDC,))
	table = mycursor.fetchall()
	if not table:
		return False
	else:
		return True

			     
#same as before not sure where to put this
def check_available(DDC):
	mycursor.execute("""
		select Availability
		from Media   
		where Media.Dewey_decimal_code = %s""", (DDC,))
	table = mycursor.fetchone()[0]
	if table == 0:
		return False
	else:
		return True

		
#same as before
def validate_member(id):
	mycursor.execute("""
		select Member_id
		from Patron
		where Patron.Member_id = %s""", (id,))
	table = mycursor.fetchall()
	if not table:
		return False
	else:   
		return True

def validate_staff(id):
	mycursor.execute("""
		select Admin_id
		from Librarian
		where Librarian.Admin_id = %s""", (id,))
	table = mycursor.fetchall()
	if not table:
		return False
	else:   
		return True
			
#same as before
def get_due_date(DDC):
	mycursor.execute("""
		select Due_date
		from Media
		where Media.Dewey_decimal_code = %s""", (DDC,))
	table = mycursor.fetchone()[0]
	return table  

#<<<<<<< HEAD
#=======

#>>>>>>> 093def56152e8ac12b0e37642deeef7f6c889eaf
def reserve_media():
	dewey_decimal_code = input("Please enter the Dewey decimal code of the item you would like to reserve: ")

#checking if item exists
	exists = validate_existance(dewey_decimal_code)
	if not exists:
		print("Item not found.")
		return

#checking if item is available
	available = check_available(dewey_decimal_code)
	if available:
		print("It looks like this item is available! Would you like to check it out now?")
		option = input("(y - Yes, n - No)")
		if (option == "y") or (option == "Y"):
			checkout_media()
		else: 
			return
	else:
#validating member id
		member_id = input("Please enter your Member ID: ")
		valid_id = validate_member(member_id) 
		if not valid_id:
			print("Member ID not found.")
			return
	
#getting due date
		due_date = get_due_date(dewey_decimal_code)

		mycursor.execute("""
			insert into Waitlist
			values (%s, %s, %s) """, (member_id, dewey_decimal_code, due_date))
		connection.commit()
		print("Item is reserved!")
		print("This item should be available", due_date)
		

def checkout_media():
	dewey_decimal_code = input("Please enter the Dewey decimal code of the item you would like to check out: ")

#checking if item exists
	exists = validate_existance(dewey_decimal_code)
	if not exists:
		print("Item not found.")
		return
		
#checking availability
	availability = check_available(dewey_decimal_code)
	if not availability:
		print("Sorry this item is not available for checkout. Would you like to reserve it?")
		option = input("(y - Yes, n - No)")
		if (option == "y") or (option == "Y"):
			reserve_media()
		else:
			return
	else:
		member_id = input("Please enter your Member ID: ")
			
#validating member id
		valid_id = validate_member(member_id)
		if not valid_id:
			print("Member ID not found.")
			return

#validating checkout
		mycursor.execute("""
			select Dewey_decimal_code, Media_name, Due_date, Member_id
			from Media
			where Media.Dewey_decimal_code = %s""", (dewey_decimal_code,))
		table_info = mycursor.fetchall()
		for row in table_info:
			print(row)
		print("Is this the item you want to check out?")
		option = input("(y - Yes, n - No) ")
		if (option == "y") or (option == "Y"):
			
		
#changing information in media table
			today = date.today()
			due = today + timedelta(days = 21)
			mycursor.execute("""
				update Media
				set Availability = 0, Due_date = %s, Member_id = %s
				where Dewey_decimal_code = %s""", (due, member_id, dewey_decimal_code))
			connection.commit()
		
			print("You checked out: ")
			for row in table_info:
				print(row)
			print("This item will be due:", due)
		else:
			return


def return_media():  
	dewey_decimal_code = input("Please enter the Dewey decimal code of the item you wish to return: ")
		
#checking that item exists
	exists = validate_existance(dewey_decimal_code)
	if not exists:
		print("Item not found.")
		return
		
#checking that item can be returned 
	availability = check_available(dewey_decimal_code)
	if availability:  
		print("This item is not currently checked out to anyone")
		return
	
	member_id = input("Please enter your Member ID: ")

#validating member id   
	valid_id = validate_member(member_id)
	if not valid_id:
		print("Member ID not found")
		return
		
#validating that this item is checked out to this member
	mycursor.execute("""   
		select Dewey_decimal_code
		from Media
		where Media.Dewey_decimal_code = %s and Media.Member_id = %s""", (dewey_decimal_code, member_id,))
	valid = mycursor.fetchall()
	if not valid:
		print("This item is not currently checked out to this Member ID")
		return 
		
#validating item entered
	mycursor.execute("""
		select *
		from Media
		where Media.Dewey_decimal_code = %s""", (dewey_decimal_code,))
	table = mycursor.fetchall()
	for row in table:
		print(row)
	print("Is this the item you wish to return?")
	option = input("(y - Yes, n - No) ")
	if (option != "y") and (option != "Y"):
		return

#updating table 
	mycursor.execute("""
		update Media
		set Availability = 1, Due_date = null, Member_id = null
		where Media.Dewey_decimal_code = %s""", (dewey_decimal_code,))
	connection.commit()
	print("Item returned!")



def edit_password():
	id_exists = 0
	id_type = 0
	id_type = input("Please enter '1' for Patron or '2' for Librarian (enter 0 to quit)")
	if id_type == "0":
		return
	while id_exists == 0:
		id = input("Please enter your ID (enter 0 to quit)")
		if id == '0':
			quit()
		if id_type == '1':
			try:
				mycursor.execute(f"SELECT * FROM Patron WHERE Member_id = {id}")
				for x in mycursor:
					id_exists += 1
			except:
				print("incorrect ID... Please try again")
		if id_type == '2':
			try:
				mycursor.execute(f"SELECT * FROM Librarian WHERE Admin_id = {id}")
				for x in mycursor:
					id_exists += 1
			except:
				print("incorrect ID... Please try again")
		if id_exists == 0:
			print("Not a valid ID.")
			ack = input("Press Enter cont. ")

	pass_correct = 0
	while pass_correct == 0:
		pswd = input("Please enter current password (enter 0 to quit): ")
		if pswd == '0':
			quit()
		if id_type == '1':
			mycursor.execute(f"SELECT * FROM Patron WHERE Member_id = %s AND Patron_password = %s", (id, pswd,))
			for x in mycursor:
				pass_correct += 1
		if id_type == '2':
			mycursor.execute(f"SELECT * FROM Librarian WHERE Admin_id = %s AND Librarian_password = %s", (id, pswd,))
			for x in mycursor:
				pass_correct += 1
		if pass_correct == 0:
			print("Invalid Password provided. Please try again. ")
			ack =input("Press Enter to cont.")
	while pass_correct == 1:
		new_pswd = input("Please enter new password (enter 0 to quit):")
		if new_pswd ==  '0':
			quit()
		if id_type == '1':
			mycursor.execute(f"UPDATE Patron SET Patron_password = %s WHERE Member_id = %s AND Patron_password = %s", (new_pswd, id, pswd,))
			for x in mycursor:
				print(x)
		if id_type == '2':
			mycursor.execute(f"UPDATE Librarian SET Librarian_password = %s WHERE Admin_id = %s AND Librarian_password = %s", (new_pswd, id, pswd,))
			for x in mycursor:
				print(x)

		ack = input("Update successful. Press Enter to cont. ")
		pass_correct += 1


def edit_location():
	media_exists = 0
	while media_exists == 0:
		DDC = input("Please enter the Dewey Decimal Code associated with the item you wish to change the Location of: ")
		mycursor.execute("SELECT * FROM Location WHERE Media_dewey_decimal_code = (%s)", (DDC,))
		for x in mycursor:
			media_exists += 1
		if media_exists >= 1:
			new_shelf_number = input("Please input a new shelf number for the Item: ")
			new_shelf_row = input("Please input a new shelf row for the Item: ")
			new_card_direction = input("Please input a new cardinal direction for the Item: ")
			mycursor.execute("UPDATE Location SET Shelf_number = %s, Shelf_row = %s, Cardinal_direction = %s WHERE Media_dewey_decimal_code = %s", (new_shelf_number, new_shelf_row, new_card_direction, DDC))
			connection.commit()
	print("Location Updated. Now printing table...")
	show_locations()
	ack = input("press Enter to cont. ")

#Delete Funcs
def delete_waitlist(condition : str):
        try:
                mycursor.execute("DELETE FROM Waitlist WHERE {}".format(condition))
                connection.commit()
        except mysql.connector.errors.IntegrityError or mysql.connector.errors.ProgrammingError as err:
                print("Error: Condition does not exist. {}".format(err))
                end = input("Press Enter to continue..." )
                return err
        mycursor.execute("SELECT * FROM Waitlist")
        for x in mycursor:
                print(x)
        del_finished = input("Database updated. Press Enter to continue... ")




def delete_media_book(condition : str):
        try:
                mycursor.execute("DELETE FROM Media_Book WHERE {}".format(condition))
                connection.commit()
        except mysql.connector.errors.IntegrityError or mysql.connector.errors.ProgrammingError as err:
                print("Error: Condition does not exist. {}".format(err))
                end = input("Press Enter to continue..." )
                return err
        mycursor.execute("SELECT * FROM Media_Book")
        for x in mycursor:
                print(x)
        del_finished = input("Database updated. Press Enter to continue... ")



def delete_media_dvd(condition : str):
        try:
                mycursor.execute("DELETE FROM Media_dvd WHERE {}".format(condition))
                connection.commit()
        except mysql.connector.errors.IntegrityError or mysql.connector.errors.ProgrammingError as err:
                print("Error: Condition does not exist. {}".format(err))
                end = input("Press Enter to continue..." )
                return err
        mycursor.execute("SELECT * FROM Media_dvd")
        for x in mycursor:
                print(x)
        del_finished = input("Database updated. Press Enter to continue... ")


def delete_media_item(condition : str):
        try:
                mycursor.execute("DELETE FROM Media_item WHERE {}".format(condition))
                connection.commit()
        except mysql.connector.errors.IntegrityError or mysql.connector.errors.ProgrammingError as err:
                print("Error: Condition does not exist. {}".format(err))
                end = input("Press Enter to continue..." )
                return err
        mycursor.execute("SELECT * FROM Media_item")
        for x in mycursor:
                print(x)
        del_finished = input("Database updated. Press Enter to continue... ")




def delete_media(condition : str):
        try:
                mycursor.execute("DELETE FROM Media WHERE {}".format(condition))
                db.commit()
        except mysql.connector.errors.IntegrityError or mysql.connector.errors.ProgrammingError as err:
                print("Error: Condition does not exist. {}".format(err))
                end = input("Press Enter to continue..." )
                return err
        mycursor.execute("SELECT * FROM Media")
        for x in mycursor:
                print(x)
        del_finished = input("Database updated. Press Enter to continue... ")



def delete_patron(condition : str):
	try:
		mycursor.execute("DELETE FROM Patron WHERE {}".format(condition))
		db.commit()
	except mysql.connector.errors.IntegrityError or mysql.connector.errors.ProgrammingError as err:
		print("Error: Condition does not exist. {}".format(err))
		end = input("Press Enter to continue..." )
		return err
	mycursor.execute("SELECT * FROM Patron")
	for x in mycursor:
		print(x)
	del_finished = input("Database updated. Press Enter to continue... ")



def delete_librarian(condition : str):
	try:
		mycursor.execute("DELETE FROM Librarian WHERE {}".format(condition))
		db.commit()
	except mysql.connector.error.IntegrityError or mysql.connector.errors.ProgrammingError as err:
		print("Error: Condition does not exist. {}".format(err))
		end = input("Press Enter to continue...")
		return err
	mycursor.execute("SELECT * FROM Librarian")
	for x in mycursor:
		print(x)
	del_finished = input("Database updated. Press Enter to continue...")
        


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


def locate_media(Dewey_decimal_code):
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

