from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
# options.add_experimental_option("debuggerAddress", "localhost:8989")
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
options.add_argument("--profile-directory=Default")
# options.add_argument("--user-data-dir=C:\\Users\\mfara\\AppData\\Local\\Google\\Chrome\\User Data\\")
# options.add_argument("--user-data-dir=C:\\Users\\mfara\\AppData\\Local\\Microsoft\\Chrome\\User Data\\")

# Specify the browser you want to use
browser = 'edge'  # Change this to 'edge' to use Microsoft Edge

# Create a new instance of the appropriate driver
if browser == 'edge':
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
elif browser == 'chrome':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
else:
    raise ValueError('Invalid browser specified.')

# Add executable path
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Navigate to the target URL
url = 'https://wd5.myworkday.com/ciena/d/home.htmld'
driver.get(url)
# Open a new tab in the existing Chrome window
# driver.execute_script("window.open('about:blank', '_blank');")

# Switch to the newly opened tab
# driver.switch_to.window(driver.window_handles[-1])

# The page loaded may or may not be the sign in page. If it is not, fill in the credentials and click the sign in button.
try: 
    sign_in_button = driver.find_element(By.CLASS_NAME, 'button-primary')
    print('Please sign in and run the Script again. :)')

    # Find the username input field and enter your email
    email = 'mfarabi@ciena.com'  # Replace with your actual email
    username_field = driver.find_element(By.ID, 'input28')
    username_field.send_keys(email)

except:
    print('Sign in button not found. Assuming you are already signed in. Continuing...')
    pass

# Close the browser window
# driver.quit()