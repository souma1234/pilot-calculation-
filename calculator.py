def distance() :
    speed = input('speed is\n ')
    time = input('time  is \n ')
    dist = float(speed) * (float(time)/60)
    print(f'distance is {dist}nm')

def speed() :
    dist = input('distance is\n ')
    time = input('time in hrs is\n ')
    speed = float(dist) / float(time)
    print(f'speed is {speed}kts')

def time() :
    speed = input('speed is\n ')
    dist = input('distance is\n')
    time = float(dist) / float(speed)
    print(f'time is {time}hours')

def headwind ():
    import math
    angle = input('angle between winds and course\n ')
    speed = input('the speed of winds in knts\n ')
    x= math.radians(float(angle))
    headwind= math.cos(x) *float(speed)

    if headwind<0:
         print(f'you have {round(abs(headwind))}kts of tailwind')
    if headwind>0:
         print(f'you have {round(headwind)}kts of headwind')
    if headwind ==0:
         print('you have 0 tailwind/headwind')

def crosswind():
    import math
    angle = input('angle between winds and course\n ')
    speed = input('the speed of winds in knts\n ')
    x= math.radians(float(angle))
    crosswind= math.sin(x) *float(speed)

    if crosswind<0:
         print(f'you have {round(crosswind)} from the left ')
    if crosswind>0:
         print(f'you have {round(crosswind)} from the right ')
    if crosswind == 0:
         print('you have 0 crosswind\n ')
def  TAS():
    altitude=input('your actual altitude\n ')
    IAS= input('your indicated airspeed \n')
    TAS= float(IAS) +((float(altitude)/1000)* 1.8)
    print(f'your true airspeed is {round(TAS)} kts')

def GS():
    print(' 1.headwind \n 2.tailwind \n ')
    choice =input()
    tas = input('what is your true airspeed \n')
    if choice == '1':
     tailwind=input('what headwind component do you have ?')
    groundspeed = float(tas) - float(tailwind)
    print(f'your GS is {groundspeed}')

    if choice == '2':
     tailwind=input('what tailwind component do you have ?')
    groundspeed = float(tas) + float(tailwind)
    print(f'your groundspeed is {groundspeed}')

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

