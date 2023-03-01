from flask import render_template 
from  app import app 

@app.route('/')
def index():
  fakebook={
        'fakebook 101': ('how to use Fakebook?','how to create account?')
  }
  return render_template('index.jinja',fakebook=fakebook, title='Home')

@app.route('/home')
def about():
    return render_template('home.jinja')

@app.route('/log_in')
def about():
    return render_template('log_in.jinja')

@app.route('/register')
def register():
    
    return render_template('register.jinja')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/blog')
def about():
    return render_template('blog.jinja')
