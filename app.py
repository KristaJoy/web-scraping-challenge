from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from mars_scrape import scrape

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():
    # Finds one record of data from mongo database
    mars_info = mongo.db.collection.find_one()
    
    # Return template with data
    return render_template("index.html", listing=mars_info)


@app.route("/scrape")
def scraper():
    # Runs the scrape function 
    mars_data = scrape()
    
    # Update the Mongo database
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
