import xbmcaddon
import xbmcgui
import os
import xbmc
import pydevd

from threading import Thread

def changeRes(res):
	
	#move the yesno dialog code to thread
	
	xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"videoscreen.resolution","value":' + res + '}}')
	print '{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"videoscreen.resolution","value":' + res + '},"id":1}'




pydevd.settrace('192.168.0.55',stdoutToServer=True, stderrToServer=True)


tempdir = xbmc.translatePath('special://temp/')
tempfile0 = os.path.join(tempdir, 'reslutiontoggle0')

if not os.path.isfile(tempfile0):
	#t1 = thread.start_new_thread(change17, ())
	thread1 = Thread(target = changeRes('17'))
	thread1.daemon = True
	thread1.start()
	#xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"videoscreen.resolution","value":17}}')
	
	if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
		xbmc.executebuiltin('SendClick(11)')
	else:
		xbmc.sleep(1000)
		if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
			xbmc.executebuiltin('SendClick(11)')
	
	
	

	#if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
	#	xbmc.executebuiltin('SendClick(11)')
	tempfile = open(tempfile0, "a")
	tempfile.close()
	thread1.join(2)
else:
	#thread.start_new_thread(change20, ())
	thread2 = Thread(target = changeRes('20'))
	thread2.daemon = True
	thread2.start()
	#xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"videoscreen.resolution","value":20}}')
	
	if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
		xbmc.executebuiltin('SendClick(11)')
	else:
		xbmc.sleep(1000)
		if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
			xbmc.executebuiltin('SendClick(11)')
		
	os.remove(tempfile0)
	thread2.join(2)
	
print 'done'