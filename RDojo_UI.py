import pymel.core as pm
import Maya.Modules.Layout.mk_Hinge_Lyt as Hinge_Lyt
reload(Hinge_Lyt)
#import Maya.Modules.Animation.Rig_Arm as Rig_Arm
#reload(Rig_Arm)

class Rdojo_UI:
 """UI for creating rig parts"""
def __init__(self):
        print "In Rdojo_UI"

        #Create a dictionary to store UI elements
        self.UIElements = {}
        self.windowWidth = 110
        self.windowHeight = 100

        #Check to see if the UI exists
        self.windowName = "RDojoUI"
        if pm.window(self.windowName, exists=True):
            pm.deleteUI(self.windowName)

        win = self.UIElements["window"] = pm.window(self.windowName, width=self.windowWidth, height=self.windowHeight, title="RDojo_UI", sizeable=True)

        #Use a flow layout for the  UI
        self.UIElements["guiFlowLayout"] = pm.flowLayout(v=True, width=self.windowWidth, height=self.windowHeight, bgc=[0.4, 0.4, 0.4])

        self.UIElements["hingeButton"] = pm.button( label='Hinge_Lyt', width=self.windowWidth, c = self.createHingeLyt)
        self.UIElements["RigArmButton"] = pm.button( label='Hinge_Lyt', width=self.windowWidth)

        #Show the window
        pm.showWindow(win)
def createHingeLyt(self, *args):
        """creates joint layout"""
        Hinge_Lyt.Hinge_Lyt()
        Hinge_Lyt.DESCRIPTION()

        pm.button(self.UIElements["lytButton"], en = False)
#def Rig_Arm(self):

Rdojo_UI()

