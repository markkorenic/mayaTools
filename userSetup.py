import os,sys
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm


print("---------Starting userSetup.py from Documents/maya/scripts-----------")

#print all maya PYTHONPATH directories
#for path in sys.path:
#print(path)

#define a path to append to Maya's pythonpath
#toolPath = 'C:/Users/Documents/maya/scripts'
#print toolPath

#Declaring a new variable to represent the testToolPath
#path = toolPath

#Check to see if the path is already part of the Maya scripts path, if it is not, add it
#if not path in sys.path:
   # sys.path.append(path)
#print ('maya scripts path was added with no problems')

comet_script = pm.evalDeferred('source "cometMenu.mel"')
#eval hangs menu after maya UI loads
if not comet_script:
    print('unable to load CometMenu')
else:
    print('cometMenu loaded with no problems')

print("----------End UserSetup.py initialization--------------")
