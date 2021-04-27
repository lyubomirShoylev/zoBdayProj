# Zo Birthday Proj
# 
# A card for the birthday since I will be missing ;(

# graphics handling tkinter
from tkinter import ttk
from tkinter import *
# some time handling in the program
import time
# used for the random movement of sprites
import random
# to play sound alongside the animation
import threading as thr
# play the happyBday song (WINDOWS ONLY)
from playSong import playSong

# colour constants used in the confetti
COLOURS = ["#bf00ff", "#8000ff", "#4000ff", "#0000ff", "#0040ff",
           "#0080ff", "#00bfff", "#00ffff", "#00ffbf", "#00ff80",
           "#00ff40", "#00ff00", "#40ff00", "#80ff00", "#bfff00",
           "#ffff00", "#ffbf00", "#ff8000", "#ff4000", "#ff0000"]

# focus the song to another thread from the graphics to have it playing
# while animation takes place
thr.Thread(target=playSong).start()

class Application(Frame):
    """GUI application for the birthday!!!"""

    def __init__(self, master):
        """Initialize the frame."""
        super(Application, self).__init__(master)
        self.grid(sticky=N+E+W+S)
        self.top = Toplevel(master=master, bg="#9900cc")
        self.top.title("Get ready!")
        self.top.geometry("250x100+250+400")
        Button(self.top,
               text="Here we go",
               command=self.toplevelManager
               ).grid(row=0, column=0, padx=85, pady=35, sticky=N+E+W+S)
        self.top.lift(aboveThis=master)
        # self.top.focus()
    
    def createWidget(self):
        """Create widgets."""
        # the main storyboard with sound and animations
        self.canvas = Canvas(self, width=500, height=700, bg="#f2ccff")
        self.canvas.grid(row=0, column=0, columnspan=3, sticky=N+E+W+S)
        
        # cake image
        self.cakeImg = PhotoImage(name="cakeImg", file="cake.png")
        self.canvas.create_image(250, 440, image=self.cakeImg, tags="cakeImg")

        # flame image
        self.flameImg = PhotoImage(name="flameImg", file="trueFlame.png")
        self.canvas.create_image(245, 230, image=self.flameImg, tags="flameImg")
        
        # wishing text
        bottomText = "Happy Birthday Zorry!!"
        self.canvas.create_text(250, 650,
                                text=bottomText,
                                font=("Harrington", "28", "bold italic"))
        # change to Helvetica if problems encountered

        # create baloons
        self.baloonLeft = PhotoImage(name="baloonleft", file="blueTop.png")
        self.canvas.create_image(90, 370, image=self.baloonLeft, tags="baloonLeft")
        self.baloonRight = PhotoImage(name="baloonRight", file="redTop.png")
        self.canvas.create_image(410, 370, image=self.baloonRight, tags="baloonRight")
        # end of images

        # "beginning" of song
        self.SONGITME = 20
        self.timeStart = time.time()

        # spectral confetti
        # list, holding confetti in check
        self.ovalList = []
        # creating confetti for the duration of the Happy Birthday song
        while time.time() - self.timeStart < self.SONGITME:
            self.moveSprites()
            for i in range(0, 20, 1):
                oval = self.canvas.create_oval(5 + i * 25,
                                               5,
                                               20 + i * 25,
                                               20,
                                               fill=COLOURS[i],
                                               outline="")
                self.ovalList.insert(0, oval)
        
        # cleaning up leftover confetti
        while time.time() - self.timeStart < self.SONGITME + 5:
            self.moveSprites()
        
        # button to make a wish and "blow" the candle
        Button(self,
               text="Make a wish..\nWait for it",
               command=self.mkWish
               ).grid(row=1, column=1, sticky=N+E+W+S)
        
        # float baloons continuously
        self.move = True
        while self.move == True:
            self.moveSprites()
    # thr.Thread(target=createWidget, name="Thread-2").start()
    
    def moveSprites(self):
        """Move confetti downwards and "float" baloons."""
        # remove confetti below a certain y point 
        trash = self.canvas.find_overlapping(0, 150, 500, 170)
        for item in trash:
            self.canvas.delete(item)
        
        # move confetti on screen
        for oval in self.ovalList:
            a = random.randint(-2, 2)
            b = random.randint(20, 25)
            self.canvas.move(oval, a, b)
        
        # float baloons
        a1 = random.randint(-2, 2)
        b1 = random.randint(-2, 2)
        a2 = random.randint(-2, 2)
        b2 = random.randint(-2, 2)
        self.canvas.move("baloonLeft", a1, b1)
        self.canvas.move("baloonRight", a2, b2)
        # get the cake onself.top (so the baloons are in the background)
        self.canvas.tag_raise("cakeImg")

        # apply changes to the canvas
        self.canvas.after(100)
        self.canvas.update()
        # time.sleep(0.1) - not needed m8888888
    
    def toplevelManager(self):
        self.top.destroy()
        self.createWidget()
        playSong()
    
    def mkWish(self):
        """Make a wish and "blow" the candle."""
        self.canvas.after(1000)
        self.canvas.bell()
        self.canvas.delete("flameImg")
        # self.
        # can have a two or several step puttin out the candle


# main
root = Tk()
root.title("Happy Birthday!!")
root.geometry("500x750")

app = Application(root)
root.mainloop()