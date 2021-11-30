from djitellopy import Tello
import cv2

 
tello = Tello()

tello.connect()

tello.streamon()

while True : 
    cap = tello.get_frame_read().frame
    cv2.imshow('tello',cap)



    key = cv2.waitKey(1)
    if key == 27 :
        tello.streamoff()
        break


 
    #     elif key == ord('t'):
    #         tello.takeoff()
    #         # time.sleep(1)
    #     elif key == ord('w'):
    #         tello.move_forward(100)
    #         # time.sleep(1)
    #     elif key == ord('u'):
    #         tello.move_up(150)
    #         # time.sleep(1)
    #     elif key == ord('s'):
    #         tello.move_back(100)
    #         # time.sleep(1)
    #     elif key == ord('l') :
    #         tello.land()
    #         # time.sleep(1)
    #     elif key == ord('f'):
    #         tello.flip_forward()
    #         # time.sleep(1)
    #     elif key == ord('d'):
    #         tello.move_right(50)
    #         # time.sleep(1)
    #     elif key == ord('a'):
    #         tello.move_left(50)
    #         # time.sleep(1)




cv2.destroyAllWindows()
