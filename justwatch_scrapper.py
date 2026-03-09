from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()

url = "https://www.justwatch.com/in/movies?rating_imdb=7&tomatoMeter=90"
driver.get(url)
time.sleep(5)

# accept cookies

driver.find_element(By.XPATH,'//*[@id="app"]/div[4]/div[1]/div[2]/button[1]/div/span').click()


# scroll page
last_height = 0
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break
    last_height = new_height

# collect movie links
movies = driver.find_elements(By.CLASS_NAME, "title-list-grid__item")
links = [m.find_element(By.TAG_NAME,"a").get_attribute("href") for m in movies]

print("Total movies:", len(links))

links = links[:1000]

html_pages = []

for link in links:
    driver.get(link)
    time.sleep(2)
    html_pages.append(driver.page_source)
    print("Visited:", link)

# save HTML
with open("movies_html.html","w",encoding="utf-8") as f:
    for i, html in enumerate(html_pages):
        f.write(f"\n\n<!-- MOVIE {i+1} -->\n")
        f.write(f"<!-- URL: {links[i]} -->\n")
        f.write(html)