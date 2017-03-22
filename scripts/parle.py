# -*- encoding: UTF-8 -*-
# broker par défaut
NAO_IP = "localhost"
NAO_PORT = 9559 

# import librairies
import sys
from naoqi import ALProxy

def main() :
	print sys.argv
        if len(sys.argv) == 1 :
                nao_ip = NAO_IP
		msg = "Hello le Monde"
        elif len(sys.argv) > 2 :
                nao_ip = sys.argv[1]
		i=2
		msg=""
		while i < len(sys.argv):
			msg = msg + sys.argv[i]
			i+=1

	    # Proxy objet TTS
        try :
            ttsProxy = ALProxy("ALTextToSpeech", nao_ip, NAO_PORT)
        except :
            print "Impossible de se connecter à NAO"
            exit(1)
            
	    # règlage hauteur du son et parole
        ttsProxy.setParameter("pitchShift", 1.3)
        ttsProxy.say(msg)
	print "Fin du script..."

if __name__ == "__main__":
    main()
