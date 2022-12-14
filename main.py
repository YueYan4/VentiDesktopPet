from turtle import bgcolor
from keep_alive import keep_alive

import random
import tkinter as tk
import time
from tkinter import *
#assets from https://www.reddit.com/r/Genshin_Impact/comments/oq2w62/i_made_a_venti_shimeji/
x = 400
y = 635
cycle = 0
check = 1
idle_num =[1,2,3,4]
sleep_num = [10,11,12,13,15]
walk_left = [6,7]
walk_right = [8,9]
flying_arr = [16,17, 18]
event_number = random.randrange(1,17,1)
lastClickX = 0
lastClickY = 0

def saveLastClickPos(event):
      global lastClickX, lastClickY
      lastClickX = event.x
      lastClickY = event.y
      
def dragging(event):
      global lastClickX, lastClickY, x, y
      x, y = event.x - lastClickX + window.winfo_x(), event.y - lastClickY + window.winfo_y()
      window.geometry("+%s+%s" % (x , y))

#impath = 'C:\\Users\\fx770\\Desktop\\Project\\Buddy\\image\\'
#transfer random no. to event
def event(cycle,check,event_number):
 global x, y
 if event_number in idle_num:
  check = 0
  #print('idle')
  window.after(400,update,cycle,check,event_number) #no. 1,2,3,4 = idle
 elif event_number == 5:
  check = 1
  #print('from idle to sleep')
  window.after(100,update,cycle,check,event_number) #no. 5 = idle to sleep
 elif event_number in walk_left:
  check = 4
  #print('walking towards left')
  window.after(100,update,cycle,check,event_number)#no. 6,7 = walk towards left
 elif event_number in walk_right:
  check = 5
  #print('walking towards right')
  window.after(100,update,cycle,check,event_number)#no 8,9 = walk towards right
 elif event_number in sleep_num:
  check  = 2
  #print('sleep')
  window.after(100,update,cycle,check,event_number)#no. 10,11,12,13,15 = sleep
 elif event_number == 14:
  check = 3
  #print('from sleep to idle')
  window.after(100,update,cycle,check,event_number)#no. 15 = sleep to idle
 elif event_number in flying_arr:
  check = 6
  window.after(100,update,cycle,check,event_number)
#making gif work 

def gif_work(cycle,frames,event_number,first_num,last_num):
 if cycle < len(frames) -1:
  cycle+=1
 else:
  cycle = 0
  event_number = random.randrange(first_num,last_num+1,1)
 return cycle,event_number

def update(cycle,check,event_number):
 global x, y
 #idle
 if check ==0:
  frame = idle[cycle]
  cycle ,event_number = gif_work(cycle,idle,event_number,1,9)
  
 #idle to sleep
 elif check ==1:
  frame = idle_to_sleep[cycle]
  cycle ,event_number = gif_work(cycle,idle_to_sleep,event_number,10,10)
#sleep
 elif check == 2:
  frame = sleep[cycle]
  cycle ,event_number = gif_work(cycle,sleep,event_number,10,15)
#sleep to idle
 elif check ==3:
  frame = sleep_to_idle[cycle]
  cycle ,event_number = gif_work(cycle,sleep_to_idle,event_number,1,1)
  x += 3
  if x >= 1200:
      x = 20
  window.geometry('+' + str(x)+'+' + str(y))
#walk toward left
 elif check == 4:
  frame = walk_positive[cycle]
  cycle , event_number = gif_work(cycle,walk_positive,event_number,1,9)
  x += 3
  if x >= 1200:
      x = 20
  window.geometry('+' + str(x)+'+' + str(y))
#walk towards right
 elif check == 5:
  frame = walk_negative[cycle]
  cycle , event_number = gif_work(cycle,walk_negative,event_number,1,9)
  x -= 3
  if x <= 20:
      x = 1200
  window.geometry('+' + str(x)+'+' + str(y))
 elif check == 6:
  frame = flying[cycle]
  cycle,event_number = gif_work(cycle, flying, event_number, 1, 9)
  y -= 20
  if y <= 200:
     y = 635
  window.geometry('+' + str(x)+'+' + str(y))
 label.config(image=frame)
 window.after(1,event,cycle,check,event_number)


window = tk.Tk()
window.tk.call('wm', 'overrideredirect', window._w, True)
window.geometry("+{}+{}".format(x, y))
#call buddy's action gif
idle = [tk.PhotoImage(file='idle.gif',format = 'gif -index %i' %(i)) for i in range(3)]#idle gif
idle_to_sleep = [tk.PhotoImage(file='idle_to_sleep.gif',format = 'gif -index %i' %(i)) for i in range(5)]#idle to sleep gif
sleep = [tk.PhotoImage(file='sleep.gif',format = 'gif -index %i' %(i)) for i in range(2)]#sleep gif
sleep_to_idle = [tk.PhotoImage(file='sleep_to_idle.gif',format = 'gif -index %i' %(i)) for i in range(10)]#sleep to idle gif
walk_positive = [tk.PhotoImage(file='walking_positive.gif',format = 'gif -index %i' %(i)) for i in range(3)]#walk to left gif
walk_negative = [tk.PhotoImage(file='walking_negative.gif',format = 'gif -index %i' %(i)) for i in range(3)]#walk to right gif
flying = [tk.PhotoImage(file='flying.gif',format = 'gif -index %i' %(i)) for i in range(1)]#walk to right gif
hang = [tk.PhotoImage(file='hang.gif',format = 'gif -index %i' %(i)) for i in range(6)]#walk to right gif


window.wm_attributes('-topmost', 'true')
window.wm_attributes('-topmost', 'true')
window.wm_attributes('-transparent', True)
window.config(bg='systemTransparent')

window.bind('<Button-1>', saveLastClickPos)
window.bind('<B1-Motion>', dragging)


label = tk.Label(window)
label.pack()

#loop the program
window.after(1,update,cycle,check,event_number)

window.mainloop()
#https://ezgif.com/maker
#venti sometimes walks offscreen