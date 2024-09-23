import pico2d
import os
from pico2d import *
open_canvas()
os.getcwd()


#file here
grass = load_image('grass.png')
image=load_image('character.png')


grass.draw_now(400,30)
image.draw_now(400,90)
x = 0
y = 90
while (1):
 while (x < 800):
  clear_canvas_now()#game randering
  grass.draw_now(400, 30)
  image.draw_now(x, y)
  x = x + 2#game logic
  delay(0.01)
  
 while (y < 600):
  clear_canvas_now()#game randering
  grass.draw_now(400, 30)
  image.draw_now(x, y)
  y = y + 2#game logic
  delay(0.01)

 while (x > 0):
  clear_canvas_now()#game randering
  grass.draw_now(400, 30)
  image.draw_now(x, y)
  x = x - 2#game logic
  delay(0.01)
  
 while (y > 90):
  clear_canvas_now()#game randering
  grass.draw_now(400, 30)
  image.draw_now(x, y)
  y = y - 2#game logic
  delay(0.01)

close_canvas()
