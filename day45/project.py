# scrapping data from a movies review website
import requests as req
from bs4 import BeautifulSoup
response=req.get(url="https://editorial.rottentomatoes.com/article/the-10-scariest-horror-movies-ever/")
response.raise_for_status()
soup=BeautifulSoup(response.text,"html.parser")
movie_lists=soup.find_all(name="h2")
titles=[]
for movie in movie_lists:
    text=movie.find("strong")
    if text:
        titles.append(text.getText())
with open("horror_movies.txt","w") as files:
    for movie in titles:
        files.write(f"{movie}😎\n")
