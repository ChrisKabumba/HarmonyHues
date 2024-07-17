from flask import Flask, render_template, request, redirect
from datetime import datetime
from classes.user import *

app = Flask(__name__)
user = User()

# Home route. Also, login route
@app.route("/", methods=['GET', 'POST'])
def home_login():
    if request.method == 'POST':
        #Perform login task here with methods from the user class
        email = request.form['email']
        password = request.form['password']

        if user.sign_in(email=email, password=password):
            return redirect('/user/')
        else:
            return render_template("index.html", message="Invalid Credentials")
        
    else:
        return render_template("index.html", message="")
    
# Sign up route
@app.route("/signup/", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST': 
        # sign up task here
        global registerUserData
        registerUserData = RegisterUserData()
        registerUserData.first_name = request.form['first-name']
        registerUserData.middle_name = request.form['middle-name']
        registerUserData.last_name = request.form['last-name']
        registerUserData.email = request.form['email']
        registerUserData.current_address = request.form['current-address']
        registerUserData.phone_number = request.form['phone-number']
        registerUserData.date_of_birth = request.form['date-of-birth']
        first_password = request.form['password-first']
        scnd_password = request.form['password-scnd']

        if first_password == scnd_password:
            registerUserData.password = request.form['password-first']
        else:
            return render_template("sign_up.html", message="Passwords do not match", data=registerUserData)  
        
        #send OTP code to the email
        global otp_code
        otp_code = user.send_otp(registerUserData.email)

        return render_template("confirm_email.html", message="")

    else:
        return render_template("sign_up.html", message="", data=None)

# confirm email route. Tied to the sign up route
@app.route("/confirm_email/", methods=['GET', 'POST'])
def confirm_email():
    if request.method == 'POST':
        #complete the sign up process
        if otp_code == request.form['otp-code']:
            if(user.sign_up(registerUserData)):
                return redirect("/")
            else:
                return "An error occured while registering you!"
        
        else:
            render_template("confirm_email.html", message="Invalid OTP code")
    else:
        return "Unauthorized access!"

#user landing page  
@app.route("/user/")
def user_page():
    return render_template("user.html", user_name=user.first_name, data=user.get_content(user.id))

#signout route
@app.route("/signout/", methods=['GET', 'POST'])
def signout():
    if request.method == 'POST':
        user.sign_out()
        return redirect("/")
    else:
        return "Unauthorized Access"  

#route for uploading the content    
@app.route("/upload_content/", methods=['GET', 'POST'])
def upload_content():
    #At this moment, only text can be uploaded
    if request.method == 'POST':
        content = Content()
        content.poster_id = user.id
        content.post_type = "text"
        content.time_posted = datetime.now()
        content.post = request.form['content']

        if user.upload_content(content):
            return redirect("/upload_content/")
        else:
            return "An error occured while processing the content"

    else:
        return render_template("upload_content.html")

#route for removing the content   
@app.route("/remove_content/", methods=['GET', 'POST'])
def remove_content():
    #Remove a posted content here
    if request.method == 'POST':
        pass
    else:
        return render_template('remove_content.html')

if __name__ == "__main__":
    app.run(debug=True)