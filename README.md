# PyNano

This is my first repository, it's a python library to create a local http server

# bash CLI steps to build

$ cd path/to/PyNano/Folder
$ python setup.py sdist
$ pip install dist/PyNano-0.2.tar.gz

# Usage in python:: a simple py file 

# main_script.py
from PyNano import PyServer

directory = "/storage/emulated/0/My_py_server"
port = 8000

# Create an instance of MyServer
my_server = PyServer(directory, port)

# Start the server
my_server.start_server()

print("\nSending GET request to local server\n")

# Send a GET request
my_server.send_get()

# Stop the server
my_server.stop_server()
