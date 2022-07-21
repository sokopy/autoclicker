# Importing required modules
import pyautogui, os, sys, time, pyttsx3
# Console decoration
os.system("title Autoclicker 2 & color 1 & cls")
# Text-to-speech engine
e = pyttsx3.Engine()
# Restart in case of str value
def err_restart():
    print("Entered value is not a number.")
    os.system("autoclicker")
print("""-------------------------\n    AUTOCLICKER (2)\n-------------------------\n""")
reps = input("How many times do you want to click? Type \"exit\" to leave\n>")
# If the input is "exit" the program will close.
if reps.lower() == "exit":
    os.system("cls")
    print("Terminating process...")
    time.sleep(1)
    sys.exit()
# Checking if str can be turned into int. Otherwise, function err_restart will be called.
try:
    reps = int(reps)
except:
    err_restart()
# Same thing as above
try:
    i = int(input("Enter waiting time in seconds:\n>"))
except:
    err_restart()
# If both str values can be turned into int, the program will wait as told by user and then will start clicking
else:
    while i >= 1:
        e.say(str(i))
        print(i)
        e.runAndWait()
        i -= 1
    for i in range(reps):
        pyautogui.click()
    e.say("Process finished. Closing application.")
    print("Process finished. Closing application.")
    e.runAndWait()
# Must mention that this project was digital torture and I could barely think