# Workday-Time-Entry-Script

I initially attempted to automate the process of entering hours into the Workday Employee portal using PyAutoGUI, but ran into a variety of issues such as:
- OpenCV failing to detecting small text.
- Accounting for variations in reponse times from the browser.
- Slight UI changes throwing off tab-key and enter-press sequences.

So I started looking into browser automation frameworks. I decided to move forward with Selenium as it is more robust with functionality to mimic complex user actions, whereas BeautifulSoup
is more of a pure webscraper that excels at parsing data.

## Features:
- The script detects the default system browser of the user, and launches it with the workday login url.
- Checks if the user is signed in or not. If not, then it clicks the 'Sign in' button and waits until the user is signed in.
- Navigates to the 'All About Me' page, and clicks the 'Enter Time' button.
- Enters hours into the 'Enter my Time' page.
