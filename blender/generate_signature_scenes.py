"""Creative Studio OS — Blender demo generator.

Usage:
  blender --background --python blender/generate_signature_scenes.py

Produces four styled mesh scenes in one .blend file.
Requires Blender; this draft has not been tested inside Blender in this release.
"""
import bpy
import math

STYLES = {
    "LUX": {"color": (0.48, 0.42, 0.33, 1), "metallic": 0.92, "roughness": 0.12},
    "MIN": {"color": (0.84, 0.86, 0.88, 1), "metallic": 0.0, "roughness": 0.45},
    "FUT": {"color": (0.10, 0.62, 0.95, 1), "metallic": 0.55, "roughness": 0.13},
    "EDI": {"color": (0.65, 0.32, 0.22, 1), "metallic": 0.0, "roughness": 0.77}
}

def make_mat(style, info):
    mat = bpy.data.materials.new(f"{style}_signature_material")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = info["color"]
    bsdf.inputs["Metallic"].default_value = info["metallic"]
    bsdf.inputs["Roughness"].default_value = info["roughness"]
    return mat

def build():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for index, (style, info) in enumerate(STYLES.items()):
        x = (index - 1.5) * 4.0
        if style in ("LUX", "FUT"):
            bpy.ops.mesh.primitive_torus_add(major_radius=1.0, minor_radius=0.28, location=(x, 0, 1.6))
        elif style == "MIN":
            bpy.ops.mesh.primitive_uv_sphere_add(segments=64, ring_count=32, location=(x, 0, 1.6))
        else:
            bpy.ops.mesh.primitive_cube_add(size=2.1, location=(x, 0, 1.6))
        obj = bpy.context.object
        obj.name = f"{style}_signature"
        obj.data.materials.append(make_mat(style, info))
        mod = obj.modifiers.new(name="Subdivision", type="SUBSURF")
        mod.levels = 2
        mod.render_levels = 2
        bpy.ops.mesh.primitive_cube_add(size=2, location=(x, 0, -0.15))
        floor = bpy.context.object
        floor.name = f"{style}_pedestal"
        floor.scale = (1.8, 1.8, 0.15)

    world = bpy.context.scene.world
    if world:
        world.use_nodes = True
        bg = world.node_tree.nodes.get("Background")
        if bg:
            bg.inputs["Color"].default_value = (0.035, 0.045, 0.065, 1)
            bg.inputs["Strength"].default_value = 0.6

    bpy.ops.object.light_add(type="AREA", location=(0, -4, 8))
    light = bpy.context.object
    light.name = "Softbox"
    light.data.energy = 2400
    light.data.shape = "RECTANGLE"
    light.data.size = 9
    light.data.size_y = 5

    bpy.ops.object.camera_add(location=(9, -17, 9))
    camera = bpy.context.object
    direction = (0, 0, 1.1) - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    bpy.context.scene.camera = camera
    bpy.context.scene.render.resolution_x = 1600
    bpy.context.scene.render.resolution_y = 900
    bpy.context.scene.render.resolution_percentage = 100
    bpy.context.scene.render.engine = "BLENDER_EEVEE_NEXT"
    bpy.ops.wm.save_as_mainfile(filepath=bpy.path.abspath("//signature_scenes.blend"))

if __name__ == "__main__":
    build()
