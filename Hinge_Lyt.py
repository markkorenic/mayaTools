import pymel.core as pm


CLASS_NAME = 'Hinge_Lyt'
TITLE = 'Hinge_LYT'
DESCRIPTION = 'Builds a hinge layout'

locatorInfo = (['locator_1', [2,9,4]], ['locator_2', [2, 6 ,6]], ['locator_3', [2, 3 ,4]])


class Hinge_Lyt:
    def __init__(self):
        print "In Hinge Lyt"
        self.Hinge_Lyt()

    def hinge_lyt(self):

        """creates locator guides for leg"""

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

Hinge_Lyt()