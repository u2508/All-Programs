import requests
from bs4 import BeautifulSoup
import urllib3
#from requests_html import HTMLSession
def get_source(url):
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns: 
        response (object): HTTP response object from requests_html. 
    """

    
        #session = HTMLSession()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    #return response
    css_identifier_result = ".dG2XIf XzTjhb"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf"
    css_identifier_text = ".hgKElc"
    
    result = soup.find(id="rcnt")
    print(result.prettify())
    output = []
    
    for result1 in result:

        item = {
            'title': result1.find(css_identifier_title, first=True).text,
            'link': result1.find(css_identifier_link, first=True).attrs['href'],
            'text': result1.find(css_identifier_text, first=True).text
        }
        
        output.append(item)
        
    return output

'''def scrape_google(query):
    
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links'''
def get_results(query):
    
    #query = urllib3.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)
    
    return response
#def parse_results(response):
    
    
def google_search(query):
    response = get_results(query)
    #return parse_results(response)
    return response
results = google_search("web scraping")
print(results)
