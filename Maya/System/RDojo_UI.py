"""
author: Mark Korenic   www.skeletech.net
file: RDojo_UI.py
"""
import pymel.core as pm
import Maya.Modules.Layout.mk_Leg_Lyt as Leg_Lyt
reload(Leg_Lyt)

class Rdojo_UI:
 """UI for creating rig parts"""
def __init__(self):
        print "In Rdojo_UI"

        #Create a dictionary to store UI elements
        self.UIElements = {}
        self.windowWidth = 110
        self.windowHeight = 100

        #Check to see if the UI exists
        self.windowName = "RDojo_UI"
        if pm.window(self.windowName, exists=True):
            pm.deleteUI(self.windowName)

        win = self.UIElements["window"] = pm.window(self.windowName, width=self.windowWidth, height=self.windowHeight, title="RDojo_UI", sizeable=True)
        #Use a flow layout for the  UI
        self.UIElements["guiFlowLayout"] = pm.flowLayout(v=True, width=self.windowWidth, height=self.windowHeight, bgc=[0.4, 0.4, 0.4])

        self.UIElements["hingeButton"] = pm.button( label='Hinge_Lyt', width=self.windowWidth, c = self.createLegLyt)
        self.UIElements["RigLegButton"] = pm.button( label='Hinge_Lyt', width=self.windowWidth, c = self.rig_leg)
        #Show the window
        pm.showWindow(self.windowName)
def createLegLyt(self, *args):
        """creates joint layout"""
        Leg_Lyt.leg_lyt()
        Leg_Lyt.DESCRIPTION()
        pm.button(self.UIElements["lytButton"], en = False)

def rig_leg(self, *args):
    """places joints in layout positions"""
    self.createLegLyt()

    for sel in selection: #this loop works, without pm.ls(sl=True)
        locPos = pm.xform(sel, q = True,t = True, ws=True)# query positions of locators
        jnt = pm.joint(position=locPos)# set joints to positions of locators

Rdojo_UI()
