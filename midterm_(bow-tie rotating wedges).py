
from __future__ import division

from psychopy import core, event, visual, gui #these are the psychopy modules

clock = core.Clock()
myWin = visual.Window(color='grey', units='pix', fullscr= True) #creates a fullscreen window
instruction = visual.TextStim(myWin, text = "press any key to continue", height = 40)

# display instructions and wait until press any key
while not event.getKeys():
    instruction.draw()
    myWin.flip()

#countdown from 10 
clock.reset()
j = 10
while clock.getTime() < 10:
    instruction.text = j-int(clock.getTime())
    instruction.draw()
    myWin.flip()
    
    if len(event.getKeys())>0:
        break

#create a bow-tie stimulus & fixation (Make two wedges (in opposite contrast) and alternate them for flashing)

Wedge1 = visual.RadialStim(myWin, pos = (0,0), size = (720,720), visibleWedge = [0,45],
    color = 1, angularCycles=12, radialCycles=5, tex='sqrXsqr', interpolate=False,autoLog=False)
Wedge2 = visual.RadialStim(myWin, pos = (0,0), size = (720,720), visibleWedge = [0,45], 
    color = -1, angularCycles=12, radialCycles=5, tex='sqrXsqr', interpolate=False,autoLog=False)
Wedge3 = visual.RadialStim(myWin, pos = (0,0), size = (720,720), visibleWedge = [180,225],
    color = 1, angularCycles=12, radialCycles=5, tex='sqrXsqr',interpolate=False,autoLog=False)
Wedge4 = visual.RadialStim(myWin, pos = (0,0), size = (720,720), visibleWedge = [180,225],
    color = -1, angularCycles=12, radialCycles=5, tex='sqrXsqr',interpolate=False,autoLog=False)
fixation = visual.Rect(myWin, pos = (0,0), size = (10,10), fillColor='white')

t = 0
rotationRate = 0.0625  # revs per sec
flashPeriod = 0.8  # seconds for one Black-White cycle (ie 1/Hz)

#let the bow-tie rotate & flash
clock.reset()
while clock.getTime() < 256: #total rotation time = 256 sec
    t = clock.getTime()
    if t % flashPeriod < flashPeriod / 2.0:  # t = 0->255
        stim = Wedge1
        stim2 = Wedge3
    else:
        stim = Wedge2
        stim2 = Wedge4
    stim.ori = t * rotationRate * 360.0  # set new rotation
    stim2.ori = t * rotationRate * 360.0  # set new rotation
    stim.draw()
    stim2.draw()
    fixation.draw()
    myWin.flip()
    
    if len(event.getKeys())>0:
        break

win.close()
core.quit()
