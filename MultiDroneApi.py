import airsim
import cv2
import numpy as np
import os
import pprint 
import tempfile
import time

client = airsim.MultirotorClient()
client.confirmConnection()
drone_names = ["Drone" + str(i) for i in range(100)]

for drone in drone_names:
    client.enableApiControl(True, drone)
for drone in drone_names:
    client.armDisarm(True, drone)

takeoff_start_time = time.time()

takeoff_tasks = [client.takeoffAsync(vehicle_name=drone) for drone in drone_names]
for task in takeoff_tasks:
    task.join()


takeoff_end_time = time.time()
takeoff_duration = takeoff_end_time - takeoff_start_time 
print(f"Takeoff time: {takeoff_duration} seconds")


for i in range(5):
    print("Lap "+str(i))   

    # airsim.wait_key('Press any key to move vehicles')
    move1_start = time.time() 
    move_tasks = [client.moveToPositionAsync(0, 0, -int(drone[-1])-5, 5, vehicle_name=drone) for drone in drone_names]
    for task in move_tasks:
        task.join()

    move1_end = time.time() 
    move_duration = move1_end - move1_start
    print(f"Movement time: {move_duration} seconds")


    # airsim.wait_key('Press any key to move vehicles again')
    move2_start = time.time() 
    move_tasks = [client.moveToPositionAsync(5, 5, -10, 3, vehicle_name=drone) for drone in drone_names]
    for task in move_tasks:
        task.join()

    move2_end = time.time() 
    move_duration = move2_end - move2_start
    print(f"Movement time: {move_duration} seconds")


    # airsim.wait_key('Press any key to move vehicles again again')
    move3_start = time.time() 
    move_tasks = [client.moveToPositionAsync(0, 0, -10, 3, vehicle_name=drone) for drone in drone_names]
    for task in move_tasks:
        task.join()

    move3_end = time.time()  
    move_duration = move3_end - move3_start
    print(f"Movement time: {move_duration} seconds")




for drone in drone_names:
    client.armDisarm(False, drone)
client.reset()
for drone in drone_names:
    client.enableApiControl(False, drone)