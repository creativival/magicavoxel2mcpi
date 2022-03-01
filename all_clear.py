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
SIZE = 200

mc = minecraft.Minecraft.create()
mc.postToChat('all clear')
mc.setBlocks(-SIZE / 2, 0, -SIZE / 2, SIZE / 2, SIZE / 2, SIZE / 2, 0)
mc.setBlocks(-SIZE / 2, -1, -SIZE / 2, SIZE / 2, -1, SIZE / 2, 2)
