import time
import argparse
import motion
import almath
from naoqi import ALProxy

NAO_IP = "localhost"
NAO_PORT = 9559

def main(robotIP, PORT=9559) :

	motionProxy  = ALProxy("ALMotion", robotIP, PORT)
	postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

	# Wake up robot
	motionProxy.wakeUp()

	postureProxy.goToPosture("StandInit", 0.5)

	# Activate Whole Body Balancer
	motionProxy.wbEnable(True)

	names = list()
	times = list()
	keys = list()

	t = 5

	motionProxy.openHand('RHand')

	names.append("HeadPitch")
	times.append([t])
	keys.append([0.3856])

	names.append("HeadYaw")
	times.append([t])
	keys.append([-0.679604])

	names.append("LAnklePitch")
	times.append([t])
	keys.append([-0.144238])

	names.append("LAnkleRoll")
	times.append([t])
	keys.append([-0.31903])

	names.append("LElbowRoll")
	times.append([t])
	keys.append([-0.102736])

	names.append("LElbowYaw")
	times.append([t])
	keys.append([-0.81613])

	names.append("LHand")
	times.append([t])
	keys.append([0.0248001])

	names.append("LHipPitch")
	times.append([t])
	keys.append([0.147306])

	names.append("LHipRoll")
	times.append([t])
	keys.append([0.334454])

	names.append("LHipYawPitch")
	times.append([t])
	keys.append([-1.04921])

	names.append("LKneePitch")
	times.append([t])
	keys.append([1.1704])

	names.append("LShoulderPitch")
	times.append([t])
	keys.append([1.21335])

	names.append("LShoulderRoll")
	times.append([t])
	keys.append([-0.314159])

	names.append("LWristYaw")
	times.append([t])
	keys.append([0.052114])

	names.append("RAnklePitch")
	times.append([t])
	keys.append([-1.18267])

	names.append("RAnkleRoll")
	times.append([t])
	keys.append([0.0567999])

	names.append("RElbowRoll")
	times.append([t])
	keys.append([0.069072])

	names.append("RElbowYaw")
	times.append([t])
	keys.append([1.75485])

	names.append("RHand")
	times.append([t])
	keys.append([0.5548])

	names.append("RHipPitch")
	times.append([t])
	keys.append([-0.702614])

	names.append("RHipRoll")
	times.append([t])
	keys.append([-0.79046])

	names.append("RHipYawPitch")
	times.append([t])
	keys.append([-1.04921])

	names.append("RKneePitch")
	times.append([t])
	keys.append([2.10776])

	names.append("RShoulderPitch")
	times.append([t])
	keys.append([1.27633])

	names.append("RShoulderRoll")
	times.append([t])
	keys.append([-0.523136])

	names.append("RWristYaw")
	times.append([t])
	keys.append([-0.891296])

	motionProxy.angleInterpolation(names, keys, times, True)

	motionProxy.angleInterpolation(names, keys, times, True)

	motionProxy.closeHand('RHand')

	postureProxy.goToPosture("Crouch", 0.5)

    # send robot to Pose Init
	postureProxy.goToPosture("StandInit", 0.5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="localhost",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)