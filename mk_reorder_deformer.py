__author: 'mark korenic'
import maya.cmds as cmds

class mk_Reorder_Deformers():
    def __init__(self):
        """ Create a dictionary to store UI elements """
    self.UIElements = {}

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


def getSelectedMesh(self, selection, *args):
    # Identify the selection
    selMesh = cmds.ls(sl=True, et='transform')
    if sel == []:
        return

def listDeformers(self, selection, *args):
    selection = self.getSelectedMesh()
    deformer = []
    listHistory = cmds.listHistory(selection)
    if listHistory == False:
        cmds.error('No history in selection')
    else:
        for node in listHistory:
            nodeTypes = cmds.nodeType(node, inherited = true)
        deformers.append(node)

def popInfluenceList(self, *args):

    selection = self.getSelectedMesh()
    deformerList = self.listDeformers(selection)
    if selection == None:
        return(mc.headsUpMessage("Select Geometry"))

    cmds.textScrollList(self.UIElements['influenceList'], edit=True, append=deformerlist)
def getSelectionSkinClusters(self, selection, *args):
    #identify skinCluster
    mel.eval ('$mesh = "%s";' % (selection[0]))
    skin = mel.eval('findRelatedSkinCluster($mesh);')
    if skin == False:
        cmds.headsUpMessage('skinCluster Not Found')
    return skin

def deformerReorder(self, *args):
    #cmds.reorderDeformers()
    pass


