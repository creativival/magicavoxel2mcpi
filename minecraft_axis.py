#!/usr/bin/env python

#
# Coordinate axis of MagicaVoxel
#

import mcpi.minecraft as minecraft
import mcpi.block as block
import math
from time import sleep

# Origin to create
x0 = 0
y0 = 0
z0 = 0

# Block ID (default = 35:0 = White Wool)
blockTypeId = 35

mc = minecraft.Minecraft.create()
mc.postToChat('create minecraft axis')

for i in range(30):
    # x-axis
    mc.setBlock(x0 + i, y0, z0, blockTypeId, 14)  # red wool
    # y-axis
    mc.setBlock(x0, y0 + i, z0, blockTypeId, 13)  # green wool
    # z-axis
    mc.setBlock(x0, y0, z0 + i, blockTypeId, 11)  # blue wool
