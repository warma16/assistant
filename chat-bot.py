
from threading import Thread

from confim.send import *
nlp_token=get_ac('4cbT6K6fvhDkcfVayvnXdB8K','hGCUvZbGKakCGpTYDyv9PGWNrSvyR7ic')
import time
import os
from playsound import playsound
def health(x):
    while 1:
        for i in range(0,25):
            time.sleep(1)
        make_voice('该休息了，同志。',show=True)
        playsound(os.getcwd()+'/ring/rest.mp3')
        for i in range(0,5):
            time.sleep(1)
        make_voice('该工作了，同志。',show=True)
        playsound(os.getcwd()+'/ring/ring.mp3')
        make_voice('敲击一下回车键就我可以正常工作。',show=True)
make_voice('主人您好，我是您的助理小程。输入文字可以跟我聊天呦。',show=True)
p1=Thread(target=health,args=('h',))
p1.start()
while 1:
    ij=input(': ')
    if ij == '再见' or ij == '退出' :
        make_voice('再见。',show=True)
        exit(0)
    else:
        emotion_u(ij,nlp_token)