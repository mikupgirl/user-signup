from flask import Flask, request, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


form = """ 
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
            <h1>Signup</h1>
                <form method="POST">
                    <table>
                        <tbody>
                            <tr>
                                <td>
                                    <label for="username">Username:</label>
                                </td>
                                <td>    
                                    <input type="text" name="Username" value/>
                                    <span class="error"></span>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <label for="Password">Password:</label>
                                </td>
                                <td>
                                    <input type="text" name="Password" />
                                </td>
                            </tr>
                            <tr>
                                <td>   
                                    <label for="Verify Password">Verify Password:</label>
                                </td>
                                <td>
                                    <input type="text" name="Verify_Password" />
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <label for="Email">Email (optional):</label>
                                </td>
                                <td>
                                    <input type="text" name="Email" />
                                </td>
                            </tr>
                        </tbody>
                    </table>         
                    <input type="submit" value="Submit" />
                </form>      
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def userForm():
    user_name = request.form['Username']
    user_password = request.form['Password']
    user_verify = request.form['Verify_Password']
    user_email = request.form['Email'] #make optional
    if len(user_name) >= 20 or len(user_name) <= 3:
        error_msg = "Sorry, that is not a valid username.".format(form)
        
        return redirect('/?error={0}'.format(error_msg))

    if "@" or "." not in user_email:
         error_msg = "Sorry, that is not a valid email.".format(form)

         return redirect('/?error={0}'.format(error_msg))

    content = user_name + user_password + user_verify + user_email
    return form.format(content)

@app.route("/")
def index():
    error = request.args.get('error')
    if error:
        esc_error = cgi.escape(error, quote=True)
        error_element = '<p class="error">{0}</p>'.format(error)
    else:
        error_element = ''

    # build the response string
    content = form + error_element

    return content

app.run()