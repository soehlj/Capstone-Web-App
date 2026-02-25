from flask import Flask, render_template, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
import pandas as pd


# Create the Flask application instance
app = Flask(__name__)
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
#Row of data
#class Maindata(db.Model):
    #Finish Late
    
# Define a route (homepage)
@app.route("/", methods=['GET'])
def home():
    #determine the query of url/user material state
    state = request.args.get('material')
    if(state == "test"):
        return render_template("home-guide.html")
    if(state == "silicone"):
        return render_template("silicone.html")
    elif(state == "rubber"):
        return render_template("rubber.html")
    elif(state == "resin"):
        return render_template("resin.html")
    else:
        return render_template("no_material.html")
    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/process")
def process():
    return render_template("process.html")

@app.route("/all_data")
def all_data():
    database = pd.read_csv('data.csv')
    rows = database.to_dict(orient='records')
    headers = database.columns.tolist()
    

    return render_template('all_data.html', headers=headers, rows=rows)



# Run the app
if __name__ == "__main__":
    app.run(debug=True)
