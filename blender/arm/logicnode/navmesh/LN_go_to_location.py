from arm.logicnode.arm_nodes import *

class GoToLocationNode(ArmLogicTreeNode):
    """Makes a NavMesh agent go to location."""
    bl_idname = 'LNGoToLocationNode'
    bl_label = 'Go To Location'
    arm_version = 1

    def init(self, context):
        super(GoToLocationNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_input('NodeSocketShader', 'Location')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(GoToLocationNode, category=PKG_AS_CATEGORY)
