# Email Sender

Sends email using Python [email](https://docs.python.org/3/library/email.html) module

## Installation

Install [Python](https://python.org/) version 3.8 and [pip](https://pip.pypa.io/en/stable/)

Create a virtual environemnt by running
```bash
python3 -m venv .venv
```

Activate the environment by running command
```bash
source .venv venv/bin/activate
```

Install dotenv module by running command
```bash
pip3 install dotenv
```

## Usage

Create a .env file in the root directory. Add your google app password as
```bash
APP_PASSWORD = google_app_password
```

You can generate temporary receiver email via this page [temp-email](https://temp-mail.org/en/)

## How to run the program
```python
python3 app.py
```
Deactivate virtual environment by simply running the below command
```python
deactivate
```

## License

[MIT](https://choosealicense.com/licenses/mit/)