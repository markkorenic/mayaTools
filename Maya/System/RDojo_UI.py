"""
author: Mark Korenic   www.skeletech.net
file: RDojo_UI.py
"""
import pymel.core as pm


class Rdojo_UI:
 """UI for creating rig parts"""

 def __init__(self):
  print "In Rdojo_UI"
  
  #Create a dictionary to store UI elements
  self.UIElements = {}
  
  #Check to see if the UI exists
  #more pymelly
  winName = self.windowName = "RD_UI"
  if pm.objExists(winName):
      winName.deleteUI()
  
  self.windowWidth = 110
  self.windowHeight = 100
  self.buttonWidth = 70
  self.buttonHeight = 33
  #create window
  windowObject= self.UIElements["window"] = pm.window(winName, width=self.windowWidth, height=self.windowHeight, title="RDUI", sizeable=True)
  #Use a flow layout for the  UI
  self.UIElements["guiFlowLayout"] = pm.flowLayout(v=True, width=self.windowWidth, height=self.windowHeight, bgc=[0.4, 0.4, 0.4])

  self.UIElements["hingeButton"] = pm.button( label='Hinge_Lyt', width=self.buttonWidth, h=self.buttonHeight, c = self.createLegLyt,p = self.UIElements["guiFlowLayout"])
  self.chkBx=self.UIElements["fkikChkBx"] = pm.checkBox(label = 'FKIK', value = True,annotation = 'sets FKIK mode', p =self.UIElements["guiFlowLayout"],cc = self.fk_ik)
  self.UIElements["RigLegButton"] = pm.button( label='RigLeg', width=self.buttonWidth,h=self.buttonHeight,c = self.rig_leg,p = self.UIElements["guiFlowLayout"])
  #Show the window
  windowObject.show()
  
 def createLegLyt(self, *args):
  """creates joint layout"""
  import Maya.Modules.Layout.mk_Leg_Lyt as Leg_Lyt
  reload(Leg_Lyt)
  Leg_Lyt.Leg_Lyt()
         
 def rig_leg(self, *args):
  """places joints in layout positions"""
  import Maya.Modules.Animation.mk_Rig_Leg as leg
  reload(leg)
  leg.Rig_Leg()

 def fk_ik(self, *args):
     
     if self.chkBx.getValue():
         print 'in FKIK'
     else:
         print 'FKIK off'
        

Rdojo_UI()
