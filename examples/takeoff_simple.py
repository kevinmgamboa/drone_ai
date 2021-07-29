from djitellopy import Tello
from time import sleep
#%%
# ------------------------------------------------------------------------------------
#                                    Drone Setup
# ------------------------------------------------------------------------------------
tello = Tello()
tello.connect()
print(tello.get_battery())
#%%
# ------------------------------------------------------------------------------------
#                                   Takeoff and Land
# ------------------------------------------------------------------------------------
# taking off the drone
tello.takeoff()
sleep(3)
print(f'taking off the ground \nBatery: {tello.get_battery()}')
# landing drone
tello.land()
#%%
# ------------------------------------------------------------------------------------
#                                  Takeoff, rotate and Land
# ------------------------------------------------------------------------------------
# taking off the drone
tello.takeoff()
sleep(5)
print(f'taking off the ground \nBatery: {tello.get_battery()}')
for i in range(4):
    # rotating drone
    tello.rotate_counter_clockwise(90)
    sleep(5)
# landing drone
tello.land()
