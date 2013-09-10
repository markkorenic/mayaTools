"""
author: Mark Korenic   www.skeletech.net
file: rig_leg.py
"""
import pymel.core as pm


CLASS_NAME = "Rig_Leg"
TITLE = "Leg_Rig"
DESCRIPTION = "builds leg rig"

class Rig_Leg():

    def __init__(self):
        print 'In Leg Rig'
        self.rig_leg()

    def rig_leg(self, *args):
	"""create leg chain based off locator positions"""
	
	locList= pm.selected()
	FK_joints = []
	IK_joints = []
	
	selection= pm.ls(sl=True)
    
	# prints the list
	print selection

	#clear selection makes sure to create more than one joint at creation
	pm.select(clear=True)

	#sets joints to positions of locators
	for i in selection:
		#locPos = pm.xform(i, q=True, t=True, ws=True)
		#instead of xform, the awesome getTranslation can do the exact same thing
		locPos= i.getTranslation(selection,q=True, ws=True)
		locList.append(pm.joint(p=locPos, name="BN_%s_JNT" % (i)))
		
	pm.select(clear=True)	
	for i in selection:
		locPos= i.getTranslation(selection,q=True, ws=True)
		FK_joints.append(pm.joint(p=locPos, n="FK_%s_JNT" % (i), rad = .4))
	pm.select(clear=True)	
	
	for i in selection:
		locPos= i.getTranslation(selection,q=True, ws=True)
		IK_joints.append(pm.joint(p=locPos, n="IK_%s_JNT" % (i), rad = .6))
		print IK_joints
		print FK_joints
		print locList
