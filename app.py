from markupsafe import escape
from flask import Flask, abort

app = Flask(__name__) 

@app.route('/')
@app.route('/index/')
def genius():
        return '<h1>Welcome to Zions  website!</h1>'

@app.route('/about/')
def about():
        return '<h3>Born in the city of Detroit,my name is zion myers and I use to do drama ask a kid and I use to play chess!</h3>'


@app.route('/capitalize/<word>/')
def capitalize(word) :
        return '<h1>{}</h1>'.format(escape(word.capitalize()))


@app.route('/add/<int:n1>/<int:n2>/')
def add(n1,n2):
        return '<h1>{}</h1>'.format(n1+n2)

@app.route('/users/<int:user_id>/')
def greet_user (user_id):
        users = ['Bob', 'Jane', 'Adam'] 
        try:  
                return '<h2> Hi {}</h2>' . format(users[user_id])   
        
        except IndexError:
         abort(404)

@app.route('/myName/<first>/<middle>/<last>/')
def myName (first, middle, last):
   return '<h1>{}</h1>'.format(first +" "+ middle +" "+ last)

@app.route('/rep_yo_city/<word>/<word1>/')
def rep_yo_city (word,word1):
    return '<h1>{}</h1>'.format(escape(word.capitalize())+" "+escape(word1.capitalize()))
 
@app.route('/sub/<int:n1>/<int:n2>/')
def sub(n1,n2):
        return '<h1>{}</h1>'.format(n1-n2)

@app.route('/multi/<int:n1>/<int:n2>/')
def multi(n1,n2):
        return '<h1>{}</h1>'.format(n1*n2)

@app.route('/div/<int:n1>/<int:n2>/')
def div(n1,n2):
        return '<h1>{}</h1>'.format(n1/n2)

@app.route('/mod/<int:n1>/<int:n2>/')
def mod(n1,n2):
        return '<h1>{}</h1>'.format(n1%n2)

@app.route('/geniuses/<int:user_id>/')
def geniuses_user (user_id):
        users = ['Zion', 'Craig', 'Enasi', 'Boyd', 'Alvin', 'Jordan', 'Tyler', 'Matt', 'Damonie', 'Prinzton', 'Derek', 'Edward', 'Isaiah i', 'Isaiah m'] 
        try:  
                return '<h2> Hi {}</h2>' . format(users[user_id])   
        
        except IndexError:
         abort(404)