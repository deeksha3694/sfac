
 
  from neo import easyGpio      # LED Beacon from neo import Accel    # import accelerometer 
from neo import Magno    # import magnometer 
from neo import Gyro     # import gyroscope 
from time import sleep   #delay element 
#import request     #internet posting request 
import httplib, urllib 
     
 
beacon = easyGpio(13) 
beacon.pinOUT() # Make pin output 

#motion sensor 
gyro = Gyro() 
accel = Accel() 
magno = Magno() 
#Heart pulse tuning 
def heartpulse(): 
        a = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read()) 
        global x 
        if a<=1638: 
 	    x=62 
        elif 1638>a and a<=1674: 
            x=63 
        elif 1674>a and a<=1710: 
            x=64 
        elif 1710>a and a<=1746: 
            x=65 
        elif 1746>a and a<=1782: 
            x=66 
        elif 1782>a and a<=1818: 
            x=67 
        elif 1818>a and a<=1854: 
            x=68 
        elif 1854>a and a<=1890: 
            x=69 
	  elif 1890>a and a<=1926: 
            x=70 
        elif 1926>a and a<=1962: 
            x=71 
        elif 1962>a and a<=1998: 
	    x=72 
        elif 1998>a and a<=2142: 
            x=73 
	elif 2142>a and a<=2178: 
            x=74 
        elif 2178>a and a<=2214: 
            x=75 
        elif 2214>a and a<=2250: 
            x=76 
        elif 2250>a and a<=2286: 
            x=77 
        elif 2286>a and a<=2322: 
            x=78 
        elif 2322>a and a<=2358: 
            x=79 
        elif 2358>a and a<=2394: 
            x=80 
        elif 2394>a and a<=2430: 
            x=81 
	elif 2430>a and a<=2466: 
            x=82 
        elif 2466>a and a<=2502: 
            x=83 
        elif 2502>a and a<=2538: 
            x=84 
        elif 2538>a and a<=2574: 
            x=85 
	elif 2574>a and a<=2610: 
            x=86 
        elif 2610>a and a<=2646: 
            x=87 
        elif 2646>a and a<=2682: 
            x=88 
        elif 2682>a and a<=2718: 
            x=89 
        elif 2718>a and a<=2754: 
            x=90 
        elif 2754>a and a<=2790: 
            x=91 
        elif 2790>a and a<=2826: 
            x=92 
        elif 2826>a and a<=2862: 
            x=93 
        elif 2862>a and a<=2898: 
            x=94 
        elif 2898>a and a<=2934: 
            x=95 
        elif 2934>a and a<=2970: 
            x=96 
        elif 2970>a and a<=3006: 
            x=97 
	elif 3006>a and a<=3042: 
            x=98 
        elif 3042>a and a<=3078: 
            x=99 
        elif 3078>a and a<=3114: 
            x=100 
        elif 3114>a and a<=3150: 
            x=101 
        elif 3150>a and a<=3186: 
            x=102 
        elif 3186>a and a<=3222: 
            x=103 
        elif 3222>a and a<=3258: 
            x=104 
        elif 3258>a and a<=3294: 
            x=105 
        elif 3294>a and a<=3330: 
            x=106 
        elif 3330>a and a<=3366: 
            x=107 
        elif 3366>a and a<=3402: 
            x=108 
        elif 3402>a and a<=3438: 
            x=109 
	elif 3438>a and a<=3474: 
            x=110 
        elif 3474>a and a<=3510: 
            x=111 
        elif 3510>a and a<=3546: 
            x=112 
        elif 3546>a and a<=3582: 
            x=113 
        elif 3582>a and a<=3618: 
            x=114 
        elif 3618>a and a<=3654: 
            x=115 
        elif 3654>a and a<=3690: 
            x=116 
        elif 3690>a and a<=3726: 
            x=117 
        elif 3726>a and a<=3762: 
            x=118 
        elif 3762>a and a<=3798: 
            x=119 
        elif 3798>a and a<=3834: 
            x=120 
        elif 3834>a and a<=3870: 
            x=121 
	elif 3870>a and a<=3906: 
            x=122 
        elif 3906>a and a<=3942: 
            x=123 
        elif 3942>a and a<=3978: 
            x=124 
        elif 3978>a and a<=4014: 
            x=125 
        elif 4014>a and a<=4050: 
            x=126 
        else: 
            x=130 
sleep(0) 
#Temperature Sensor Tuning 
def temperature(): 
    global y 
    temp = int(open("/sys/bus/iio/devices/iio:device0/in_voltage1_raw").read()) 
    if temp<=440: 
        y=94 
        print "Temp is:"+str(y) 
    elif temp>440 and temp<=450: 
        y=95 
        print "Temp is:"+str(y) 
    elif temp>450 and temp<=460: 
        y=96 
    print "Temp is:"+str(y) 
    elif temp>460 and temp<=470: 
        y=97 
        print "Temp is:"+str(y) 
    elif temp>470 and temp<=480: 
        y=98 
        print "Temp is:"+str(y) 
    elif temp>480 and temp<=490: 
        y=99 
        print "Temp is:"+str(y) 
    elif temp>490 and temp<=500: 
        y=100 
        print "Temp is:"+str(y) 
    elif temp>510 and temp<=520: 
        y=101 
        print "Temp is:"+str(y) 
    elif temp>520 and temp<=530: 
        y=102 
 print "Temp is:"+str(y) 
    elif temp>530 and temp<=540: 
        y=103 
 print "Temp is:"+str(y)
sleep(0) 
    #internet posting 
def doit(): 
    print ("doit") 
    #params = urllib.urlencode({'field1': x,'field2': y,'field3':accelVals[0],'key':'5R638RJU5X8G3I1E'}) 
    params = urllib.urlencode({'field1': x,'field2':          y,'field3':accelVals[0],'field4':accelVals[1],'field5':accelVals[2],'field6':gyroVals[0],'field 7':gyroVals[1],'field8':gyroVals[2],'key':'5R638RJU5X8G3I1E'}) 
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"} 
    conn = httplib.HTTPConnection("api.thingspeak.com:80") 
    try: 
        conn.request("POST", "/update", params, headers) 
        response = conn.getresponse() 
print response.status, response.reason 
        data = response.read() 
        conn.close() 
except: 
        print "connection failed"  
 
sleep(0) 
#Main Thread 
while True: 
#Post Temperature to Terminal 
        temperature() 
  #Post Heart pulse to Terminal 
        heartpulse() 
        print'Heart Pulse:'+str(x) 
  
 #9 Axis data 
 gyroVals = gyro.get() # Returns a full xyz list [x,y,z] realtime (integers/degrees) 
 print "Gyroscope X: "+str(gyroVals[0])+" Y: "+str(gyroVals[1])+" Z: "+str(gyroVals[2])# turn current values (ints) to strings 
 
 accelVals = accel.get() # Same as gyro return xyz of current displacment force 
 print "Accelerometer X: "+str(accelVals[0])+" Y: "+str(accelVals[1])+" Z: "+str(accelVals[2]) 
 
 magnoVals = magno.get() # Above 
 print "Magnometer X: "+str(magnoVals[0])+" Y: "+str(magnoVals[1])+" Z: "+str(magnoVals[2]) 
 #beacons LED 
 beacon.on() 
 sleep(0.5)  
 beacon.off() 
 sleep(0.5) 
 #POST DATA 
 doit() 
 sleep(1) 
  
