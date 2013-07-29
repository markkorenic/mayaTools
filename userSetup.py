'''
File: userSetup.py

@author: markkorenic		www.skeletech.net
Created on: Sept. 6th, 2012
'''
import sys
import maya.cmds as cmds
import maya.mel as mel

#print PYTHONPATHS
for path in sys.path:
    print path
#define a path to append to pythonpath 

toolPath = 'C:\Users\markkorenic\Google Drive\maya_scripts\scripts'
print toolPath
 
#Check to see if the path is already part of the Maya scripts path, if it is not, add it.
if not path in sys.path:
    sys.path.append(toolPath)
print 'Loaded Maya tools path.'

#load cometMenu
loadCometMenu = mel.eval('evalDeferred("source cometMenu.mel");')

if loadCometMenu==False:
    print 'unable to load CometMenu.'
else:
    print 'Comet Menu loaded with no probs.'