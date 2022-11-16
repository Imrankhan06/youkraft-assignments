
# YouKraft Assignment


## Features

- Signup
- logging


## Project setup in local env

Clone the Project Repo

```bash
  mkdir <name>
  cd <name>
  git clone https://github.com/Imrankhan06/youkraft-assignments
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
Migrate
```bash
  python manage.py migrate
```
Run the application
```bash
  python manage.py runserver
```

## List of APIs

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
