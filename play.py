import pygame
import sys
import time
from pydub import AudioSegment
pygame.mixer.init()
if len(sys.argv) == 2:
    s=AudioSegment.from_file(sys.argv[1])
    se=int(s.duration_seconds)+1
    temp=sys.argv[1].split('.')
    temp[1]='mp3'
    temp='.'.join(temp)
    s.export(temp)
    print('load')
    pygame.mixer.music.load(temp)
    print('play')
    pygame.mixer.music.play()
    time.sleep(int(se))