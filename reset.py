#!/usr/bin/env python

#
# Reset
#

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
mc.postToChat('reset the world')
mc.setBlocks(-100, 0, -100, 100, 63, 100, 0, 0)
mc.setBlocks(-100, -63, -100, 100, -2, 100, 1, 0)
mc.setBlocks(-100, -1, -100, 100, -1, 100, 2, 0)
mc.player.setPos(0, 0, 0)
