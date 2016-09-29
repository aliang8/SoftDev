from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route("/")
@app.route("/login/")
def login():
    print request
    print request.headers
    print app
    return render_template('login.html')

@app.route("/authenticate/", methods = ['GET','POST'])
def auth():
    if (request.method == 'GET'):
        print request.args
        print request.args['user']
        print request.args['pass']
        if (request.args['user'] == "Anthony" and request.args['pass'] == "Liang"):
            return "Success"
        else:
            return "Failure"
    else :
        print request.form
        print request.form['user'] ##works like a dictionary
        if (request.form['user'] == "Anthony" and request.form['pass'] == "Liang") :
            return "Success"
        else :
            return "Failure"

if __name__ == '__main__': 
    app.debug = True #save file, restart webserver
    app.run() 
