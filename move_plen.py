from djitellopy import Tello

tello = Tello()

tello.connect()

tello.takeoff()
tello.move_up(150)
# tello.move_right(100)
tello.move_forward(500)
tello.move_forward(200)
tello.flip_forward()
tello.flip_right()
tello.flip_right()
tello.flip_right()
tello.flip_right()
tello.flip_right()
tello.move_left(300)
tello.move_back(200)
tello.move_back(500)

tello.land()

pass