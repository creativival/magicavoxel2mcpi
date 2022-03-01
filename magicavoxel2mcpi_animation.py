#!/usr/bin/env python

#
# MagicaVoxel2MinecraftPi
#


from voxel_util import create_voxel, post_to_chat, ply_to_positions, reset_area
from magicavoxel_axis import axis
from all_clear import clear
from time import sleep

# polygon file format exported from MagicaVoxel
ply_files = ['frog1.ply', 'frog2.ply', 'frog3.ply', 'frog4.ply', 'frog5.ply', 'frog4.ply', 'frog3.ply', 'frog2.ply']

# reset_stop
reset_stop = 0.01

# create_stop
create_stop = 0.1

# repeat repeat_count
repeat_count = 50

# reset area
reset_size = (-10, 0, -10, 10, 20, 10)

# Origin to create (Minecraft)
x0 = 0
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

post_to_chat('animation polygon file format model')
box_positions_list = [ply_to_positions(ply_file) for ply_file in ply_files]

clear()
for i in range(repeat_count):
    print(i)
    reset_area(*reset_size)
    sleep(reset_stop)
    create_voxel(box_positions_list[i % len(ply_files)], model_settings)
    sleep(create_stop)
