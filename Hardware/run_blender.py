import bpy
import json


# read parameters
configFile =  bpy.path.abspath("//par_file.json")

print(configFile)

with open(configFile, 'r') as f:
  data = json.load(f)

print(data)

length = data["length"]
width = data["width"]
height = data["height"]


# set parameters
bpy.ops.transform.resize( value=(length,width,height))


# render image
bpy.context.scene.render.filepath = "//images/image.png"
print(bpy.path.abspath(bpy.context.scene.render.filepath))
bpy.context.scene.render.resolution_x = 640 
bpy.context.scene.render.resolution_y = 480
bpy.ops.render.render(write_still = True)