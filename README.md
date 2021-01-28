# Raspberry Pi Camera
Making a "real" raspberry pi camera with 3d printed case.

![raspberry_pi_camera](/images/camera.png)

# Hardware
![hardware](/images/hardware.png)
* Raspberry Pi
* Raspberry Pi HQ Camera (Sony IMX477 sensor)
* CS-mount lens, 2.8-12mm, f1.4
* Raspberry Pi battery module
* 3.5 inch touch screen
* buttons and wires (photo button to pin 19, video button to pin 20)

# Steps
1. Install display driver, https://github.com/goodtft/LCD-show
2. Install Apache web server, to view photos, `sudo apt-get install apache2`
3. Run the python script in this repo, `sudo python main.py`. The photos are saved to /var/www/html folder
4. To run the python script at startup, `sudo nano /etc/rc.local`, then add `sudo python main.py &` before exit 0
