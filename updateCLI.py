import os
import time
def update():
  """
  Updates CLI to YTS nightly build
  """
 # os.chdir("/home/doughfactory/") 
 # os.system("curl -O -L https://dev.yts.devicecertification.youtube/yts_server.zip; rm -rf yts_server; unzip yts_server.zip -d yts_server")

  os.chdir(r"C:\Users\ppsde") 
  os.system("curl -O -L https://dev.yts.devicecertification.youtube/yts_server.zip")
  time.sleep(2)
  os.system("rmdir yts_server")
  os.system("unzip yts_server.zip -d yts_server")
  

  #  unzip yts_server.zip -d yts_server; cd yts_server; npm link")