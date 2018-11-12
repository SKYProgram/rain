x=123
print x
import RPi.GPIO as GPIO
import os
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.IN)
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(11,1)
while 1:
	time.sleep(10)
	if GPIO.input(13):
		print "Get Data Success"
		os.system("play rain.mp3")
		#os.system("python wechatmsg.py")
else:
		print"Failed"

