def distance() :
    speed = input('speed is\n ')
    time = input('time is\n ')
    dist = float(speed) * float(time)
    print('distance in nm is\n', dist)

def speed() :
    dist = input('distance is\n ')
    time = input('time is\n ')
    speed = float(dist) / float(time)
    print('speed in kts is\n', speed)

def time() :
    speed = input('speed is\n ')
    dist = input('distance is\n')
    time = float(dist) / float(speed)
    print('time in hours is \n',time)

def headwind ():
    import math
    angle = input('angle between winds and course\n ')
    speed = input('the speed of winds in knts\n ')
    x= math.radians(float(angle))
    headwind= math.cos(x) *float(speed)

    if headwind<0:
         print('you have tailwind of\n ', round(abs(headwind)))
    if headwind>0:
         print('you have headwind of\n', round(headwind))
    if headwind ==0:
         print('you have 0 tailwind/headwind\n')

def crosswind():
    import math
    angle = input('angle between winds and course\n ')
    speed = input('the speed of winds in knts\n ')
    x= math.radians(float(angle))
    crosswind= math.sin(x) *float(speed)

    if crosswind<0:
         print('you have crosswind from the left\n ', round(abs(crosswind)))
    if crosswind>0:
         print('you have crosswind from the right\n ', round(crosswind))
    if crosswind == 0:
         print('you have 0 crosswind\n ')
def  TAS():
    altitude=input('your actual altitude\n ')
    IAS= input('your indicated airspeed \n')
    TAS= float(IAS) +((float(altitude)/1000)* 1.8)
    print('your true airspeed in kts is\n',round(TAS))

def GS():
    print(' 1.headwind \n 2.tailwind \n ')
    choice =input()
    tas = input('what is your true airspeed \n')
    if choice == '1':
     tailwind=input('what headwind component do you have ?')
    groundspeed = float(tas) - float(tailwind)
    print('your ground speed is\n',groundspeed)

    if choice == '2':
     tailwind=input('what tailwind component do you have ?')
    groundspeed = float(tas) + float(tailwind)
    print('your groundspeed is\n',groundspeed)


print('please enter a function\n 1. distance \n 2. speed \n 3.time \n 4.headwind/Tailwind \n 5. crosswind \n 6. TAS\n 7.Ground speed \n' )
choice = input()

if choice == '1':
    distance()
if choice == '2':
    speed()
if choice == '3':
    time()
if choice == '4':
    headwind()
if choice == '5':
    crosswind()
if choice== '6':
    TAS()
if choice=='7':
    GS()

