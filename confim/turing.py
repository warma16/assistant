import requests
import json
import urllib.parse
def answer(word):
    w=urllib.parse.quote(word)
    data={"key":"5636c0854e88430383a861151bf764ca","info":word,"userid": "123456"}
    resp = requests.post("http://www.tuling123.com/openapi/api", data=data)  #应该随便取值，图灵承接上下文用的
    if resp.json()['code'] != 40004:
        return str(resp.json()['text'])
    else:
        data={'key':'free','appid':'0','msg':str(w)}
        resp = requests.get("http://api.qingyunke.com/api.php", params=data)
        return str(json.loads(str(resp.text))['content'])