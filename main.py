import pyautogui, pyttsx3, os
os.system("title Autoclicker")
os.system("color 9")
os.system("cls")
try:
    reps = int(input("How many times do you want to click? "))
except:
    print("The entered value is not a number.")
    os.system("autoclicker")
else:
    e = pyttsx3.Engine()
    print("Starting clicks in: ")
    i=5
    while i>=1:
        e.say(str(i))
        print(i)
        e.runAndWait()
        i-=1

    for i in range(reps):
        pyautogui.click()