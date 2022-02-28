#!/usr/bin/env python

#
# Voxel Util
#

import mcpi.minecraft as minecraft
import math
from time import sleep

mc = minecraft.Minecraft.create()


def post_to_chat(message):
    mc.postToChat(message)


def create_voxel(ply_file, model_settings):
    box_positions = ply_to_position_list(ply_file)

    for bp in box_positions:
        x = bp[0]
        y = bp[1]
        z = bp[2]
        block_type_id = bp[3]
        block_data = bp[4]
        set_block(x, y, z, block_type_id, block_data, model_settings)


def is_included_six_numbers(_line):
    line_list = _line.split()
    if len(line_list) != 6:
        return False
    for i in range(6):
        try:
            float(line_list[i])
        except ValueError:
            return False
    return True


def ply_to_position_list(ply_file):
    # PLY よりボックスの座標を読み込む
    block_type_id = 35
    box_positions = set()
    with open(ply_file, 'r') as f:
        lines = f.read()
        lines = lines.replace('\r\n', '\n')
        lines = lines.strip()
        positions = [list(map(float, ln.split())) for ln in lines.split('\n') if is_included_six_numbers(ln)]

        number_of_faces = int(len(positions) / 4)
        for i in range(number_of_faces):
            vertex1 = positions[i * 4]
            vertex2 = positions[i * 4 + 1]
            vertex3 = positions[i * 4 + 2]
            vertex4 = positions[i * 4 + 3]  # no need
            x = min(vertex1[0], vertex2[0], vertex3[0])
            y = min(vertex1[1], vertex2[1], vertex3[1])
            z = min(vertex1[2], vertex2[2], vertex3[2])
            r = int(vertex1[3])
            g = int(vertex1[4])
            b = int(vertex1[5])

            # block color
            if r == 0:
                if g == 0:
                    if b == 0:
                        block_data = 15  # black 0,0,0
                    else:
                        block_data = 11  # blue 0,0,255
                elif g == 80:
                    if b == 0:
                        block_data = 13  # green 0,80,0
                    else:
                        block_data = 0  # white(default) 0,80,x
                else:
                    if b == 0:
                        block_data = 5  # lime 0,255,0
                    else:
                        block_data = 9  # cyan 0,255,255
            else:
                if g == 0:
                    if b == 0:
                        block_data = 14  # red 255,0,0
                    else:
                        block_data = 2  # magenta 255,0,255
                elif g == 165:
                    if b == 0:
                        block_data = 1  # orange 255,165,0
                    else:
                        block_data = 0  # white(default) 255,165,x
                else:
                    if b == 0:
                        block_data = 4  # yellow 255,255,0
                    else:
                        block_data = 0  # white(default) x,x,x

            # ボックスを置く方向を解析
            if vertex1[0] == vertex2[0] and vertex2[0] == vertex3[0]:  # y-z plane
                step = max(vertex1[1], vertex2[1], vertex3[1]) - y
                if vertex1[1] != vertex2[1]:
                    x -= step
            elif vertex1[1] == vertex2[1] and vertex2[1] == vertex3[1]:  # z-x plane
                step = max(vertex1[2], vertex2[2], vertex3[2]) - z
                if vertex1[2] != vertex2[2]:
                    y -= step
            else:  # x-y plane
                step = max(vertex1[0], vertex2[0], vertex3[0]) - x
                if vertex1[0] != vertex2[0]:
                    z -= step

            # minimum unit: 0.1
            box_positions.add(
                (int(x * 10 / step) / 10.0, int(y * 10 / step) / 10.0, int(z * 10 / step) / 10.0, block_type_id,
                 block_data)
            )

        # sort
        box_positions = list(box_positions)
        box_positions.sort(key=lambda x: x[2])

        return box_positions


def set_block(x, y, z, block_type_id, block_data, model_settings):
    x0 = model_settings['x0']
    y0 = model_settings['y0']
    z0 = model_settings['z0']
    is_even = model_settings['is_even']
    alpha = model_settings['alpha']
    beta = model_settings['beta']
    gamma = model_settings['gamma']
    offset_x = model_settings['offset_x']
    offset_y = model_settings['offset_y']
    offset_z = model_settings['offset_z']

    if is_even:
        x += 0.5
        z += 0.5

    # x-rotation degree alpha
    xx = x - offset_x
    yx = ((y - offset_y) * math.cos(math.radians(alpha)) - (z - offset_z) * math.sin(math.radians(alpha)))
    zx = ((y - offset_y) * math.sin(math.radians(alpha)) + (z - offset_z) * math.cos(math.radians(alpha)))
    # y-rotation degree beta
    xy = (zx * math.sin(math.radians(beta)) + xx * math.cos(math.radians(beta)))
    yy = yx
    zy = (zx * math.cos(math.radians(beta)) - xx * math.sin(math.radians(beta)))
    # z-rotation degree gamma
    xz = (xy * math.cos(math.radians(gamma)) - yy * math.sin(math.radians(gamma)))
    yz = (xy * math.sin(math.radians(gamma)) + yy * math.cos(math.radians(gamma)))
    zz = zy

    # bug fix
    x = round(xz, 3)
    y = round(yz, 3)
    z = round(zz, 3)
    # player position
    player_position = list(map(int, mc.player.getPos()))
    x += player_position[2]
    y += player_position[0]
    z += player_position[1]
    # set block
    mc.setBlock(x0 + y + offset_y, y0 + z + offset_z, z0 + x + offset_x, block_type_id, block_data)
