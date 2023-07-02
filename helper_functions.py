import pyautogui

# Check if userInput was valid or not
def check_user_input(prompt, validInputs):
    userInput = input(prompt).lower()
    while userInput not in validInputs:
        userInput = input("Valid inputs are: " + str(validInputs) + "\nPlease enter a valid input: ").lower()
    return userInput

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
    # return work_week

# Check if an image is on the screen, and wait until it is
def wait_until_loaded(image):
    time_elapsed = 0
    while pyautogui.locateCenterOnScreen(image,confidence=0.9) == None:
        pyautogui.sleep(0.1)
        time_elapsed += 1
        if time_elapsed % 5 == 0:
            print("Waiting for target image. Is your broswer window open and on your main monitor?\n")
            print("Please be patient if the website is loading. The script will continue a soon as the image is found.\n")
    return pyautogui.locateCenterOnScreen(image,confidence=0.9)

#  Press enter after tabbing a certain number of times
def tabEnter(count):
    pyautogui.press('tab', presses=count)
    pyautogui.press('enter')
    pyautogui.sleep(0.75)

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