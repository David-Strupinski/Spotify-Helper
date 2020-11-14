import os
import pygetwindow as gw

titles = gw.getAllTitles()
# print(titles)

if 'Advertisement' in titles or 'Spotify' in titles:
    print('Ad detected')

# print('No ad detected')
