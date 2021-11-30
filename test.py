from djitellopy import Tello
import cv2

 
tello = Tello()

tello.connect()

tello.streamon()

while True : 
    cap = tello.get_frame_read().frame
    cv2.imshow('tello',cap)





    z = cv2.waitKey(1)
    if z == 27 :
        break

    
cv2.destroyAllWindows()
