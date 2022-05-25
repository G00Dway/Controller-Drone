from djitellopy import tello
import cv2
import os

main = tello.Tello()
main.connect()
main.streamon()
while True:
    img = main.get_frame_read().frame
    cv2.imshow("Image", img)
    cv2.waitKey(1)