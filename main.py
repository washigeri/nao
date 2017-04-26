def main(robotIP, PORT=9559, ballSize, landMarkSize):

    # Get the services ALMotion & ALRobotPosture.

    motion_service = session.service("ALMotion")
    posture_service = session.service("ALRobotPosture")

    # Wake up robot
    motion_service.wakeUp()

    # Send robot to Stand Init
    posture_service.goToPosture("StandInit", 0.5)

    tracker = ALProxy("ALTracker", IP, PORT)

    # Add target to track.
    eventName = "ALTracker/RedBallDetected"
    diameterOfBall = ballSize
    tracker.registerTarget(targetName, diameterOfBall)

    # set mode
    tracker.setMode("Move")

    tracker.trackEvent(eventName)

    while(!tracker.isNewTargetDetected()):
        motionProxy.moveTo(0, 0, 1.05)

    tracker.setRelativePosition([-0.5, 0.0, 0.0, 0.0, 0.0, 0.0])
    #position = tracker.getTargetPosition(0)
    if(!tracker.isTargetLost()):

        execfile("ramassage.py")

        while(!tracker.isNewTargetDetected()):
            motionProxy.moveTo(0, 0, 1.05)

        eventName = "ALTracker/LandMarkDetected"
        size = landMarkSize
        LandMarkId = LandMarkId
        tracker.setMode("Move")

        tracker.trackEvent(eventName)
        tracker.setRelativePosition([-0.5, 0.0, 0.0, 0.0, 0.0, 0.0])

    # Stop tracker.
    tracker.stopTracker()
    tracker.unregisterAllTargets()

    time.sleep(1.0)


    if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="localhost",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")
    parser.add_argument("--ballsize", type=float, default=0.04,
                        help="Diameter of ball.")
    parser.add_argument("--landmarksize", type=float, default=0.2,
                        help="Land Mark Size.")


    args = parser.parse_args()
    main(args.ip, args.port, args.ballsize)