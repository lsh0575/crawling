# # 가상환경설정
# python -m venv selenium             # 경로 및 폴더명 설정 / https://docs.python.org/ko/3/library/venv.html
# pip install seleninum               # 가상환경에 selenium 설치

# # ChromeDriver 다운로드
# # https://chromedriver.chromium.org/home
# # 버전에 맞는 ChromeDriver 다운로드 후 가상환경 폴더로 이동


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request


driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("찾고자 하는 이미지")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count += 1
    except:
        pass
driver.close()