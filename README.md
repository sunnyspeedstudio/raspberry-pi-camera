# Raspberry Pi Camera with film simulation
Making a "real" raspberry pi mirrorless interchangeable-lens camera (MILC) with 3d printed case.

![raspberry_pi_camera](/images/camera-top.png)

# Hardware
![hardware](/images/hardware.png)
* Raspberry Pi
* Raspberry Pi HQ Camera (Sony IMX477 sensor)
* CS-mount lens, 2.8-12mm, f1.4
* Raspberry Pi battery module
* 3.5 inch touch screen
* buttons (12x12x7.3mm) and wires (photo button to pin 19, video button to pin 20, to match with the script)
* 3D printed case: https://www.thingiverse.com/thing:4740323

# Steps
1. Install display driver, https://github.com/goodtft/LCD-show
2. Install Apache web server, to view photos, `sudo apt-get install apache2` (optional, can also try "rsync")
3. Run the python script in this repo, `sudo python3 main.py`. The photos are saved to /var/www/html folder
4. To run the python script at startup, `sudo nano /etc/rc.local`, then add `sudo python3 full-path-to/main.py &` at the beginning of the file

For film simulation, ImageMagick (https://imagemagick.org/index.php) is required.

![raspberry_pi_camera](/images/camera.png)


Demo YouTube video:

[![YouTube Demo Video](https://img.youtube.com/vi/InYgHwcxmpg/0.jpg)](https://www.youtube.com/watch?v=InYgHwcxmpg&feature=youtu.be&ab_channel=sunnyspeedstudio)
