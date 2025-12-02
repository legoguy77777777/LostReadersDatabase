import mysql.connector
import random
from enum import Enum

#code notes :
# entering "0" results in moving back one step
# only 2 types of login accounts

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


#shows all three media types and tables
def show_media():



def show_patrons():




