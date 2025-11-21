from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy


# Create the Flask application instance
app = Flask(__name__)
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
#Row of data
#class Maindata(db.Model):
    #Finish Late
    
# Define a route (homepage)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/process")
def process():
    return render_template("process.html")



# Run the app
if __name__ == "__main__":
    app.run(debug=True)
