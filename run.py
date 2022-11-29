#! /usr/bin/python3
from pathlib import Path
import time
import os, json, subprocess
import discoverDevices, updateCLI, refreshTestPlan, updateFW, openConfig, UAreplace, adbCon, wakeOnLan

def runYTS(deviceDets):
  """
  Grabs device details from config.json and interoplate into a custom yts command.
  """
  plist=[]
  adbCon.connect()
  for n in range(len(deviceDets)):
     brand = deviceDets[n].keys()
     brand = list(brand).pop()
     UA = UAreplace.replace(deviceDets, brand, n)
     ytsCommand = f"""yts cert "{deviceDets[n][brand]["ip"]}" --test-version=dev --user-agent="{UA[0]}" --nonprod-api --no-colors --retry-failed=2 --skip "In-app Overall Endurance" 
     "In-app Video Endurance" "In-app 4 Hours Browse Watch" "Functional Tests User Agent Cobalt Version User Agent" "HDRPQ" "HDRHLG" --rerun --json-output="C:\\Users\\ppsde\\logs\\{updateFW.getDevVer()}_{deviceDets[n][brand]["certscope"]}.json" --submit >> C:\\Users\\ppsde\\logs\\{updateFW.getDevVer()}_{deviceDets[n][brand]["certscope"]} """ 
     subprocess.call(f"""echo {ytsCommand}"\n\n{UA[1]}\n\n" > C:\\Users\\ppsde\\logs\\{updateFW.getDevVer()}_{deviceDets[n][brand]["certscope"]}""", shell=True)
     p = subprocess.Popen([ytsCommand], shell=True)
     plist.append(p)
  exit_codes = [p.wait() for p in plist]  
#   subprocess.call("""gsutil -h "Content-Type:text/plain;charset=utf-8" -m cp -r C:\\Users\\ppsde\\logs* gs://daily-bread-logs""", shell=True)
  return exit_codes

def run():
   #powerSwitch.cycleAll()
   wakeOnLan.verify_wake()   
  #  updateCLI.update()
#   refreshTestPlan.freshPlan(openConfig.read())    
   runYTS(openConfig.read()) 

if __name__ == "__main__":
    run()
