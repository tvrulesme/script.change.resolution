#import xbmcaddon
#import xbmcgui
import os
import xbmc
import pydevd
import time
import threading


global hasRun

class YesNoDialog(threading.Thread):
	def start(self):
		while not hasRun:
			if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
				print 'clicking yesnodialog'
				xbmc.executebuiltin('SendClick(11)')
			else:
				time.sleep(1)
				print 'running window checker'


		
				
def sendCommand(res):
	xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"videoscreen.resolution","value":'+res+'},"id":1}')
	
pydevd.settrace('192.168.0.55', stdoutToServer=True, stderrToServer=True)

tempdir = xbmc.translatePath('special://temp/')
tempfile0 = os.path.join(tempdir, 'reslutiontoggle0')


hasRun = False
print 'set hasrun'

t1 = YesNoDialog()
t1.start()

if not os.path.isfile(tempfile0):
	print 'will switch to resolution 17'
	sendCommand('17')
	tempfile = open(tempfile0, "a")
	tempfile.close()
	
else:
	print 'will switch to resolution 20'
	sendCommand('20')
	os.remove(tempfile0)

hasRun = True	
print 'done'
t1.join(3)
#quit()