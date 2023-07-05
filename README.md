# Workday Time Entry Script

https://github.com/MFarabi619/Workday-Time-Entry-Script/assets/54924158/502a9e33-e1c0-4037-a63c-a4df73d4214e

Before running the script, open a terminal with administrator privileges and paste the following: `pip install pyautogui opencv-python tabulate colorama`

This installs the necessary modules the script requires to run. You only have to do this once, not every time before you run the script. The modules will stay installed on your system. :)

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

## Release v3.0.0 Features and Changelog:

### Major Changes:
- The browser window moving feature has been de-activated due to reliability issues.
  - The function that moves the browser window is still in the helper_functions.py file, but it is not called.
- After the user inputs their hours, the work week dictionary will be printed vertically in a tabulated format instead of horizontally. The weekdays will be yellow and the hours will be green. This is to make it easier for the user to read the dictionary and verify that the hours were entered correctly.
- Once the review time screen is reached, the user is provided with an option to either submit the hours or to clear their entire entry and restart. This is in case the user notices that they made a mistake in their hours entry.

### Minor Changes:
- Images for buttons have been moved into a separate folder.
- Unused images have been removed.
- All images are now imported as variables from a separate file.
- MoveToandClick helper function has been added to improve code readability.

## Release v2.1.1-hotfix Features and Changelog:
- Fixed a bug where the script would try to move the browser window even though it was already on the main monitor.
## Release v2.1.0 Features and Changelog:
- Detects if the browser is on the main monitor or not. If not, then moves it to the main monitor automatically.

## Release v2.0.0 Features and Changelog:
- Asks the user if they worked a regular work week. If not, then the script will prompt the user for the number of hours worked per day.
  - The hours entry menu also provides the user with the options to undo the last entry, restart from the beginning, or to exit the menu.
  - Input filtering is implemented to prevent the user from entering invalid values and breaking the script.
- No need for the user to press enter in the console when signing in. The script will automatically continue when the hamburger icon is found.
- If the browser is not on the main monitor, the script waits until the browser is moved to the main monitor rather than crashing.
  - The script also prints a message to the console every half second to let the user know that the script is either waiting for the browser to be moved, or for the page to load.
## Release v1.0.0-alpha Features:
https://github.com/MFarabi619/Workday-Time-Entry-Script/assets/54924158/7a8c1143-e3bc-4cc1-b2e4-269962adfced
- Improved robustness by waiting until the image is found rather than using the sleep() function, as a webpage could take any amount of time to load.
- Improved code readability through separation of helper functions to a different file.


## Planned Features and improvements:
- Create a test feature at the end of the script to clear all entries into workday.
- Check if the user has all the dependencies installed, if not then install them.
- Create a reliable feature that moves the browser window to the main monitor.


## Learning Log:
- Automating browser actions using Selenium Webdriver.
- Parsing HTML using Selenium Webdriver.
- Improving robustness of PyAutoGUI scripts by using waiting for image to show up rather than using sleep() function.
- Choosing a large and distinct enough image to be reliably detected by OpenCV.
- Storing values in a dictionary and iterating through them.
- Manipulating the order of items in a dictionary.
- Considered using multithreading/multiprocessing to for the sign-in check stage, but decided against it as it would be too complicated for this use case. Used a while loop instead.
- If there is no browser open, the webbrowser module will open the default browser in the main monitor. If there is a browser open, it will open a new tab in the same browser, with the browser remaining on the monitor screen it was originally in.
- Unfortunately, the PyAutoGUI function keyDown() does not reliably work for more than one key. I was unable to use the Win+Shift+LeftArrow key combination to move the browser to the main monitor. I had to use Win+LeftArrow to move the browser to the main window, and then Win+UpArrow to maximize the browser.
- The PyAutoGUI function localeOnScreen() and locateCenterOnScreen() look for images that are the exact same dimensions as provided. If you take a large screenshot, and look for the same image in the gui but a smaller version of it, the function will not find it. I had to take a screenshot of the image I wanted to find, in the exact dimension that it would show up in the alt+tab gui.
- ANSI escape sequences are special character sequences used to control text formatting and styling in terminal or console environments. They are a standardized way of achieving effects like changing text color, background color, text style (bold, underline, etc.), cursor position, and more.
  - Not all terminals and consoles fully support ANSI escape sequeces. But most modern terminals and consoles support a subset of them and will default to ignoring the unsupported ones. The `colorama` library can be used to make ANSI escape sequences work on all platforms, and simplify the syntax. 
- Printing dictionaries in a more readable format using the `tabulate` library, and coloring the text using the `colorama` library.
