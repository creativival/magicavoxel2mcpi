#!/usr/bin/env python

#
# MagicaVoxel2MinecraftPi
#


from voxel_util import create_voxel, post_to_chat, ply_to_positions, reset
from time import sleep

# polygon file format exported from MagicaVoxel
body_ply_file = 'robot-body.ply'
head_ply_file = 'robot-head.ply'
hands_ply_file = 'robot-hands.ply'
propeller_ply_file = 'robot-propeller.ply'

# reset_stop
reset_stop = 0.01

# create_stop
create_stop = 0.5

# repeat repeat_count
repeat = 100

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

# Offset for rotation(MagicaVoxel)
offset_x = 0  # x-axis
offset_y = 0  # y-axis
offset_z = 7  # z-axis

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
body_box_positions = ply_to_positions(body_ply_file)
head_box_positions = ply_to_positions(head_ply_file)
hands_box_positions = ply_to_positions(hands_ply_file)
propeller_box_positions = ply_to_positions(propeller_ply_file)

# create body
create_voxel(body_box_positions, model_settings)

for i in range(repeat):
    reset(-5, 9, -5, 5, 15, 5)
    reset(-8, 0, -7, 7, 14, -5)
    reset(-7, 0, 4, 7, 14, 7)
    reset(-6, 3, -4, -4, 11, 4)
    sleep(reset_stop)
    model_settings['alpha'] = 0
    model_settings['beta'] = 0
    model_settings['gamma'] = 6 * i
    create_voxel(head_box_positions, model_settings)
    model_settings['alpha'] = 6 * i
    model_settings['beta'] = 0
    model_settings['gamma'] = 0
    create_voxel(hands_box_positions, model_settings)
    model_settings['alpha'] = 0
    model_settings['beta'] = 6 * i
    model_settings['gamma'] = 0
    create_voxel(propeller_box_positions, model_settings)
    if (6 * i) % 90 == 0:
        sleep(2 * create_stop)
    else:
        sleep(create_stop)
