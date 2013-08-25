"""
author: Mark Korenic   www.skeletech.net
file: mk_leg_rig.py
"""
import pymel.core as pm

CLASS_NAME = "Rig_Leg"
TITLE = "Leg_Rig"
DESCRIPTION = "builds leg rig"


class Rig_Leg():

	def __init__(self):
		print 'In Leg Rig'
		self.rig_leg()
		
	
	def rig_leg(self):
		"""create leg chain based off locator positions"""
		
		legJoints = []
		selection= pm.selected()
		
		# prints the list
		print selection
		
		#clear selection makes sure to create more than one joint at creation
		pm.select(deselect=True)
		
		#sets joints to positions of locators
		for i in selection:
			#locPos = pm.xform(i, q=True, t=True, ws=True)
			locPos= i.getTranslation()
			legJoints.append(pm.joint(p=locPos))
			#rename joints
			jntSel = pm.selected(dag=True, type="joint")
			#set prefix for joints
			prefix = 'bn_'
			for jnt in jntSel:
				jnt.rename(prefix + jnt.name().split('|')[-1])
Rig_Leg()
