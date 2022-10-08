## OverView
The City of Bayjing won the bid to host the next FunOlympic Games in 2022. The FunOlympic committee has decided that they require a project which needs to be completed before the games start to ensure that worldwide audiences can enjoy the games online. They have decided to broadcast the game through an online platform. Therefore, they have appointed a team of IT systems and infrastructure professionals to develop the online game-watching portal.

## Goal 
A user-centric FunOlympic web application will be delivered to the client that will webcast all of FunOlympic's games, and users can watch the games from any location at any time.

## Functionality
### Functional Functionality 
* User Panel
  a.	Registration: User should be able to register to the site with Username, Email, Password, and Confirm-Password. 
  b.	Login: User should be able to access the site with valid Username and Password. Users can also login with their Google account. User can reset their password.
  c.	After login, users can search, select and watch game. Additionally, users will be allowed to like/dislike and comment on game. User can change their password as well.          Futhermore, users can watch News and schedule related to the FunOlympic games.
  d.	Logout: Users should be able to logout from the system.
  e.	Security Feature like CAPTCHA, Password Strength Checker, Form Validation, and Email Verification etc. 
* Admin Panel
  a.	Admin panel should contain view user interaction, and reset password etc. 
  b.	Content (game video, news, schedule etc.) managed by admin.

### Non-Functional Functionality
* Unauthorized users to access the system should be avoided. Non-user should not allow to watch games.
* The site should be user-friendly and responsive to all screen sizes. 
* System should perform smoothly and should be reliable. 
* System should be open door for maintainability.
* The system should be secured by implementing different security.
* The system color and theme should implement as per the client.


## Tool, Programming language and Technique used to develop this project
* Tool - Visual studio code
* Programming langauge -
  * Frontend - HTML, CSS and JavaScript
  * Backend - Python and Django
* Technique - MVT (Model View Template)

## Setup
Start by creating a new Django project. This code can live anywhere on your computer. We can do all of the normal configuration from the command line:
* Run requirements.txt - pip install -r requirements.txt
* python -m pip install --upgrade pip setuptools virtualenv
* pip install Django
* pip install django-jazzmin
* pip install authentication
* pip install django_cleanup
* pip install django-embed-video
* pip install django-allauth
* pip install pillow


## Here are the commands to run:
* Run the Application - python manage.py runserver
* Application will run in the local server. Go to - http://localhost:8000/
If you navigate to http://127.0.0.1:8000 you'll see the application landing page.


## For Admin Login
Credentials for admin login are:
Username : admin
Password : admin
