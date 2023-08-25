import requests
from bs4 import BeautifulSoup

# Set the desired encoding for Korean text
desired_encoding = 'utf-8'

url = "https://www.jobbank.gc.ca/home"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
# Set the encoding for the response to 'utf-8'
res.encoding = desired_encoding

res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# with open('title.txt', 'w', encoding='utf-8') as file:
#    file.write(soup.title.get_text())
# file.write(soup.a.get_text())
#   file.write(soup.a.attrs)

# print(soup.title.get_text())
# print(soup.a.get_text())
# print(soup.a.attrs)
# print(soup.find("a", attrs={"class": "app-name"}))
menu = soup.find("ul", attrs={"class": "list-inline menu"})
# print(menu.a.get_text())
# print(menu.next_element)
menu2 = menu.next_element.next_element
menu3 = menu2.next_sibling.next_sibling
print(menu2)
print(menu3)
# print(menu.next_sibling.next_sibling)

print(menu.parent)
print(menu.parent.parent)
