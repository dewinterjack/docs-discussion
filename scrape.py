import os
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from urllib.parse import urljoin, urlparse

def scrape_website(start_url):
    visited = set()
    to_visit = {start_url}
    
    base_directory = "data"
    if not os.path.exists(base_directory):
        os.makedirs(base_directory)

    while to_visit:
        url = to_visit.pop()

        if url in visited:
            continue

        visited.add(url)
        response = requests.get(url)
        url = response.url

        soup = BeautifulSoup(response.text, 'html.parser')

        content_tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        contents = []
        for tag in content_tags:
            contents += soup.find_all(tag)

        markdown_text = "\n".join(md(str(tag)) for tag in contents)

        # use the path from the URL to create directories
        url_path = urlparse(url).path
        directory = os.path.join(base_directory, *url_path.split('/')[1:-1])
        os.makedirs(directory, exist_ok=True)

        file_name = os.path.basename(url_path)
        if file_name == "":
            file_name = "index"
        file_path = os.path.join(directory, file_name + '.md')
        
        with open(file_path, 'w') as f:
            f.write(markdown_text)

        # Collect links from the sidebar
        sidebar = soup.find_all('aside')
        if sidebar:
            for link in sidebar[0].find_all('a', href=True):
                absolute_link = urljoin(url, link['href'])
                if absolute_link not in visited:
                    to_visit.add(absolute_link)

if __name__ == '__main__':
    try:
        scrape_website('https://python.langchain.com/docs/get_started/introduction')
    except KeyboardInterrupt:
        pass
