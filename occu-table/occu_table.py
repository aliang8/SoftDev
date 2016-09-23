from flask import Flask, render_template
import csv
import work1

app = Flask(__name__) 

file = {}
##Read CSV file and deleted non-numerical data                                                   
with open('occupations.csv','rb') as f:
    reader = csv.reader(f)
    for row in reader:
      file[row[0]] = [row[1],row[2]]
    del file["Job Class"]

@app.route("/occupations")

def occu_table():
    return render_template('table.html',  message = work1.randOccupation(), file = file)
    
if __name__ == '__main__': 
    app.debug = True #save file, restart webserver
    app.run() 
