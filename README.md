# Workday Time Entry Script

https://github.com/MFarabi619/Workday-Time-Entry-Script/assets/54924158/7a8c1143-e3bc-4cc1-b2e4-269962adfced

I initially attempted to automate the process of entering hours into the Workday Employee portal using PyAutoGUI, but ran into a variety of issues such as:

- OpenCV failing to detecting small text.
- Accounting for variations in reponse times from the browser.
- Slight UI changes throwing off tab-key and enter-press sequences.
- So I started looking into browser automation frameworks. I decided to move forward with Selenium as it is more robust with functionality to mimic complex user actions, whereas BeautifulSoup is more of a pure webscraper that excels at parsing data.

UPDATE: The recent Selenium version (4.10.0) has rendered pretty much every piece of documentation and youtube tutorial prior to June 7th, 2023 useless for my specific use case. So I've reverted back to PyAutoGUI.

## Features:
- The script detects the default system browser of the user, and launches it with the workday login url.
- Checks if the user is signed in or not. If not, then it clicks the 'Sign in' button and waits until the user is signed in.
- Navigates to the hamburger menu, and clicks the 'Time' button.
- Clicks the 'My Calendar' button.
- Clicks on 'Actions', then 'Quick Add'.
- Enters hours and clicks the 'Ok' button.
- Clicks the 'Review' button and ends at the submit page.

## Release v1.0.0-alpha Features:
- Improved robustness by waiting until the image is found rather than using the sleep() function, as a webpage could take any amount of time to load.
- Improved code readability through separation of helper functions to a different file.

## Release v2.0.0 Features:
- Asks the user if they worked a regular work week. If not, then the script will prompt the user for the number of hours worked per day.
  - The hours entry menu also provides the user with the options to undo the last entry, restart from the beginning, or to exit the menu.
- No need for the user to press enter in the console when signing in. The script will automatically continue when the hamburger icon is found.
- If the browser is not on the main monitor, the script waits until the browser is moved to the main monitor rather than crashing.
  - The script also prints a message to the console every half second to let the user know that the script is either waiting for the browser to be moved, or for the page to load.

## Planned Features and improvements:
- Move the button images to a separate folder and import them into a file. Import from that file into the script.
- Check if the user has all the dependencies installed, if not then install them.

## Learning Log:
- Automating browser actions using Selenium Webdriver.
- Parsing HTML using Selenium Webdriver.
- Improving robustness of PyAutoGUI scripts by using waiting for image to show up rather than using sleep() function.
- Choosing a large and distinct enough image to be reliably detected by OpenCV.
- Storing values in a dictionary and iterating through them.
- Manipulating the order of items in a dictionary.
- Considered using multithreading/multiprocessing to for the sign-in check stage, but decided against it as it would be too complicated for this use case. Used a while loop instead.
