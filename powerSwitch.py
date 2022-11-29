from __future__ import print_function
import dlipower, time, sys

"""
OUTLET NAMES:
1. lg
2. samsung
3. roku
4. hisense
5. sabrina
6. amazon
7. amlogic

These are case-sensitive
"""

switch = dlipower.PowerSwitch(hostname="10.0.0.8", userid="admin", password="device123")

def status(arg=None):
  """
  Prints status of all outlets.
  type 'python3 powerSwitch.py status' from DailyBread directory
  """
  print("Status of all the outlets are: ", switch)

def cycleAll(arg=None):
  """
  Power cycles all the outlets 
  type 'python3 powerSwitch.py cycleAll' from DailyBread directory
  """
  allOnOff("OFF")
  print("Wait for 10 seconds..")
  time.sleep(10)
  allOnOff("ON")

def cycleSingle(device):
  """
  Target a specific outlet by name and turn it off then on
  type 'python3 powerSwitch.py cycleSingle <brand>'
  """
  for outlet in range(len(switch)):
    if device == switch[outlet].name:
      print("Status of device is: ", switch[outlet].state)
      print("Powering off..")
      switch[outlet].state = "OFF"
      time.sleep(3)
      print("Powering on..")
      switch[outlet].state = "ON"
      print("Outlet for", switch[outlet].description, "is currently:", switch[outlet].state)

def toggle(device):
  """
  Toggles power to specific outlet. Flips the outlet status
  type 'python3 powerSwitch.py toggle <brand>'
  """
  for outlet in range(len(switch)):
    if device == switch[outlet].name:
      state = "ON" if switch[outlet].state == "OFF" else "OFF"
      switch[outlet].state = state
      print("Outlet for", switch[outlet].description, "is currently:", switch[outlet].state)

def allOnOff(option):
  """
  Sets status of all outlets to desired option.
  type 'python3 powerSwitch.py allOnOff <ON|OFF>' 
  """
  print("Cycling all outlets %s.." % (option.upper()))
  for outlet in range(len(switch)):
    switch[outlet].state = option.upper() 
  time.sleep(8)
  status()

if __name__ == "__main__":
  switch = dlipower.PowerSwitch(hostname="10.0.0.8", userid="admin", password="device123")
  argument = "nothing" if len(sys.argv) == 2 else sys.argv[2]
  globals()[sys.argv[1]](argument)

