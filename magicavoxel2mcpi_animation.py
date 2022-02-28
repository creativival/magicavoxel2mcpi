#!/usr/bin/env python

#
# MagicaVoxel2MinecraftPi
#


from voxel_util import create_voxel, post_to_chat, ply_to_position_list, reset
from time import sleep

# polygon file format exported from MagicaVoxel
ply_files = ['frog1.ply', 'frog2.ply', 'frog3.ply', 'frog4.ply', 'frog5.ply', 'frog4.ply', 'frog3.ply', 'frog2.ply']

# reset_stop
reset_stop = 0.01

# create_stop
create_stop = 0.1

# repeat repeat_count
repeat_count = 200

# reset area
reset_area = (-10, 0, -10, 10, 20, 10)

# Origin to create (Minecraft)
x0 = 0
y0 = 0
z0 = 0

# Model size
is_even = True

# Rotation degree (MagicaVoxel)
alpha = 0  # x-axis
beta = 0  # y-axis
gamma = 0  # z-axis

# Offset for rotation (MagicaVoxel)sssss
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

post_to_chat('animation polygon file format model')
box_positions_list = [ply_to_position_list(ply_file) for ply_file in ply_files]

i = 0
while True:
    print(i)
    reset(*reset_area)
    sleep(reset_stop)
    create_voxel(box_positions_list[i % len(ply_files)], model_settings)
    sleep(create_stop)
    i += 1
    if i > repeat_count:
        break
