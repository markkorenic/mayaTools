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
        locators = []
        """creates locator guides for leg"""
        locatorInfo = (['Root', [2,9,4]], ['knee', [2, 6 ,6]], ['ankle', [2, 3 ,4]])
        
        #create leg guides, set initial positions
        for item in range(len(locatorInfo)):
                print locatorInfo[item]
        
                loc = pm.spaceLocator(n = locatorInfo[item][0],relative =True)
                loc.setPosition(locatorInfo[item][1])
        
        if item != 0: # Use a condition to make sure this is not the root
                loc.setParent(locatorInfo[item][0], locatorInfo[item-1][0]) #parent locator_3 to locator_1
        
        #append locators to list
        locators.append(loc)
        
        print locators
