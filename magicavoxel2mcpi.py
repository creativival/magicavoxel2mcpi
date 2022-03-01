#!/usr/bin/env python

#
# MagicaVoxel2MinecraftPi
#

from voxel_util import create_voxel, post_to_chat, ply_to_positions
from magicavoxel_axis import axis
from all_clear import clear
from time import sleep

# polygon file format exported from MagicaVoxel
ply_file = 'piyo.ply'

# Origin to create (Minecraft)
x0 = 0
y0 = 5
z0 = 0

# Rotation degree (MagicaVoxel)
alpha = 0  # x-axis
beta = 0  # y-axis
gamma = 0  # z-axis

model_settings = {
    'x0': x0,
    'y0': y0,
    'z0': z0,
    'alpha': alpha,
    'beta': beta,
    'gamma': gamma,
}

clear()
post_to_chat('create polygon file format model')
box_positions = ply_to_positions(ply_file)
create_voxel(box_positions, model_settings)
