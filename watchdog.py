import xbmc
from subprocess import call

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
        call(["sudo","cpupower frequency-set -g "+newGovernor]

player = MyPlayer()

while player.active:
	xbmc.sleep(1000);

