# event-calendar-backend
Event Calendar Backend using Django Rest Framework


# Installation

After cloning you need to setup python environment

# Windows

1. pip install virtualenv
2. virtualenv venv
3. (a folder named venv will be created) 
4. Run this command "venv/scripts/activate"(virtual env activated) (at root directory of venv)
5. Go to cloned directory then go to 'backend'
6. run command "pip install -r requirements.txt"
7. run command "python manage.py runserver"   "localhost:8000"
8. Now frontend can be used. 


# Linux
1. pip3 install virtualenv
2. virtualenv venv
3. (a folder named venv will be created) 
4. Run this command "source venv/bin/activate"(virtual env activated) (at root directory of venv)
5. Go to cloned directory then go to 'backend'
6. run command "pip install -r requirements.txt"
7. run command "python manage.py runserver"   "localhost:8000"
8. Now frontend can be used. 


Now it is running at localhost:8000
# Endpoints
1. localhost:8000/api/events -> api of all events
2. localhost:8000/api/upcoming -> api of all upcoming events
3. localhost:8000/eventConsumer -> Socket link which is called in the react project