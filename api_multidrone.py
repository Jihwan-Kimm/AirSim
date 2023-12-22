import airsim
import cv2
import numpy as np
import os
import pprint 
import tempfile

# Connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()

# Start control
drone_names = ["Drone" + str(i) for i in range(100)]
for drone in drone_names:
    client.enableApiControl(True, drone)
for drone in drone_names:
    client.armDisarm(True, drone)

for i in range(10):
    # Takeoff command must be given before the flight command
    airsim.wait_key('Press any key to takeoff')
    takeoff_tasks = [client.takeoffAsync(vehicle_name=drone) for drone in drone_names]
    for task in takeoff_tasks:
        task.join()

    # Flight control command
    airsim.wait_key('Press any key to move vehicles')
    move_tasks = [client.moveToPositionAsync(0, 0, -int(drone[-1])-5, 5, vehicle_name=drone) for drone in drone_names]
    for task in move_tasks:
        task.join()

# Finish control
for drone in drone_names:
    client.armDisarm(False, drone)
client.reset()
for drone in drone_names:
    client.enableApiControl(False, drone)