from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy


# Create the Flask application instance
app = Flask(__name__)

# Define a route (homepage)
@app.route("/")
def home():
    return render_template("index.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
