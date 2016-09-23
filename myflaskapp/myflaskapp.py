from flask import Flask

app = Flask(__name__) 

@app.route("/") 
def main_page():
    return ("This is the main page")
@app.route("/flask") 
def hola():
    return __name__ + ("\tWow, flask is so cool")
@app.route("/flask/sublinks")
def testing():
    return ("omg i love this")
    
if __name__ == '__main__':
    app.run() 
