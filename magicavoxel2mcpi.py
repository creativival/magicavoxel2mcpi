#!/usr/bin/env python

#
# MagicaVoxel2MinecraftPi
#

from voxel_util import create_voxel, post_to_chat

# polygon file format exported from MagicaVoxel
ply_file = 'chick.ply'

# Origin to create (Minecraft)
x0 = 0
y0 = 0
z0 = 0

# Model size
is_even = False

# Rotation degree (MagicaVoxel)
alpha = 0  # x-axis
beta = 0  # y-axis
gamma = 180  # z-axis

# Offset for rotation (MagicaVoxel)
offset_x = 0  # x-axis
offset_y = 0  # y-axis
offset_z = 0  # z-axis

# Block ID (default = 35:0 = White Wool)
blockTypeId = 35
blockData = 0

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
create_voxel(ply_file, model_settings)
