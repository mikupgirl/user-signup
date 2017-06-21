from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['POST'])
def userForm():
    user_name = request.form['Username']
    user_password = request.form['Password']
    user_verify = request.form['Verify_Password']
    user_email = request.form['Email'] #make optional

    name_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    verify = ''
    password = ''
    email = ''
    name = ''

    if len(user_name) >= 20 or len(user_name) <= 3 or len(user_name) == 0:
        name_error = "Sorry, that is not a valid username."
        name = ''

    if len(user_password) == 0:
        password_error = "Please enter a password."
        password = ''
    else:
        if user_verify != user_password:
            verify_error = "Passwords don't match."
            verify = ''       
        
    if len(user_email) > 0:
        if "@" not in user_email or "." not in user_email:
            email_error = "Sorry, that is not a valid email."
            email = ''
          
    if not name_error and not password_error and not verify_error and not email_error:
            return render_template('welcome_form.html', name=user_name)
    else:    
        return render_template('signup_form.html',
            name_error=name_error,
            name=name,
            password_error=password_error,
            password=password,
            verify_error=verify_error,
            verify=verify,
            email_error=email_error,
            email=email)


@app.route("/")
def index():
    return render_template('signup_form.html')

@app.route("/hello", methods=["POST"])
def hello():
    user_name = request.form['user_name']
    return render_template('welcome_form.html', name=user_name)

app.run()