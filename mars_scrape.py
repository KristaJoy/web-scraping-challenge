#!/usr/bin/env python
# coding: utf-8

# In[117]:


from bs4 import BeautifulSoup
import requests
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import pandas as pd

def scrape():
    # ## NASA Mars News

    # In[2]:


    # Setup Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[3]:


    # Connect to the website
    url = 'https://redplanetscience.com/'
    browser.visit(url)


    # In[6]:


    # Use BeautifulSoup to parse html
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[44]:


    # Create lists of looped through results
    news_title = [] 
    news_p = [] 

    results = soup.find_all('div', class_='row')

    for result in results:
        try:
            # Identify title
            title = result.find('div', class_='content_title')
            # Identify paragraph description
            para = result.find('div', class_='article_teaser_body')
            

            # Create list
            if (title and para):
                news_title.append(title.text)
                news_p.append(para.text)
                
        except AttributeError as e:
            print(e)


    # In[46]:


    # Disconnect from website
    browser.quit()


    # In[48]:


    # Lists are complete
    print(news_title, news_p)


    # ## JPL Mars Space Images - Featured Image

    # In[65]:


    # Setup Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[66]:


    # Connect to the website
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)


    # In[67]:


    # Use BeautifulSoup to parse html
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[73]:


    for x in range(1):

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        header = soup.find('div', class_='header')
        target = header.find('a', class_='fancybox-thumbs')
        href = target['href']
        featured_image_url = ('https://spaceimages-mars.com/' + href)


    # In[76]:


    print(featured_image_url)


    # In[75]:


    # Disconnect from website
    browser.quit()


    # ## Mars Facts

    # In[79]:


    # Website location
    url = 'https://galaxyfacts-mars.com/'


    # In[98]:


    # Use pandas to find a table on website
    tables = pd.read_html(url)
    mars_df = tables[1]
    mars_df


    # In[99]:


    # Clean up dataframe
    mars_df.set_index(0, inplace=True)
    mars_df.columns = ['Mars Planet Profile']
    mars_df.index.names = ['']


    # In[100]:


    # Preview final dataframe
    mars_df


    # In[101]:


    # Export to html
    mars_df.to_html('table.html')


    # ## Mars Hemispheres

    # In[130]:


    # Setup Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[131]:


    # Connect to the website
    url = 'https://marshemispheres.com/'
    browser.visit(url)


    # In[141]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all('div', class_='item')
    page_links = []

    for result in results:
        link = result.find('a')['href']
        page_links.append(f'{url}'+ link)

    hemisphere_image_urls = {}

    for link in page_links:
        browser.visit(link)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h2', class_='title').text
        if 'title' in hemisphere_image_urls:
            hemisphere_image_urls['title'].append(title)
        else:
            hemisphere_image_urls['title'] = [title]
        desc = soup.find('div', class_='description')
        img_loc = desc.a['href']
        img_path = (f'{url}{img_loc}')
        if 'img_url' in hemisphere_image_urls:
            hemisphere_image_urls['img_url'].append(img_path)
        else:
            hemisphere_image_urls['img_url'] = [img_path]


    # In[142]:


    print(hemisphere_image_urls)


    # In[143]:


    # Disconnect from website
    browser.quit()

    # store data in dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "hemisphere_image_urls": hemisphere_image_urls

    }

    return mars_data