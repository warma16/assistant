
from threading import Thread

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

if sc == 'Linux':
    pl[0]='/'+pl[0]
    path='/'.join(pl)
def health(x):
    while 1:
        for i in range(0,25):
            time.sleep(60)
        make_voice('该休息了，同志。',show=True)
        playsound(os.getcwd()+'/ring/rest.mp3')
        for i in range(0,5):
            time.sleep(60)
        make_voice('该工作了，同志。',show=True)
        playsound(os.getcwd()+'/ring/ring.mp3')
        make_voice('敲击一下回车键就我可以正常工作。',show=True)
make_voice('主人您好，我是您的助理小程。输入文字可以跟我聊天呦。',show=True)
p1=Thread(target=health,args=('h',))
p1.setDaemon(True)  # thread1,它做为程序主线程的守护线程,当主线程退出时,thread1线程也会退出,由thread1启动的其它子线程会同时退出,不管是否执行完任务
p1.start()
while 1:
    ij=input(': ')
    if ij == '再见' or ij == '退出' :
        make_voice('再见。',show=True)
        exit(0)
    elif '升级' in ij or 'update' in ij:
        os.system('python3 ./confim/update.py')
        os.chdir(path+'/assistant')
        make_voice('小程已经更新完毕，请输入命令重新启动。',show=True)
        exit(0)
    else:
        emotion_u(ij,nlp_token)