def createLegGuide():
    """creates locator guides for leg joints"""
    
    #create hip locator
    hipLoc = cmds.spaceLocator( p=(3,15,0), n = 'locator_1' )
    #check to see if hip was created, then center its pivot with xform command
    for item in hipLoc:
        cmds.xform( item, cp = True )
        print 'hip guide created'
    if not item:
        print item + 'failed'
    
    #create knee locator
    kneeLoc = cmds.spaceLocator( p=(3, 7, 2), n = 'locator_2' )
    for item in kneeLoc:
        cmds.xform( item, cp = True ) 
        print 'knee guide created'
    if not item:
        print item + 'failed'
    
    #create ankle locator
    ankleLoc= cmds.spaceLocator( p=(3, 1, -1), n = 'locator_3' )
    for item in ankleLoc:
        cmds.xform( item, cp = True )
        print 'ankle guide created'
    if not item:
        print item + 'failed'
createLegGuide()