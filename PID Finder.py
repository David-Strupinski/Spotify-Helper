import psutil
import os
import pygetwindow as gw
import win32gui
import win32process
import time
import pyautogui

things = [i for i in psutil.process_iter()]
# print(things)

clean_things = []
pid_list = []

# print(things[1])
# print(len(things))

for i in range(len(things)):
    process = str({things[i]})
    process_list = process.split(', ')
    process_list[0] = process_list[0][20:]
    process_list[1] = process_list[1][6:-1]

    if 'Spotify' in process_list[1]:
        pid_list.append(process_list[0])
        pid_list.append(process_list[1])

        clean_things.append(pid_list)

    pid_list = []

print(clean_things)

uncut_hwnd = str(gw.getWindowsWithTitle("Spotify Free"))
# splicing string to get hwnd, then making it an int
hwnd = int(uncut_hwnd.split('=')[1][0:-2])
threadid, pid = win32process.GetWindowThreadProcessId(hwnd)
print(pid)
p = psutil.Process(pid)
p.terminate()

# time.sleep(1)
# os.system('START /MIN C:/Users/david/AppData/Roaming/Spotify/Spotify.exe')
# time.sleep(1)
# pyautogui.press('playpause')
