from flask import Flask, request, render_template, url_for, session, redirect
app = Flask(__name__)
app.secret_key = 'pet'
@app.route('/')
def homepage():
    return render_template("home.html")
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/registerdata', methods=["POST", "GET"])
def register():
    msg = ""
    alert = ""
    count = 0
    if request.method == "POST":
        name = request.form['firstname'] + " " + request.form['lastname']
        fname = request.form['firstname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        mobile = request.form['mobile']

        if (user):
            msg = "Sorry a member with username %s exists" % (user[2])
            count = 1
        elif (account):
            msg = "You're already a member with email %s" % (account[3])
            count = 1
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = "Please Enter a Valid E-mail ID"
            count = 1
        elif not re.match(r'^[A-Za-z0-9_.-]*$', username):
            msg = "Please Enter Valid Username"
            count = 1
        elif not (password == cpassword):
            msg = "Please make sure your passwords match."
            count = 1
        elif not (request.form.get('checkbox')):
            msg = "Please tick accept to terms and conditions "
            count = 1
        else:

            msg = "Congratulations, Dear %s You've Successfully Registered." % (fname)

        if (count == 1):
            alert = "failure"
        else:
            alert = "success"
        return render_template('signup.html', msg=msg, indicator=alert)
@app.route('/login')
def login():
    return render_template('login.html', title="Login")
@app.route('/loginauth', methods=["POST", "GET"])
def loginauth():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if (account):
            session['loggedin'] = True
            session['id'] = account[0]
            session['name'] = account[1]
            session['username'] = account[2]
            session['email'] = account[3]
            username = account[2]
            return redirect(url_for('home'))
        else:
            msg = "Incorrect Username/Email and Password Combination"
            return render_template("login.html", msg=msg, indicator="failure", title="Login")
    else:
        return render_template("login")
def dashboard():
    return render_template('dashboard.html')
@app.route('/forgot', methods=["POST", "GET"])
def forgot():
    return render_template("forgot.html", title="Forgot")
@app.route('/forgotpassword', methods=["POST", "GET"])
def forgotpassword():
    msg = ""
    if request.method == "POST":
        email = request.form['username']

        if (account):
            TEXT = """\
                    <!DOCTYPE html>
                    <html>
                    <body>
                        <div class="containter" style="display: block;">
                            <span style="font-size: 48px;left: 20px;font-weight:bold; font-family:Arial, Helvetica, sans-serif; color:#7048a9;">Budget Buddy!</span>
                            <h3 style="font-size: 24px; font-family:serif"> Dear """ + account[1] + """, </h3>
                            <div class="side" style="width: 400px; height: 150px; border: 2px solid #7048a9; padding:30px; border-radius:10px; position:relative; left:100px;" >
                                <div class="details"style="position:relative; top:20px; left:60px; font-size:20px; font-family:'Courier New', Courier, monospace;text-align:left   ;">
                                    <p >Username : <span style="color: green; font-weight:bold;">""" + account[2] + """</span> </p>
                                    <p>Password : <span style="color: green; font-weight:bold;">""" + account[4] + """</span> </p>
                                </div>
                            </div>
                        </div>
                    </body>
                    </html>"""
            msg = "Your login credentials are sent to your registered mail id"
            forgotemail(TEXT, email)
            return render_template("forgot.html", msg=msg, indicator="success", title="Forgot")
        else:
            msg = "No account found with Email %s" % (email)
            return render_template("forgot.html", msg=msg, indicator="failure", title="Forgot")
    else:
        return redirect(url_for("forgot"))
if (__name__ == '__main__'):
    app.run(host="0.0.0.0", port=8080)