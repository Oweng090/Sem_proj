"""
Create a roll logic function to shorten code for gui dice roller
"""

def rollLogic(side, rollZone, dot1, dot2, dot3, dot4, dot5, dot6):
    if(side == 1):
        rollZone.coords(dot1, 68.75, 64.75, 93.75, 89.75) # middle
        rollZone.coords(dot2, 0, 0, 0, 0) # moving every dot back to 0s so when you roll multiple times it can still show one.
        rollZone.coords(dot3, 0, 0, 0, 0)
        rollZone.coords(dot4, 0, 0, 0, 0)
        rollZone.coords(dot5, 0, 0, 0, 0)
        rollZone.coords(dot6, 0, 0, 0, 0)
    elif(side == 2): # make some bug prevention ( move things to their original spot or to 0,0,0,0) (for when it goes froma high number to a low number.)
        # the side will be 2
        # Need to move dot and dot to show a classic 2 on the dice face
        rollZone.coords(dot1, 25.75, 110.25, 50.75, 135.25) # for proportions have x1 and x2 25 apart and the same for y1 and 2
        rollZone.coords(dot2, 113.75, 24.25, 138.75, 49.25)
        rollZone.coords(dot3, 0, 0, 0, 0)
        rollZone.coords(dot4, 0, 0, 0, 0)
        rollZone.coords(dot5, 0, 0, 0, 0)
        rollZone.coords(dot6, 0, 0, 0, 0)
    elif(side == 3):
        # the side will be 3
        rollZone.coords(dot1, 68.75, 64.75, 93.75, 89.75)
        rollZone.coords(dot2, 25.75, 110.25, 50.75, 135.25)
        rollZone.coords(dot3, 113.75, 24.25, 138.75, 49.25)
        rollZone.coords(dot4, 0, 0, 0, 0)
        rollZone.coords(dot5, 0, 0, 0, 0)
        rollZone.coords(dot6, 0, 0, 0, 0)
    elif(side == 4):
        #the side will be 4
        rollZone.coords(dot1, 25.75, 110.25, 50.75, 135.25) # bottom left
        rollZone.coords(dot2, 113.75, 24.25, 138.75, 49.25) # top right
        rollZone.coords(dot3, 113.75, 110.25, 138.75, 135.25) # bottom right
        rollZone.coords(dot4, 25.75, 24.25, 50.75, 49.25) # top left
        rollZone.coords(dot5, 0, 0, 0, 0)
        rollZone.coords(dot6, 0, 0, 0, 0)
    elif(side == 5):
        # the side will be 5
        rollZone.coords(dot1, 25.75, 110.25, 50.75, 135.25) # bottom left
        rollZone.coords(dot2, 113.75, 24.25, 138.75, 49.25) # top right
        rollZone.coords(dot3, 113.75, 110.25, 138.75, 135.25) # bottom right
        rollZone.coords(dot4, 25.75, 24.25, 50.75, 49.25) # top left
        rollZone.coords(dot5, 68.75, 64.75, 93.75, 89.75) # middle
        rollZone.coords(dot6, 0, 0, 0, 0)
    else:
        # the side will be 6
        rollZone.coords(dot1, 25.75, 110.25, 50.75, 135.25) # bottom left
        rollZone.coords(dot2, 113.75, 24.25, 138.75, 49.25) # top right
        rollZone.coords(dot3, 113.75, 110.25, 138.75, 135.25) # bottom right
        rollZone.coords(dot4, 25.75, 24.25, 50.75, 49.25) # top left
        rollZone.coords(dot5, 25.75, 64.75, 50.75, 89.75) # middle left
        rollZone.coords(dot6, 113.75, 64.75, 138.75, 89.75) # middle right
"""def rollLogicRight(side, rollZone, dot):
    if(side == 1):
        rollZone.coords(dot, 220, 64.75, 245, 89.75) # middle
        rollZone.coords(dot, 0, 0, 0, 0)
        rollZone.coords(dot, 0, 0, 0, 0)
        rollZone.coords(dot, 0, 0, 0, 0)
        rollZone.coords(dot, 0, 0, 0, 0)
        rollZone.coords(dot, 0, 0, 0, 0)
    elif(side == 2):
        rollZone.coords(dot, 177, 110.25, 202, 135.25) # bottom left
        rollZone.coords(dot, 265, 24.25, 290, 49.25) # top right
        rollZone.coords(dot, 0, 0, 0, 0)
        rollZone.coords(dot, 0, 0, 0, 0)
        rollZone.coords(dot, 0, 0, 0, 0)
        rollZone.coords(dot, 0, 0, 0, 0)
    elif(side == 3):
        rollZone.coords(dot, 177, 110.25, 202, 135.25)# bottom left
        rollZone.coords(dot, 265, 24.25, 290, 49.25) # top right
        rollZone.coords(dot, 220, 64.75, 245, 89.75) # middle
        rollZone.coords(dot, 0, 0, 0, 0)
        rollZone.coords(dot, 0, 0, 0, 0)
        rollZone.coords(dot, 0, 0, 0, 0)
    elif(side == 4):
        rollZone.coords(dot, 177, 110.25, 202, 135.25) # bottom left
        rollZone.coords(dot, 265, 24.25, 290, 49.25) # top right
        rollZone.coords(dot, 265, 110.25, 290, 135.25) # bottom right
        rollZone.coords(dot, 177, 24.25, 202, 49.25) # top left
        rollZone.coords(dot, 0, 0, 0, 0)
        rollZone.coords(dot, 0, 0, 0, 0)
    elif(side == 5):
        rollZone.coords(dot, 177, 110.25, 202, 135.25) # bottom left
        rollZone.coords(dot, 265, 24.25, 290, 49.25) # top right
        rollZone.coords(dot, 265, 110.25, 290, 135.25) # bottom right
        rollZone.coords(dot, 177, 24.25, 202, 49.25) # top left
        rollZone.coords(dot, 220, 64.75, 245, 89.75) # middle 
        rollZone.coords(dot, 0, 0, 0, 0)
    else:
        rollZone.coords(dot, 177, 110.25, 202, 135.25) # bottom left
        rollZone.coords(dot, 265, 24.25, 290, 49.25) # top right
        rollZone.coords(dot, 265, 110.25, 290, 135.25) # bottom right
        rollZone.coords(dot, 177, 24.25, 202, 49.25) # top left
        rollZone.coords(dot, 177, 64.75, 202, 89.75) # middle left
        rollZone.coords(dot, 265, 64.75, 290, 89.75) # middle right"""