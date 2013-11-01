import xbmc

class MyPlayer(xbmc.Player):

	def __init__(self):
		xbmc.Player.__init__(self)
		self.active = True
		self.player_is_playing = False

	def onPlayBackStarted(self):
	    if not self.player_is_playing and\
	      self.active and xbmc.Player().isPlayingVideo():
		    self.player_is_playing = True
		    self.changeGovernor('performance')

	def onPlayBackStopped(self):
	    if self.player_is_playing and self.active:
		    self.changeGovernor('ondemand')
		    self.player_is_playing = False
            
    def changeGovernor(self,newGovernor='ondemand'):
        gov = open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor", "w")
        gov.write(newGovernor)
        gov.close()


player = MyPlayer()

while player.active:
	xbmc.sleep(1000);

