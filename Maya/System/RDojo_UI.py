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
  
  #Check to see if the UI exists
  #more pymelly
  winName = self.windowName = "RDojo_UI"
  if pm.objExists(winName):
      winName.deleteUI()
  
  self.windowWidth = 110
  self.windowHeight = 100
  self.buttonWidth = 70
  self.buttonHeight = 33
  
  #create window
  windowObject= self.UIElements["window"] = pm.window(winName, width=self.windowWidth, height=self.windowHeight, title="RDojo_UI", sizeable=True)
  #Use a flow layout for the  UI
  self.UIElements["guiFlowLayout"] = pm.flowLayout(v=True, width=self.windowWidth, height=self.windowHeight, bgc=[0.4, 0.4, 0.4])

  self.UIElements["hingeButton"] = pm.button( label='Hinge_Lyt', width=self.buttonWidth, h=self.buttonHeight, c = self.createLegLyt)
  self.UIElements["RigLegButton"] = pm.button( label='RigLeg', width=self.buttonWidth,h=self.buttonHeight,c = self.rig_leg)
  #Show the window
  windowObject.show()
Rdojo_UI()
        
def createLegLyt(self, *args):
        """creates joint layout"""
        Leg_Lyt.leg_lyt()
        Leg_Lyt.DESCRIPTION()
        pm.button(self.UIElements["lytButton"], en = False)

def rig_leg(self, *args):
    """places joints in layout positions"""
    import mk_rig_leg as leg
    reload(leg)
    Rig_Leg.DESCRIPTION()
    leg.Rig_Leg()
    pm.button(self.UIElements['rigLegBtn'], en = False)
    
Rdojo_UI()
