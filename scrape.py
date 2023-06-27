import os
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from urllib.parse import urljoin, urlparse

def scrape_website(start_url):
    visited = set()
    to_visit = {start_url}
    
    # create the directory to store the markdown files
    directory = "data"
    if not os.path.exists(directory):
        os.makedirs(directory)

    while to_visit:
        url = to_visit.pop()

        if url in visited:
            continue

        visited.add(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        content_tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        contents = []
        for tag in content_tags:
            contents += soup.find_all(tag)

        markdown_text = "\n".join(md(str(tag)) for tag in contents)

        # use os.path.basename() to get the last part of the url
        file_name = os.path.basename(urlparse(url).path)
        if file_name == "":
            file_name = "index"
        file_name = os.path.join(directory, file_name + '.md')
        
        with open(file_name, 'w') as f:
            f.write(markdown_text)

        # Collect links from the sidebar
        sidebar = soup.find_all('aside')  
        for link in sidebar[0].find_all('a', href=True):
            absolute_link = urljoin(url, link['href'])
            if absolute_link not in visited:
                to_visit.add(absolute_link)

scrape_website('https://docs.langchain.com/docs/')
