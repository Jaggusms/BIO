import pandas as pd
from flask import Flask
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/hello')
# ‘/’ URL is bound with hello_world() function.
def hello():
    return 'Hello World'

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def welcome():
    return 'Hello welcome'
 
# main driver function
if __name__ == '__main__':
    print("hey kousar, how are you!. take care")
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0")

