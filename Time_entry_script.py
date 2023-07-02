# Author: Mumtahin Farabi

import pyautogui
import webbrowser
from helper_functions import wait_until_loaded, tabEnter

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

# Create a function to check if userInput was valid or not
def check_user_input(prompt, validInputs):
    userInput = input(prompt).lower()
    while userInput not in validInputs:
        userInput = input("Valid inputs are: " + str(validInputs) + "\nPlease enter a valid input: ").lower()
    return userInput

# Welcome message👋
def welcome():
    print("Welcome to the Workday Time Entry Script main menu!👋\n")
    print("This script will help you enter your time for the week in Workday.📅\n")
    print("Prior to proceeding, please ensure that you have an instance of your browser open on your main monitor.🖥️\n")
    userInput = check_user_input("Did you work a regular work week? A regular work week is 8 hours Monday-Friday(y/n): ", ["y", "n"])

    if (userInput == "Y" or userInput == "y"):
        print("Great! Let's get started!🚀\n")
    elif (userInput == "N" or userInput == "n"):
        print("\nNo worries. Let's collect your number of hours worked for each day of the week.📅\n")
        print("If you made a mistake, you can simply enter 'u' to undo your last entry.⬅️\n") 
        print("If you want to start over, you can enter 'r' to reset all your entries.🔃\n")
        print("If you want to exit the script, you can enter 'e' to exit.👋\n")
        collect_hours()

# Collect hours worked for each day of the week
def collect_hours():
    # Loop through each day of the week and collect the number of hours worked
    days = list(work_week.keys())
    worked_weekend = False
    i = 0

    while i < len(days)+1:
        if i <0:
            i = 0

        # Check if we've reached the end of the week
        if i == len(days):
            print("These are hours you entered for each day of the week:\n")
            print(work_week)
            userInput = check_user_input("Are these hours correct? y/n\n", ["y", "n"])
            if (userInput == "N" or userInput == "n"):
                print("No worries. Let's start over.🔃\n")
                worked_weekend=False
                i = 0
                continue
            else:
                print("Great! Let's get started!🚀\n")
                break
            
        if days[i] == "Saturday" and worked_weekend == False:
            userInput = check_user_input("Did you work over the weekend? y/n\n", ["y", "n"])
            if (userInput == "Y" or userInput == "y"):
                worked_weekend = True
                continue
            else:
                i = len(days)
                continue

        day = days[i]
            
        hours = input("How many hours did you work on " + day + "?\n")
        try:
            if hours == "u":
                print("Undoing last entry...\n")
                i-=1
            elif hours == "r":
                print("Resetting all entries...\n")
                i = 0
            elif hours == "e":
                print("Exiting script...\n")
                exit()
            elif int(hours) > 24:
                print("Please enter a valid number between 0-24.\n")
            else:
                work_week[day] = hours
                i +=1 
        
        except ValueError:
            print("Valid inputs are 'u','r','e', and any number between 0-24.\n")

# Open workday in a new tab on the default system browser
def open_workday():
    # Open Workday in a new tab
    URL = 'https://wd5.myworkday.com/ciena/d/home.htmld'

    # Open a browser tab with the URL
    webbrowser.open_new(URL)

    # Wait a bit to account for your potato pc🥔
    pyautogui.sleep(2)

# Detect if the user isn't signed in to Workday yet
def check_sign_in():
    if (pyautogui.locateCenterOnScreen('images/workday_sign_in.png',region=(0, 70, 1920, 158), confidence = 0.9) != None):
        pyautogui.sleep(0.5)
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('images/workday_sign_in_button.png',region=(805, 710, 1115, 755), confidence = 0.9))
        pyautogui.click()

        pyautogui.alert("Please verify your Okta credentials so the script can continue. :)")
        print("Please ensure that you're logged into Workday, hit enter when you're on the Workday homepage.")
        input()

def go_to_enter_time_page():

    pyautogui.moveTo(wait_until_loaded('images/menu_hamburger_button.png'))
    pyautogui.click()
    pyautogui.moveTo(wait_until_loaded('images/time_button.png'))
    pyautogui.click()
    pyautogui.moveTo(wait_until_loaded('images/my_calendar_button.png'))
    pyautogui.click()
    pyautogui.moveTo(wait_until_loaded('images/actions_button.png'))
    pyautogui.click()
    wait_until_loaded('images/drop_down_menu.png')
    pyautogui.press('down', presses=4)
    pyautogui.press('enter')
    
    wait_until_loaded('images/quick_add_text.png')
    tabEnter(3)

def enter_time():
    pyautogui.press('tab', presses=13)
    pyautogui.typewrite(hours)
    pyautogui.press('tab')
    pyautogui.typewrite(hours)
    pyautogui.press('tab')
    pyautogui.typewrite(hours)
    pyautogui.press('tab')
    pyautogui.typewrite(hours)
    pyautogui.press('tab')
    pyautogui.typewrite(hours)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('images/orange_ok_button.png',confidence=0.9))
    pyautogui.click()
    pyautogui.moveTo(
    wait_until_loaded('images/review_button.png'))
    pyautogui.click()
    print("Time entry complete!🎉")

def main ():
    welcome()
    # open_workday()
    # check_sign_in()
    # go_to_enter_time_page()
    # enter_time()

# Run the main function if this file is run directly
if __name__ == "__main__":
    main()