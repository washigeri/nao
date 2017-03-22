#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--é€àçœ--
####Afficher les données des moteurs

NAO_IP = "localhost"
NAO_PORT = 9559

import time
import datetime
import os
import sys

def main() :
        if len(sys.argv) < 2 :
                nao_ip = NAO_IP
        else:
                nao_ip = sys.argv[1]

	R2D=57.295779513082320876798154814105

	try:
		from naoqi import ALProxy
	except:
		print "Le module naoqi n'a pas été trouvé"
		exit (1)

	almemoryproxy = ALProxy("ALMemory", nao_ip, 9559)

	#----clés à lire---
	points=['HeadPitch','HeadYaw','LAnklePitch','LAnkleRoll','LElbowRoll','LElbowYaw','LHand','LHipPitch','LHipRoll','LHipYawPitch','LKneePitch','LShoulderPitch','LShoulderRoll','LWristYaw','RAnklePitch','RAnkleRoll','RElbowRoll','RElbowYaw','RHand','RHipPitch','RHipRoll','RKneePitch','RShoulderPitch','RShoulderRoll','RWristYaw']
	tmpl=['Device/SubDeviceList/%s/Position/Sensor/Value','Device/SubDeviceList/%s/Temperature/Sensor/Value','Device/SubDeviceList/%s/ElectricCurrent/Sensor/Value','Device/SubDeviceList/%s/Hardness/Actuator/Value']
	alkeys=[]
	for point in points:
		for t in tmpl:
			alkeys.append(t%point)

	#----taille de la première colonne----
	maxlen=7
	for point in points:
		l=len(point)
		if l>maxlen:
			maxlen=l
	nbTmpl=len(tmpl)

	#----process----
	values=almemoryproxy.getListData(alkeys) # lecture des données instantanées
	ttp="----"+str(datetime.datetime.now())+"----\n"+("--Nom--".center(maxlen))+" - --Pos-- - -Temp-- - Courant- Stiffness\n" # titre à afficher
	courant=0.0 #total courant
	i=0
	for point in points: # pour chaque articulation
		courant+=values[i+2]
		ttp+="%s =% 7.02f - % 2.01fC - %1.03fA -% 4d%%\n"%(point.ljust(maxlen),values[i]*R2D,values[i+1],values[i+2],int(values[i+3]*100))
		#ttp+="%s =% 7.02f\xF8 - % 2.01f\xF8C - %1.03fA -% 4d%%\n"%(point.ljust(maxlen),values[i]*R2D,values[i+1],values[i+2],int(values[i+3]*100))
		i+=4
	print ttp, #affichage d'un seul coup
	print 'Total courant=%.03fA'%courant


if __name__ == "__main__":
    main()
