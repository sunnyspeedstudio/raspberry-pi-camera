from datetime import datetime
from gpiozero import Button
import picamera
import time
import os
import subprocess

photo_button = Button(19)
# video_button = Button(20)
preview_button = Button(20)

pc = picamera.PiCamera()
pc.resolution = (2400, 1600) # same aspect ratio to the screen resolution (480x320 on the 3.5 inch screen), so that the preview can take up the whole screen.
pc.start_preview()

running = True
recording = False
inPreview = True
filmSimulation = True # put wanted HaldCLUT files in the HaldCLUT folder
outputFolder = '/var/www/html/'


def toggle_preview():
        global inPreview
        if inPreview:
                inPreview = False
                pc.stop_preview()
        else:
                inPreview = True
                pc.start_preview()


def apply_film_simulation(convertTool, inputFile, haldClutFile, outputFile):
	process = subprocess.Popen([convertTool, inputFile, haldClutFile, '-hald-clut', outputFile], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
	return


def take_photo():
	timestamp = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
	outputFile = outputFolder + 'photo-' + timestamp + '.jpg'
	pc.capture(outputFile)
	print('Photo is taken')
	if filmSimulation:
		toggle_preview()
		for subfolder, folders, files in os.walk('/home/pi/raspberry_pi_camera/HaldCLUT'):
			for f in files:
				haldClutFile = subfolder + os.sep + f
				haldClutName = f[:-4]
				outputFileWithFilmSimulation = outputFolder + 'photo-' + timestamp + '-' + haldClutName + '.jpg'
				apply_film_simulation('convert', outputFile, haldClutFile, outputFileWithFilmSimulation)
		toggle_preview()
	print('Film simulation is applied')


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
		# video_button.when_pressed = record_video
		preview_button.when_pressed = toggle_preview
		time.sleep(1)

except KeyboardInterrupt:
	pc.stop_preview()
	running = False
