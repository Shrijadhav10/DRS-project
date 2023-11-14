
from concurrent.futures import thread
from email.mime import image
import tkinter
from turtle import width
import cv2 #pip install opencv-python
import PIL.Image, PIL.ImageTk #pip install pillow
from functools import partial
import threading
import imutils
import time


#width and height on main screen
SET_WIDTH=650
SET_HEIGHT=470
stream=cv2.VideoCapture("dhoni runout.mp4")
def play(speed):
    global flag
    print(f"you clicked on play {speed}")
    
        #play in reverse mode
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 +speed)

    grabbed,frame=stream.read()
    if not grabbed:
            exit()
    frame=imutils.resize(frame ,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    if flag:
        canvas.create_text(120,25,fill="green",font="times 20 italic bold",text="Decision pending")
        #play in reverse mode
    flag= not flag

def pending(decision):
    #1.Display decision pending image
    frame=cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)
    #2.wait for 1 sec
    time.sleep(2)
    #3.display sponser
    frame=cv2.cvtColor(cv2.imread("sponser.png"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)
    #4.wait for 1.5 sec
    time.sleep(3)
    #5.display out/notout
    if decision=='out':
        decision_img="out.png"
        frame=cv2.cvtColor(cv2.imread(decision_img),cv2.COLOR_BGR2RGB)
        frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
        frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image=frame
        canvas.create_image(0,0,image=frame, anchor=tkinter.NW)
    else :
        decision_img="notout.png"
        frame=cv2.cvtColor(cv2.imread(decision_img),cv2.COLOR_BGR2RGB)
        frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
        frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image=frame
        canvas.create_image(0,0,image=frame, anchor=tkinter.NW) 
def out():
    thread=threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()
    print("player is out")
def not_out():
    thread=threading.Thread(target=pending,args=("Notout",))
    thread.daemon=1
    thread.start()
    print("player is Notout") 

cv_img=cv2.cvtColor(cv2.imread("drs.png"),cv2.COLOR_BGR2RGB)
#tkinter starts here 
window=tkinter.Tk()
window.title=("DRS REVIEW SYSYEM")
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()

#buttons to control playback
btn=tkinter.Button(window ,text="<< Previous (fast) ",width=50,command=partial(play,-5))
btn.pack()
btn=tkinter.Button(window ,text="< previous (slow) ",width=50,command=partial(play,-2))
btn.pack()
btn=tkinter.Button(window ,text="  Next (slow) > ",width=50,command=partial(play,2))
btn.pack()
btn=tkinter.Button(window ,text="  Next (fast) >> ",width=50,command=partial(play,5))
btn.pack()

btn=tkinter.Button(window ,text="  Give Out >> ",width=50,command=out)
btn.pack()
btn=tkinter.Button(window ,text="  Give Notout >> ",width=50,command=not_out)
btn.pack()
window.mainloop()