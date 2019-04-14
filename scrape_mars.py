def scrape():
    """ Scrape data from different urls and convert it into one dictionary
    """
import pymongo
import pandas as pd
import requests
from bs4 import BeautifulSoup
from splinter import Browser

# ------------ Scrape data from NASA Mars News ------------
executable_path = {"executable_path":"chromedriver.exe"}
browser = Browser('chrome', **executable_path, headless=False)
# Scrape NASA Mars News Site
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

news_list = []
# collect latest News title and paragraph Text
headers = soup.find_all("div", class_="list_text")
for header in headers:
    news_title = header.find("div", class_="content_title").text
    parag = header.find("div", class_="article_teaser_body").text
    news_list.append({"news_title": news_title, "news_desc": parag})

# ---------- JPL MARS SPACE IMAGE ---------
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
featured_image_url = soup.find("div","carousel_container").article["style"]
featured_image_url = featured_image_url[23:]
featured_image_url = featured_image_url[:-3]
featured_image_url = "https://www.jpl.nasa.gov" + featured_image_url

# -------------- Mars Weather -----------
url = "https://twitter.com/marswxreport?lang=en"
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
# Scrape latest Mars weather tweet.
# "find" will always find the latest(very top) weather tweet
mars_weather = soup.find("p", class_="tweet-text").text 

# ------------- Mars Facts -----------------
url = "https://space-facts.com/mars/"
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
# Use pandas to scrape table
# We see here is only one table therefore simply call [0]'th item
table = pd.read_html(str(soup.find_all("table")[0]))

# ------------- Mars Hemisphere -------------
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
# soup.find("div", class_="results")
products = soup.find_all("div", class_="item")

link_list = []
# looping through each block of hemispheres
for product in products:
    # extract link, make it full link and append to a list
    link_list.append("https://astrogeology.usgs.gov" + product.a["href"])

# not we can loop through each link and extract info and store into list as dict
hemisphere_image_urls = []
for link in link_list:
    browser.visit(link)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    # img url
    img_url = "https://astrogeology.usgs.gov" + soup.find("div", class_="wide-image-wrapper").find("img",class_="wide-image")["src"]
    
    # Hesmisphere title, drop "Enhanced" for each title
    hem_title = soup.find("section", class_="block").find("h2", class_="title").text
    hem_title = hem_title[:-9]
    
    hemisphere_image_urls.append({"title": hem_title, "img_url":img_url})


# --------- Final Touch --------
print(news_list)
print(hemisphere_image_urls)
print(table)

final_dictionary = {}