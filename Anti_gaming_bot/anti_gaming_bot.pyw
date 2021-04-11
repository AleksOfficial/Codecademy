import psutil
import time
import ctypes

lolno ="terminated some steam app. No more gaming"
title="Pls stop gaming"

while True:
  terminator = 0
  print('getting process list ...')
  procs = [p.info for p in psutil.process_iter(['name', 'pid'])]
  for p in procs:
    if 'steam' in p['name']:
      terminator = 1
      #print(p['name']+' is running ...')
      psutil.Process(p['pid']).terminate()
  if terminator:
    ctypes.windll.user32.MessageBoxW(0, lolno, title, 1)
  time.sleep(30)

#Maybe extend this with some stats or smth. save the dry time and the attempts per month n stuff
