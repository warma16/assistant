import requests
import re
class search:
    def __init__(self,word):
        push={'wd':str(word),'pn':'10'}
        headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        r = requests.get("https://www.baidu.com/s", params=push,headers=headers)
        data=r.text
        self.data=data
def get_tittle(data):
    pat2='"title":"(.*?)",'
    rst2=re.compile(pat2).findall(data)
    return rst2
def get_url(data):
    pat2='"url":"(.*?)"}'
    url2=re.compile(pat2).findall(data)
    return url2
def make_dict(la,lb,m):
    out={}
    for i in la:
        if m > 0:
            temp={i:lb[la.index(i)]}
        elif m <0:
            temp={lb[la.index(i)]:i}
        out.update(temp)
    return out
        