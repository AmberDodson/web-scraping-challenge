from flask import Flask, render_template, redirect
from pymongo import MongoClient
from flask_pymongo import PyMongo
import mission_to_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
#mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
client=MongoClient("mongodb://localhost:27017")
mars=client.MissionMars.mars  #collection name m_data
# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = mars.find_one()

    # Return template and data
    return render_template("index.html", mission_mars=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_datas = mission_to_mars.scraper()


    # Update the Mongo database using update and upsert=True
    mars.update({}, mars_datas, upsert=True)


    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)