import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies?hl=en_CA&gl=US"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={
                       "class": "ULeU3b neq64b"})

print(len(movies))

with open("movies.html", "w", encoding="utf8") as f:
    # f.write(res.text)
    f.write(soup.prettify())  # show html readable

# for movie in movies:
#     title = movie.find("div", attrs={"class": "ubGTjb"}).get_text()
#     print(title)
