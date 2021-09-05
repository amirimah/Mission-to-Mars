# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

news_soup.find('div', class_='article_teaser_body').get_text()


# ### Featured Images

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]

full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ## Deliverable 1
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
html = browser.html
img_soup = soup(html, 'html.parser')
hemispheres = []
for i in range (4):
    html = browser.html
    img_soup = soup(html, 'html.parser')
    value = img_soup.find_all('h3')[i].get_text()
    
    browser.find_by_tag('h3')[i].click()
    html = browser.html
    img_soup = soup(html, 'html.parser')
    img_url_rel= img_soup.find('img', class_='wide-image').get('src')
    img_url = f'https://astrogeology.usgs.gov/{img_url_rel}'
    url = {'img_url': img_url, 'title': value}
    hemispheres.append(url)
    browser.back()
hemispheres


# ### Scrape Mars Data from a Table
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()

browser.quit()



