from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from mars_scrape import scrape

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():
    # Finds one record of data from mongo database
    mars_data = mongo.db.collection.find_one()
    if mars_data:
    # Return template with data
        return render_template("index.html", listing=mars_data)
    else:
        mars_data = mars_data = {
        "news_title": "",
        "news_p": "",
        "featured_image_url": "",
        "hemisphere_image_urls": {"title":["", "", "", ""], "img_url":["", "", "", ""],
        "mars_data_table": "<div><\div>"}}
        return render_template("index.html", listing=mars_data)


@app.route("/scrape")
def scraper():
    # Runs the scrape function 
    scraped = scrape()
    
    # Update the Mongo database
    mongo.db.collection.update({}, scraped, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
