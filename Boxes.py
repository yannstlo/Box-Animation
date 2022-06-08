import bpy
import random

for x in range(1, 100):
    for y in range(1, 100):
        xSpacing = x * 1.2
        ySpacing = y * 1.2
        height = random.randint(2, 15)
        location = (xSpacing, ySpacing, height / 2)
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(
            location), scale=(1, 1, 1 * height))


bpy.ops.object.select_all(action='SELECT')
for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        obj.location.z = 0.0
        obj.scale = (1, 1, 0)
        obj.keyframe_insert(data_path="scale", frame=0)

counter = 1

# mat1 = bpy.data.materials['Material.001']
# mat2 = bpy.data.materials['Material.002']
for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        obj.location.z = 0.0
        height = random.randint(2, 10)
        obj.scale = (1, 1, 1 * height)
        obj.keyframe_insert(data_path="scale", frame=height*10)
        # print("Frame: " + str(counter))
        counter += 1
        
        mat = bpy.data.materials.new(name='Material')
        mat.use_nodes = True
        principled_node = mat.node_tree.nodes.get('Principled BSDF')
        principled_node.inputs[0].default_value = (random.random(), random.random(), random.random(), 0.5)
        obj.data.materials.append(mat)

bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
