#!/usr/bin/env python

#
# MagicaVoxel2MinecraftPi
#


from voxel_util import create_voxel, post_to_chat, ply_to_positions, reset
from time import sleep

# polygon file format exported from MagicaVoxel
body_ply_file = 'data/drone-body.ply'
part_ply_file = 'data/drone-propeller.ply'

# reset_stop
reset_stop = 0.01

# create_stop
create_stop = 0.5

# repeat repeat_count
repeat_count = 50

# Origin to create (Minecraft)
x0 = 0
y0 = 0
z0 = 0

# Rotation degree (MagicaVoxel)
alpha = 0  # x-axis
beta = 0  # y-axis
gamma = 0  # z-axis

# Offset for rotation(MagicaVoxel)
offset_x = 0  # x-axis
offset_y = 0  # y-axis
offset_z = 0  # z-axis

model_settings = {
    'x0': x0,
    'y0': y0,
    'z0': z0,
    'alpha': alpha,
    'beta': beta,
    'gamma': gamma,
    'offset_x': offset_x,
    'offset_y': offset_y,
    'offset_z': offset_z,
}

post_to_chat('animation polygon file format model')
body_box_positions = ply_to_positions(body_ply_file)
part_box_positions = ply_to_positions(part_ply_file)

# create body
model_settings['x0'] = 0
create_voxel(body_box_positions, model_settings)
# create parts
for i in range(repeat_count):
    print(i)
    reset(-25, 18, -25, 25, 18, 25)
    sleep(reset_stop)
    model_settings['gamma'] = 6 * i
    model_settings['x0'] = 14
    model_settings['y0'] = 0
    model_settings['z0'] = 0
    create_voxel(part_box_positions, model_settings)
    model_settings['x0'] = -14
    model_settings['y0'] = 0
    model_settings['z0'] = 0
    create_voxel(part_box_positions, model_settings)
    model_settings['x0'] = 0
    model_settings['y0'] = 0
    model_settings['z0'] = -14
    create_voxel(part_box_positions, model_settings)
    model_settings['x0'] = 0
    model_settings['y0'] = 0
    model_settings['z0'] = 14
    create_voxel(part_box_positions, model_settings)
    if (6 * i) % 90 == 0:
        sleep(2 * create_stop)
    else:
        sleep(create_stop)
