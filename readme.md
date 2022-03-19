# Blender World Builder

### Procedural environment generation with Python

##### Intended for efficient design and development in gaming and VR

>> blender --background --python run.py

Algo:
1. New .blend
2. Select all; then delete all
3. Create Plane
4. Subdivide 64 times
5. Apply displace modifier (randomized gradient pattern, for basic terrain shape and lakes/rivers)
6. Subdivide smooth

1. Generate rocks
2. Generate water meshes
3. Apply base textures
4. Apply normal maps (noise)
5. Place natural props
6. Place structural props

1. Generate bird’s view (png)
2. Generate thumbnail (png)
3. Export as GLB


© Ralf Kraemer 2022