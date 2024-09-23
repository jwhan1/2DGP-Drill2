
import pico2d
import os
import math

from pico2d import *

open_canvas()


os.getcwd()

#file here
grass = load_image('grass.png')
image = load_image('character.png')


r=270
x=400 + 200 * math.cos(r/360*2*math.pi)
y=290 + 200 * math.sin(r/360*2*math.pi)





while(1):
  clear_canvas_now()#game randering
  grass.draw_now(400, 30)
  image.draw_now(x, y)
  r=(r+2)%360#game logic
  x=400 + 200 * math.cos(r/360*2*math.pi)
  y=290 + 200 * math.sin(r/360*2*math.pi)
  delay(0.01)

close_canvas()
