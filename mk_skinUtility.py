'''
created by: markkorenic        www.skeletech.net
date: 8/6/2012
'''
import maya.cmds as mc
import maya.mel as mel

class Skin_Utils():

    def __init__(self):
        """ Create a dictionary to store UI elements """
        self.UIElements = {}

        """ Check to see if the UI exists """
        
        if mc.dockControl('dockControl', exists=True):
            mc.deleteUI('dockControl')

        """ Define UI elements width and height """
        self.windowWidth = 360
        self.windowHeight = 400
        buttonWidth = 110
        buttonHeight = 30

        """ Define a window"""
        self.UIElements["mk_skinUtils"] = mc.window('mk_skinUtils', width=self.windowWidth, height=self.windowHeight,\
                                                         title="mk_skinUtility", sizeable=True, mxb=False, mnb=False, menuBar=True)
        """create menubarLayout"""
        #self.UIElements['menuBar'] = mc.menuBarLayout(bgc = [0.3, 0.3, 0.3],p = self.UIElements["mk_skinUtils"])
        """ Make a menu bar """
        self.UIElements['menu'] = mc.menu( label='File', tearOff=False,p =self.UIElements["mk_skinUtils"] )
        mc.menuItem( label='Export Weights', c=self.saveSkin )
        mc.menuItem( label='Import Weights', c=self.loadSkin )
        #self.UIElements['tabLayout'] = mc.tabLayout(edit = True)
        """ The root layout """
        self.UIElements["rowColumnLayout"] = mc.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 120), (2, 240)], cs=[2, 10])

        """ Use a flow layout for the  UI """
        self.UIElements["guiFlowLayout"] = mc.flowLayout(v=True, width=120, height=self.windowHeight)
        mc.setParent(self.UIElements["rowColumnLayout"])

        self.UIElements["guiFlowLayout2"] = mc.flowLayout(v=True, width=240, height=self.windowHeight)
        mc.setParent(self.UIElements["rowColumnLayout"])

        self.UIElements['Separator'] = mc.separator(height=20, style='single', p=self.UIElements['guiFlowLayout'])
        self.UIElements['BindOptionsText'] = mc.text(label='Bind Method:', align='left',p=self.UIElements["guiFlowLayout"])
    
        """ Organise all the bind options here.
            Start with a dropdown Menu """
        self.UIElements['DropDownMenu1'] = mc.optionMenu( ni=4, width=buttonWidth, height=buttonHeight, enable=True,
        p=self.UIElements['guiFlowLayout'])
        self.UIElements['DropDownItem1'] = mc.menuItem(label='Skeleton', p=self.UIElements['DropDownMenu1'])
        self.UIElements['DropDownItem1'] = mc.menuItem(label='Selected Joints', c=self.skeletonBind, p=self.UIElements['DropDownMenu1'])
        self.UIElements['DropDownItem1'] = mc.menuItem(label='Closest Point', c=self.bindToSurface, p=self.UIElements['DropDownMenu1'])
        
        
        #self.UIElements['rmvInfChkBx'] = mc.checkBox(label = 'Remove Unused',annotation = "Adds skinCluster to front of input order", onc = self.skin_foc,p=self.UIElements['guiFlowLayout'])
        self.UIElements['BindBtn'] = mc.button(label='Bind', width=buttonWidth, height=buttonHeight, enable=True,
        annotation='Bind Skin based off selection',  p=self.UIElements['guiFlowLayout'], c=self.skeletonBind)
        self.UIElements['NormChkBx'] = mc.checkBox(label = 'Normalize Weights',annotation = "Normalizes Weights in post", onc = self.weightNormalize,p=self.UIElements['guiFlowLayout'])
        self.UIElements['PruneChkBx'] = mc.checkBox(label = 'Prune Weights', annotation = 'Removes unused points in deformer', onc = self.weightPrune,p=self.UIElements['guiFlowLayout'])        
        """ Edit Bind elements """
        self.UIElements['Separator'] = mc.separator(height=34, style='none', p=self.UIElements['guiFlowLayout'])
        self.UIElements['EditBindText'] = mc.text(label='Edit Bind:' , align='left', p=self.UIElements["guiFlowLayout"])

        """Unbind skin drop down menu"""
        self.UIElements['DropDownMenu2'] = mc.optionMenu(ni=4, width=buttonWidth, height=buttonHeight, enable=True,
            p=self.UIElements['guiFlowLayout'])
        self.UIElements['DropDownItem2'] = mc.menuItem(label='Detach w/ Hist.', p=self.UIElements['DropDownMenu2'])
        self.UIElements['DropDownItem2'] = mc.menuItem(label='Detach w/o Hist.',  p=self.UIElements['DropDownMenu2'])
        
        self.UIElements['EditBindBtn'] = mc.button(label='Edit Skin', aop = True, width=buttonWidth, height=buttonHeight, enable=True,
        annotation='Edit Skin based off of selection', p=self.UIElements['guiFlowLayout'], c=self.editBind)

        self.UIElements['Separator'] = mc.separator(h=20, style='none', p=self.UIElements['guiFlowLayout'])
        
        self.UIElements['EditJntsBtn'] = mc.button(label='Move Joints Off', width=buttonWidth, height=buttonHeight, enable=True,
        annotation='Put the skin in edit joint mode', p=self.UIElements['guiFlowLayout'], c=self.toggleJoints)
        self.UIElements['Separator'] = mc.separator(h=20, style='none', p=self.UIElements['guiFlowLayout'])
        #self.UIElements['paintBtn'] = mc.symbolButton(image = 'paintSkinWeights.png', p = self.UIElements['guiFlowLayout'], c = self.paintSkinButton)
        """ Now we have an empty flow layout to use for something else like a text scroll list of influences """
        self.UIElements['Separator'] = mc.separator(h=20, style='none', p=self.UIElements['guiFlowLayout2'])
        
        """ A text Scroll List.  Now you can make a method to find all the influences associated with the selected skinCluster """
        self.UIElements['influenceList'] = mc.textScrollList( numberOfRows=10, w=230, h=230, allowMultiSelection=True, sc=self.selectJoint, p=self.UIElements['guiFlowLayout2'])
        
        """ We need a way to populate the text scroll list once we have a selection.  Maya handles this in the 
        skinning tools by having a selection callback that runs when one of those windows are open.
        We can do the same, but let's start simple by making a button to load this info.
        """
        self.UIElements['Separator'] = mc.separator(h=10, style='none', p=self.UIElements['guiFlowLayout2'])
        self.UIElements['loadInfBtn'] = mc.button(label='Load influences', width=220, height=30, enable=True,
        annotation='Load Influences', p=self.UIElements['guiFlowLayout2'], c=self.popInfluenceList)
             
        self.UIElements['Separator'] = mc.separator(h=10, style='none', p=self.UIElements['guiFlowLayout2'])
        """ Show the window"""

        #mc.showWindow(self.UIElements["mk_skinUtils"] )
        mc.dockControl('dockControl',label = 'SkinUtils',area = 'right', allowedArea = 'right',h =self.windowHeight, w = self.windowWidth,content = self.UIElements["mk_skinUtils"])
    
    def popInfluenceList(self, *args):
        selection = self.getSelectedMesh()

        if selection == None:
            return(mc.headsUpMessage("Select Geometry"))
        
        # Doing this to verify we have a skin cluster
        sknCluster = self.getSelectionSkinClusters(selection)

        if sknCluster == None:
            return(mc.headsUpMessage('skinCluster Not Found'))
        
        # Get the list of verts   
        #vertList = self.listVertices(selection)
        #print vertList
        jointList = self.listJoints(selection)
        print jointList
        mc.textScrollList(self.UIElements['influenceList'], edit=True, removeAll = True, append=jointList)
        
    def listJoints(self, selection, *args):
        selection = self.getSelectedMesh()
        jointList = mc.skinCluster(selection, q =True, inf = True)
        
        return jointList
        
    #def listVertices(self, selection, *args):
        #get vtx influences
        #listVerts = (mc.ls ([selection[0] + '.vtx[*]'], flatten=True))
        
        #return listVerts        
    
    def selectJoint(self,*args):
        jnts = self.listJoints(selection)
        mc.select(selection, r =True, add =True)
        
        print selection
         
    def saveSkin(self, *args):
        print 'In Save Skin'
        print 'In Save Skin'
        selection = self.getSelectedMesh()

        if selection == None:
            return(mc.headsUpMessage("Select Geometry"))

        sknCluster = self.getSelectionSkinClusters(selection)

        if sknCluster == None:
            return(mc.headsUpMessage('skinCluster Not Found'))

        # Add a file browser

        basicFilter = "*.xml"
        fdir = mc.fileDialog2(fileFilter=basicFilter, dialogStyle=3)

        fileName = fdir[0].rpartition('/')[2]

        filePath = fdir[0].rpartition('/')[0]

        mc.deformerWeights (fileName, ex=True, deformer=sknCluster[0], p=filePath)
        mc.headsUpMessage("Skin Exported")

    def loadSkin(self, selection, *args):
        
        print "In Load Skin"

        #Open Browser
        basicFilter = "*.xml"
        fdir = mc.fileDialog2(fileFilter=basicFilter, cap='Import weights:',
            okCaption='Load', dialogStyle=2)

        fileName = fdir[0].rpartition('/')[2]

        filePath = fdir[0].rpartition('/')[0]
        selection = self.getSelectedMesh()

        print filePath
        sknCluster = self.getSelectionSkinClusters(selection)
        if sknCluster == None:
            return(mc.headsUpMessage('skinCluster Not Found'))

        #import weights
        print sknCluster
        importSkin = mc.deformerWeights (fileName, im=True, deformer=sknCluster[0], m="index", p=filePath)

        mc.headsUpMessage(fileName + ' Imported Successfully')
#------------------------------------------------------------------------------------------------
    def getSelectedMesh(self, *args):
        # Identify the selection 
        sel = mc.ls(sl=True, et='transform')
        if sel == []:
            return
        return sel

    def getSelectedShape(self, selection, *args):
        shp = mc.listRelatives(selection[0], s=True, type="shape")
        print shp
        return shp

    def getSelectionSkinClusters(self, selection, *args):
        print selection
        # I added this to verify a skin cluster exists
        rel = self.getSelectedShape(selection)

        # findRelatedSkinCluster does not have a return value so let's try a new method.
        #skin = mel.eval('findRelatedSkinCluster($mesh);')
        skin = mc.listConnections(rel[0], t="skinCluster")
        print "SKIN"
        print skin

        if skin == None:
            return
        return skin

    def unBindSkin(self, *args):
        print "In Unbind"
        #unbind skin keep history/keep weight values
        self.getSelectedMesh()

        try:
            mc.skinCluster(edit=True, unbindKeepHistory=True)
        except: pass

    def detachSkin(self, *args):
        print "In Detach"
        self.getSelectedMesh()
        try:
            mc.skinCluster(edit=True, unbind=True)
        except: pass

    def moveJoints(self, *args):
        print 'In Edit'
        self.getSelectedMesh()
        try:
            mc.skinCluster(edit =True,moveJointsMode = True)
        except: pass

    def bindToSurface(self, selection, *args):
        #bind each object by closest point on selection
        sel = mc.ls(sl=True)
        if sel == []:
            mc.headsUpMessage("Select desired joints then geometry")
            return sel
        else:
            mc.bindSkin(bcp=True)

    def skeletonBind(self, *args):

        # Find the mesh and joint selection

        selection = self.getSelectedMesh()

        if selection == None:

            return(mc.headsUpMessage("Select Geometry"))

        selJnts = self.getSelectedJoints()

        if selJnts == None:

            return(mc.headsUpMessage("Select Joints"))

        sknCluster = self.getSelectionSkinClusters(selection)

        if sknCluster != None:

            print "Skin Information Exists"

        #bind the skin based off the option selected in bind method. 
        #First we need to query the active item in the drop down menu.

        ddVal = mc.optionMenu(self.UIElements['DropDownMenu1'], q=True, v=True)

        print ddVal

        if ddVal =='Skeleton':

        #Bind to selected joints-->

            try:
                mc.skinCluster(tsb=True, sm=0)

            except:
                return(mc.headsUpMessage("The Skin Was Already Bound"))

        if ddVal == 'Selected Joints':

            #Bind to selected joints

            try:
                mc.skinCluster(tsb=True, sm=0)

            except:
                return(mc.headsUpMessage("The Skin Was Already Bound"))

            mc.headsUpMessage("Skin Bound")

    def weightNormalize(self,selection, *args):
        sel = mc.ls(sl=True, et='transform')
        if sel == []:
            return (mc.headsUpMessage("Please select a deformer"))
        else:
            mc.skinCluster(edit = True, normalizeWeights = 2)
            #Normalize in post = default
            return (mc.headsUpMessage("Weights normalized"))
                   
        
    def weightPrune(self, selection, *args):
        sel = mc.ls(sl=True, et='transform')

        if sel == []:
            return (mc.headsUpMessage("Please select a deformer"))
        else:
            mc.skinCluster(edit = True, prune = True)
        return (mc.headsUpMessage("Unused Points removed"))

    """Removes any points not being deformed by the deformer in its current configuration
    from the deformer set"""

    def editBind(self,selection, *args):

        selection = self.unBindSkin()
        if selection == True:

            return(mc.headsUpMessage("skin detached"))
        
        sknCluster = self.getSelectionSkinClusters(selection)

        delSkin = self.detachSkin()

        if delSkin == True:
            return(mc.headsUpMessage("Skin Detached"))

        if sknCluster != False:

            print "skin information exists"

        #query active item in drop Down
        ddVal2 = mc.optionMenu(self.UIElements['DropDownMenu2'], q=True, v=True)

        print ddVal2

        if ddVal2 == 'detach w/ Hist.':
            try:
                mc.skinCluster(edit=True, unbindKeepHistory=True)
            except:

                return (mc.headsUpMessage("Skin is Detached with History"))

        if ddVal2 == "Detach w/o Hist.":
            #unbinds joints in edit mode, can move joints without effecting skinCluster
            try:
                mc.skinCluster(edit =True, unbind= True)

            except:
                return (mc.headsUpMessage("Skin Detached Without History"))

       
    def toggleJoints(self, *args):

    # Verify we have a mesh selected
        selection = self.getSelectedMesh()

        if selection == None:
            return(mc.headsUpMessage("Select Geometry"))

            # Verify we have a skin cluster
        sknCluster = self.getSelectionSkinClusters(selection)

        if sknCluster == None:
            return(mc.headsUpMessage('skinCluster Not Found'))

        # Query the button state
        buttonState = mc.button(self.UIElements['EditJntsBtn'], aop = True, q=True, label=True)

        # Toggle the button state and run the skinCluster command
        if buttonState == 'Move Joints Off':

            mc.button(self.UIElements['EditJntsBtn'], edit=True,  label='Move Joints On')

            mc.skinCluster(edit=True, mjm=False)

        if buttonState == 'Move Joints On':

            mc.button(self.UIElements['EditJntsBtn'], edit=True, label='Move Joints Off')

            mc.skinCluster(edit=True, mjm=True)

Skin_Utils()
