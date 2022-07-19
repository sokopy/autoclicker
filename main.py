import os
os.system("cls")
import pyautogui, time, pyttsx3, sys
try:
    reps = int(input("How many times do you want to click? "))
except:
    print("The entered value is not a number. Please execute the program again.")
    sys.exit()
else:
    e = pyttsx3.Engine()
    print("Starting clicks in: ")
    i=5
    while i>=1:
        time.sleep(0.05)
        e.say(str(i))
        print(i)
        e.runAndWait()
        i-=1

    for i in range(reps):
        pyautogui.click()