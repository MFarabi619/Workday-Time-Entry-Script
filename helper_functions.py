import pyautogui
from colorama import Fore, Style, Back, init
from tabulate import tabulate

# Check if userInput was valid or not
def check_user_input(prompt, validInputs):
    userInput = input(prompt).lower()
    while userInput not in validInputs:
        userInput = input("Valid inputs are: " + str(validInputs) + "\nPlease enter a valid input: ").lower()
    return userInput

# Only uncommented for testing purposes
# work_week = {
#     "Monday": "8",
#     "Tuesday": "8",
#     "Wednesday": "8",
#     "Thursday": "8",
#     "Friday": "8",
#     "Saturday": "0",
#     "Sunday": "0"
# }

def print_work_week(work_week):
    
    # Initialize colorama
    init()
    
    table_data = []
    for day, hours in work_week.items():
        formatted_day = f"{Fore.YELLOW}{day}{Style.RESET_ALL}"
        formatted_hours = f"{Fore.GREEN}{hours}{Style.RESET_ALL}"
        table_data.append([formatted_day, formatted_hours])

    table = tabulate(table_data, headers=["Day", "Hours Worked"], tablefmt="grid")

    # Change the row and column borders to blue
    formatting_chars = ["+", "|", "-", "="]
    formatted_table = table

    for char in formatting_chars:
        formatted_table = formatted_table.replace(char, f"{Fore.LIGHTCYAN_EX}{char}{Style.RESET_ALL}")

    formatted_table = formatted_table.replace("Day", f"{Fore.MAGENTA}Day{Style.RESET_ALL}")
    formatted_table = formatted_table.replace("Hours Worked", f"{Fore.MAGENTA}Hours Worked{Style.RESET_ALL}")

    print(formatted_table)

# Collect the number of hours worked for each day of the week
def collect_hours(work_week):
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
            print_work_week(work_week)
            userInput = check_user_input("\nAre these hours correct? y/n\n", ["y", "n"])
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
    
# Check if an image is on the screen, and wait until it is
def wait_until_loaded(image):
    time_elapsed = 0
    while pyautogui.locateCenterOnScreen(image,confidence=0.9) == None:
        pyautogui.sleep(0.1)
        time_elapsed += 1
        if time_elapsed % 5 == 0:
            print("Waiting for target image. Is your browser window open and on your main monitor?\n")
            print("Please be patient if the website is loading. The script will continue a soon as the image is found.\n")
    return pyautogui.locateCenterOnScreen(image,confidence=0.9)

# Detect if browser is on the main monitor, if not then move it to the main monitor
def move_browser_window():
    if pyautogui.locateCenterOnScreen('images/browser_sign_in_window.png', confidence=0.9) == None and pyautogui.locateCenterOnScreen('images/browser_signed_in_window.png', confidence=0.9) == None:
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.sleep(0.5)
        
        if pyautogui.locateCenterOnScreen('images/browser_sign_in_window.png', confidence=0.7) != None:
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('images/browser_sign_in_window.png',confidence=0.9)) 
            print("Reaching browser sign in window...")
        elif pyautogui.locateCenterOnScreen('images/browser_signed_in_window.png', confidence=0.7) != None:
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('images/browser_signed_in_window.png',confidence=0.9))
        else: 
            print("Browser window not detected. Please bring your browser window to the main monitor.")
            pyautogui.keyUp('alt')
            return 0

        print("Browser window detected.")
        pyautogui.click()
        pyautogui.keyUp('alt')

    while (pyautogui.locateCenterOnScreen('images/workday_sign_in.png', confidence=0.9) is None and pyautogui.locateCenterOnScreen('images/menu_hamburger_button.png', confidence=0.9) is None):
        pyautogui.keyDown('winleft')
        pyautogui.press('left')
        print("Moving browser window to main monitor...\n")
        # pyautogui.sleep(0.05)
    
    pyautogui.press('up', presses=2)
    pyautogui.keyUp('winleft')
    print("Browser window is on main monitor.\n")

#  Press enter after tabbing a certain number of times
def tabEnter(count):
    pyautogui.press('tab', presses=count)
    pyautogui.press('enter')
    pyautogui.sleep(0.75)

# Move to an image and click on it
def moveToandClick(image):
    pyautogui.moveTo(wait_until_loaded(image))
    pyautogui.click()

# Function to display mouse position, for testing purposes
def mouse_position():
    try:
        while True:
            # Get the current mouse position
            x, y = pyautogui.position()
            print('X:', x, 'Y:', y)
            
            # Sleep for a short period to reduce the number of messages printed
            pyautogui.sleep(0.1)
    except KeyboardInterrupt:
        print('\nDone.')
