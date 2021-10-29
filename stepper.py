import RPi.GPIO as GPIO
import time
import PCF8591

class photoresister:
  def __init__(self,address):
    self.photo = PCF8591(address)
  
  def readLight(self):
    return (self.photo.read(0))
  #217-220 "off"
  #194 on 

pr = photoresister(0x48)
led = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 1)

pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

# Define the pin sequence for counter-clockwise motion, noting that
# two adjacent phases must be actuated together before stepping to
# a new phase so that the rotor is pulled in the right direction:
sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
            [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
        
state = 0  # current position in stator sequence

def delay_us(tus): # use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass

def halfstep(dir):
  # dir = +/- 1 (ccw / cw)
  state += dir
  if state > 7: state = 0
  elif state < 0: state =  7
  for pin in range(4):    # 4 pins that need to be energized
    GPIO.output(pins[pin], sequence[state][pin])
  delay_us(1000)

def moveSteps(steps, dir):
  # move the actuation sequence a given number of half steps
  for step in steps:
    halfstep(dir)

class Stepper:

  def goAngle(num):
    moveSteps(num, 1)
    
    
  def zero():
    while (pr.readLight()>200): 
      moveSteps(5,1)
      

try:
  moveSteps(1000,1)
except:
  pass
GPIO.cleanup() 