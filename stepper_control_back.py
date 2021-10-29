import stepper
import PCF8591
import json
import RPi.GPIO as GPIO
import time

while true:
  with open("inAngle.txt", 'r') as f:
    info = json.load(f) #read the text file
    zer = info['Zero']
    ang = info['Angle']
    if zer==1:
      stepper.zero()
    if ang >0:
      stepper.goAngle(ang)
