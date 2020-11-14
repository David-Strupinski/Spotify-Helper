from os import system, getpid
from pyautogui import press
from time import sleep
import pygetwindow as gw
import psutil
import win32process
import subprocess


# needs to run on startup of program to find name of user dir
p = psutil.Process(getpid())
dir_string = p.username()
user_dir = dir_string.split('\\')[1]


def checkIfProcessRunning(processName='spotify'):
    # Iterate over the all the running processes
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string
            if processName.lower() in proc.name().lower():
                return True
        except:
            continue
    return False


def ad(title=None):
    # stop any sound from ad playing
    # press('playpause')

    # different ways to terminate Spotify player
    if title != None:
        # terminates specific player ID instead of all spotify.exe processes
        uncut_hwnd = str(gw.getWindowsWithTitle(title))
        # splicing string to get hwnd, then making it an int
        hwnd = int(uncut_hwnd.split('=')[1][0:-2])
        threadid, pid = win32process.GetWindowThreadProcessId(hwnd)
        p = psutil.Process(pid)
        p.terminate()
    else:
        system('TASKKILL /F /IM spotify.exe')

    # restart Spotify without causing it to not respond
    # info = subprocess.STARTUPINFO()
    # info.dwFlags = 1
    # info.wShowWindow = 0
    # subprocess.Popen("AppData/Roaming/Spotify/Spotify.exe", startupinfo=info)

    system(
        f'start /min C:/Windows/Spotify.lnk')

    sleep(2)


def detector():
    # initialize variable to determine if the player could be paused
    possibly_paused = False
    # stays running indefinitely, sleep functions help reduce load
    while True:
        sleep(0.5)
        if checkIfProcessRunning():
            # gets titles of all actively running programs
            titles = gw.getAllTitles()

            # looks if one of the program titles is Advertisement or Spotify, which is what Spotify is called only when it's playing an ad
            if 'Spotify Free' not in titles:
                possibly_paused = False

            # if the program title is Spotify Free, there could be an ad or Spotify could be paused
            if 'Spotify Free' in titles:
                if not possibly_paused:
                    # restarting Spotify quickly makes it repeat the last track
                    sleep(2)
                    ad('Spotify Free')
                    # only unpauses tracks that have just started, detecting if it was paused or not! P.S. Will start music on the track you left off at
                    # press('prevtrack')
                # means Spotify is either paused or playing a type of ad
                possibly_paused = True
                sleep(60)

            elif 'Advertisement' in titles or 'Spotify' in titles:
                if 'Advertisement' in titles:
                    # restarting Spotify quickly makes it repeat the last track
                    ad('Advertisement')

                if 'Spotify' in titles:
                    ad('Spotify')

                # press('playpause') can be used instead but slower
                press('nexttrack')
                sleep(60)


if __name__ == '__main__':
    # this sleep is here given that this is started with a song or the computer, so things can boot up; and ads never come first
    sleep(15)
    detector()
