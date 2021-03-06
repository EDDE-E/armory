from arm.logicnode.arm_nodes import *

class SpawnSceneNode(ArmLogicTreeNode):
    """Spawns the given scene."""
    bl_idname = 'LNSpawnSceneNode'
    bl_label = 'Spawn Scene'
    arm_version = 1

    def init(self, context):
        super(SpawnSceneNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketShader', 'Scene')
        self.add_input('NodeSocketShader', 'Transform')
        self.add_output('ArmNodeSocketAction', 'Out')
        self.add_output('ArmNodeSocketObject', 'Root')

add_node(SpawnSceneNode, category=PKG_AS_CATEGORY)
