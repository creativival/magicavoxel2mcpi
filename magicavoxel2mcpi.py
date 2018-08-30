#!/usr/bin/env python

#
# MagicaVoxel2MinecraftPi
#

import mcpi.minecraft as minecraft
import mcpi.block as block
import server
import math
from time import sleep

# polygon file format from MagicaVoxel
ply = 'chick.ply'

# Origin to create
x0 = 0
y0 = 0
z0 = 0

# Rotation degree
alpha = 0 # x-axis
beta  = 0 # y-axis
gamma = 0 # z-axis

# Block ID (defalut = 35:0 = White Wool)
blockTypeId = 35
blockData = 0

mc = minecraft.Minecraft.create(server.address)

def create_voxel(ply):
    mc.postToChat('create polygon file format model')

    def setblock(x, y, z):
        # x-rotation degree alpha
        xx = x
        yx = (y * math.cos(math.radians(alpha)) - z * math.sin(math.radians(alpha)))
        zx = (y * math.sin(math.radians(alpha)) + z * math.cos(math.radians(alpha)))
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
        mc.setBlock(x0 + y, y0 + z, z0 + x, blockTypeId, blockData)

    polygon_data = open(ply, "r") # open .ply file

    lines = polygon_data.readlines()

    element_face = lines[11].split()

    for i in range(0, int(element_face[2])): # number of element face
        vertex1 = lines[4 * i + 14].split()
        vertex2 = lines[4 * i + 15].split()
        vertex3 = lines[4 * i + 16].split()
        # block color
        if vertex1[3] == '0':
            if vertex1[4] == '0':
                if vertex1[5] == '0':
                    blockData = 15
                else:
                    blockData = 5
            else:
                if vertex1[5] == '0':
                    blockData = 13
                else:
                    blockData = 9
        else:
            if vertex1[4] == '0':
                if vertex1[5] == '0':
                    blockData = 14
                else:
                    blockData = 2
            else:
                if vertex1[5] == '0':
                    blockData = 4
                else:
                    blockData = 0
        # position to set block
        if vertex1[0] == vertex2[0] and vertex2[0] == vertex3[0]:#y-z plane
            y = min(int(vertex1[1]), int(vertex2[1]), int(vertex3[1]))
            z = min(int(vertex1[2]), int(vertex2[2]), int(vertex3[2]))
            if vertex1[1] == vertex2[1]:
                x = int(vertex1[0])
            else:
                x = int(vertex1[0]) - 1
        elif vertex1[1] == vertex2[1] and vertex2[1] == vertex3[1]:#z-x plane
            z = min(int(vertex1[2]), int(vertex2[2]), int(vertex3[2]))
            x = min(int(vertex1[0]), int(vertex2[0]), int(vertex3[0]))
            if vertex1[2] == vertex2[2]:
                y = int(vertex1[1])
            else:
                y = int(vertex1[1]) - 1
        else:#x-y plane
            x = min(int(vertex1[0]), int(vertex2[0]), int(vertex3[0]))
            y = min(int(vertex1[1]), int(vertex2[1]), int(vertex3[1]))
            if vertex1[0] == vertex2[0]:
                z = int(vertex1[2])
            else:
                z = int(vertex1[2]) - 1
        setblock(x, y, z)

create_voxel(ply)
