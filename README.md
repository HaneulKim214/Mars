# Mission-to-Mars

## Project Status: Finished

**Part I:**
* Automated process of webscraping and scraped data from multiple websites such as [NASA Mars News Site](https://mars.nasa.gov/news/), [Mars weather twitter account](https://twitter.com/marswxreport?lang=en), [Mars Facts
website](https://space-facts.com/mars/), and [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars).

* Since all website had different html I had to inspect each page's html and correctly identify which tags to click and extract.

* At the end of each scraping step I've stored all the data into non-relational database, MongoDB.
  - Linked python with database to conveniently push and pull data.
 
**Part II:**
* From database extracted all needed info and displayed to html page I've created, all data from homepage has been
scraped and directly displayed from database using Flask.

* Added stlying to pages to display data in visually accepting places.
 
 
**Programs and Libraries used:**
- Main coding: Python(bs4, splinter, flask, pymongo, pandas), HTML5, CSS3(Bootstrap)
- Database: MongoDB
