from flask import Flask, render_template, request
import csv
import hashlib
import os.path

app = Flask(__name__) 
if not(os.path.isfile('data/credentials.csv')):
    file = open('data/credentials.csv','w')
    header = ["Username","Password","HashPass"]
    writer = csv.writer(file, delimiter = ",")
    writer.writerow(header)
    file.close()

@app.route("/")
@app.route("/login/")
def login():
    print request
    print request.headers
    print app
    return render_template('login.html')

@app.route("/authenticate/", methods = ['POST'])
def auth():
    #debug
    #print request.form
    #print request.form['user']
    #print request.form['pass']

    if request.method == 'POST':
 
       ##store user info and hash
        user = request.form['user']
        pasz = request.form['pass']
        paszhash = hashlib.sha224(request.form['pass']).hexdigest()    

        ##login 
        if request.form['submit'] == 'Login' and not(user == "" or pasz == ""):
            with open("data/credentials.csv", "r") as c:
                reader = csv.reader(c)
                for row in reader:
                    if row[0] == user and row[2] == paszhash:
                        return render_template("login.html", message = "Login successful! Congratulations")
                return render_template("login.html", message = "Account was not found. Please try again.")
            c.close()
        else:
            return render_template("login.html")

        ##register
        if request.form['submit'] == 'Register' and not(user == "" or pasz == ""):
            with open("data/credentials.csv", "r") as c:
                reader = csv.reader(c)
                for row in reader:
                    if row[0] == user:
                        return render_template("login.html", message = "This user is already registered!")
            c.close()
            with open("data/credentials.csv", "a") as c:
                writer = csv.writer(c, delimiter = ",")
                credentials = [user,pasz,paszhash]
                writer.writerow(credentials)
                return render_template("login.html", message = "Register successful. You may proceed to login")
            c.close()
        else:
            return render_template("login.html", message = "Don't leave stuff blank!")
                                    
if __name__ == '__main__': 
    app.debug = True #save file, restart webserver
    app.run() 
