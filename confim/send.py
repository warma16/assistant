import urllib.request
import urllib.parse
import sys
import ssl
import json
import requests
import math
import time
from playsound import playsound
import confim.mus as mus
import confim.search as baidu
import uuid
import confim.turing as bot2
def get_mac_add():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ','.join([mac[e:e+2] for e in range(0,11,2)])
def get_in(word):
    make_voice(word,show=False)
    return input('请回答出刚才说的内容 : ')
def playit(name):
    playsound(name)
def make_voice(text,show=None):
    ac=get_ac('Bi9Vj1zUtnUI9ivLcpLzkATD','eMlzgXgBjN09caFEbjpf4UqaHGnXwKNn')
    push_text=str(urllib.parse.quote(text))
    push_data={'tex':str(push_text),'lan':'zh','cuid':str(get_mac_add()),'ctp':'1','per':'111','aue':'3','tok':str(ac)}
    r=requests.get('https://tsn.baidu.com/text2audio',params=push_data)
    with open('text.mp3','wb') as f:
        f.write(r.content)

    if show:
        print(text)
    playit('text.mp3')
def get_ac(ak,sk):
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+str(ak)+'&client_secret='+str(sk)
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    data=json.loads(str(content,encoding='utf-8'))
    return data['access_token']
def check_word(text,ac):
    text_a=text.encode("utf-8")
    host='https://aip.baidubce.com/rpc/2.0/nlp/v1/ecnet?charset=UTF-8&access_token='+str(ac)
    headers={'Content-Type': "application/json"}
    dataname=json.dumps({'text':str(text)})
    r=requests.post(host,data=dataname,headers=headers)
    data=json.loads(str(r.text))
    try:
        d=data['error_msg']
        print(d)
    except:
        a=data['item']
        #print(a)
        result=a['correct_query']
        return result
def emotion_check(text,ac):
    host='https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token='+str(ac)
    headers={'Content-Type': "application/json"}
    dataname=json.dumps({'text':str(text)})
    r=requests.post(host,data=dataname,headers=headers)
    data=json.loads(str(r.text))
    try:
        d=data['error_msg']
        print('check-emotion:err:'+d)
    except:
        a=data['items']
        a=a[0]
        if a['sentiment'] == 2:
            result='正面'
            return result
        elif a['sentiment'] == 1:
            result='中性'
            return result
        elif a['sentiment'] == 0:
            result='负面'
            return result
def tct(text1,text2,ac):
    host='https://aip.baidubce.com/rpc/2.0/nlp/v2/simnet?charset=UTF-8&access_token='+str(ac)
    headers={'Content-Type': "application/json"}
    dataname=json.dumps({'text_1':str(text1),'text_2':str(text2)})
    r=requests.post(host,data=dataname,headers=headers)
    data=json.loads(str(r.text))
    try:
        d=data['error_msg']
        print('text-check-text:err:'+d)
    except:
        a=data['score']
        a=round(a)
        return a
def emotion_u(text,ac):
    if '搜索' in text:
        a=get_in('您要搜索什么')
        s=baidu.search(a)
        url=baidu.get_url(s.data)
        title=baidu.get_tittle(s.data)
        d1=baidu.make_dict(title,url,1)
        d2=baidu.make_dict(title,url,-1)  
        make_voice('为您找到搜索结果',show=True)
        for i in title:
            print(d2[d1[i]]) 
            make_voice(d2[d1[i]])
            make_voice('查看网页，请点击下面链接',show=True)
            print(d1[i])
            print('--------------------------')    
    mcl={'下一首':1,'上一首':2,'听':3}
    for i in mcl:
        if i in text:
            if mcl[i] == 1:
                if mus.next_song() != '无法播放':
                    playit('music.m4a')
            elif mcl[i] == 2:
                mus.back_song()
                if mus.back_song() != '无法播放':
                    playit('music.m4a')
            elif mcl[i] == 3:
                mkey=get_in('您想听什么歌曲')
                a=mus.search_song(mkey)  
                if a != '无法播放':
                    make_voice('正在播放',show=True)
                    playit('music.m4a')  
    text_a=text.encode("utf-8")
    host='https://aip.baidubce.com/rpc/2.0/nlp/v1/emotion?charset=UTF-8&access_token='+str(ac)
    headers={'Content-Type': "application/json"}
    dataname=json.dumps({'text':str(text)})
    r=requests.post(host,data=dataname,headers=headers)
    data=json.loads(str(r.text))
    #print(data)
    try:
        d=data['error_msg']
        print(d)
    except:
        a=data['items']
        a=a[0]
        a=a['replies']
        a='.'.join(a)
        if a == '对不起，我会继续努力' or a == '':
            a=bot2.answer(text)
            if a == '对不起，我会继续努力' or a == '':            
                s=baidu.search(text)
                url=baidu.get_url(s.data)
                title=baidu.get_tittle(s.data) 
                make_voice('为您找到搜索结果',show=True)            
                try:
                    make_voice(title[0],show=True)
                    make_voice('请点击下面链接',show=True)
                    print(url[0])
                    print('-------------------------')
                except:
                    make_voice('没有为您找到搜索结果',show=True)            
            else:
                make_voice(str(a),show=True)
        else:
            make_voice(str(a),show=True)

'''print(emotion_u('我真的很不错',get_ac()))
print(emotion_u('眼睛疼',get_ac()))
print(emotion_u('动脉在哪里',get_ac()))
print(emotion_u('不想活了',get_ac()))'''
#emotion_u('你好棒',get_ac())
