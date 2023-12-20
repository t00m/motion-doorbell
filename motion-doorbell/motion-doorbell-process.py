import os
import psutil

CMD_MOTION = "motion -c /home/pi/motion-doorbell.conf"

found = False
for proc in psutil.process_iter():
  try:
    if 'motion' in proc.name():
      found = True
  except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

if not found:
  print("Executing motion")
  os.system(CMD_MOTION)
else:
  print("Motion already running")
