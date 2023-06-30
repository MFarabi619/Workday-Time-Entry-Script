# Author: Mumtahin Farabi

import pyautogui
import pyperclip
import webbrowser
import time

# Welcome message👋
print("Welcome to the Ciena Workday Time Entry Script!👋\n")

# Open workday in a new tab on the default system browser
def open_workday():
    # Open Workday in a new tab
    URL = 'https://wd5.myworkday.com/ciena/d/home.htmld'

    # Copy the URL to the clipboard
    pyperclip.copy(URL)

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
        print("Please ensure that you're logged into Workday, hit enter when ready.")
        input()

#Helper function to press tab and enter keys
def tabEnter(count):
    pyautogui.press('tab', presses=count)
    pyautogui.press('enter')
    pyautogui.sleep(0.75)

def go_to_enter_time_page():
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('images/menu_hamburger_button.png',region=(0, 72, 113, 130), confidence = 0.9))
    pyautogui.click()
    pyautogui.sleep(0.5)
    # pyautogui.moveTo(pyautogui.locateCenterOnScreen('images/time_button.png',region=(0, 400, 400, 500), confidence = 0.7))
    # print(pyautogui.locateCenterOnScreen('images/time_button.png',region=(0, 400, 400, 500), confidence = 0.9))
    # pyautogui.click()
    # pyautogui.sleep(0.75)
    # pyautogui.moveTo(pyautogui.locateCenterOnScreen('images/this_week_button.png',region=(605, 280, 920, 330), confidence = 0.7))
    # pyautogui.click()
    # pyautogui.sleep(2)


    # tabEnter(3) # Click on hamburger button
    tabEnter(6)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('images/time_text.png',confidence=0.9))
    pyautogui.click()
    tabEnter(2)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('images/actions_button.png',confidence=0.9))
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.press('down', presses=4)
    pyautogui.press('enter')
    
    while pyautogui.locateCenterOnScreen('images/quick_add_text.png',confidence=0.9) == None:
        pyautogui.sleep(0.5)

    print("reached")

    # tabEnter(10)

secs_between_keys = 0.05
hours = 8

# This function was supposed to find the day columns, and add the times. 
# Unfortunately, OpenCV couldn't find the image matches. :(
# def find_weekdays():
    # weekdays = ['/images/weekdays/monday.png',
    #             '/images/weekdays/tuesday.png',
    #             '/images/weekdays/wednesday.png',
    #             '/images/weekdays/thursday.png',
    #             '/images/weekdays/friday.png']

    # for day in weekdays:
    #     # x, y = pyautogui.locateCenterOnScreen(day,region=(0, 277, 1623, 360), grayscale=True, confidence = 0.9)
    #     x, y = pyautogui.locateCenterOnScreen(day, grayscale=True, confidence = 0.9)
    #     pyautogui.moveTo(x,y+230)
    #     pyautogui.click()
    #     pyautogui.sleep(0.5)
    #     pyautogui.press('tab', presses=2)
    #     pyautogui.write(hours)
    #     pyautogui.press('tab', presses=2)
    #     pyautogui.press('enter')
    #     pyautogui.sleep(0.5)

def enter_time():
    pyautogui.press('tab')
    pyautogui.press('enter')
    # pyautogui.moveTo(pyautogui.findCenterOnScreen('images/actions_button.png',confidence = 0.9))
    pyautogui.press('tab', presses=10)
    pyautogui.press('enter')
    pyautogui.sleep(0.5)
    pyautogui.press('down', presses=4)
    pyautogui.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('images/next_button.png',confidence = 0.9))
    print(pyautogui.locateCenterOnScreen('images/next_button.png',confidence = 0.9))
    pyautogui.click()
    pyautogui.sleep(0.5)


# Function to display mouse position, for testing purposes
def mouse_position():
    try:
        while True:
            # Get the current mouse position
            x, y = pyautogui.position()
            print('X:', x, 'Y:', y)
            
            # Sleep for a short period to reduce the number of messages printed
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('\nDone.')

open_workday()
# check_sign_in()
go_to_enter_time_page()
# enter_time()
# mouse_position()
