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
  id_type = input("Please enter '1' for Patron Login or '2' for Librarian Login: ")
  while id_exists == 0:
    id = input("Please enter your ID (enter '0' to quit): ")
    if id == '0':
      quit()
    if id_type == '1':
      mycursor.execute("SELECT * FROM Patron WHERE Patron_id = (%s)", (id,))
    if id_type == '2':
      mycursor.execute("SELECT * FROM Librarian WHERE librarian_id = (%s)", (id,))

#search media by ..... type?
def search_media():



def show_media_attributes():



def show_wishlist():



def reserve_media():



def checkout_media():



def return_media():



def add_to_wishlist():



def delete_from_wishlist():



def overdue_flag():



def edit_password():



def add_patron():


#admin access only below
def edit_location():



def add_media():



def edit_media():



def delete_media():



#aggregate functions below
def get_sum_media_type():



def get_sum_media():



def get_sum_available():



#overall functions to show tables
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


#shows all three media types and tables
def show_media():



def show_patrons():




