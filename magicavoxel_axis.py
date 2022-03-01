#!/usr/bin/env python

#
# Coordinate axis of MagicaVoxel
#

import mcpi.minecraft as minecraft

# Origin to create
x0 = 0
y0 = 0
z0 = 0

# Block ID (default = 35:0 = White Wool)
blockTypeId = 35
blockData = 0


def axis():
    mc = minecraft.Minecraft.create()
    mc.postToChat('create magicavoxel axis')

    for i in range(30):
        # x-axis
        mc.setBlock(x0, y0, z0 + i, blockTypeId, 14)  # red wool
        # y-axis
        mc.setBlock(x0 + i, y0, z0, blockTypeId, 13)  # green wool
        # z-axis
        mc.setBlock(x0, y0 + i, z0, blockTypeId, 11)  # blue wool


if __name__ == '__main__':
    axis()
