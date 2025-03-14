# 🎓 Student Registration & Login System  

This is a **GUI-based Signup & Login System** built using **Python (Tkinter) and MySQL**. The application allows users to register with their details and log in securely.  

---

## 📌 Features  
✅ **User Registration** – Collects user details and stores them in a MySQL database.  
✅ **Secure Login** – Users can log in using their registered credentials.  
✅ **GUI Interface** – Built with Tkinter for a user-friendly experience.  
✅ **MySQL Database** – Stores user information securely.  

---

## 🛠️ Technologies Used  
- **Python** (Tkinter for GUI)  
- **MySQL** (pymysql for database connectivity)  
- **OS Module** (for system operations)  

---

## 📂 Project Setup  

### 1️⃣ Install Required Modules  
Ensure you have Python installed, then install the required module:  
```sh
pip install pymysql
```  

### 2️⃣ Create MySQL Database  
Login to MySQL and run:  
```sql
CREATE DATABASE student_database;
```  

### 3️⃣ Create Table  
Switch to the `student_database` and execute:  
```sql
CREATE TABLE student_register (
   name VARCHAR(50) NOT NULL,
   dob VARCHAR(18) NOT NULL,
   gender VARCHAR(10) NOT NULL,
   email VARCHAR(50) NOT NULL PRIMARY KEY,
   phone_no VARCHAR(20) NOT NULL,
   password VARCHAR(30) NOT NULL
);
```  

### 4️⃣ Configure Database Connection  
Modify the database credentials in the Python script:  
```python
import pymysql

db = pymysql.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="student_database"
)
```  

### 5️⃣ Run the Application  
Execute the Python script:  
```sh
python main.py
```  

---

## 🎯 How to Use  

### 1️⃣ Sign Up  
- Enter your details (Name, DOB, Gender, Email, Phone No, and Password).  
- Click **Register** to save your details.  

### 2️⃣ Login  
- Enter your registered **Email** and **Password**.  
- Click **Login** to access your account.  

---

## 🏆 Author & Credits  
Developed by **Manikanta1239**. Feel free to modify and improve the project! 🚀  

