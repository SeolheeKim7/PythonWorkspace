import time
from selenium import webdriver

browser = webdriver.Chrome()  # "./chromedriver.exe"

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element("class name", "MyView-module__link_login___HpHMW")
elem.click()

# 3. id, pw 입력
browser.find_element("id", "naver_id")
browser.find_element("id", "password")

# # 4. 로그인 버튼 클릭
browser.find_element("id", "log.login").click()

time.sleep(3)

# 5. id 를 새로 입력
# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element("id", "id").clear()
browser.find_element("id", "id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit()  # 전체 브라우저 종료
