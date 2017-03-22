# -*- encoding: UTF-8 -*-

ROBOT_IP = "localhost"

import sys
from naoqi import ALProxy

def main():
        if len(sys.argv) < 2:
                nao_ip = ROBOT_IP
        else:
                nao_ip = sys.argv[1]

	ttsProxy = ALProxy("ALTextToSpeech",nao_ip,9559)

        ttsProxy.setParameter("pitchShift", 1.3)
        ttsProxy.say("Hello le Monde")

if __name__ == "__main__":
    main()

