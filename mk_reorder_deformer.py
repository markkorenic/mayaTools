"""
author: mark korenic
file: mk_reorder_deformer.py
created: April 21,2013
"""
import maya.cmds as cmds

class mk_ReorderDeformers():
    def __init__(self):
        self.deformers = []
        #Create a dictionary to store UI elements
        self.UIElements = {}
        
        #Check to see if the UI exists
        self.windowName = "reorderDeformers"
        if cmds.window(self.windowName, exists=True):
            cmds.deleteUI(self.windowName)
            
        #Define UI elements width and height
        self.windowWidth = 380
        self.windowHeight = 300
        self.buttonWidth = 110
        self.buttonHeight = 20
        
        #create a window
        self.UIElements["reorderDeformers"] = cmds.window(self.windowName, width=self.windowWidth, height=self.windowHeight,
            title="mk_reorder", sizeable=True, mxb=False, mnb=False)

        #create root layout
        self.UIElements["rowColumnLayout"] = cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 120), (2, 240)], cs=[2, 10], bgc=[0.2, 0.2, 0.2])
    
        #flow layout for the  UI
        self.UIElements["guiFlowLayout"] = cmds.flowLayout(v=True, width=self.windowWidth, height=self.windowHeight)
        cmds.setParent(self.UIElements["rowColumnLayout"])
        
        #influence list
        self.UIElements['scrollList'] = cmds.textScrollList( numberOfRows=8, w=210, h=200, bgc=[.4, .4, .4], allowMultiSelection=True, append = self.deformers, ra =True, dgc = self.dragItem, dpc = self.dropItem, p=self.UIElements['rowColumnLayout'])
        
        #create buttons
        self.UIElements['reorderBtn'] = cmds.button(label='list inputs', width=380, height=30, enable=True,
        annotation='',p=self.UIElements['rowColumnLayout'], command = self.popDeformerList)
        
        #show window
        cmds.showWindow(self.windowName)

    def popDeformerList(self, selection, *args):
        selection = self.getSelectedMesh()
       
        if selection == False:
            print(mc.headsUpMessage("Select Geometry"))     
         
         # Get the list of verts   
        deformerList = self.listDeformers(selection)
        print deformerList
        
        
    def getSelectedMesh(self, *args):
        # Identify the selection
        selMesh = cmds.ls(sl=True, et='transform')
        if selMesh == []:
            return
    
    def listDeformers(self, *args):
        self.getSelectedMesh()
        self.deformers = []
        listHistory = cmds.listHistory()
        for node in listHistory:
            nodeTypes = cmds.nodeType(node, inherited = True)
            if 'geometryFilter' in nodeTypes:       
                self.deformers.append(node)
        #scroll list needed here to populate list
        cmds.textScrollList(self.UIElements['scrollList'], edit=True,removeAll = True, append=self.deformers)
    
    def deformerReorder(self, *args):
        cmds.reorderDeformers()
    
    
    def dropItem(self, dragControl, dropControl, messages, x, y, dragType = 1, *args):
         #self.deformers()list object is not callable
         print dragControl
         print dropControl
         print messages
         print x, ",", y
         print dragType
         
    def dragItem(self, dragControl, x, y, modifiers, *args):
        #self.deformers()
        print dragControl
        print x, ",", y
        print modifiers
        
mk_ReorderDeformers()

