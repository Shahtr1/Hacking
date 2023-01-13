import requests
import re
# import urlparse # python 2
import urllib.parse as urlparse

target_url = "http://10.0.2.9/mutillidae/"
target_links = []

def extract_links_from(url):
    response = requests.get(url)
    # return re.findall('(?:href=")(.*?)"', response.content) # python 2
    return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore")) # python 3

def crawl(url):
    href_links = extract_links_from(url)

    for link in href_links:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

crawl(target_url)
