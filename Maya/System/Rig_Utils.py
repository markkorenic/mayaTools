import pymel.core as pm


def createIK(sj, ej):
    print 'creating IK'
    legIK = pm.ikHandle(sj=sj, ee=ej, solver='ikRPsolver', n='leg_ikh')
    
def constrainJoints(IK, BN):
    pm.orientConstraint(IK, BN, mo=True)
