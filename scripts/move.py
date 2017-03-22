# -*- encoding: UTF-8 -*-
# broker par défaut

import sys
import argparse
import motion
import time
import almath
from naoqi import ALProxy
import os

NAO_IP = "localhost"
NAO_PORT = 9559

def main() :
        print sys.argv
        if len(sys.argv) == 1 :
                nao_ip = NAO_IP
                pos = sys.argv[1]
        else :
                nao_ip = sys.argv[1]
		pos = sys.argv[2] 

	try:
		postureProxy = ALProxy("ALRobotPosture", nao_ip, NAO_PORT)
	except:
		print "Impossible de se connecter a ", nao_ip
		sys.exit(1)

	# position du robot
	postureProxy.goToPosture(pos, 0.7)
        print "Fin du script..."

if __name__ == "__main__":
    main()
