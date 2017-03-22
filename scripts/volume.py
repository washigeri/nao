# -*- encoding: UTF-8 -*- 
#!/usr/bin/env python
from naoqi import ALProxy
import sys

NAO_IP = "localhost"
PORT = 9559

if len(sys.argv) == 3:
	adr_ip = sys.argv[1]
	volume = sys.argv[2]
	methode = "set"
elif len(sys.argv) == 2:
	adr_ip = sys.argv[1]
	methode = "get"
else:
	sys.exit(1)


alAudioDev = ALProxy("ALAudioDevice", adr_ip, PORT)
ttsProxy = ALProxy("ALTextToSpeech", adr_ip, PORT)

if methode == "get":
	vol = alAudioDev.getOutputVolume()
	print str(vol)
elif methode == "set":
	alAudioDev.setOutputVolume(int(volume))
	ttsProxy.say("Volume " + volume)
"Fin du script..."
sys.exit(0)

