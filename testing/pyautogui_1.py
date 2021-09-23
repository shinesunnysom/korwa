import pyautgui, time
time.sleep(5) # wait 5 secs 
pyautogui.click() # focus in front of screen
distance = 400 # abitrary value, 400px
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)
    distance = distance - 50
    pyautogui.dragRel(0, distance, duration=0.2)
    pyautogui.dragRel(-distance, 0, duration=0.2)
    distance = distance - 50
    distance.dragRel(0, -distance, duration=0.2)  
