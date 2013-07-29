"""
<<<<<<< HEAD
author: mark korenic skeletech.net
=======
author: mark korenic    skeletech.net
>>>>>>> origin/master
file: mk_reorder_deformer.py
created: April 21,2013

SYNOPSIS: Reorder deformer inputs when 'All Inputs' fail to load.
"""

import maya.cmds as cmds
from functools import partial

class mk_ReorderDeformers():
<<<<<<< HEAD
'''read SYNOPSIS'''
=======
    '''read Synopsis'''
>>>>>>> origin/master
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
<<<<<<< HEAD
            title ="mk_ReorderDeformer", sizeable=False, mxb=False, mnb=False)
=======
            title="mk_ReorderDeformer", sizeable=False, mxb=False, mnb=False)
>>>>>>> origin/master

        #create root layout
        self.mainLayout = cmds.columnLayout(rs = 5, bgc=[0.2, 0.2, 0.2])
    
        #influence list
        self.scrollDeformerList = cmds.textScrollList( numberOfRows=8, w=350, h=140, bgc=[.4, .4, .4], ra =True,append=self.deformers, p=self.mainLayout)
        
        #create buttons
        self.inputBtn = cmds.button(label='List Deformer Inputs', width=350, height=30, enable=True,
        annotation='',p=self.mainLayout, command = self.popDeformerList)
        ### I adjusted the command arguments see imports at the top(functools) ###
        self.moveUpBtn = cmds.button(label='Move Up', width=350, height=30, enable=True,\
                                     annotation='',p=self.mainLayout, command = partial(self.moveItem,"up"))
        self.moveDwnBtn = cmds.button(label='Move Down', width=350, height=30, enable=True,\
                                      annotation='',p=self.mainLayout,command = partial(self.moveItem,"down"))
        
        #show window
        cmds.showWindow(self.windowName)

    def popDeformerList(self, selection, *args):
<<<<<<< HEAD
        """populate inputs to scroll list from selected mesh"""
        selection = self.getSelectedMesh()
        if selection == False:
            cmds.headsUpMessage("Select Geometry")
         # Get the list of verts
=======
        """populate inputs to scroll list from selected mesh"""        
        selection = self.getSelectedMesh()       
        if selection == False:
            cmds.headsUpMessage("Select Geometry")
         # Get the list of verts   
>>>>>>> origin/master
        deformerList = self.listDeformers(selection)
        print self.listDeformers()
        
    def getSelectedMesh(self, *args):
        # Identify the selection
        selMesh = cmds.ls(sl=True, et='transform')
        if selMesh:
<<<<<<< HEAD
            return selMesh[0]
    
    def listDeformers(self, *args):
        """get deformer inputs from selected mesh"""
        #Make sure a mesh is selected
        mesh = self.getSelectedMesh()
        if mesh:
            self.deformers = []
            #pass name to listHistory()
            history = cmds.listHistory(mesh)
            for node in history:
                nodeTypes = cmds.nodeType(node, inherited = True)
                if 'geometryFilter' in nodeTypes:
=======
            return selMesh[0]        
    
    def listDeformers(self, *args):
        """get deformer inputs from selected mesh"""
        ### Make sure a mesh is selected
        mesh = self.getSelectedMesh()
        if mesh:
            self.deformers = []
            ### pass name to listHistory()
            history = cmds.listHistory(mesh)
            for node in history:
                nodeTypes = cmds.nodeType(node, inherited = True)
                if 'geometryFilter' in nodeTypes:       
>>>>>>> origin/master
                    self.deformers.append(node)
            #scroll list needed here to populate list
            cmds.textScrollList(self.scrollDeformerList, edit=True,removeAll = True, append =self.deformers)
        else:
            cmds.headsUpMessage("Please select an object.")
   
    def moveItem(self,move="up", *args):
        """moves deformer up in list"""
<<<<<<< HEAD
        #Get mesh name
        mesh = self.getSelectedMesh()
        cmds.select(mesh,r=True)
        #Get shape node
        cmds.pickWalk(direction="down")
        meshShape = cmds.ls(sl=True)[0]
        #Reselect transform node
        cmds.select(mesh,r=True)
        current_state = cmds.textScrollList(self.scrollDeformerList, query=True,ai = True)
        selected_item = cmds.textScrollList(self.scrollDeformerList, query=True,si= True)[0]
        indexNum = current_state.index(selected_item)
        # Move item UP
        if move == 'up':
            #Dont move item if it is at the top of the list
            if indexNum > 0:
                # Get item ABOVE selected
                previousItem = current_state[indexNum-1]
                cmds.reorderDeformers(selected_item,previousItem,meshShape)
                #Update scroll list
                self.listDeformers()
                #Re-select item
                cmds.textScrollList(self.scrollDeformerList,edit=True,si= selected_item)
        # Move item DOWN
        else:
            # Get item BELOW selected
            lastIndexNum = (len(current_state)-1)
            #Dont move item if it is at the bottom of the list
            if indexNum < lastIndexNum:
                nextItem = current_state[indexNum+1]
                cmds.reorderDeformers(nextItem,selected_item,meshShape)
                #Update scroll list
                self.listDeformers()
                #Re-select item
                cmds.textScrollList(self.scrollDeformerList,edit=True,si= selected_item)

mk_ReorderDeformers()
=======
        ### Get mesh name
        mesh = self.getSelectedMesh()
        cmds.select(mesh,r=True)
        ### Get shape node
        cmds.pickWalk(direction="down")
        meshShape = cmds.ls(sl=True)[0]
        ### Reselect transform node
        cmds.select(mesh,r=True)        
        current_state = cmds.textScrollList(self.scrollDeformerList, query=True,ai = True)
        selected_item = cmds.textScrollList(self.scrollDeformerList, query=True,si= True)[0]             
        indexNum = current_state.index(selected_item)
        # Move item UP
        if move == 'up':
            ### Dont move item if it is at the top of the list
            if indexNum > 0:
                # Get item ABOVE selected 
                previousItem = current_state[indexNum-1]            
                cmds.reorderDeformers(selected_item,previousItem,meshShape)
                ### Update scroll list
                self.listDeformers()
                ### Re-select item
                cmds.textScrollList(self.scrollDeformerList,edit=True,si= selected_item)
        # Move item DOWN
        else:
            # Get item BELOW selected 
            lastIndexNum = (len(current_state)-1)
            ### Dont move item if it is at the bottom of the list
            if indexNum < lastIndexNum:
                nextItem = current_state[indexNum+1]            
                cmds.reorderDeformers(nextItem,selected_item,meshShape)
                ### Update scroll list
                self.listDeformers()
                ### Re-select item
                cmds.textScrollList(self.scrollDeformerList,edit=True,si= selected_item) 
>>>>>>> origin/master

mk_ReorderDeformers()
