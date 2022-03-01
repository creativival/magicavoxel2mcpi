#!/usr/bin/env python

#
# MagicaVoxel2MinecraftPi
#

from voxel_util import create_voxel, post_to_chat, ply_to_positions, reset_area
from magicavoxel_axis import axis
from all_clear import clear
from time import sleep

# polygon file format exported from MagicaVoxel
ply_file = 'drone-propeller.ply'

# Origin to create (Minecraft)
x0 = 20
y0 = 0
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

post_to_chat('create polygon file format model')
box_positions = ply_to_positions(ply_file)

clear()
axis()
for i in range(60):
    reset_area(x0 - 25, y0 + 18, z0 - 25, x0 + 25, y0 + 18, z0 + 25)
    sleep(0.01)
    model_settings['gamma'] = i * 30
    create_voxel(box_positions, model_settings)
    sleep(0.1)
