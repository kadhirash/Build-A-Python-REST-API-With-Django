# REST API with Django Rest Framework

> A web application allowing me to learn more about Representational state transfer(REST)ful API's using pure Django as well as the Django Rest Framework (DRF) and implementing Create, Retrieve, Update, Delete (CRUD) funcionalities with my REST API. Althought tedious work in Django, helped me appreciate the usefulness of DRF and the reason for REST.

# Table of Contents

* [General Information](#general-information)
* [Technologies/Tools](#technologiestools)
* [Setup](#setup)
* [Screenshots and Code Examples](#screenshots-and-code-examples)
* [Status](#status)
* [Credits](#credits)
* [Roadblocks](#roadblocks)
## General Information
*(todo)*
## Technologies/Tools

* Python
* Django/DRF
* RESTful APIs

## Setup
I will show you how I went about this with just the Django portion. The DRF portion was really similar and without excess steps.

Assuming that pip3 is already installed in your local machine since Python3 should be as well, and you're in a folder,
create a [virtual environment](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-Python-s-virtualenv-using-Python-3) and begin building simply by doing 

1) `virtualenv -p python3 .` 

Followed by 

2) `source bin/activate` (don't forget to type `deactivate` when you want to leave the virtual environment!)

to activate the virtual environment. It was there I installed certain libraries required such as Django, Requests, Pillow, etc. Again, it would depend on your machine. I will skip some of those steps but add them as required if compilation errors.

3) `mkdir src` 

To create a folder for where to write all your source code.

4) `pip3 install django` 

5) `cd src'

6) `django-admin startproject RESTfulAPI .` 

Note, the name of the project can be anything, as I called it "testapi" in my source code.

You should see a "manage.py" file in the current directory you're in.

7) `python3 manage.py migrate`

[Migrate](https://www.geeksforgeeks.org/django-manage-py-migrate-command-python/) allows the machine to execute SQL commands in the database file. To confirm, if you do `ls`, a new "db.sqlite3" file should have appeared.

8) `python3 manage.py createsuperuser` 

And simply fill in the requirements. This step is just to see how admin privleges via Django works. 

Next,

9) `python3 manage.py runserver`

I recommend opening another terminal window and activating the virtual enironemnt (but not running the server) to be able to write and execute code and see the live updates on the running server of the first terminal. 

Lastly,

10) `Python3 manage.py startapp [insert name here]`

Awesome! This should allow you now to start on your RESTful API creation journey as well as implementing CRUD functionalities of course!


## Screenshots and Code Examples
### Pure Django
#### Admin Features
![Admin Login](/../restapi/img/django_admin_login.png)

![Admin Front Page]

## Status

Project is: *in progress*

## Credits
This implementation was based on the [Udemy course](https://www.udemy.com/course/build-a-python-rest-api-with-the-django-rest-framework/) by Justin Mitchel!! Although old and from 2018, it was fun to try and implement a newer version in 2020 with a newer version of Django and Python3.

## Roadblocks
As mentioned above, the Udemy course was based on an older version of Python3 and Django (1.11.8). Thus, I had to either downgrade my current Python3 version to 3.6 to use the Django in the video or upgrade my Django but implement in a different way. I went along with the latter option. I faced quite a few bugs in the beginning since I had a newer version of Django so implementing certain functions had to be done differently. For example, when writing this line of code, `user = models.ForeignKey(settings,AUTH_USER_MODEL)` is perfectly fine in the older version of Django. However, in the newer one I kept getting "TypeError: __init__() missing 1 required positional argument: 'on_delete'" I was confused and from a quick troubleshoot using the Django [document](https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.ForeignKey) I realized I needed to actually write `user = models.ForeignKey(settings,AUTH_USER_MODEL, on_delete = models.cascade)` and the error went away! 

Other than these small errors from time to time, the overall project was fun to implement and watch the project in action! 




