import pyautgui, time
time.sleep(5) # wait 5 secs 
pyautogui.click() # focus in front of screen
distance = 400 # abitrary value, 400px
  while distance > 0:
      pyautogui.dragReli(distance, 0, duration=0)
