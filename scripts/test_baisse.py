import argparse
import motion
import time
import almath
from naoqi import ALProxy


def main(robotIP, PORT=9559):

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)# Wake up robot
    motionProxy.wakeUp()

    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)

    # Activate Whole Body Balancer
    motionProxy.wbEnable(True)

    # Legs are constrained fixed
    stateName  = "Fixed"
    supportLeg = "Legs"
    motionProxy.wbFootState(stateName, supportLeg)

    # Constraint Balance Motion
    supportLeg = "Legs"
    motionProxy.wbEnableBalanceConstraint(True, supportLeg)

    # Com go to LLeg
    supportLeg = "LLeg"
    motionProxy.wbGoToBalance(supportLeg, 2.0)

    # RLeg is free
    stateName  = "Free"
    supportLeg = "RLeg"
    motionProxy.wbFootState(stateName, supportLeg)

    # RLeg is optimized
    effector = "RLeg"
    axisMask = 63
    frame    = motion.FRAME_WORLD

    # RLeg motion
    effector = "RLeg"

    initTf = almath.Transform(motionProxy.getTransform(effector, frame, False))

    # Motion of the RLeg
    deltaTf  = almath.Transform(-0.1, -0.1, 0.0)*almath.Transform().fromRotZ(-45.0*almath.TO_RAD)
    targetTf = initTf*deltaTf
    path     = list(targetTf.toVector())
    times    = 2.0 # seconds

    motionProxy.transformInterpolations(effector, frame, path, axisMask, times)

    time.sleep(2.0)

    # Lower the Torso
    effector = "Torso"
    initTf   = almath.Transform(motionProxy.getTransform(effector, frame, False))
    deltaTf  = almath.Transform(0.01, 0.0, -0.03) # x, y, z
    targetTf = initTf*deltaTf
    path     = list(targetTf.toVector())
    times    = 2.0 # seconds
    #motionProxy.transformInterpolations(effector, frame, path, axisMask, times)

    time.sleep(2.0)

    motionProxy.openHand('LHand')

    effector   = "LArm"
    frame      = motion.FRAME_ROBOT
    axisMask   = almath.AXIS_MASK_VEL    # just control position

    deltaTf  = almath.Transform(0.0, 0.0, -0.1)
    initTf = almath.Transform(motionProxy.getTransform(effector, frame, False))
    targetTf = initTf*deltaTf
    path     = list(targetTf.toVector())
    times    = 2.0 # seconds

    motionProxy.transformInterpolations(effector, frame, path, axisMask, times)
    
    motionProxy.closeHand('LHand')


    # send robot to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

    # Go to rest position
    motionProxy.rest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="localhost",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)