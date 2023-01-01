# Go to https://getrssfeed.com/ to obtain the RSS feed link to use in the user input

# Import librarires
import xml.etree.ElementTree as ET
import urllib.request
import requests
import ssl
import os

# Disable the certificate check
ssl._create_default_https_context = ssl._create_unverified_context

# Reading the contents of the user defined RSS feed
try:
    rss_feed_link = input('RSS Feed link: ')
    with urllib.request.urlopen(rss_feed_link) as url:
        xml_rss_feed = url.read()

except:
    print('Please enter a valid podcast RSS URL')
    quit()

# User defined number of episodes to download
try:
    number = int(input('How many recent podcasts do you want to download: '))

except:
    print('Please enter an integer only')
    quit()

# Parse the XML RSS feed
root = ET.fromstring(xml_rss_feed)

# Find the list of titles and download links
titles = root.findall('channel/item/title')
links = root.findall(".//*[@url]")

# Downloading the podcasts to a user defined local directory
try:
    directory = input('Full local directory path: ')
    for n, (title, link) in enumerate(zip(titles, links)):
        file_name = title.text
        file_url = link.get('url')
        response = requests.get(file_url)
        urllib.request.urlretrieve(file_url, os.path.join(directory, file_name+'.mp3'))
        print('Completed: ',file_name)
        if n == number-1: break
    print("Downloads completed! Files downloaded to: ", directory)

except:
    print('Please enter a valid directory')
