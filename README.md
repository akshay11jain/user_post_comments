User_Post_Comments
-----------------
Python Version 3.6.2

Django Version 1.11.3

---------------
Getting Started
---------------

These instructions will get you a copy of the project up and running 
on your local machine for development and testing purposes.

-------------
Prerequisites
-------------

Install Python 3.6.2
------------------------------------
Run the following command in order :
------------------------------------
sudo add-apt-repository ppa:jonathonf/python-3.6

sudo apt-get update

sudo apt-get install python3.6

-------------------------------
Make Virtual Environment - MUST
-------------------------------
python3.6 -m venv author


----------------------------
Activate Virtual Environment
----------------------------
source author/bin/activate

------------------------------------------------
Clone the repository inside the author directory
------------------------------------------------
cd author

git clone https://github.com/akshay11jain/user_post_comments.git

cd user_post_comments

pip install -r requirements.txt


--------------
Database Setup
--------------
Refer this link for xampp setup on linux :
https://www.wikihow.com/Install-XAMPP-on-Linux

After following the link, check the apache running port and run the localhost on that port.

Open phpMyAdmin

Create a new Database 

Use a default user from the User Accounts or create a new User.

Update the user_post_comments/settings.py with the DB credentials.

-----------------------------
Run migrations after DB setup.
-----------------------------
python manage.py migrate


-----------
Run Server
-----------
python manage.py runserver









