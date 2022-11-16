
# YouKraft Assignment

Task 1
  - Custom User Model

Task 2
  - Registration
  - Login


## Project setup in local env

Clone the Project Repo

```bash
  mkdir <name>
  cd <name>
  git clone https://github.com/Imrankhan06/youkraft-assignments.git
```
Create virtual environment(Ubuntu, Mac)

```bash
  python3 -m venv <name>
```
Activate virtual environment
```bash
  source <name>/bin/activate
```
Install project dependencies
```bash
  pip install -r requirements.txt
```
## Run the application
## Task 1(Custom User Model and hash password before saving to DB)
```bash
  cd Task1/  
  python manage.py runserver
  
  API: http://localhost:8000/api/users/
	
	Method: POST

	payload: {
		'username':<username>,
		'email': <email>,
		'password':<password>
	}
```

## Task 2(Check Password)
```bash
  cd Task2/youkraftTask2/  
  python manage.py runserver

* Registration:
```bash
    Url: http://localhost:8000/user/register/
	
	Method: POST

	payload: {
		'username':<username>,
		'password':<password>
	}
```
* Login:
```bash
    Url: http://localhost:8000/user/authenticate/
	
	Method: POST

	payload: {
		'username':<username>,
		'password':<password>		
	}

```
