import pymel.core as pm

#make  global list of locator names and positions
locatorInfo = (['locator_1', [2,9,4]], ['locator_2', [2, 6 ,6]], ['locator_3', [2, 3 ,4]])

def createLegGuides():

    """creates locator guides for leg"""

    locators = [] #create empty list

    #create leg guides, set initial positions

    for i in range(len(locatorInfo)):

        print locatorInfo[i] #print list contents

        loc = pm.spaceLocator(n = locatorInfo[i][0]) # create locators, rename

        loc.setPosition(locatorInfo[i][1]) # set positions with locatorInfo positions[1]

        if i != 0: # Use a condition to make sure this is not the root locator_1

            loc.setParent(locatorInfo[i][0], locatorInfo[i-1][0]) #parent locators

        #append locators to list

        locators.append(loc)

    print locators

createLegGuides()
