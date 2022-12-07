import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst

Gst.init(None)

from  playsound import playsound
class Player(object):
    '''
    播放器实现类
    '''

    def __init__(self):
        self.player = Gst.ElementFactory.make("playbin", "player")

        self.bus = self.player.get_bus()
        self.bus.add_signal_watch()
        self.bus.enable_sync_message_emission()
        # self.bus.connect('sync-message::eos', self.on_eos)

    def play(self, uri):
        '''
        播放
        :param uri:播放资源地址
        :return:
        '''
        self.player.set_state(Gst.State.NULL)
        self.player.set_property('uri', uri)
        self.player.set_state(Gst.State.PLAYING)

    def stop(self):
        '''
        停止
        :return:
        '''
        self.player.set_state(Gst.State.NULL)

    def pause(self):
        '''
        暂停
        :return:
        '''
        self.player.set_state(Gst.State.PAUSED)

    def resume(self):
        '''
        回复播放
        :return:
        '''
        self.player.set_state(Gst.State.PLAYING)

    def add_callback(self, name, callback):
        '''
        播放状态回调
        :param name: {eos, ...}
        :param callback: 回调函数
        :return:
        '''
        if not callable(callback):
            return

        def on_message(bus, message):
            callback()

        self.bus.connect('sync-message::{}'.format(name), on_message)

    @property
    def duration(self):
        '''
        播放时长
        :return:
        '''
        success, duration = self.player.query_duration(Gst.Format.TIME)
        if success:
            return int(duration / Gst.MSECOND)

    @property
    def position(self):
        '''
        播放位置
        :return:
        '''
        success, position = self.player.query_position(Gst.Format.TIME)
        if not success:
            position = 0

        return int(position / Gst.MSECOND)

    @property
    def state(self):
        '''
        播放状态
        :return:
        '''
        # GST_STATE_VOID_PENDING        no pending state.
        # GST_STATE_NULL                the NULL state or initial state of an element.
        # GST_STATE_READY               the element is ready to go to PAUSED.
        # GST_STATE_PAUSED              the element is PAUSED, it is ready to accept and process data.
        #                               Sink elements however only accept one buffer and then block.
        # GST_STATE_PLAYING             the element is PLAYING, the GstClock is running and the data is flowing.
        _, state, _ = self.player.get_state(Gst.SECOND)
        return 'FINISHED' if state != Gst.State.PLAYING else 'PLAYING'
class playl(Player):
    def __init__(self,mode):
        if mode==0:
            self.mode='playsound'
            self.err='no auth'
        elif mode == 1:
            self=Player()
        else:
            self.mode='unknown error' 
    def out_warning(label):
        if label == 'unknown error':
            raise ValueError('Unknown Value') 
        elif label == 'no auth':
            raise ValueError('the player is not avilable.')
    def play(self,name):
        try:
            if self.mode == 'playsound':
                playsound(name)
            else:
                out_warning(self.mode)
        except:
            self.play(name)
    def control(self,command=None):
        try:
            if self.mode == 'playsound':
                out_warning(self.err)
        except:
            exec('return '+str(self)+'.'+command+'()')
