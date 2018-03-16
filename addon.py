#import xbmcaddon
#import xbmcgui
import os
import xbmc
import pydevd
import time
import threading


global hasRun

def yesNoDialog():
		while not hasRun:
			if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
				print 'clicking yesnodialog'
				xbmc.executebuiltin('SendClick(11)')
				#hasRun = True
			else:
				time.sleep(2)
				print 'running window checker'


pydevd.settrace('192.168.0.55',stdoutToServer=True, stderrToServer=True)


tempdir = xbmc.translatePath('special://temp/')
tempfile0 = os.path.join(tempdir, 'reslutiontoggle0')


hasRun = False

t1 = threading.Thread(target=yesNoDialog)
t1.start()

if not os.path.isfile(tempfile0):
	print 'will switch to resolution 17'
	tempfile = open(tempfile0, "a")
	tempfile.close()
	
#	xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"videoscreen.resolution","value":' + 17 or 20 + '}}')

	
else:
	print 'will switch to resolution 20'
	os.remove(tempfile0)
#	thread2.join(2)


hasRun = True	
print 'done'