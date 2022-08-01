import sys
import bpy

# Gather input
world_input = sys.argv[5]
world_name = "".join([c for c in world_input if c.isalpha() or c.isdigit()]).rstrip()
print(world_name)


# Set up work environment
bpy.ops.wm.open_mainfile(filepath="./input/template.blend")
bpy.ops.object.select_all(action='DESELECT')

# Input seed
print("Seeding...")
node_group = bpy.data.node_groups['Seeder']
node_group.nodes["SeedOutput"].inputs[0].default_value = int(world_name[0]+world_name[1], 16)
node_group.nodes["SeedOutput"].inputs[1].default_value = int(world_name[2]+world_name[3], 16)
node_group.nodes["SeedOutput"].inputs[2].default_value = int(world_name[4]+world_name[5], 16)

# Generate terrain
def bakeTerrain():
    print("Baking terrain...")
    bpy.data.objects['_Terrain'].select_set(True)
    bpy.ops.object.modifier_apply(modifier="GeometryNodes")

bakeTerrain()


# Generate structures
def applyAndSeparate():
    bpy.ops.object.modifier_apply(modifier="GeometryNodes")
    bpy.ops.mesh.separate(type='LOOSE')
    
def setOriginToGeometry():
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
    
def bakePrefabLocations(str):
    bpy.ops.object.select_all(action='DESELECT')
    for obj in bpy.data.objects[str].children:
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        applyAndSeparate()
        obj.select_set(False)
        bpy.context.view_layer.objects.active = None
    for obj in bpy.data.objects[str].children:
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        setOriginToGeometry()
        print("Expected:", obj)
        print("Actual:", bpy.context.active_object)
        obj.select_set(False)
        bpy.context.view_layer.objects.active = None
        

print("Generating prefab locations...")
bakePrefabLocations('_Regions')
bakePrefabLocations('_Props')

# Beautify


# Export to GLB
target_directory = "./output/"
target_path = target_directory + world_name
print("Exporting to", target_path)
bpy.ops.export_scene.gltf(filepath=target_path, check_existing=False, export_format='GLB', export_copyright='Created by A.C.E. DAO', export_materials='PLACEHOLDER', use_renderable=True)
print("Done.")