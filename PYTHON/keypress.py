from pynput.keyboard import Key, Listener
import os
def show(key):
    print(key)
    if format(key)[1]=='w':
        os.system(("taskkill /IM brave.exe "))
        return False
    # by pressing 'delete' button
    # you can terminate the loop
    if key == Key.delete:
        os.system(("taskkill /IM brave.exe "))
        return False
# Collect all event until released
with Listener(on_press = show) as listener:
	listener.join()
