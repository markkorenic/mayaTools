import pymel.core as pm


def rig_organizer():
	'''creates group hierarchy for rig components'''
	
	#create groups
	charGrp = pm.group(n = 'Character', w = True )
	charGrp.deselect()
	globMove = pm.group(n = 'globalMove_GRP')
	globMove.deselect()
	jntGrp = pm.group(n = "joints_GRP")
	jntGrp.deselect()
	geoGrp = pm.group(n = "geo_GRP")
	geoGrp.deselect()
	ikGrp = pm.group(n = "IK_GRP")
	ikGrp.deselect()
	ctrlGrp = pm.group(n = "ctrl_GRP")
	ctrlGrp.deselect()
	hideGrp= pm.group(n = "toHide_GRP")
	hideGrp.deselect()
	
	#parent children 
	charGrp.addChild(globMove)
	charGrp.addChild(geoGrp)
	charGrp.addChild(hideGrp)
	globMove.addChild(jntGrp)
	globMove.addChild(ikGrp)
	globMove.addChild(ctrlGrp)
	
	#lock all channels
	for vec in ["t", "r","s"]:
		for ch in ["x", "y", "z"]:
			charGrp.attr("%s%s"%(vec, ch)).lock()
			globMove.attr("%s%s"%(vec, ch)).lock()
			geoGrp.	attr("%s%s"%(vec, ch)).lock()
			jntGrp.attr("%s%s"%(vec, ch)).lock()
			ikGrp.attr("%s%s"%(vec, ch)).lock()
			hideGrp.attr("%s%s"%(vec, ch)).lock()
rig_organizer()
