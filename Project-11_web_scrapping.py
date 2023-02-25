# web scrapping means extracting data from a web site
import requests # requests the url 
from bs4 import BeautifulSoup # used to get data what we need

url="https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/"

response=requests.get(url)  #requests the url and returns response like 200 if it allows

soup=BeautifulSoup(response.content,"html.parser") #returns contents


titles=soup.find_all("title") # we take what we require as a list from object soup

print(titles)

