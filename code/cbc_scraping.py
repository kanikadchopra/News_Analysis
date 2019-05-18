import urllib
from bs4 import BeautifulSoup
from get_urls import cbc_urls 

cbc_url = 'https://www.cbc.ca/news/canada/toronto'

def extract_info(url):
    page_html = urllib.request.urlopen(url)
    souped_html = BeautifulSoup(page_html, 'html.parser')
    
    # Author Information: Author name, Author biography
    try:
        author_name = souped_html.find(attrs={'class': 'authorText'}).text
    # When there are cases with extracting the author name, we extract the bylineDetails instead
    # which can have information such as 'Canadian Press'
    except:
        byline_details = souped_html.find('div', attrs={'class': 'bylineDetails'}).text
        author_name = byline_details.split(' · ')[0]
        
    # Story Information: Headline Title, Date, Summary
    headline = souped_html.find(attrs={'class': 'detailHeadline'}).text
    date = souped_html.find(attrs={'class': 'timeStamp'}).text
    summary = souped_html.find(attrs={'class':'detailSummary'}).text

    
    return {'headline': headline,
            'summary': summary,
            'author': author_name,
            'date': date,
            'url': url}
   
    
    
   