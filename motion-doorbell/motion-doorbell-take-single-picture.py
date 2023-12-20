import os
import datetime
now = datetime.datetime.now()
FILENAME = "/home/pi/motion-doorbell/output/%04d%02d%02d_%02d%02d.jpg" % (now.year, now.month, now.day, now.hour, now.minute)
os.system("echo %s >> /tmp/pictures.txt" % FILENAME)
CMD = "fswebcam -d /dev/video0 -r 1920x1080 --jpeg 85 --timestamp '%%Y-%%m-%%d %%H:%%M (%%Z)' --font 'sans:20' --line-colour '#FF000000' --title 'Motion Doorbell' --no-shadow --save %s" % FILENAME
os.system(CMD)
