from flask import Flask
'''
It creates an instance of the Flask class,
 which will be your WSGI (Web server Gateway Interface) application
'''
###  WSGI application
application = Flask(__name__)

@app.route("/index")

def index():
    return "Welcome to this best Flask course.This should be an amazing course"
    

if __name__== "__main__":
    app.run(debug= True)