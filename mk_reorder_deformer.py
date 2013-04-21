<<<<<<< HEAD
import maya.cmds as cmds
import maya.mel as mel
=======
__author: 'mark korenic'
import maya.cmds as cmds
>>>>>>> 645cefdd077a7caa2d25a6eaa4dcfaaac88c9e7a

class mk_Reorder_Deformers():
    def __init__(self):
        """ Create a dictionary to store UI elements """
<<<<<<< HEAD
        self.UIElements = {}

<<<<<<< HEAD
        """ Check to see if the UI exists """
        self.windowName = "reorderDeformers"
        if cmds.window(self.windowName, exists=True):
            cmds.deleteUI(self.windowName)
            
        """ Define UI elements width and height """
        self.windowWidth = 380
        self.windowHeight = 300
        self.buttonWidth = 110
        self.buttonHeight = 20
        
        self.UIElements["reorderDeformers"] = cmds.window(self.windowName, width=self.windowWidth, height=self.windowHeight,
            title="mk_reorder", sizeable=True, mxb=False, mnb=False)
=======
=======
    self.UIElements = {}

>>>>>>> 645cefdd077a7caa2d25a6eaa4dcfaaac88c9e7a
    """ Check to see if the UI exists """
    self.windowName = "mk_reorderDeformers"
    if cmds.dockControl(self.windowName, exists=True):
        cmds.deleteUI(self.windowName)

    """ Define UI elements width and height """
    self.windowWidth = 380
    self.windowHeight = 300
    buttonWidth = 110
    buttonHeight = 20
    """ The root layout """
    self.UIElements["rowColumnLayout"] = cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 120), (2, 240)], cs=[2, 10], bgc=[0.2, 0.2, 0.2])

""" Use a flow layout for the  UI """
self.UIElements["guiFlowLayout"] = cmds.flowLayout(v=True, bgc=[.4, .4, .4], width=120, height=self.windowHeight)
cmds.setParent(self.UIElements["rowColumnLayout"])
self.UIElements['influenceList'] = cmds.textScrollList( numberOfRows=8, w=210, h=200, bgc=[.4, .4, .4], allowMultiSelection=True, p=self.UIElements['guiFlowLayout'])
<<<<<<< HEAD
>>>>>>> 645cefdd077a7caa2d25a6eaa4dcfaaac88c9e7a

        
        """ The root layout """
        self.UIElements["rowColumnLayout"] = cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 120), (2, 240)], cs=[2, 10], bgc=[0.2, 0.2, 0.2])
    
        """ Use a flow layout for the  UI """
        self.UIElements["guiFlowLayout"] = cmds.flowLayout(v=True, width=self.windowWidth, height=self.windowHeight)
        cmds.setParent(self.UIElements["rowColumnLayout"])
        self.UIElements['influenceList'] = cmds.textScrollList( numberOfRows=8, w=210, h=200, bgc=[.4, .4, .4], allowMultiSelection=True, p=self.UIElements['rowColumnLayout'])
        self.UIElements['reorderBtn'] = cmds.button(label='reorder', width=380, height=30, enable=True,
        annotation='', p=self.UIElements['rowColumnLayout'])
        #show window
        cmds.showWindow(self.windowName)
=======

>>>>>>> 645cefdd077a7caa2d25a6eaa4dcfaaac88c9e7a

def getSelectedMesh(self, selection, *args):
    # Identify the selection
    selMesh = cmds.ls(sl=True, et='transform')
<<<<<<< HEAD
    if selMesh == []:
=======
    if sel == []:
>>>>>>> 645cefdd077a7caa2d25a6eaa4dcfaaac88c9e7a
        return

def listDeformers(self, selection, *args):
    selection = self.getSelectedMesh()
    deformer = []
    listHistory = cmds.listHistory(selection)
    if listHistory == False:
        cmds.error('No history in selection')
    else:
        for node in listHistory:
<<<<<<< HEAD
            nodeTypes = cmds.nodeType(node, inherited = True)
            deformer.append(node)

def popInfluenceList(self, *args):
<<<<<<< HEAD
<<<<<<< HEAD
    
=======
    #list inputs based on base mesh selection
>>>>>>> 645cefdd077a7caa2d25a6eaa4dcfaaac88c9e7a
=======
    #list inputs based on base mesh selection
>>>>>>> 645cefdd077a7caa2d25a6eaa4dcfaaac88c9e7a
    selection = self.getSelectedMesh()
    deformerList = self.listDeformers(selection)
    if selection == None:
        return(cmds.headsUpMessage("Select Geometry"))
   
        cmds.textScrollList(self.UIElements['influenceList'], edit=True, append=deformerList)
=======
            nodeTypes = cmds.nodeType(node, inherited = true)
        deformers.append(node)

def popInfluenceList(self, *args):
    #list inputs based on base mesh selection
    selection = self.getSelectedMesh()
    deformerList = self.listDeformers(selection)
    if selection == None:
        return(mc.headsUpMessage("Select Geometry"))

    cmds.textScrollList(self.UIElements['influenceList'], edit=True, append=deformerlist)
>>>>>>> 645cefdd077a7caa2d25a6eaa4dcfaaac88c9e7a
def getSelectionSkinClusters(self, selection, *args):
    #identify skinCluster
    mel.eval ('$mesh = "%s";' % (selection[0]))
    skin = mel.eval('findRelatedSkinCluster($mesh);')
    if skin == False:
        cmds.headsUpMessage('skinCluster Not Found')
    return skin
#comment
def deformerReorder(self, *args):
<<<<<<< HEAD
    cmds.reorderDeformers()
    
mk_Reorder_Deformers()
=======
    #cmds.reorderDeformers()
    pass


>>>>>>> 645cefdd077a7caa2d25a6eaa4dcfaaac88c9e7a
