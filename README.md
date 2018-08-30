# magicavoxel2mcpi

Python script to connect MagicaVoxel to Minecraft PI.

<img width="1440" alt="screenshot_1122" src="https://user-images.githubusercontent.com/33368327/44855279-ab667500-aca5-11e8-8320-a025afcab091.png">

Reqire: Minecraft Pi (Rasppberry Pi) or  
        Minecraft (JAVA EDITION) + Forge + RaspberryJamMod
        
Create a voxel-model with MagicaVoxel and export ply (polygon filr format).

Download python-scripts.zip from    
https://github.com/arpruss/raspberryjammod/releases

Unzip python-scripts.zip and create an mcpipy folder

Move files as  
mcpipy/  
    ├ mcpi/  
    │    ├ block.py  
    │    └ minecraft.py  
    ├ magicavoxel2mcpi.py  
    └ xxx.ply

Terminal

```
cd xxx/mcpipy
python magicavoxel2mcpi.py
```

## Rotation model:   
alpha (x-rotaion degree)  
beta (y-rotaion degree)   
gamma (z-rotaion degree)    
Note: It is the coordinate axis of MagicaVoxel not Minecraft.  

![magicavoxel2mcpi_rotaion](https://user-images.githubusercontent.com/33368327/44855928-1a909900-aca7-11e8-9182-99df906f43be.jpg)

## Animation:  
Create a few voxel-model and edit   

```
magicavoxel2mcpi_animation.py
plys = ['xxx1.ply', 'xxx2.ply', 'xxx3.ply',...]
```

Terminal

```
python magicavoxel2mcpi_animation.py
```

<img width="1440" alt="screenshot_1125" src="https://user-images.githubusercontent.com/33368327/44855949-28deb500-aca7-11e8-9145-c3ae320ff334.png">



