# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.52])
keys.append([0.480647])

names.append("HeadYaw")
times.append([0.52])
keys.append([-0.17952])

names.append("LAnklePitch")
times.append([0.52])
keys.append([0.693326])

names.append("LAnkleRoll")
times.append([0.52])
keys.append([-0.155101])

names.append("LElbowRoll")
times.append([0.52])
keys.append([-0.753152])

names.append("LElbowYaw")
times.append([0.52])
keys.append([-2.08567])

names.append("LHand")
times.append([0.52])
keys.append([0.2616])

names.append("LHipPitch")
times.append([0.52])
keys.append([-0.589014])

names.append("LHipRoll")
times.append([0.52])
keys.append([0.17185])

names.append("LHipYawPitch")
times.append([0.52])
keys.append([-0.747016])

names.append("LKneePitch")
times.append([0.52])
keys.append([0.490838])

names.append("LShoulderPitch")
times.append([0.52])
keys.append([2.00029])

names.append("LShoulderRoll")
times.append([0.52])
keys.append([-0.15651])

names.append("LWristYaw")
times.append([0.52])
keys.append([-1.35763])

names.append("RAnklePitch")
times.append([0.52])
keys.append([-1.1863])

names.append("RAnkleRoll")
times.append([0.52])
keys.append([-0.0720561])

names.append("RElbowRoll")
times.append([0.52])
keys.append([0.0349066])

names.append("RElbowYaw")
times.append([0.52])
keys.append([1.40357])

names.append("RHand")
times.append([0.52])
keys.append([0.0608])

names.append("RHipPitch")
times.append([0.52])
keys.append([-0.579894])

names.append("RHipRoll")
times.append([0.52])
keys.append([-0.231592])

names.append("RHipYawPitch")
times.append([0.52])
keys.append([-0.747016])

names.append("RKneePitch")
times.append([0.52])
keys.append([2.11255])

names.append("RShoulderPitch")
times.append([0.52])
keys.append([1.01095])

names.append("RShoulderRoll")
times.append([0.52])
keys.append([-0.227074])

names.append("RWristYaw")
times.append([0.52])
keys.append([0.662646])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err
