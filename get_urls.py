import urllib
from bs4 import BeautifulSoup

cbc_url = 'https://www.cbc.ca/news/canada/toronto'

def extract_urls(url):
    page_html = urllib.request.urlopen(url)
    souped_html = BeautifulSoup(page_html, 'html.parser')
    
    # Only focusing on the Featured Articles
    urls = []
    # Get urls from Primary and Secondary Stories 
    primary_stories = souped_html.find(attrs={'class': 'primaryTopStories'})
    prim_urls = list(map(lambda x: 'https://www.cbc.ca/' + x['href'], primary_stories.findAll('a')))

    secondary_stories = souped_html.find(attrs={'class':'secondaryTopStories'})
    sec_urls = list(map(lambda x: 'https://www.cbc.ca/' + x['href'], secondary_stories.findAll('a')))
    
    urls.extend(prim_urls)
    urls.extend(sec_urls)
    
    return urls

cbc_urls = extract_urls(cbc_url)
    
    