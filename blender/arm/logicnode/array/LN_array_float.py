from arm.logicnode.arm_nodes import *

class FloatArrayNode(ArmLogicTreeNode):
    """Stores an array of float elements as a variable."""
    bl_idname = 'LNArrayFloatNode'
    bl_label = 'Array Float'
    arm_version = 1

    def __init__(self):
        array_nodes[str(id(self))] = self

    def init(self, context):
        super(FloatArrayNode, self).init(context)
        self.add_output('ArmNodeSocketArray', 'Array', is_var=True)
        self.add_output('NodeSocketInt', 'Length')

    def draw_buttons(self, context, layout):
        row = layout.row(align=True)

        op = row.operator('arm.node_add_input', text='New', icon='PLUS', emboss=True)
        op.node_index = str(id(self))
        op.socket_type = 'NodeSocketFloat'
        op2 = row.operator('arm.node_remove_input', text='', icon='X', emboss=True)
        op2.node_index = str(id(self))

add_node(FloatArrayNode, category=PKG_AS_CATEGORY, section='variable')
