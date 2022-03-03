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


def reset_area(x1, y1, z1, x2, y2, z2):
    mc.setBlocks(x1, y1, z1, x2, y2, z2, 0)


def create_voxel(box_positions, model_settings):
    for bp in box_positions:
        x = math.ceil(bp[0])
        y = math.ceil(bp[1])
        z = math.ceil(bp[2])
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


def ply_to_positions(ply_file):
    # PLY よりボックスの座標を読み込む
    block_type_id = 35
    box_positions = set()
    with open('data/' + ply_file, 'r') as f:
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
            if [r, g, b] == [255, 255, 255]:  # white
                block_data = 0
            elif [r, g, b] == [255, 127, 0] or [r, g, b] == [255, 165, 0]:  # orange
                block_data = 1
            elif [r, g, b] == [255, 0, 255]:  # magenta
                block_data = 2
            elif [r, g, b] == [127, 127, 255]:  # lightblue
                block_data = 3
            elif [r, g, b] == [255, 255, 0]:  # yellow
                block_data = 4
            elif [r, g, b] == [0, 255, 0]:  # lime
                block_data = 5
            elif [r, g, b] == [255, 127, 127]:  # pink
                block_data = 6
            elif [r, g, b] == [127, 127, 127]:  # gray
                block_data = 7
            elif [r, g, b] == [191, 191, 191]:  # lightgray
                block_data = 8
            elif [r, g, b] == [0, 255, 255]:  # cyan
                block_data = 9
            elif [r, g, b] == [127, 0, 127]:  # purple
                block_data = 10
            elif [r, g, b] == [0, 0, 255]:  # blue
                block_data = 11
            elif [r, g, b] == [127, 0, 0]:  # brown
                block_data = 12
            elif [r, g, b] == [0, 127, 0] or [r, g, b] == [0, 80, 0]:  # green
                block_data = 13
            elif [r, g, b] == [255, 0, 0]:  # red
                block_data = 14
            elif [r, g, b] == [0, 0, 0]:  # black
                block_data = 15
            else:  # default (white)
                block_data = 0

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
            position_x = round(x * 10.0 / step) / 10.0
            position_y = round(y * 10.0 / step) / 10.0
            position_z = round(z * 10.0 / step) / 10.0
            box_positions.add(
                (
                    position_x,
                    position_y,
                    position_z,
                    block_type_id,
                    block_data
                )
            )

        # sort
        box_positions = list(box_positions)
        box_positions.sort(key=lambda x: x[2])
        # print(box_positions)

        # centering
        max_x = max([bp[0] for bp in box_positions])
        min_x = min([bp[0] for bp in box_positions])
        average_x = int((max_x + min_x) * 5) / 10.0
        max_y = max([bp[1] for bp in box_positions])
        min_y = min([bp[1] for bp in box_positions])
        average_y = int((max_y + min_y) * 5) / 10.0
        centering_box_positions = []
        for bp in box_positions:
            x = round((bp[0] - average_x) * 10) / 10.0
            y = round((bp[1] - average_y) * 10) / 10.0
            centering_box_positions.append(
                (
                    x,
                    y,
                    bp[2],
                    bp[3],
                    bp[4],
                 )
            )
        # print(centering_box_positions)

        return centering_box_positions


def set_block(x, y, z, block_type_id, block_data, model_settings):
    x0 = model_settings['x0']
    y0 = model_settings['y0']
    z0 = model_settings['z0']
    alpha = model_settings['alpha']
    beta = model_settings['beta']
    gamma = model_settings['gamma']
    offset_x = model_settings['offset_x'] if 'offset_x' in model_settings else 0
    offset_y = model_settings['offset_y'] if 'offset_y' in model_settings else 0
    offset_z = model_settings['offset_z'] if 'offset_z' in model_settings else 0

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
    position_x = yz + offset_y
    position_y = zz + offset_z
    position_z = xz + offset_x
    if position_x > 0:
        position_x = int(position_x + 0.0001)
    else:
        position_x = int(position_x - 0.0001)
    if position_y > 0:
        position_y = int(position_y + 0.0001)
    else:
        position_y = int(position_y - 0.0001)
    if position_z > 0:
        position_z = int(position_z + 0.0001)
    else:
        position_z = int(position_z - 0.0001)
    # set block
    mc.setBlock(
        x0 + position_x,
        y0 + position_y,
        z0 + position_z,
        block_type_id,
        block_data
    )
