#import the Flask class from the flask module
from flask import Flask 

#Create an instance of the Flask class and give it the variable name 'app'
app = Flask(__name__)

#Create a route using the @app.route to trigger function based on endpoint
@app.route('/') 
def index():
    return 'Hello this is the index'

@app.route('/posts') 
def posts():
    return 'Hi this is posts'
