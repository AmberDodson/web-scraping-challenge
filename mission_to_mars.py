import time
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


#NASA Mars News
def scraper():
    #set up Splinter
    executable_path={"executable_path":ChromeDriverManager().install()}
    browser=Browser('chrome', **executable_path, headless=True)
    #visit mars
    url="https://redplanetscience.com"
    browser.visit(url)
    
    time.sleep(2)
    
    #scrape page into soup
    html=browser.html
    soup=BeautifulSoup(html, "lxml")
    
    #get the data
    div=soup.find('div', {'class':'row'})
    news_title=div.find('div', {'class':'content_title'}).text
    news_p=div.find('div', {'class':'article_teaser_body'}).text
    #store data in dictionary
    mars_data={
        'news_title':news_title,
        'news_p':news_p  
    }
    
    url_img="https://spaceimages-mars.com"
    browser.visit(url_img)
    
    time.sleep(2)
    
    #scrape page into soup
    html_img=browser.html
    soup_img=BeautifulSoup(html_img, "lxml")
    
    #get the data
    featured_image=soup_img.find_all('img')[1]["src"]
    featured_image_url=url_img+ '/' +featured_image
    #store data in dictionary
    mars_data['featured_image_url']=featured_image_url



    links=['cerberus.html', 'schiaparelli.html', 'syrtis.html', 'valles.html']
    #get the data
    hemisphere_image_urls = []
    for link in links:
        url="https://marshemispheres.com"+'/'+link
        browser.visit(url)

        time.sleep(2)

        #scrape page into soup
        html=browser.html
        soup=BeautifulSoup(html, "lxml")
        
        news_p=soup.find_all('img')[4] ['src']
        news_p_url="https://marshemispheres.com"+'/'+news_p
        div=soup.find('div', {'class':'cover'})
        news_title=div.find('h2').text
        #store data in dictionary
        img_data={
            'news_title':news_title,
            'news_p':news_p_url 
        }

        hemisphere_image_urls.append(img_data)

    mars_data['hemisphere_image_urls']=hemisphere_image_urls
    browser.quit()
    return mars_data