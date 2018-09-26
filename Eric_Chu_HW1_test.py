import math, numpy, random #handy system and math functions
from psychopy import core, event, visual, gui #these are the psychopy modules

myWin = visual.Window(color='white', units='pix', size=[1500,1500], allowGUI=False, fullscr=False) #creates a window
myClock = core.Clock() #this creates and starts a clock which we can later read

diskLeft = visual.Circle(myWin, radius=40, pos=[-350,0], lineWidth=2.5, fillColor='red', lineColor=None)
diskRight = visual.Circle(myWin, radius=40, pos=[350,0], lineWidth=2.5, fillColor='red', lineColor=None)
diskcentral = visual.Circle(myWin, radius=40, pos=[0,0], lineWidth=2.5, fillColor='red', lineColor=None) #add a new disk
ringLeft = visual.Circle(myWin, radius=90, pos=[-350,0], lineWidth=2.5, fillColor=None, lineColor='black')
ringRight = visual.Circle(myWin, radius=145, pos=[350,0], lineWidth=2.5, fillColor=None, lineColor='black')
ringcentral = visual.Circle(myWin, radius=45, pos=[0,0], lineWidth=2.5, fillColor=None, lineColor='black')#add a new ring

myScale = visual.RatingScale(myWin, pos=[0, -290], low=20, high=60,  textSize=0.6, lineColor='black',  tickHeight=False, scale=None, showAccept=False, singleClick=True) #change scale position
myScale2 = visual.RatingScale(myWin, pos=[0, 290], low=20, high=60,  textSize=0.6, lineColor='black',  tickHeight=False, scale=None, showAccept=False, singleClick=True) #add a new scale
information=visual.TextStim(myWin, pos=[0,-315], text='', height=18, color='black') #change information position
information2=visual.TextStim(myWin, pos=[0,315], text='', height=18, color='black') #information for new scale 

# the main loop
def mainLoop(): 
    
    finished = False
    hideOnlydiskLeft = False
    hideOnlydiskRight = False
    standardRadius = 40.
    diskLeft.setRadius(standardRadius)
    diskRight.setRadius(standardRadius)
    diskcentral.setRadius(standardRadius)
    
    while not finished: 
    
        diskcentral.draw()

        ringcentral.draw()

        myScale.draw()
        myScale2.draw()
        information.draw()
        information2.draw()
        myWin.flip()
        
        if myScale.noResponse ==False: #some new value has been selected with the mouse
            size = myScale.getRating()
            percentage = (size-standardRadius) / standardRadius * 100
            information.setText(str(percentage) + "%")
            diskRight.setRadius(size)
            myScale.reset()
            
        if myScale2.noResponse ==False: #some new value has been selected with the mouse
            size = myScale2.getRating()
            percentage = (size-standardRadius) / standardRadius * 100
            information2.setText(str(percentage) + "%")
            diskLeft.setRadius(size)
            myScale2.reset()
            
        if hideOnlydiskLeft ==False:
            diskLeft.draw()
            ringLeft.draw()
            
        if hideOnlydiskRight ==False:
            diskRight.draw()
            ringRight.draw()

        pressedList =event.getKeys(keyList=['escape','a','s']) #pressing ESC quits the program
        if len(pressedList) >0:
            if pressedList[0] =='escape':
                finished =True
            elif pressedList[0] =='a': #image on the left side will disappear while press 'a' 
                hideOnlydiskLeft = not hideOnlydiskLeft
            elif pressedList[0] =='s': #image on the right side will disappear while press 's' 
                hideOnlydiskRight = not hideOnlydiskRight
            event.clearEvents()

mainLoop() #enters the main loop
myWin.close() #closes the window
core.quit() #quits