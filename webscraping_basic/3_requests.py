import requests
# res = requests.get("http://www.naver.com")
res = requests.get("http://google.com")
# print("response code :", res.status_code)  # 200: success

# if res.status_code == requests.codes.ok:
#     print("OK")
# else:
#     print("Error : ", res.status_code)

res.raise_for_status()  # if error occurs, raise an exception
# print("Done")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
