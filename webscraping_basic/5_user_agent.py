import requests
url = "http://google.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
# res = requests.get("http://www.naver.com")
res = requests.get(url, headers=headers)
res.raise_for_status()  # if error occurs, raise an exception
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
