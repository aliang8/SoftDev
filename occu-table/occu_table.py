from flask import Flask, render_template
import work1

app = Flask(__name__) 
file = work1.d
@app.route("/occupations")


def occu_table():
    return render_template('main.html',  message = work1.randOccupation(), file = file)
    
if __name__ == '__main__': 
    app.debug = True #save file, restart webserver
    app.run() 
