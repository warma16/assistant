

import cv2 as cv
import os
import easygui
import platform
import sys
time =0
def brightness(imf):   
    im=cv.imread(imf)
    dark=0
    light=0
    for i in im:
        for j in i:
            for k in j:
                if k < 100:
                    dark=dark+1
                else:
                    light=light+1
    if dark > light:
        print(light)
        print(dark)
        return light/dark
s=platform.system()
cam=cv.VideoCapture(0)
ret,frame=cam.read()
if ret != True:
    frame=0
cam.release()
cv.imwrite('check.jpg',frame)
mark=brightness('check.jpg')
print(mark)
if mark != None:
    if mark*100< 35:
        while 1:
            print(mark)
            easygui.msgbox('请开灯，否则会对眼睛造成伤害。')
            if s == 'Linux':
                os.system('xgamma -gamma '+str(10.00*mark))
            elif s == 'Darwin':
                if os.system('brightness '+str(1*mark)) != True:
                    if os.system('brew install brightness'):
                        easygui.msgbox('请您安装homebrew')
            cam=cv.VideoCapture(0)
            ret,frame=cam.read()
            if ret != True:
                frame=0
            cam.release()
            cv.imwrite('check.jpg',frame)
            mark=brightness('check.jpg')
            if mark != None:
                if mark*100 > 35:
                    break
                else:
                    continue
            else:
                break