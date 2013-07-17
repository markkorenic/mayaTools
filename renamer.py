'''
Created on Jun 5, 2013

@author: markkorenic


Renamer UI based off of Jeremy Ernst Python Programming
'''


import maya.cmds as cmds
from functools import partial

def addSuffixOrPrefix(type):
    """adds prefix or suffix to text objects"""
    #get selection
        
    selection = cmds.ls(sl = True)
    #check length
    if len(selection) > 0:
       
        #ask user for suffix or prefix
        cmds.promptDialog(title = 'Add Suffix/Prefix', message = 'Enter Name:', button = ["OK","Cancel"], defaultButton = "OK", cancelButton ="Cancel", dismissString = "Cancel")
        text = cmds.promptDialog(q =True, text =True)
        
        if text != "":
            if type == 'prefix':
                for object in selection:
                    cmds.rename(object, text + "_" + object)                
            if type == "suffix":
                for object in selection:
                    cmds.rename(object, object + "_" + text)                 
            
            #add suffix
            for object in selection:
                cmds.rename(object, object + "_" + text)

def checkboxChange(type, *args):
    
    value = cmds.checkBox(type + "CB", q =True, v =True)
    #if check box value is True enable text field
    if value == True:
        cmds.textField(type + "TF", edit = True, enable = True)
    #if false, disable text field
    if value == False:
        cmds.textField(type + "TF", edit = True, enable = False)

def accept(*args):
    
    prefix = cmds.textField('prefixTF', q =True, text = True)
    suffix = cmds.textField('suffixTF', q =True, text = True)
    print prefix
    print suffix
    
def cancel(*args):
    
    cmds.deleteUI("renamerUI")
    
def UI():
    """Build window elements"""
    if cmds.window("renamerUI", exists = True):
        cmds.deleteUI("renamerUI")
        
    window = cmds.window("renamerUI", w = 300, h = 150, title = 'mk_renamer', mnb = False, mxb = False, sizeable = False)
    #create layout
    layout = cmds.formLayout() 
    #create checkboxes
    prefixCB = cmds.checkBox('prefixCB',label = "Add Prefix", v = False, cc = partial(checkboxChange,'prefix'))
    suffixCB = cmds.checkBox('suffixCB', label = "Add Suffix", v = False,cc = partial(checkboxChange,'suffix'))
    
    textA = cmds.text(label = "Prefix:")
    textB = cmds.text(label = "Suffix:")
    prefixTF = cmds.textField("prefixTF", w = 200,enable = False)
    suffixTF = cmds.textField("suffixTF", w = 200, enable = False)
    
    acceptBtn = cmds.button(label = 'Accept', w = 135,command = accept)
    cancelBtn = cmds.button(label = "Cancel", w = 135,command = cancel)
    #layout items
    
    cmds.formLayout(layout, edit = True, af = [(prefixCB, "left", 10), (prefixCB, "top", 10)])
    cmds.formLayout(layout, edit = True, af = [(suffixCB, "left", 100), (suffixCB, "top", 10)])
    cmds.formLayout(layout, edit = True, af = [(prefixTF, "left", 60), (prefixTF, "top", 45)])
    cmds.formLayout(layout, edit = True, af = [(suffixTF, "left", 60), (suffixTF, "top", 70)])               
    cmds.formLayout(layout, edit = True, af = [(textA, "left", 10), (textA, "top", 45)])
    cmds.formLayout(layout, edit = True, af = [(textB, "left", 10), (textB, "top", 70)])
    
    cmds.formLayout(layout, edit = True, af = [(acceptBtn, "left", 10), (acceptBtn, "bottom", 10)])
    cmds.formLayout(layout, edit = True, af = [(cancelBtn, "left", 155), (cancelBtn, "bottom", 10)])
    
    #show window
    cmds.showWindow(window)

UI()