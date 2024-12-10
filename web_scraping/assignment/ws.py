"""
Scrape the following web page to find out AvailableSpaceBlockPlacementPolicy configurations:
https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsBlockPlacementPolicies.html 
create a table: Config to store the properties: name, value, description.

"""
import requests
from bs4 import BeautifulSoup

url = "https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsBlockPlacementPolicies.html"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify())
