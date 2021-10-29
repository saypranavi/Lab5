#!/usr/bin/python37all
import cgi
import json

 #op1 = 0 #intialize all options
zer = data.getvalue('Zero')
s1 = data.getvalue('slider1') #get slider value
#op1 = s1

jsondata = {"Zero":zer, "Angle":s1} #create the json text list to send data to

with open('inAngle.txt', 'w') as f:  #input the data from the submission to the txt file
  json.dump(jsondata, f)


print ('Content-type: text/html\n\n')
print ('<html>')
print ('<form action="/cgi-bin/stepper_control.py" method="POST">')
print ('<input type="submit" value="Zero" style="font-size: 15px"><br> <br>')
print ('<input type="range" name="slider1" min ="0" max="360" value ="180" style="width: 250px">' % s1)
print ('<input type="submit" value="Submit" style="font-size: 15px">')
print ('</form>')
print ('Angle (degrees) = %s' % s1) #display the brightness value after submission
print ('</html>')