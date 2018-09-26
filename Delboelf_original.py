import math, numpy, random #handy system and math functions
from psychopy import core, event, visual, gui #these are the psychopy modules

myWin = visual.Window(color='white', units='pix', size=[1000,1000], allowGUI=False, fullscr=False) #creates a window
myClock = core.Clock() #this creates and starts a clock which we can later read

diskLeft = visual.Circle(myWin, radius=40, pos=[-200,0], lineWidth=2.5, fillColor='red', lineColor=None)
diskRight = visual.Circle(myWin, radius=40, pos=[200,0], lineWidth=2.5, fillColor='red', lineColor=None)
ringLeft = visual.Circle(myWin, radius=48, pos=[-200,0], lineWidth=2.5, fillColor=None, lineColor='black')
ringRight = visual.Circle(myWin, radius=140, pos=[200,0], lineWidth=2.5, fillColor=None, lineColor='black')

myScale = visual.RatingScale(myWin, pos=[0, -290], low=20, high=60,  textSize=0.5, lineColor='black',  tickHeight=False, scale=None, showAccept=False, singleClick=True)
information=visual.TextStim(myWin, pos=[0,-315], text='', height=18, color='black') 

# the main loop
def mainLoop(): 
    
    finished = False
    standardRadius = 40.
    diskLeft.setRadius(standardRadius)
    diskRight.setRadius(standardRadius)
    
    while not finished:
    
        diskLeft.draw()
        diskRight.draw()

        ringLeft.draw()
        ringRight.draw()
    
        myScale.draw()
        information.draw()
        myWin.flip()
        
        if myScale.noResponse ==False: #some new value has been selected with the mouse
            size = myScale.getRating()
            percentage = (size-standardRadius) / standardRadius * 100
            information.setText(str(percentage) + "%")
            diskRight.setRadius(size)
            myScale.reset()
    
        pressedList =event.getKeys(keyList=['escape']) #pressing ESC quits the program
        if len(pressedList) >0:
            if pressedList[0] =='escape':
                finished =True
            event.clearEvents()

mainLoop() #enters the main loop
myWin.close() #closes the window
core.quit() #quits
