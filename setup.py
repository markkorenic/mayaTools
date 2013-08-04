import pymel.core as pm 

currentUnit = pm.currentUnit(time = 'ntsc')


def createMenu():
    """ creates drop down tool menu"""
#query all maya window names
    mi = pm.window('MayaWindow',ma = True, q = True)
    #print all window names at at startup
    for win in mi:
        print win
#if window equals 'DojoTools, delete it'
        if win == 'DojoTools':
            win.deleteUI('DojoTools', m = True)
            print 'deleted RT'
#Then, recreate unique menu
    dojoMenu = pm.menu('DojoTools', label = 'DojoTools', tearOff = True, p = 'MayaWindow')
    pm.menuItem(p = dojoMenu, label = 'RD_UI')
createMenu()





