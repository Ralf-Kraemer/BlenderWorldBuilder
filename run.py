import bpy
import quickHandler

# Gather input
print("What should your world be called?")
world_name = input()
world_file_name = "".join([c for c in world_name if c.isalpha() or c.isdigit()]).rstrip()

# Set up work environment
bpy.ops.wm.open_mainfile(filepath="./input/template.blend")

# Generate terrain

# Generate water, dirt and natural props

# Generate structures

# Beautify

# Export to GLB
target_directory = "./output/"
target_path = target_directory + world_file_name
print(target_path)
bpy.ops.export_scene.gltf(filepath=target_path, export_format='GLB')