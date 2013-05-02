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
        self.windowWidth = 350
        self.windowHeight = 350
        self.buttonWidth = 100
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
        self.UIElements['scrollList'] = cmds.textScrollList( numberOfRows=8, w=210, h=140, bgc=[.4, .4, .4], allowMultiSelection=True, ra =True,append=self.deformers, dgc = self.dragItem, dpc = self.dropItem, p=self.UIElements['rowColumnLayout'],sc = self.listDeformers)
        
        #create buttons
        self.UIElements['reorderBtn'] = cmds.button(label='list inputs', width=380, height=30, enable=True,
        annotation='',p=self.UIElements['rowColumnLayout'], command = self.popDeformerList)
        self.UIElements['moveDeformer'] = cmds.button(label='Move', width=50, height=30, enable=True,
        annotation='',p=self.UIElements['guiFlowLayout'], command = self.moveDeformer)
        
        
        #show window
        cmds.showWindow(self.windowName)

    def popDeformerList(self, selection, *args):
        selection = self.getSelectedMesh()
       
        if selection == False:
            cmds.headsUpMessage("Select Geometry")     
         
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
        deformers = []
        listHistory = cmds.listHistory()
        for node in listHistory:
            nodeTypes = cmds.nodeType(node, inherited = True)
            if 'geometryFilter' in nodeTypes:       
                deformers.append(node)
        #scroll list needed here to populate list
        cmds.textScrollList(self.UIElements['scrollList'], edit=True,removeAll = True, append =deformers)
    
    def deformerReorder(self, *args):
        #cmds.reorderDeformers()
        pass
    
    
    def dropItem(self, dragControl, dropControl, messages, x, y, dragType):
         print dragControl
         print dropControl
         print messages
         print x, ",", y
         print dragType
         
         
    def dragItem(self, dragControl, x, y, modifiers):
        
        print dragControl
        print x, ",", y
        print modifiers
        return ['0']
        
            
mk_ReorderDeformers()
