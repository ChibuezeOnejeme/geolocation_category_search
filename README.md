
# Geolocation and Location Search Api


This project is designed to search POI(Point of Interests) in a specific location making use of TomTom API category search endpoint.

## Installing / Getting started

A quick introduction of the minimal setup you need to project up and running .

```shell
git clone https://github.com/ChibuezeOnejeme/geolocation_category_search.git

cd geolocation_category_search

code .   < This will open an editor from shell/bash  >

pip install virtualenv

python3.8 -m venv env <This creates a virtual venv on your local machine>

env/Scripts/activate.bat //In CMD < activate venv for  windows>
env/Scripts/Activate.ps1 //In Powershel<activate venv for windows>

source env/bin/activate< activate venv for Mac>

pip install -r requirements.txt

create a .env file and add your "API_KEY"




```

For the above code to properly function an API key must be gotten from https://www.tomtom.com/en_gb/. and the key must be stored in ".env file " in the project and the name variable must be  **API_KEY** .
The back end for the html template is **FLASK** and it will be running on localhost port  http://127.0.0.1:5000.


**Files  and  Functions**:
i) **.env file**: This stores the API KEY for security purposes and keep in gitignore


ii) **extract .py**: This file contains a python function for extracting required keys from a json file eg "name" ie for hospital name, eatry name etc.


iii) **main . py**: This is the main python file for running program.


iv) **item .txt**: This text file contains possible searchable category.


v)**requirements .txt**: This contains all dependency programs to be installed for the full functionality of project.

