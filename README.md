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

# Thought Process

Here my main goal was to make everything real time. I created the APIs using Django Rest Framework, I added the endpoints above then I read the email again and noticed that I was told to use sockets, so i didn't delete any of the Code but I had to implement Channels. 

# CREATE

When data is sent to the server if there is no ID present in the request body then an object is created

# EDIT
When ID is present in the request body but no 'action' element then it takes the data retrieves the object with pk ID and updates that object.

# DELETE
When ID is present and 'action' is DELETE then the object with the pk ID is retrieved and deleted.

# READ 
Now this was done in two ways, when an initial handshake is made with the react socket then immediately all the event data is sent. Then after that, when any kind of modification is made like new object being created, or object being edited, and object being deleted, then immediately the modified set of data is sent through the socket to the client which is the Javascript REACT portion.