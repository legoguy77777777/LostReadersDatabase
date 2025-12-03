#creating tables
create table Librarian(
	Admin_id int primary key,
	Librarian_password varchar(20) not null,
	Librarian_name varchar(25) not null
);

create table Patron(
	Member_id int primary key,
    Patron_passowrd varchar(20) not null,
    Patron_name varchar(25) not null,
    Wishlist varchar(1000)
);

create table Media(
	Dewey_decimal_code real primary key,
    Summary varchar(1000),
    Media_name varchar(50) not null,
    Availability int not null,
    Copies int not null,
    Due_date varchar(10),
    Member_id int references Patron
		on delete cascade
);

create table Media_Book(
	Author varchar(25),
    Genre varchar(20), 
    Dewey_decimal_code real references Media
		on delete cascade,
    primary key(Dewey_decimal_code)
);
    
create table Media_dvd(
	Director varchar(25),
    Genre varchar(15),
    Dewey_decimal_code real references Media
		on delete cascade,
    primary key(Dewey_decimal_code)
);

create table Media_item(
	Dewey_decimal_code real references Media
		on delete cascade,
	primary key(Dewey_decimal_code)
);

create table Location(
	Shelf_number int not null unique,
    Media_dewey_decimal_code real references Media (Dewey_decimal_code),
    Shelf_row int,
    Cardinal_direction varchar (8),
    primary key (Shelf_number, Media_dewey_decimal_code)
);

CREATE TABLE Edit (
    Admin_id INT REFERENCES Librarian,
    Shelf_number INT REFERENCES Location(Shelf_number),
    Dewey_decimal_code REAL REFERENCES Media,
    Last_edit_date VARCHAR(10),
    PRIMARY KEY (Admin_id , Shelf_number , Dewey_decimal_code , Last_edit_date)
);

create table Overdue_flag(
	Admin_id int references Librarian,
    Dewey_decimal_code real references Media,
    primary key (Admin_id, Dewey_decimal_code)
);

create table Waitlist(
	Patron_id int references Patron,
    Dewey_decimal_code real references Media,
    Due_date varchar(10),
    primary key (Patron_id, Dewey_decimal_code)
);

#adding sample data
#Librarian
insert into Librarian
values (123456, "asdfghjkl", "John Smith");
insert into Librarian
values (121212, "password", "Jane Doe");
insert into Librarian
values (888888, "iheartbooks", "Monroe Bragg");

#Patron
insert into Patron
values (8675309, "ilovecats", "Taylor Swift", null);
insert into Patron
values (189392, "1893sMorganDollar", "Maya Southard", null);
insert into Patron
values (149281, "finalsweek=:(", "Angie Southard", null);

#Media
#Books
insert into Media
values (191.513, 
"In the highly anticipated Thinking, Fast and Slow, Kahneman takes us on a groundbreaking tour of the mind and explains the two systems that drive the way we think. System 1 is fast, intuitive, and emotional; System 2 is slower, more deliberative, and more logical. Kahneman exposes the extraordinary capabilities—and also the faults and biases—of fast thinking, and reveals the pervasive influence of intuitive impressions on our thoughts and behavior. The impact of loss aversion and overconfidence on corporate strategies, the difficulties of predicting what will make us happy in the future, the challenges of properly framing risks at work and at home, the profound effect of cognitive biases on everything from playing the stock market to planning the next vacation—each of these can be understood only by knowing how the two systems work together to shape our judgments and decisions.",
"Thinking, Fast and Slow", 1, 3, null, null);
insert into Media
values (425.925, 
"Snatched from her ancestral lands, a giant tortoise finds herself in an exclusive estate in southern California where she becomes an astute observer of societal change. Her journey is one of discovery, as she learns to embrace the music of jazz and the warmth of human connection.",
"The Tortoise's Tale", 0, 2, null, null);
insert into Media
values (934.812, 
"Laurie is sixty-five and living with Alzheimer’s. Her daughter Amelia, a once fiery and strong-willed activist, can’t bear to see her mother’s mind fade. Faced with the reality of losing her forever, Amelia signs them up to take part in the world’s first experimental merging process for Alzheimer’s patients, in which Laurie’s ailing mind will be transferred into Amelia’s healthy body and their consciousness will be blended as one. Soon Amelia and Laurie join the opaque and mysterious group of other merge teenage Lucas, who plans to merge with his terminally ill brother Noah; Ben, who will merge with his pregnant fiancée Annie; and Jay, whose merging partner is his addict daughter Lara. As they prepare to move to The Village, a luxurious rehabilitation center for those who have merged, they quickly begin to question whether everything is really as it seems.",
"The Merge", 1, 2, null, null);

#dvd
insert into Media
values (123.456, "A group of young misfits called The Goonies discover an ancient map and set out on an adventure to find a legendary pirate's long-lost treasure.",
"The Goonies", 0, 4, null, null);
insert into Media
values (352.910, "A diamond heist reunites retired Horsemen illusionists with new performers Greenblatt, Smith and Sessa as they target dangerous criminals.",
"Now You See Me: Now You Don't", 0, 2, null, null);
insert into Media
values (629.210, "While trying to lead a quiet suburban life, a family of undercover superheroes are forced into action to save the world.",
"The Incredibles", 0, 4, null, null);

#items
insert into Media
values (031.705, "USB-C to USB charging cable", "USB-C charging cable", 1, 7, null, null);
insert into Media
values (792.469, "MAC laptop charger", "MAC laptop charger", 0, 10, null, null);
insert into Media
values (072.304, "Expo Markers: Red, Blue, Green, Black", "Dry Erase Markers", 1, 10, null, null);

#Media_book
insert into Media_Book
values ("Daniel Kahneman", "Self Help", 191.513);
insert into Media_Book
values ("Kendra Coulter", "Historical Fiction", 425.925);
insert into Media_Book
values ("Grace Walker", "Science Fiction", 934.812);

#Media_dvd
insert into Media_dvd
values ("Richard Donner", "Adventure", 123.456);
insert into Media_dvd
values ("Ruben Fleischer", "Thriller", 352.910);
insert into Media_dvd
values ("Brad Bird", "Superhero", 629.210);

#Media_item
insert into Media_item
values (031.705);
insert into Media_item
values (792.469);
insert into Media_item
values (072.304);

#Location
insert into location
values (15, 191.513, 3, "North");
insert into location
values (4, 425.925, 1, "East");
insert into location
values (9, 934.812, 2, "South");
insert into location
values (19, 123.456, 4, "East");
insert into location
values (18, 352.910, 3, "East");
insert into location
values (20, 629.210, 2, "South");
insert into location
values (1, 031.705, 1, "West");
insert into location
values (2, 792.469, 1, "West");
insert into location
values (3, 072.304, 1, "West");

#Edit
insert into Edit
values (888888, 3, 072.304, "08/12/23");
insert into Edit
values (123456, 20, 629.210, "01/03/25");
insert into Edit
values (123456, 15, 191.513, "12/01/25");

#Overdue_flag
insert into Overdue_flag
values (121212, 352.910);
insert into Overdue_flag
values (123456, 123.456);
insert into Overdue_flag
values (888888, 031.705);

#Waitlist
insert into Waitlist
values (8675309, 352.910, "01/03/26");
insert into Waitlist
values (8675309, 629.210, "02/07/26");
insert into Waitlist
values (149281, 123.456, "03/17/26");



