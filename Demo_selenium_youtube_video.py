# Import Selenium webdriver to control the browser
from selenium import webdriver

# Service helps Selenium start the ChromeDriver
from selenium.webdriver.chrome.service import Service

# Automatically downloads the correct ChromeDriver version
from webdriver_manager.chrome import ChromeDriverManager

# By is used to locate elements (ID, NAME, XPATH, etc.)
from selenium.webdriver.common.by import By

# Keys is used to press keyboard keys like ENTER
from selenium.webdriver.common.keys import Keys

# time module is used to pause execution for a few seconds
import time


# Create Chrome options object to customize browser behaviour
options = webdriver.ChromeOptions()

# Keeps the browser open even after the script finishes
options.add_experimental_option("detach", True)

# Helps reduce Selenium automation detection by websites
options.add_argument("--disable-blink-features=AutomationControlled")


# Start Chrome browser using the automatically installed ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# Open Google homepage
driver.get("https://www.google.com")

# Wait 2 seconds for the page to fully load
time.sleep(2)


# Locate Google search box using NAME attribute "q"
user_input = driver.find_element(By.NAME, "q")

# Type "YouTube" into the search box
user_input.send_keys("youtube")

# Press ENTER key to perform the search
user_input.send_keys(Keys.ENTER)

# Wait for Google results to load
time.sleep(2)


# Locate the first search result title using XPath
# (//h3)[1] means select the first h3 element (first result)
link = driver.find_element(By.XPATH,'(//h3)[1]')

# Click the first result (which usually opens YouTube)
link.click()

# Wait for YouTube page to load
time.sleep(3)


# Locate YouTube search bar using its NAME attribute
yt_search = driver.find_element(By.NAME,"search_query")

# Type "Selenium tutorials" into the YouTube search bar
yt_search.send_keys("Selenium tutorials")

# Press ENTER to search on YouTube
yt_search.send_keys(Keys.ENTER)

# Wait for video results to load
time.sleep(3)


# Find all video titles on the results page
tutorial_videos = driver.find_elements(By.ID,"video-title")

# Click the first video in the list
tutorial_videos[0].click()