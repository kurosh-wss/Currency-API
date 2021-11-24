 ## Currency-API

An API to exchange different currencies to IRR
 

## Requirements

1. Python >= 3.8

2. Pip > 3

3. virtualenv (or any other virtual enviroment for python)

## installation

1. Create and activate virtual enviroment

	1. If you don't have virtualenv run  `pip install virtualenv`
	
	> `virtualenv env`
	> `env\Scripts\Activate.bat`

2. Install project requirements

	> `pip install -r requirements.txt`

3. Start server
  
	> `python manage.py migrate`
	> `python mange.py runserver`

## First User

1. If you don't have any users or don't have any user's credentials use this command to create a new superuser

	> `env\Scripts\Activate.bat`
	> `python manage.py createsuperuser`
