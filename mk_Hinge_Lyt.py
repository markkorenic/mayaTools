import pymel.core as pm

def createLegGuides():
    """creates locator guides for leg"""
    locators = []
    #create leg guides, set initial positions
    hipLoc = pm.spaceLocator(n = 'locator_1')
    hipLoc.setPosition([2,9,4])
   
    kneeLoc = pm.spaceLocator(n = 'locator_2')
    kneeLoc.setPosition([2, 6 ,6])
    
    ankleLoc = pm.spaceLocator(n = 'locator_3')
    ankleLoc.setPosition([2, 3 ,4])
    #parent leg guides
    ankleLoc.setParent(kneeLoc, hipLoc)
    for each in hipLoc, kneeLoc, ankleLoc:
        print each
    #append locators to group
    locators.append([hipLoc, kneeLoc,ankleLoc])
    print locators
    
createLegGuides()
