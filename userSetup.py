import os, sys
import maya.cmds as cmds
import pymel.core as pm
import maya.mel as mel


for path in enumerate(sys.path):
    print path

envPath = os.environ['RDOJO']

if not path in sys.path:
    sys.path.append(envPath)
    print 'R: directory loaded'
else:
    print 'R: directory failed'

#startup = pm.evaldeferred('import Maya.setup')
loadCometMenu = mel.eval('evalDeferred("source cometMenu.mel");')

if loadCometMenu == False:
    print 'unable to load CometMenu.'
else:
    print 'Comet Menu loaded'
