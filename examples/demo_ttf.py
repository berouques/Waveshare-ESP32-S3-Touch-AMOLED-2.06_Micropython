
import random
import utime
import amoled

BOARD = "WS_180_AMOLED" #LG_191_AMOLED or LG_241_AMOLED or WS_180_AMOLED or WS_241_AMOLED

if BOARD == "LG_191_AMOLED" :
    from config.LG_191_AMOLED import *
elif BOARD == "LG_241_AMOLED" :
    from config.LG_241_AMOLED import *
elif BOARD == "WS_180_AMOLED" :
    from config.WS_180_AMOLED import *
elif BOARD == "WS_241_AMOLED" :
    from config.WS_241_AMOLED import *


font = display.ttf_load_font("/fonts/test.ttf")
display.ttf_init_font()

text = "Hello!"

display.reset()
display.init()
display.brightness(255)

display.ttf_scale_font(16)
display.ttf_draw(text,50,50,amoled.RED)

display.ttf_scale_font(32)
display.ttf_draw(text,50,100,amoled.GREEN)

display.ttf_scale_font(64)
display.ttf_draw(text,50,180,amoled.BLUE)

display.ttf_scale_font(128)
display.ttf_draw(text,50,320,amoled.MAGENTA)
