from djitellopy import Tello
import utils
import cv2 as cv
import time
#%%

startCounter = 0

# connecting to tello
me = Tello()
me.connect()
#%%
# initializing velocity variables
me.for_back_velocity, me.left_right_velocity, me.up_down_velocity, me.yaw_velocity = 0, 0, 0, 0
# batery information
print(me.get_battery())
#%%

me.streamoff()
me.streamon()
#%%
while True:

    # GET THE IMGAE FROM TELLO
    frame_read = me.get_frame_read()
    myFrame = frame_read.frame
    img = cv.resize(myFrame, (utils.dim_img['width'], utils.dim_img['height']))

    # TO GO UP IN THE BEGINNING
    if startCounter == 0:
        me.takeoff()
        time.sleep(8)
        me.rotate_clockwise(90)
        time.sleep(3)
        me.move_left(35)
        time.sleep(3)
        me.land()
        startCounter = 1

    # # SEND VELOCITY VALUES TO TELLO
    # if me.send_rc_control:
    #     me.send_rc_control(me.left_right_velocity, me.for_back_velocity, me.up_down_velocity, me.yaw_velocity)

    # DISPLAY IMAGE
    cv.imshow("MyResult", img)

    # WAIT FOR THE 'Q' BUTTON TO STOP
    if cv.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break
