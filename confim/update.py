import platform
import os
import time
import requests
pathy=os.getcwd()
sc=platform.system()
def update():
    if sc == 'Linux':
        pl=pathy.split('/')
        del pl[0]
        del pl[-2:]
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
    elif sc == 'Windows':
        try:
            pyl=pathy.split('\\')
        except:
            pyl=pathy.split('\\')
        del pyl[-2:]
        path='/'.join(pyl)
        os.chdir(path)
        os.system('rd /s/q assistant')
        if os.system('git clone https://gitee.com/yueiuieui/assistant.git'):
            print('请输入密码，这是必备的安装包，请一路选下一个。')
            print("Hello,Admin.Please enter your accont password.This package must be installed.So,Please clicked next button when you have entered correct accont password.")
            r=requests.get('https://github.com/git-for-windows/git/releases/download/v2.23.0.windows.1/Git-2.23.0-64-bit.exe')
            with open('setup.exe','wb') as f:
                f.write(r.content)
            print('正在启动安装程序。')
            os.system(path+'/setup.exe')
            print('一路next 6 下')
            print('然后点中间那个按钮')
            print('然后再一次一路next')
            if os.system(path+'/setup.exe'):
                r=requests.get('https://github.com/git-for-windows/git/releases/download/v2.23.0.windows.1/Git-2.23.0-32-bit.exe')
                with open('setup.exe','wb') as f:
                    f.write(r.content)
                os.system(path+'/setup.exe')
                print('一路next 6 下')
                print('然后点中间那个按钮')
                print('然后再一次一路next')
        for i in range(11):
            time.sleep(0.1)
            print('['+i*'|'+']'+str(i*10)+'%',end="\r")
        os.chdir(path+'/assistant')
        if os.system('python3 chat-bot.py'):
            os.system('python chat-bot.py')
    elif sc == 'Darwin':
        pl=pathy.split('/')
        del pl[0]
        del pl[-2:]
        pl[0]='/'+pl[0]
        path='/'.join(pl)
        os.chdir(path)
        os.system('rm -rf '+path+'/assistant')
        if os.system('git clone https://gitee.com/yueiuieui/assistant.git'):
            print('请输入密码，这是必备的安装包，请一路选y')
            print("Hello,Admin.Please enter your accont password.This package must be installed.So,Please entered y when you have entered correct accont password.")
            if os.system('brew install git'):
                print('您的MacBook缺少brew，请一路选y')
                os.system("/usr/bin/ruby -e "+"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)")
        for i in range(11):
            time.sleep(0.1)
            print('['+i*'|'+']'+str(i*10)+'%',end="\r")
        os.chdir(path+'/assistant')
        os.system('python3 chat-bot.py')        
    