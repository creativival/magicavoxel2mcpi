#!/usr/bin/env python

#
# MagicaVoxel2MinecraftPi
#

from voxel_util import create_voxel, post_to_chat, ply_to_positions

# polygon file format exported from MagicaVoxel
ply_file = 'box2x2.ply'

# Origin to create (Minecraft)
x0 = 0
y0 = 5
z0 = 0

# Model size
is_even = False

# Rotation degree (MagicaVoxel)
alpha = 0  # x-axis
beta = 0  # y-axis
gamma = 0  # z-axis

# Offset for rotation (MagicaVoxel)
offset_x = 0  # x-axis
offset_y = 0  # y-axis
offset_z = 0  # z-axis

model_settings = {
    'x0': x0,
    'y0': y0,
    'z0': z0,
    'is_even': is_even,
    'alpha': alpha,
    'beta': beta,
    'gamma': gamma,
    'offset_x': offset_x,
    'offset_y': offset_y,
    'offset_z': offset_z,
}

post_to_chat('create polygon file format model')
box_positions = ply_to_positions(ply_file)
create_voxel(box_positions, model_settings)
