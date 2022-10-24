#import the Flask class from the flask module
from flask import Flask 

#Create an instance of the Flask class - central object of the whole app /and give it the variable name 'app'
app = Flask(__name__)

#import all of the routes from the routes module in the current folder
from . import routes 
