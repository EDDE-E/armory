from arm.logicnode.arm_nodes import *

class OnCanvasElementNode(ArmLogicTreeNode):
    """Activates the output whether an action over the given UI element is done."""
    bl_idname = 'LNOnCanvasElementNode'
    bl_label = 'On Canvas Element'
    arm_version = 1

    property0: EnumProperty(
        items=[('click', 'Click', 'Listen to mouse clicks'),
               ('hover', 'Hover', 'Listen to mouse hover')],
        name='Listen to', default='click')
    property1: EnumProperty(
        items=[('down', 'Down', 'Down'),
               ('started', 'Started', 'Started'),
               ('released', 'Released', 'Released')],
        name='Status', default='down')
    property2: EnumProperty(
        items=[('left', 'Left', 'Left Button'),
               ('right', 'Right', 'Right Button'),
               ('middle', 'Middle', 'Middle Button')],
        name='Mouse Button', default='left')

    def init(self, context):
        super(OnCanvasElementNode, self).init(context)
        self.add_input('NodeSocketString', 'Element')
        self.add_output('ArmNodeSocketAction', 'Out')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')

        if self.property0 == "click":
            layout.prop(self, 'property1')
            layout.prop(self, 'property2')

add_node(OnCanvasElementNode, category=PKG_AS_CATEGORY)
