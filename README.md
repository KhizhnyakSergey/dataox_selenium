#  Test task for DataOx

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/KhizhnyakSergey/dataox_selenium.git
$ cd dataox_selenium
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv
$ venv\Scripts\activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

After installing the dependencies, you need to change the path to the **chromedriver.exe** file in the **main.py** file.
The **chromedriver.exe** file is already in your folder.
```sh
s = Service("C:/DataOx/chromedriver.exe")
```
Install PostgreSQL if you don't already have it.
The next step is to create a database and modify the **config.py** file.
```buildoutcfg
DATABASE = {
    'drivername': 'postgresql',
    'host': '127.0.0.1',
    'username': 'postgres',
    'password': '@Pos07s',
    'database': 'dataox'
}
```
This is necessary in order for you to connect to your database.

Run **main.py**
```sh
(venv)$ python main.py
```

## Task
From the website, https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273
collect all ads, pagination includes.
From every ad, you need to gather next points:

![This is an image](https://github.com/KhizhnyakSergey/dataox_selenium/blob/main/task.png?raw=true)

- Image: save only url in database.
- Date: save in format dd-mm-yyyy.
- Currency must be saved as a separate attribute.
- Save database dump to SQL file, with database creation schema

## Technical requirements
- For sending requests to the website, you can use any of the following:
  - requests, aiohttp, httpx.
- If you decide to render page to get information from site pages, use any of the
following:
  - Selenium, Playwright.
- As ORM you can use the following:
  - peewee, SQLAlchemy, mongoengine.
- Database for storing parsed data, any of the following:
  - PostgreSQL, MySQL, MongoDB
### Must have
  
- Using of any virtual environment manager(venv, pipenv, poetry)
- All your source code should be uploaded to VCS. (GitHub, GitLab, Bitbucket)
### Nice to have

- Use docker.
- Asynchronous requests.
- Upload results into Google Sheet.
### Result of task

Fully working code and SQL database dump that must be uploaded on any VCS. Please add
readme file with a short description of the project and instructions on how to set it up.