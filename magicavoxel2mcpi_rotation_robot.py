#!/usr/bin/env python

#
# MagicaVoxel2MinecraftPi
#

import mcpi.minecraft as minecraft
import mcpi.block as block
import math
from time import sleep

# polygon file format exported from MagicaVoxel
plys = ['robot-body.ply', 'robot-head.ply', 'robot-hands.ply', 'robot-propeller.ply']

lines_list = []

for i in range(len(plys)):
    polygon_data = open(plys[i], "r") # open .ply file
    lines_list.append(polygon_data.readlines())

# reset_stop
reset_stop = 0.01

# create_stop
create_stop  = 0.5

# repeat repeat_count
repeat = 1000

# Origin to create (Minecraft)
x0 = 20
y0 = 0
z0 = 0

# Model size
is_even = True

# Rotation degree (MagicaVoxel)
alpha = 0 # x-axis
beta  = 0 # y-axis
gamma = 0 # z-axis

# Offset for rotation(MagicaVoxel)
offset_x = 0 # x-axis
offset_y = 0 # y-axis
offset_z = 7 # z-axis

# Block ID (default = 35:0 = White Wool)
blockTypeId = 35
blockData = 0

mc = minecraft.Minecraft.create()

def reset(x1, y1, z1, x2, y2, z2):
    #mc.postToChat('reset the world')
    mc.setBlocks(x1 + x0, y1 + y0, z1 + z0, x2 + x0, y2 + y0, z2 + z0, 0, 0)

def create_voxel(lines):
    #mc.postToChat('create polygon file format model')

    def setblock(x, y, z):
        if is_even:
            # x-rotation degree alpha
            xx = x - offset_x + 0.5
            yx = ((y - offset_y + 0.5) * math.cos(math.radians(alpha)) - (z - offset_z + 0.5) * math.sin(math.radians(alpha)))
            zx = ((y - offset_y + 0.5) * math.sin(math.radians(alpha)) + (z - offset_z + 0.5) * math.cos(math.radians(alpha)))
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
            # set block
            mc.setBlock(x0 + y + offset_y, y0 + z + offset_z, z0 + x + offset_x, blockTypeId, blockData)
        else: # odd
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
            # set block
            mc.setBlock(x0 + y + 0.5 + offset_y, y0 + z + 0.5 + offset_z, z0 + x + 0.5 + offset_x, blockTypeId, blockData)

    element_face = lines[11].split()

    for i in range(0, int(element_face[2])): # number of element face
        vertex1 = lines[4 * i + 14].split()
        vertex2 = lines[4 * i + 15].split()
        vertex3 = lines[4 * i + 16].split()
        # block color
        if vertex1[3] == '0':
            if vertex1[4] == '0':
                if vertex1[5] == '0':
                    blockData = 15 # black 0,0,0
                else:
                    blockData = 11 # blue 0,0,255
            elif vertex1[4] == '80':
                if vertex1[5] == '0':
                    blockData = 13 # green 0,80,0
                else:
                    blockData = 0 # white(default) 0,80,x
            else:
                if vertex1[5] == '0':
                    blockData = 5 # lime 0,255,0
                else:
                    blockData = 9 # cyan 0,255,255
        else:
            if vertex1[4] == '0':
                if vertex1[5] == '0':
                    blockData = 14 # red 255,0,0
                else:
                    blockData = 2 # magenta 255,0,255
            elif vertex1[4] == '165':
                if vertex1[5] == '0':
                    blockData = 1 # orange 255,165,0
                else:
                    blockData = 0 # white(default) 255,165,x
            else:
                if vertex1[5] == '0':
                    blockData = 4 # yellow 255,255,0
                else:
                    blockData = 0 # white(default) x,x,x
        # position to set block
        if vertex1[0] == vertex2[0] and vertex2[0] == vertex3[0]:#y-z plane
            y = min(float(vertex1[1]), float(vertex2[1]), float(vertex3[1]))
            z = min(float(vertex1[2]), float(vertex2[2]), float(vertex3[2]))
            if vertex1[1] == vertex2[1]:
                x = float(vertex1[0])
            else:
                x = float(vertex1[0]) - 1
        elif vertex1[1] == vertex2[1] and vertex2[1] == vertex3[1]:#z-x plane
            z = min(float(vertex1[2]), float(vertex2[2]), float(vertex3[2]))
            x = min(float(vertex1[0]), float(vertex2[0]), float(vertex3[0]))
            if vertex1[2] == vertex2[2]:
                y = float(vertex1[1])
            else:
                y = float(vertex1[1]) - 1
        else:#x-y plane
            x = min(float(vertex1[0]), float(vertex2[0]), float(vertex3[0]))
            y = min(float(vertex1[1]), float(vertex2[1]), float(vertex3[1]))
            if vertex1[0] == vertex2[0]:
                z = float(vertex1[2])
            else:
                z = float(vertex1[2]) - 1
        setblock(x, y, z)

for i in range(len(lines_list)):
    create_voxel(lines_list[i])
    
sleep(5)

for i in range(repeat):
    reset(-5, 9, -5, 5, 15, 5)
    reset(-8, 0, -7, 7, 14, -5)
    reset(-7, 0, 4, 7, 14, 7)
    reset(-6, 3, -4, -4, 11, 4)
    sleep(reset_stop)
    alpha = 0
    beta = 0
    gamma = 6 * i
    create_voxel(lines_list[1])
    alpha = 6 * i
    beta = 0
    gamma = 0
    create_voxel(lines_list[2])
    alpha = 0
    beta = 6 * i
    gamma = 0
    create_voxel(lines_list[3])
    if (6 * i) % 90 == 0:
        sleep (2 * create_stop)
    else:
        sleep(create_stop)
        