import pyxbmct.addonwindow as pyxbmct 
import xbmcaddon

import xbmcgui
 
import urllib, os,re,urllib2
import xbmc
import shutil
import sqlite3
import xbmcplugin



url ='http://www.pjalpha.co.nf/kids/source.db'
url2 ='http://www.pjalpha.co.nf/source.db'
url3 ='http://www.pjalpha.co.nf/Adult/source.db'


def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("Downloading TV Guide","Downloading File")
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
    
 
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print percent
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print "DOWNLOAD CANCELLED" # need to get this part working
        del window
	dp.close()
	

	
	

# Create a window instance. (Title)
window = pyxbmct.AddonDialogWindow('Project @lpha TV Guide Update 1.5.1')

# Set the window width, height and the grid resolution: 3 rows, 3 columns.
window.setGeometry(750, 350, 3, 3)

# Create a text label.
label = pyxbmct.Label('Please Select your TV Guide.', alignment=pyxbmct.ALIGN_CENTER)

# Place the label on the window grid.
window.placeControl(label, 0, 0, columnspan=3)

# Create a button.
button = pyxbmct.Button('Kids Tv Guide')
button2 = pyxbmct.Button('Tv Guide')
button3 = pyxbmct.Button('Adult Tv Guide')
button4 = pyxbmct.Button('EXIT')


# Place the button on the window grid.
window.placeControl(button, 1, 0)
window.placeControl(button2, 1, 1)
window.placeControl(button3, 1, 2)
window.placeControl(button4, 2, 1)


# Set Navigation Control
button.controlRight(button2)
button2.controlRight(button3)
button3.controlLeft(button2)
button2.controlLeft(button)
button2.controlDown(button4)
button4.controlUp(button2)

# Set initial focus on the button.
window.setFocus(button4)



# Connect the button to a function.
window.connect(button, lambda: DownloaderClass(url,"/sdcard/android/data/org.xbmc.kodi/files/.kodi/userdata/addon_data/script.renegadestv/source.db"))
window.connect(button2,lambda: DownloaderClass(url2,"/sdcard/android/data/org.xbmc.kodi/files/.kodi/userdata/addon_data/script.renegadestv/source.db"))
window.connect(button3,lambda: DownloaderClass(url3,"/sdcard/android/data/org.xbmc.kodi/files/.kodi/userdata/addon_data/script.renegadestv/source.db"))
window.connect(button4, window.close)


# Connect a key action to a function.
window.connect(pyxbmct.ACTION_NAV_BACK, window.close)

	
# Show the created window.
window.doModal()


# Delete the window instance when it is no longer used.

# make connection to existing db

conn = sqlite3.connect('C:\Users\Loopy\Desktop\source.db')
c = conn.cursor()

# Set New Login details

UserN=xbmcplugin.getSetting(int(sys.argv[1]), 'Duser')

PWord=xbmcplugin.getSetting(int(sys.argv[1]), 'Dpass')


# Change to new Login details

UserNameSend = "UPDATE custom_stream_url SET stream_url = REPLACE(stream_url,'projectalpha%40myway.com','" + UserN + "')"
PasswordSend = "UPDATE custom_stream_url SET stream_url = REPLACE(stream_url,'roxanne1','" + PWord + "')"


# update field

c.execute(UserNameSend) 
c.execute(PasswordSend) 

# Save the changes

conn.commit()


# close connection
conn.close()

