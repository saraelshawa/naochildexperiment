class MyClass():

  def onLoad(self):
    #put initialization code here
    pass

  def onUnload(self):
    #put clean-up code here
    pass

  def onInput_onStart(self):
    # Choregraphe simplified export in Python.
    from naoqi import ALProxy
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([0, 0, -0.333358, -0.333358])

    names.append("HeadYaw")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([0, 0, 1.41385, 1.41385])

    names.append("LAnklePitch")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([-0.35, -0.35, -0.35, -0.35])

    names.append("LAnkleRoll")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([0, 0, 0, 0])

    names.append("LElbowRoll")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([-1.00956, -1.00956, -1.00956, -0.764406])

    names.append("LElbowYaw")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([-1.3894, -1.3894, -1.3894, -1.3894])

    names.append("LHand")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([0.25, 0.25, 0.25, 0.47])

    names.append("LHipPitch")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([-0.45, -0.45, -0.45, -0.45])

    names.append("LHipRoll")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([0, 0, 0, 0])

    names.append("LHipYawPitch")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([0, 0, 0, 0])

    names.append("LKneePitch")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([0.7, 0.7, 0.7, 0.7])

    names.append("LShoulderPitch")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([1.3994, 1.3994, 1.3994, 0.171018])

    names.append("LShoulderRoll")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([0.299871, 0.299871, 0.299871, 0.299871])

    names.append("LWristYaw")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([0, 0, 0, 0.82877])

    names.append("RAnklePitch")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([-0.35, -0.35, -0.35, -0.35])

    names.append("RAnkleRoll")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([0, 0, 0, 0])

    names.append("RElbowRoll")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([1.00956, 1.00956, 0.559413, 0.559413])

    names.append("RElbowYaw")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([1.3894, 1.3894, 1.3894, 1.3894])

    names.append("RHand")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([0.25, 0.25, 0.66, 0.66])

    names.append("RHipPitch")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([-0.45, -0.45, -0.45, -0.45])

    names.append("RHipRoll")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([0, 0, 0, 0])

    names.append("RHipYawPitch")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([0, 0, 0, 0])

    names.append("RKneePitch")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([0.7, 0.7, 0.7, 0.7])

    names.append("RShoulderPitch")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([1.3994, 0.347584, 0.347584, 0.347584])

    names.append("RShoulderRoll")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([-0.299871, -0.299871, 0.0584174, 0.0584174])

    names.append("RWristYaw")
    times.append([1.08, 1.8, 2.68, 3.2])
    keys.append([0, 0, 0, 0])
    print("here")
    try:
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", "169.254.124.254", 9559)
      # motion = ALProxy("ALMotion")
      motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

    self.onStopped() #activate the output of the box
    pass

  def onInput_onStop(self):
    self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
    self.onStopped() #activate the output of the box
