
import random
import utime
import amoled
import fonts.large as font

BOARD = "WS_180_AMOLED" #LG_191_AMOLED or LG_241_AMOLED or WS_180_AMOLED or WS_241_AMOLED

if BOARD == "LG_191_AMOLED" :
    from config.LG_191_AMOLED import *
elif BOARD == "LG_241_AMOLED" :
    from config.LG_241_AMOLED import *
elif BOARD == "WS_180_AMOLED" :
    from config.WS_180_AMOLED import *
elif BOARD == "WS_241_AMOLED" :
    from config.WS_241_AMOLED import *

POLYGON = [(50,-25),(25,-25),(25,-50),(-25,-50),(-25,-25),(-50,-25),(-50,25),(-25,25),(-25,50),(25,50),(25,25),(50,25),(50,-25)]

#font = display.ttf_load_font("/fonts/test.ttf")

def main():
    display.reset()
    display.init()
    display.rotation(3)
    display.brightness(0)
    display.jpg("/bmp/smiley_small.jpg",80,0)
    for i in range(255):
        display.brightness(i)
        utime.sleep(0.02)
    utime.sleep(1)
    display.fill(amoled.BLACK)
    utime.sleep(1)
    
    text = "Hello!"
    text_length = display.write_len(font,text)
    text_height = font.HEIGHT

    while True:

        for rotation in range(4):
            display.rotation(rotation)
            display.fill(amoled.BLACK)
            col_max = display.width()
            row_max = display.height()
            text_xmax = col_max - text_length
            text_ymax = row_max - text_height
            
            filled = random.randint(0,1)
            kind = random.randint(0,5)
            
            start_time = utime.ticks_ms()

            for _ in range(128):
                xpos = random.randint(0, col_max)
                ypos = random.randint(0, row_max)
                length = random.randint(0, col_max - xpos) // 2
                height = random.randint(0, row_max - ypos) // 2
                radius = random.randint(0, min(col_max - xpos, xpos, row_max - ypos, ypos )) // 2
                angle = random.randint(0,628) / 100
                color = display.colorRGB(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8))
                color2 = display.colorRGB(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8))
                
                if kind == 0 :
                    if filled :
                        display.fill_circle(xpos,ypos,radius, color)
                    else :
                        display.circle(xpos, ypos, radius, color)
                
                if kind == 1 :
                    if filled :
                        display.fill_rect(xpos,ypos,length, height, color)
                    else :
                        display.rect(xpos,ypos,length, height, color)
                
                if kind == 2 :
                    if filled :
                        display.fill_bubble_rect(xpos,ypos,length, height, color)
                    else :
                        display.bubble_rect(xpos,ypos,length, height, color)
                        
                if kind == 3 :
                    if filled :
                        display.fill_trian(random.randint(0, col_max), random.randint(0, row_max),
                                       random.randint(0, col_max), random.randint(0, row_max),
                                       random.randint(0, col_max), random.randint(0, row_max), color)
                    else :
                        display.trian(random.randint(0, col_max), random.randint(0, row_max),
                                       random.randint(0, col_max), random.randint(0, row_max),
                                       random.randint(0, col_max), random.randint(0, row_max), color)
                        
                if kind == 4 :
                    if filled :
                        display.write(font,text, random.randint(10, text_xmax-10), random.randint(10, text_ymax-10), color,color2)
                    else :
                        display.write(font,text, random.randint(10, text_xmax-10), random.randint(10, text_ymax-10), color)
                        
                if kind == 5 :
                    if filled :
                        display.fill_polygon(POLYGON, random.randint(55, col_max-55), random.randint(55, row_max-55) , color, angle)
                    else :
                        display.polygon(POLYGON, random.randint(55, col_max-55), random.randint(55, row_max-55) , color, angle)
            
            end_time = utime.ticks_ms()
            fps = 1000*128/(end_time - start_time)
            fps_txt = "Rot {:.0f} - {:.0f}/s".format(rotation,fps)
            display.write(font,fps_txt, 0, 0, color)
            print(rotation, kind, filled, fps) 
            
            utime.sleep(2)
       
main()

