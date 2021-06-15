# web-scraping-challenge
Scrape four websites for Mission to Mars info and display results on an html page using Flask and MongoDB.

### Scraping

Used Splinter to visit redplanetscience.com and use BeautifulSoup to parse through the html to find the title and article teaser for the most recent Mars news. Used a for loop to find and build the lists.

Next, visited spaceimages-mars.com and in the same way found the url for Mars image of the day.

After that used Pandas to read the html on the galaxyfacts-mars.com page and created a data frame out of one of the tables found on the page. Lightly formatted the table, creating a new index and relabeling the index column. Then exported to html that included some table styling.

Lastly, and the most challenging part of the project for me, was to once again use Splinter and BeautifulSoup to find the title and image links for the four hemispheres of Mars on marshemispheres.com. With getting partial information but not able to cycle through the pages effectively, I started at the end, making sure I could parse the html and find the information I needed on one individual page. Once I knew that was working I ended up creating a list of the four webpages I needed to visit, and then looped through those to build a new dictionary of titles and image urls.

### MongoDB and Flask App

Asked to recreate a webpage that will use the information I scraped above. I set up the Flask app, built the html layout using Bootstrap, and turned the Jupyter Notebook I used for writing my code for scraping, into a python file and created a function that returned a dictionary of values that I had scraped so could feed those into MongoDB and populate my webpage. 

Another problem to solve was getting the html page to load before doing the first scrape. Flask always spit back an error saying the variables I created were "none" so the html page would not render. This wasn't the case in any of our class demonstrations so I was at a loss. But eventually decided on creating a if/else statement in the app to force it. If mars_data is empty, then set up an empty dictionary of mars_data. That way it would render my index.html page without error. 

**My Mission to Mars webpage**
![My finished page.](https://github.com/KristaJoy/web-scraping-challenge/blob/main/Mission_to_Mars/webpage.png)