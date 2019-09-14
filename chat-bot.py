
from threading import Thread
import datetime
from confim.send import *
nlp_token=get_ac('4cbT6K6fvhDkcfVayvnXdB8K','hGCUvZbGKakCGpTYDyv9PGWNrSvyR7ic')
import time
import os
import platform
from playsound import playsound
sc=platform.system()
pathy=os.getcwd()
pl=pathy.split('/')
del pl[0]
del pl[-2:]

def healtht(x):
    while 1:
        if datetime.datetime.now().hour == 12:
            make_voice('该吃饭了，同志。',show=True) 
        if datetime.datetime.now().hour == 9+12:
            make_voice('该睡觉了，同志。',show=True)
        if datetime.datetime.now().hour == 9+12+8-24:
            make_voice('该起床了，同志。',show=True)
            playsound(os.getcwd()+'/ring/ring.mp3') 
def healthr(x):   
        for i in range(0,25):
            time.sleep(60)
        make_voice('该休息了，同志。舒活舒活筋骨，抖擞抖擞精神。',show=True)
        playsound(os.getcwd()+'/ring/rest.mp3')
        for i in range(0,5):
            time.sleep(60)
        make_voice('该工作了，同志。',show=True)
        playsound(os.getcwd()+'/ring/ring.mp3')
        make_voice('敲击一下回车键就我可以正常工作。',show=True)
make_voice('主人您好，我是您的助理小程。输入文字可以跟我聊天呦。',show=True)
p1=Thread(target=healthr,args=('h',))
p1.setDaemon(True) 
p2=Thread(target=healtht,args=('h',))
p2.setDaemon(True)
p2.start()
p1.start()
while 1:
    ij=input(': ')
    if ij == '再见' or ij == '退出' :
        make_voice('再见。',show=True)
        exit(0)
    elif '升级' in ij or 'update' in ij:
        os.system('python3 ./confim/update.py')
        make_voice('小程已经更新完毕，请输入命令重新启动。',show=True)
        exit(0)
    else:
        emotion_u(ij,nlp_token)