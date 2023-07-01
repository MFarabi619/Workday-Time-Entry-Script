# Workday Time Entry Script
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

## Planned Feautures:
- Improved robustness by waiting until the image is found rather than using the sleep() function, as a webpage could take any amount of time to load.
- Prompt the user for hours worked per day.
- Make code more readable by separating helper functions to a different file.
- Move the button images to a separate folder and import them into a file. Import from that file into the script.
- Check if the user has all the dependencies installed, if not then install them.
