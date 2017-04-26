# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.52])
keys.append([-0.0399261])

names.append("HeadYaw")
times.append([0.52])
keys.append([0.076658])

names.append("LAnklePitch")
times.append([0.52])
keys.append([-0.326784])

names.append("LAnkleRoll")
times.append([0.52])
keys.append([0.135034])

names.append("LElbowRoll")
times.append([0.52])
keys.append([-1.0891])

names.append("LElbowYaw")
times.append([0.52])
keys.append([-1.85005])

names.append("LHand")
times.append([0.52])
keys.append([0.2616])

names.append("LHipPitch")
times.append([0.52])
keys.append([-0.11194])

names.append("LHipRoll")
times.append([0.52])
keys.append([0.786984])

names.append("LHipYawPitch")
times.append([0.52])
keys.append([0.0107799])

names.append("LKneePitch")
times.append([0.52])
keys.append([0.394196])

names.append("LShoulderPitch")
times.append([0.52])
keys.append([1.75639])

names.append("LShoulderRoll")
times.append([0.52])
keys.append([-0.314159])

names.append("LWristYaw")
times.append([0.52])
keys.append([-0.783916])

names.append("RAnklePitch")
times.append([0.52])
keys.append([-1.1863])

names.append("RAnkleRoll")
times.append([0.52])
keys.append([0.0511902])

names.append("RElbowRoll")
times.append([0.52])
keys.append([0.377406])

names.append("RElbowYaw")
times.append([0.52])
keys.append([1.40664])

names.append("RHand")
times.append([0.52])
keys.append([0.0608])

names.append("RHipPitch")
times.append([0.52])
keys.append([-0.93118])

names.append("RHipRoll")
times.append([0.52])
keys.append([-0.335904])

names.append("RHipYawPitch")
times.append([0.52])
keys.append([0.0107799])

names.append("RKneePitch")
times.append([0.52])
keys.append([2.11255])

names.append("RShoulderPitch")
times.append([0.52])
keys.append([1.26252])

names.append("RShoulderRoll")
times.append([0.52])
keys.append([-0.105888])

names.append("RWristYaw")
times.append([0.52])
keys.append([0.766958])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err
