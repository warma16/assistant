import platform
import os
import time
pathy=os.getcwd()
pl=pathy.split('/')
del pl[0]
del pl[-2:]
sc=platform.system()
def update():
    if sc == 'Linux':
        pl[0]='/'+pl[0]
        path='/'.join(pl)
        os.chdir(path)
        os.system('rm -rf '+path+'/assistant')
        if os.system('git clone https://gitee.com/yueiuieui/assistant.git'):
            print('请输入密码，这是必备的安装包，请一路选y')
            print("Hello,Admin.Please enter your accont password.This package must be installed.So,Please entered y when you have entered correct accont password.")
            os.system('sudo apt-get install git')
        for i in range(11):
            time.sleep(0.1)
            print('['+i*'|'+']'+str(i*10)+'%',end="\r")
        os.chdir(path+'/assistant')
        os.system('python3 chat-bot.py')
    
    
    
    