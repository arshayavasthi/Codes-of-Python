import pygame as pg
def play_music(music_file,volume=0.8):
    freq=44100
    bitsize=-16
    channels=2
    buffer=2048
    pg.mixer.init(freq,bitsize,channels,buffer)
    pg.mixer.music.set_vol(volume)
    clock=pg.time.clock()
    try:
        pg.mixer.music.load(music_file)
        print("music file{} loaded".format(music_file))
    except pg.error:
        print("file{} not found!({})".format(music_file,pg.get_error()))
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        clock.tick(30)
music_file="spyder.mp3"
volume=0.8
play_music(music_file,volume)
