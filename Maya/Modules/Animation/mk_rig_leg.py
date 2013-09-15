"""
author: Mark Korenic   www.skeletech.net
file: rig_leg.py
"""
import pymel.core as pm
import Maya.System.Rig_Utils as rigUtils
reload(rigUtils)

CLASS_NAME = "Rig_Leg"
TITLE = "Leg_Rig"
DESCRIPTION = "builds leg rig"

class Rig_Leg():

    def __init__(self):
        print 'In Leg Rig'
        self.rig_leg()


    def rig_leg(self, *args):
        """create leg chain based off locator positions"""
        BN_joints = []
        FK_joints = []
        IK_joints = []
        jointOri = 'XYZ'
        selection = pm.selected()

        print selection

    # clear selection makes sure to create more than one joint at creation
        pm.select(clear=True)

    # sets joints to positions of locators
        for i in selection:

            locPos = i.getTranslation(selection, q=True, ws=True)
            BN_joints.append(pm.joint(p=locPos, name="BN_%s_JNT" % (i), oj=jointOri))

        pm.select(clear=True)
        for i in selection:
            locPos = i.getTranslation(selection, q=True, ws=True)
            FK_joints.append(pm.joint(p=locPos, n="FK_%s_JNT" % (i), rad=.4, oj=jointOri))
            print FK_joints

	pm.select(clear=True)

        for i in selection:
            locPos = i.getTranslation(selection, q=True, ws=True)
            IK_joints.append(pm.joint(p=locPos, n="IK_%s_JNT" % (i), rad=.6, oj=jointOri))

            print IK_joints
            print FK_joints
            print BN_joints
	pm.delete(selection)
	#constrain joint chains
	rigUtils.constrainJoint(FK_joints[0:1], IK_joints[0:1], BN_joints[0:1])
	#build IK
	buildIK = rigUtils.createIK(IK_joints[0], IK_joints[2])

        # legContain = pm.container([BN_joints, IK_joints, FK_joints])
