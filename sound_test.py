import os
from playsound import playsound
import time

#~ print "Hello Sound"
#~ playsound('kanye-west-power-intro.wav')

file = "kanye-west-power-intro.wav"
os.system("omxplayer --no-keys {} &".format(file))
#~ time.sleep(4)
#~ os.system("omxplayer --no-keys {} &".format(file))
