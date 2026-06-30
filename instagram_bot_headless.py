from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Set your Instagram username
instagram_username = 'jaydendoesarts'

# Set up headless options for cloud environments (or background local running)
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Runs Chrome without a visual GUI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

try:
    print("Opening website...")
    driver.get('https://heyfreefollowers.com/free-instagram-followers/')

    # Set up a max wait time of 15 seconds
    wait = WebDriverWait(driver, 15)

    # 1. Find and fill the username input field
    print("Entering username...")
    username_input = wait.until(
        EC.presence_of_element_located((By.ID, 'smm-url'))
    )
    # Scroll to the input box to ensure visibility
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", username_input)
    time.sleep(0.5)
    
    username_input.clear()  # Ensure the field is clean before typing
    username_input.send_keys(instagram_username)

    # 2. Find and handle the quantity field if present
    try:
        print("Checking for quantity field...")
        quantity_input = wait.until(
            EC.presence_of_element_located((By.NAME, 'quantity'))
        )
        # Scroll to quantity input box
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", quantity_input)
        time.sleep(0.5)
        
        quantity_input.send_keys(Keys.CONTROL + "a")  # Select all existing text
        quantity_input.send_keys(Keys.BACKSPACE)      # Clear it
        quantity_input.send_keys('100')
        print("Quantity successfully set to 100.")
    except Exception:
        print("Quantity field not found or not required, proceeding directly to submit...")

    # 3. Find and click the submit button
    print("Locating start button...")
    start_button = wait.until(
        EC.presence_of_element_located((By.ID, 'smm-submit-btn'))
    )
    
    # Scroll the button cleanly into the view window
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", start_button)
    time.sleep(1)  # Brief pause to allow any scroll animations to complete

    print("Clicking start button via JavaScript execution...")
    # Using JS click to bypass SVG overlays or element blocking issues
    driver.execute_script("arguments[0].click();", start_button)

    print("\nSuccessfully clicked! Waiting out the 6-minute timer process...")
    time.sleep(360)

except Exception as e:
    print(f"\nAn error occurred during execution: {e}")
    time.sleep(10)

finally:
    print("Closing browser session.")
    driver.quit()
