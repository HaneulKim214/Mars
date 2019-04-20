from flask import Flask, render_template, redirect
import scrape_mars
import pymongo

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db


@app.route("/")
def home():
    mars = db.data.find_one()
    return render_template("home.html", mars=mars)

@app.route("/scrape")
def scraper():
    mars = db.data
    scraped_data = scrape_mars.scrape()
    mars.update_one({}, {"$set":scraped_data}, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)