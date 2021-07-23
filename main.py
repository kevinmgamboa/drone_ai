from djitellopy import Tello
import utils
import cv2 as cv

#%%

start_counter = 0

# connecting to tello
me = Tello()
me.connect()
#%%
# initializing velocity variables
me.for_back_velocity, me.left_right_velocity, me.up_down_velocity, me.yaw_velocity = 0, 0, 0, 0
# batery information
print(me.get_battery())
#%%
while True:
    pass
