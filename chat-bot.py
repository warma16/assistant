
from confim.send import *
nlp_token=get_ac('4cbT6K6fvhDkcfVayvnXdB8K','hGCUvZbGKakCGpTYDyv9PGWNrSvyR7ic')
make_voice('主人您好，我是您的助理小程。输入文字可以跟我聊天呦。',show=True)
while 1:
    ij=input(': ')
    if ij == '再见' or ij == '退出' :
        make_voice('再见。',show=True)
        exit(0)
    else:
        emotion_u(ij,nlp_token)