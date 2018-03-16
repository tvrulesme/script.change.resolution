#import xbmcaddon
#import xbmcgui
import os
import xbmc
#import pydevd
import time
import threading


global hasRun

def yesNoDialog():
		while not hasRun:
			if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
				print 'clicking yesnodialog'
				xbmc.executebuiltin('SendClick(11)')
			else:
				time.sleep(2)
				print 'running window checker'

tempdir = xbmc.translatePath('special://temp/')
tempfile0 = os.path.join(tempdir, 'reslutiontoggle0')


hasRun = False
print 'set hasrun'

t1 = threading.Thread(target=yesNoDialog)
t1.start()

if not os.path.isfile(tempfile0):
	print 'will switch to resolution 17'
	xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"videoscreen.resolution","value":17},"id":1}')
	tempfile = open(tempfile0, "a")
	tempfile.close()
	
else:
	print 'will switch to resolution 20'
	xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"videoscreen.resolution","value":20},"id":1}')
	os.remove(tempfile0)

hasRun = True	
print 'done'
quit()