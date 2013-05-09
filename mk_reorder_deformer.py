"""
author: mark korenic
file: mk_reorder_deformer.py
created: April 21,2013
"""
import maya.cmds as cmds

class mk_ReorderDeformers():
    def __init__(self):
        
        self.deformers = []
        
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
        self.UI = cmds.window(self.windowName, width=self.windowWidth, height=self.windowHeight,
            title="mk_reorder", sizeable=True, mxb=False, mnb=False)

        #create root layout
        self.mainLayout = cmds.columnLayout(rs = 5, bgc=[0.2, 0.2, 0.2])
    
        #influence list
        self.scrollDeformerList = cmds.textScrollList( numberOfRows=8, w=self.windowWidth, h=140, bgc=[.4, .4, .4], ra =True,append=self.deformers, p=self.mainLayout)
        
        #create buttons
        self.inputBtn = cmds.button(label='list inputs', width=380, height=30, enable=True,
        annotation='',p=self.mainLayout, command = self.popDeformerList)
        self.moveUpBtn = cmds.button(label='Move Up', width=380, height=30, enable=True,
        annotation='',p=self.mainLayout, command = self.moveItem)
        self.moveDwnBtn = cmds.button(label='Move Down', width=380, height=30, enable=True,
        annotation='',p=self.mainLayout, command = self.popDeformerList)
        
        #show window
        cmds.showWindow(self.windowName)

    def popDeformerList(self, selection, *args):
        selection = self.getSelectedMesh()
       
        if selection == False:
            cmds.headsUpMessage("Select Geometry")     
         
         # Get the list of verts   
        deformerList = self.listDeformers(selection)
        print self.listDeformers()
        
        
    def getSelectedMesh(self, *args):
        # Identify the selection
        selMesh = cmds.ls(sl=True, et='transform')
        if selMesh == []:
            return selMesh[0]
    
    def listDeformers(self, *args):
        self.getSelectedMesh()
        self.deformers = []
        listHistory = cmds.listHistory()
        for node in listHistory:
            nodeTypes = cmds.nodeType(node, inherited = True)
            if 'geometryFilter' in nodeTypes:       
                self.deformers.append(node)
        #scroll list needed here to populate list
        cmds.textScrollList(self.scrollDeformerList, edit=True,removeAll = True, append =self.deformers)
    
    def deformerReorder(self, *args):
        #cmds.reorderDeformers()
        pass
    
    def moveItem(self, direction = 'up', *args):
        """moves deformer up in list"""
        
        original_list = cmds.textScrollList(self.scrollDeformerList, query=True,ai = True)
        selected_item = cmds.textScrollList(self.scrollDeformerList, query=True, si= True)
        
        indexNum = original_list.index(selected_item[0])
        print selected_item, indexNum
        if direction == 'up':
            previousItem = original_list[indexNum -1]
            print previousItem
            cmds.reorderDeformers(previousItem, selected_item, self.getSelectedMesh)
            print self.deformers
            cmds.textScrollList(self.scrollDeformerList, edit=True,removeAll = True, append =self.deformers)
        
        
        
    
    #def dropItem(self, dragControl, dropControl, messages, x, y, dragType):
         #print dragControl
         #print dropControl
         #print messages
         #print x, ",", y
         #print dragType
         
         
    #def dragItem(self, dragControl, x, y, modifiers):
        
        #print dragControl
        #print x, ",", y
        #print modifiers
        #return ['0']
        
            
mk_ReorderDeformers()
