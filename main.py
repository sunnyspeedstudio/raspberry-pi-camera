from datetime import datetime
from gpiozero import Button
import picamera
import time

photo_button = Button(19)
video_button = Button(20)

pc = picamera.PiCamera()
pc.resolution = (1920, 1080)
pc.start_preview()

running = True
recording = False

def take_photo():
	pc.capture('/var/www/html/photo-' + str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) + '.jpg')
	print('Photo is taken')

def record_video():
	global recording
	if recording:
		recording = False
		pc.stop_recording()
		print('Video is stopped')
	else:
		recording = True
		pc.start_recording('/var/www/html/video-' + str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) + '.h264')
		print('Video is started')

try:
	while running:
		photo_button.when_pressed = take_photo
		video_button.when_pressed = record_video
		#print('recording = ', recording)
		time.sleep(1)

except KeyboardInterrupt:
	pc.stop_preview()
	running = False
