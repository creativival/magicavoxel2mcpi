#!/usr/bin/env python

#
# MagicaVoxel2MinecraftPi
#


from voxel_util import create_voxel, post_to_chat, ply_to_positions, reset_area
from magicavoxel_axis import axis
from all_clear import clear
from time import sleep

# polygon file format exported from MagicaVoxel
body_ply_file = 'walking_cat_body.ply'
part_ply_file = 'walking_cat_limbs.ply'
part_reverse_ply_file = 'walking_cat_limbs_reverse.ply'

# reset_stop
reset_stop = 0.01

# create_stop
create_stop = 0.5

# repeat repeat_count
repeat_count = 20

# Origin to create (Minecraft)
x0 = 0
y0 = 0
z0 = -100

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
body_box_positions = ply_to_positions(body_ply_file)
part_box_positions = ply_to_positions(part_ply_file)
part_reverse_box_positions = ply_to_positions(part_reverse_ply_file)

clear()
sleep(5)
for i in range(repeat_count):
    reset_area(
        -10,
        0,
        -10 + model_settings['z0'],
        10,
        25,
        10 + model_settings['z0']
    )
    model_settings['z0'] += 10
    sleep(reset_stop)
    create_voxel(body_box_positions, model_settings)
    if i % 2 == 0:
        create_voxel(part_box_positions, model_settings)
    else:
        create_voxel(part_reverse_box_positions, model_settings)
    sleep(create_stop)
else:
    reset_area(
        -10,
        0,
        -10 + model_settings['z0'],
        10,
        25,
        10 + model_settings['z0']
    )
