from flask import Flask, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True


form = """ 
<!DOCTYPE html>
<html>
    <head>
        <title>User Signup</title>
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
    #if user_name or user_password or user_verify or user_email == NULL:
     #   error_msg = "All fields must be filled.".format(form)

      #  return redirect('/error={0}'.format(error_msg)) 


    content = user_name + user_password + user_verify + user_email
    return form.format(content)

@app.route("/")
def index():
    return form.format('')

app.run()