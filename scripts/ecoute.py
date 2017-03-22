# -*- encoding: UTF-8 -*-
import time
from naoqi import ALProxy

# Replace this with your robot's IP address
# import librairies
import sys
NAO_IP = "localhost"
ZIA = "10.0.8.6"
TAO = "10.0.8.4"
#NAO_IP = "10.0.8.6"
PORT = 9559

def dire(nao_ip, phrase):
    try :
        ttsProxy = ALProxy("ALTextToSpeech", nao_ip, PORT)
    except :
        print "Impossible de se connecter Ã  NAO"
        exit(1)

    # rÃ¨glage hauteur du son et parole
    ttsProxy.setParameter("pitchShift", 1.3)
    ttsProxy.say(phrase)

def ecoute(nao_ip):
    motreconnu=''
    try :
        asr = ALProxy("ALSpeechRecognition", nao_ip, PORT)
    except :
        print "Impossible de se connecter � NAO "+nao_ip
        exit(1)
    memory = ALProxy("ALMemory", nao_ip, PORT)
    try:
        asr.unsubscribe("Test_ASR")
    except:
        pass

    asr.setLanguage("French")

    # Example: Adds "yes", "no" and "please" to the vocabulary (without wordspotting)
    vocabulary = "oui;non;bonjour;bonsoir;tao;zia;fin;au revoir;non zia"

    asr.setVocabulary(vocabulary.split(';'),True)

    try:
        asr.subscribe("Test_ASR")
        print 'Speech recognition engine started'
        time.sleep(5)
        val = memory.getData("WordRecognized")
        if(len(val) > 1 and val[1] >= 0.5):
            dit = val[0]
            dit2=dit.split()
            for i in range (0, len(dit2)-1) :
		motreconnu = dit2[i]
            print dit2
#            dire(ZIA, str(dit2[1]))
        else:
            dire(ZIA, "Je n'ai pas compris")
    except Exception as e:
        raise

    #memory.subscribeToEvent("WordRecognized", getName(), "onWordRecognized")

    # try:
    #     # Start the speech recognition engine with user Test_ASR
    #     asr.subscribe("Test_ASR")
    #     print 'Speech recognition engine started'
    #     time.sleep(20)
    #     if asr.SpeechDetected:
    #         print str(asr.WordRecognized)
    #         dire(ZIA,asr.WordRecognized)
    # except:
    #     print "Je n'ai pas compris"
    #
    asr.unsubscribe("Test_ASR")
    return motreconnu

def onWordRecognized(key, value, message):
    if(len(value) > 1):# and value[1] >= self.getParameter("Confidence threshold (%)")/100.):
        print wordRecognized(value[0]) #~ activate output of the box
    else:
        pass

def main() :
    if len(sys.argv) < 2 :
        nao_ip = NAO_IP
    else:
        nao_ip = sys.argv[1]

    phr=""
    dire(ZIA, "bonjour")
    while phr != "fin" :
    	dire(ZIA, "je t'écoute")
    	phr = ecoute(ZIA)
    	dire(ZIA, phr)

main()
