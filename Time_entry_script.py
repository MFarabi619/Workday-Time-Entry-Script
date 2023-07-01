# Author: Mumtahin Farabi

import pyautogui
import webbrowser
from helper_functions import wait_until_loaded, tabEnter

# Welcome message👋
print("Welcome to the Ciena Workday Time Entry Script!👋\n")

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

hours = str(8)

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


open_workday()
check_sign_in()
go_to_enter_time_page()
enter_time()
