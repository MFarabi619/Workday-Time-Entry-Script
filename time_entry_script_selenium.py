from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

# Specify the browser you want to use
browser = 'chrome'  # Change this to 'edge' to use Microsoft Edge

# Create a new instance of the appropriate driver
if browser == 'edge':
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
elif browser == 'chrome':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
else:
    raise ValueError('Invalid browser specified.')

# Navigate to the target URL
url = 'https://wd5.myworkday.com/ciena/d/home.htmld'
driver.get(url)
driver.maximize_window()

# The page loaded may or may not be the sign in page. If it is not, fill in the credentials and click the sign in button.
try: 
    sign_in_button = driver.find_element(By.CLASS_NAME, 'button-primary')
    print('Sign in button found')

    # Find the username input field and enter your email
    email = ''  # Replace with your actual email
    username_field = driver.find_element(By.ID, 'input28')
    username_field.send_keys(email)

    # Find the password input field and enter your password
    password_field = driver.find_element(By.ID, 'input36')
    password_field.send_keys('')

    # Click Sign in button
    sign_in_button.click()
    print('Sign in button clicked')

except:
    pass

# Close the browser window
# driver.quit()