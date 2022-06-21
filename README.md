# CreativesConnect[Licence: MIT](https://github.com/Beldine-Moturi/CreativesConnect/blob/master/LICENSE)
# ![CreativesConnect](images/icon1.png)
# CreativesConnect
<table>
<tr>
<td>
  A webapp using various APIs to display projects available for creatives to work on. It serves as a one-stop shop for Africa’s Creative minds to showcase their skills and portfolios, collaborate with each other and find jobs/projects and information about the creative industry.
</td>
</tr>
</table>

## Demo

## Features

## Usage

## File Descriptions
| Folder | File | Description |
| :--- | :--- | :--- |
| tests |  | Contains unittests for the project |
|  | console.py | Command line Interpreter for managing objects/data in this project |
| models | base_model.py | Defines all common attributes/methods for other classes |
| models | * | Define all other objects/classes used in this project |
| models/engine | db_storage.py | Defines methods that interact with mysql database for storing data |
| api | * | Exposes the data in our storage via an API |
| app/* | * | Contains the html, css and javascript files the web interface |
| app | app.py |  Starts a Flask web application for the project |
|  | setup_mysql_dev.sql | sets us the mysql database |
|  | setup_mysql_test.sql | sets up the mysql database for testing |
| To be updated |

## To be Implemented...
1. Define classes for all other objects in this project
2. create a console: command interpreter for  manipulating(create, update, delete, etc) objects in this project
3. API: Expose data in the database via an API
4. static web: create the user web interface for the app
5. dynamic we: make the app dynamic with Javascript
6. Populate app with data
7. Deploy app
8. DEMO: add demo to README file

## Bugs
No known bugs at this time

## Technologies used
- Languages: python, HTML, CSS, Javascript, sql, Bash
- Frameworks: Flask, flask_sqlalchemy, Flask-CORS, JQuery, RESTful API, Bootstrap
- Operating system: This project is interpreted/tested on Ubuntu 14.04 LTS using python3
- style: Pycodestyle
- Version control: Git

## Authors
- Beldine Moturi | [Linkedin](https://www.linkedin.com/in/beldine-moturi-00811615a/)