

# 04 Automate your browser to scrape this jobs page: https://people.bamboohr.com/careers
""" 
    Make a program that:
        1. Opens the browser
        2. Navigates to the jobs page URL
        3. Scrapes the jobs page
"""
# This simple program opens the browser, goes to the jobs page, and prints the page title.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the browser in headless mode (no window will pop up)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options,
)

# Go to the jobs page
jobs_url = "https://people.bamboohr.com/careers"
driver.get(jobs_url)

print("Waiting for the jobs page to load...")
time.sleep(5)  # Wait for the page to load

# Scrape the page title as a simple example
print("Page title is:", driver.title)

# Close the browser
driver.quit()



# This program opens the browser, goes to the jobs page, waits for it to load, prints the page title, and then closes the browser.
# Would you like me to go step by step through the code?

# 05 Make a website showing the wave height in Nazare
""" 
    Make a program that:
        1. Gets the wave height in Nazare
        2. Creates a website showing the wave height
"""