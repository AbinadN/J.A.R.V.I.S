# Wasif Uddin Inspo
# pyautogui sluggish hence we use mouse function
# solve the jittering problem by giving a predetermined use-zone

# IMPORTS
import cv2
from cvzone.HandTrackingModule import HandDetector
import mouse
import numpy as np
import time
import threading

detector = HandDetector(detectionCon=0.9, maxHands=1)
cap = cv2.VideoCapture(0)
cam_w, cam_h = 640, 480
cap.set(3, cam_w)
cap.set(4, cam_h)

# frame reduction variable change accordingly
frameR = 100
l_delay = 0
r_delay = 0
double_delay = 0

# change based on screen connections
fp_wy = 3455
fp_hx = 863
# Laptop + Monitor (3455,863)
# Laptop (1371,914)

def l_clk_delay():
    global l_delay
    global l_clk_thread
    time.sleep(1)
    l_delay = 0
    l_clk_thread = threading.Thread(target=l_clk_delay)

def r_clk_delay():
    global r_delay
    global r_clk_thread
    time.sleep(1)
    r_delay = 0
    r_clk_thread = threading.Thread(target=r_clk_delay)

def double_clk_delay():
    global double_delay
    global double_clk_thread
    time.sleep(2)
    double_delay = 0
    double_clk_thread = threading.Thread(target=double_clk_delay)

l_clk_thread = threading.Thread(target=l_clk_delay)
r_clk_thread = threading.Thread(target=r_clk_delay)
double_clk_thread = threading.Thread(target=double_clk_delay)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    cv2.rectangle(img, (frameR,frameR), (cam_w-frameR, cam_h-frameR), (255,0,255), 2)

# extracts hand landmarks
    if hands:
        lmlist = hands[0]['lmList']
        ind_x, ind_y = lmlist[8][0], lmlist[8][1]
        mid_x, mid_y = lmlist[12][0], lmlist[12][1]

        cv2.circle(img, (ind_x,ind_y), 5, (0,255,255), 2)
        fingers = detector.fingersUp(hands[0])
        # print(fingers)

# Mouse Movement (Index Finger Up)
        if fingers[1] == 1 and fingers[2] == 0 and fingers[0] == 1:
            # interchangeable based on different screen connections
            conv_x = int(np.interp(ind_x, (frameR, cam_w - frameR), (0, fp_wy)))
            conv_y = int(np.interp(ind_y, (frameR, cam_h - frameR), (0, fp_hx)))
            mouse.move(conv_x, conv_y)

# Left Click Mouse (Index and Middle Finger Up then Together)
        if fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 1:
            if abs(ind_x-mid_x) < 25:
                if fingers[4] == 0 and l_delay == 0:
                    mouse.click(button="left")
                    l_delay = 1
                    l_clk_thread.start()
# Right Click Mouse (Index, Middle, Thumb Up then Index and Middle Together)
        if fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 0:
            if abs(ind_x - mid_x) < 25:
                if r_delay == 0:
                    mouse.click(button="right")
                    r_delay = 1
                    r_clk_thread.start()

# Scroll Down (Index, Middle, Ring Up then Index and Middle Together)
        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[0] == 1:
            if abs(ind_x-mid_x) < 25:
                mouse.wheel(delta=-1)
# Scroll Up (Index, Middle, Ring, Pinky Up then Index and Middle Together)
        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1 and fingers[0] == 1:
            if abs(ind_x-mid_x) < 25:
                mouse.wheel(delta=1)

# Double Click Mouse (Index, Middle, Ring, Pinky, and Thumb Up then Index and Middle Together)
        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1 and fingers[0] == 0:
            if abs(ind_x - mid_x) < 25:
                if double_delay == 0:
                    mouse.double_click(button="left")
                    double_delay = 1
                    double_clk_thread.start()


    cv2.imshow('Camera Feed', img)
    cv2.waitKey(1)

