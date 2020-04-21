import time
import random
import math
random.seed(time.time())

# revise parameters here
original_loc = [30.5081351900, 120.6791814900-0.00015] #center of your playground
radius_round = 0.00030
angle = 0 #radius
starttime = time.time()
count = 0
speed = 1/10 #for this the speed is about 6:02/1km

# part for generate gpx files.
frontstring = '''<?xml version="1.0"?>
<gpx version="1.1" creator="Xcode">'''
points=[]
while count<1600:
    count += 1
    radius = radius_round + math.cos(2*count*speed-0.8-0.5-2+2*angle)*radius_round/5+random.random()*radius_round*0.1
    loc = [math.cos((count*speed))*radius+original_loc[0], math.sin((count*speed))*radius*2+original_loc[1]]
    locationstring ='''
    <wpt lat="'''+str(loc[0])+'''" lon="'''+str(loc[1])+'''">'''
    timeAdd = '''
        <name>Haining</name>
        <time>'''
    current_time = time.localtime( starttime+count )
    timestring = str(current_time[0])+'-'+str(current_time[1])+'-'+str(current_time[2])+'T'+str(current_time[3])+':'+str(current_time[4])+':'+str(current_time[5])+'Z</time>'
    point = locationstring+timeAdd+timestring+'''
    </wpt>'''
    points.append(point)
endstring = '''
</gpx>'''

file = open("Location.gpx",'w')
file.write(frontstring)
for point in points:
    file.write(point)
file.write(endstring)
file.close()