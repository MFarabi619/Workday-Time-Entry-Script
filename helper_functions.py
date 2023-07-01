import pyautogui

# Helper function to check if an image is on the screen, and wait until it is
def wait_until_loaded(image):
    while pyautogui.locateCenterOnScreen(image,confidence=0.9) == None:
        pyautogui.sleep(0.1)

    return pyautogui.locateCenterOnScreen(image,confidence=0.9)

# Helper function to press tab and enter keys
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