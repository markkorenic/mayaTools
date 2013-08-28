"""author: Mark Korenic   www.skeletech.net
file: mk_Leg_Lyt.py
"""
import pymel.core as pm

CLASS_NAME = 'Leg_Lyt'
TITLE = 'Leg_LYT'
DESCRIPTION = 'Builds a leg layout'

class Leg_Lyt:

    def __init__(self):
        print "In Hinge Lyt"
        self.leg_lyt()
        
    def leg_lyt(self,*args):

        """creates locator guides for leg"""
        locatorInfo = (['root_locator', [2,9,4]], ['knee_locator', [2, 6 ,6]], ['ankle_locator', [2, 3 ,4]])
        locators = []
        #create leg guides, set initial positions
        for i in range(len(locatorInfo)):
                print locatorInfo[i]
        
                loc = pm.spaceLocator(n = locatorInfo[i][0])
                loc.setPosition(locatorInfo[i][1])
        
        if i != 0: # Use a condition to make sure this is not the root
                loc.setParent(locatorInfo[i][0], locatorInfo[i-1][0]) #parent locator_3 to locator_1
        
        #append locators to list
        locators.append(loc)
        
        print locators

Leg_Lyt()
