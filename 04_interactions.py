# 04 - Interactions

# 01 Create a program that jiggles the mouse so that the computer doesn't go to sleep
""" 
    Make a program that:
        1. Jiggles the mouse so that the computer doesn't go to sleep
"""
# This simple program moves the mouse a little bit to keep the computer awake.
# It uses a library called 'pyautogui' to move the mouse.

print("This program will move your mouse a little bit to keep your computer awake.")

print("Press Ctrl+C in the terminal to stop the program.")

try:
    import pyautogui
    import time
    
    while True:
        pyautogui.move(1, 0)  # move mouse right by 1 pixel
        time.sleep(1)
        pyautogui.move(-1, 0) # move mouse left by 1 pixel
        time.sleep(1)
except ImportError:
    print("You need to install the 'pyautogui' library first.")
    print("Run this command in your terminal: pip install pyautogui")
    print("Skipping the mouse jiggler program...")


# 02 Create a python program that asks the user for a URL and downloads the corresponding video in the lowest quality. Use a reliable library and no APIs.
""" 
    Make a program that:
        1. Asks the user for a URL
        2. Downloads the corresponding video in the lowest quality
"""


# 03 Automate your browser to answer this survey: https://forms.gle/uXPeoEpXkdFEfRw49
""" 
    Make a program that:
        1. Opens the browser
        2. Navigates to the survey URL
        3. Answers the survey
"""
print("This program will open your browser and try to answer the survey automatically.")

print("You need to install the 'selenium' library for this to work.")
print("Run this command in your terminal: pip install selenium")

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    import time
except ImportError:
    print("Selenium is not installed. Please install it and try again.")
    exit()

# Open the browser (headless)
chrome_options = Options()
chrome_options.add_argument("--headless")  # run without opening a window
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options,
)

# Go to the survey URL
survey_url = "https://forms.gle/uXPeoEpXkdFEfRw49"
driver.get(survey_url)

print("Waiting for the page to load...")
time.sleep(5)  # Wait for the page to load

# Try to answer the first question (if it's a multiple choice)
try:
    # Find the first radio button and click it
    first_option = driver.find_element(By.CSS_SELECTOR, "div[role='radio']")
    first_option.click()
    print("Selected the first option.")
except Exception as e:
    print("Could not select the first option:", e)

# Try to submit the form
try:
    submit_button = driver.find_element(By.XPATH, "//span[contains(text(),'Submit')]/ancestor::button")
    submit_button.click()
    print("Form submitted.")
except Exception as e:
    print("Could not submit the form:", e)

print("Done! You can close the browser window.")


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