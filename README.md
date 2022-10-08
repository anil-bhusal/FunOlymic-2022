## OverView
The City of Bayjing won the bid to host the next FunOlympic Games in 2022. The FunOlympic committee has decided that they require a project which needs to be completed before the games start to ensure that worldwide audiences can enjoy the games online. They have decided to broadcast the game through an online platform. Therefore, they have appointed a team of IT systems and infrastructure professionals to develop the online game-watching portal.

## Goal 
A user-centric FunOlympic web application will be delivered to the client that will webcast all of FunOlympic's games, and users can watch the games from any location at any time.

## Functionality
* UserSite
  * Secure Register with form validation, captcha, password strength checker and email verification
  * Log in (with username and password) with form validation and captcha 
  * Google login
  * User landing page
  * Games video
  * Likes/Dislikes on games video
  * Comment on games video
  * Watch news
  * Search games
  * Watch schedule
  * Change password
  * Logout
  * Forgot password 

* AdminSite
  * Login
  * Admin Dashboard
  * Users list
  * Remove users feature
  * Games list
  * Add games
  * Remove games
  * News list
  * Add news
  * Remove/update news
  * Schedule list
  * Add schedule
  * Remove/update schedule
  * Change users password
  * Logout and more


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
