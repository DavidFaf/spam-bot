import pyautogui, time
time.sleep(9)
f = open("beescript", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")