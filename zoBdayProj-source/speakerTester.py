import winsound

try:
    print("This program test the PC speaker. You should hear a 440 Hz beep for some duration.")
    winsound.Beep(440, 2000)
except:
    print("Your speakers are not working. Resolve the issue and try again")