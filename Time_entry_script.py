import webbrowser
import pyautogui
from helper_functions import wait_until_loaded, tabEnter, check_user_input, collect_hours
from images import *

# Create a dictionary that stores hours worked for each day of the week
work_week = {
    "Monday": "8",
    "Tuesday": "8",
    "Wednesday": "8",
    "Thursday": "8",
    "Friday": "8",
    "Saturday": "0",
    "Sunday": "0"
}

# Welcome message👋
def welcome(work_week):
    print("Welcome to the Workday Time Entry Script main menu!👋\n")
    print("This script will help you enter your time for the week in Workday.📅\n")
    userInput = check_user_input("Did you work a regular work week? A regular work week is 8 hours Monday-Friday(y/n): ", ["y", "n"])

    if (userInput == "Y" or userInput == "y"):
        print("Great! Let's get started!🚀\n")
    elif (userInput == "N" or userInput == "n"):
        print("\nNo worries. Let's collect your number of hours worked for each day of the week.📅\n")
        print("If you made a mistake, you can simply enter 'u' to undo your last entry.⬅️\n") 
        print("If you want to start over, you can enter 'r' to reset all your entries.🔃\n")
        print("If you want to exit the script, you can enter 'e' to exit.👋\n")
        collect_hours(work_week)

# Open workday in a new tab on the default system browser
def open_workday():
    # Open Workday in a new tab
    URL = 'https://wd5.myworkday.com/ciena/d/home.htmld'

    # Open a browser tab with the URL
    webbrowser.open_new(URL)
    # webbrowser.open(URL, new = 1, autoraise=True)
    # webbrowser.get(URL)

    # Wait a bit to account for your potato pc🥔
    pyautogui.sleep(2)

# Detect if the user isn't signed in to Workday yet
def check_sign_in():

    time_elapsed = 0
    while (pyautogui.locateCenterOnScreen(workday_sign_in, confidence=0.9) is None and pyautogui.locateCenterOnScreen(menu_hamburger_button, confidence=0.9) is None):
        pyautogui.sleep(0.1)
        time_elapsed += 1
        if time_elapsed % 5 == 0:
            print("Waiting for target image. Is your browser window open and on your main monitor?\n")
            print("Please be patient if the website is loading. The script will continue a soon as the image is found.\n")

    if pyautogui.locateCenterOnScreen(workday_sign_in, confidence=0.9) is not None:
        print("Workday sign in page detected. Signing in...\n")
        # Wait for browser to autofill credentials
        pyautogui.sleep(0.5)
        pyautogui.moveTo(pyautogui.locateCenterOnScreen(workday_sign_in_button, confidence = 0.9))
        pyautogui.click()
        pyautogui.alert("Please verify your Okta credentials so the script can continue. :)")

# Navigate to the enter time page
def go_to_enter_time_page():

    pyautogui.moveTo(wait_until_loaded(menu_hamburger_button))
    pyautogui.click()
    pyautogui.moveTo(wait_until_loaded(time_button))
    pyautogui.click()
    pyautogui.moveTo(wait_until_loaded(my_calendar_button))
    pyautogui.click()
    pyautogui.moveTo(wait_until_loaded(actions_button))
    pyautogui.click()
    wait_until_loaded(drop_down_menu)
    pyautogui.press('down', presses=4)
    pyautogui.press('enter')
    
    wait_until_loaded(quick_add_text)
    tabEnter(3)

# Enter time for the week
def enter_time(work_week):

    # Keep tabbing and stop just before the first day of the week
    pyautogui.press('tab', presses=11)

    # Make the dictionary start with Sunday, because that's the first day of the week in Workday
    first_day = work_week.pop("Sunday")
    work_week = {**{"Sunday": first_day}, **work_week}

    # Loop through the dictionary and enter the hours for each day, starting with Sunday
    for day, hours in work_week.items():
        pyautogui.press('tab')
        pyautogui.typewrite(hours)

    # Click the OK button
    pyautogui.moveTo(pyautogui.locateCenterOnScreen(orange_ok_button,confidence=0.9))
    pyautogui.click()

    # Click the review button
    pyautogui.moveTo(wait_until_loaded(review_button))
    pyautogui.click()
    print("Time entry complete!🎉")

# Main function
def main ():
    welcome(work_week)
    open_workday()
    check_sign_in()
    go_to_enter_time_page()
    enter_time(work_week)

# Run the main function if this file is run directly
if __name__ == "__main__":
    main()