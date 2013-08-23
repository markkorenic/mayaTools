"""
author: Mark Korenic    www.skeletech.net
file: startup.py
Synopsis: Runs at maya load, imports rig Menu
"""
import pymel.core as pm
import Maya.System.RDojo_UI as RDojo_UI
reload(RDojo_UI)

# Changing default preferences
pm.currentUnit( time='ntsc' )

def createMenu():
    """create UI menu to hold layout tools"""

    # Query the names of all "MayaWindows"
    mi = pm.window('MayaWindow', ma=True, q=True)
    for m in mi:
        print m
        # If a name matches 'UserScripts', delete it
        if m == 'DojoTools':
            pm.deleteUI('DojoTools', m=True)
    # Create the menu.
    pm.menu('DojoTools', label='DojoTools', to=True, p="MayaWindow")
    # Create a menu item for the RDojo UI
    pm.menuItem('DojoTools', label='RD_UI', c=createLytItem)


def createLytItem(self,*args):
    """imports layout UI"""
    RDojo_UI.Rdojo_UI()
createMenu()
