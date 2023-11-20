# Signup & login page using Python & MySQL
It's a GUI project using python tkinter and MySQL database.

Steps to follow after installing all the modules. Otherwise this application will not work properly.

->Create a database with this name, "student_database"
->create a table with this name, "student_register"

USE this code to create the table under the "student_database" database

create table student_register(
   name VARCHAR(50) NOT NULL,
   dob VARCHAR(18) NOT NULL,
   gender VARCHAR(10) NOT NULL,
   email VARCHAR(50) NOT NULL,
   phone_no VARCHAR(20) NOT NULL,
   password VARCHAR(30) NOT NULL,
   PRIMARY KEY ( email )
);
