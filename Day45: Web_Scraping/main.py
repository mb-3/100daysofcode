from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, 'html.parser')

movie_text = [movie.getText() for movie in soup.findAll(name="h3", class_="title")]
movie_text.reverse()

with open("movies.txt", "w", encoding='utf-8') as file:
    for i in movie_text:
        file.write(f"{i}\n")
