# magicavoxel2mcpi

Python script to connect MagicaVoxel to Minecraft PI.

<img width="1440" alt="screenshot_1122" src="https://user-images.githubusercontent.com/33368327/44855279-ab667500-aca5-11e8-8320-a025afcab091.png">

Reqire: Minecraft Pi (Rasppberry Pi) or  
        Minecraft (JAVA EDITION) + Forge + RaspberryJamMod
        
Create a voxel-model with MagicaVoxel and export "ply" (polygon file format).

Download python-scripts.zip from    
https://github.com/arpruss/raspberryjammod/releases

Unzip python-scripts.zip and you will get an "mcpipy" folder

Download "magicavoxel2mcpi-master.zip" and Unzip

Move all ".py" and ".ply" files into "mcpipy" folder

mcpipy/  
    ├ mcpi/  
    │    ├ block.py  
    │    └ minecraft.py  
    ├ magicavoxel2mcpi.py  
    ├ xxx.ply    
    ├ ...    
    ├ ...    
    
Terminal command    

```
cd xxx/mcpipy
python magicavoxel2mcpi.py
```

## Colors
There are 10 colors to reproduce. When create, you need to use only 8 colors     
Black(0, 0, 0) White (255, 255, 255) Red(255, 0, 0) lime(0, 255, 0) Blue(0,0,255) Yellow(255, 255 0) Cyan(0, 255, 255) Magenta(255, 0, 255) Orange(255,165,0) Green(0,80,0)     

## Rotation:   
alpha (x-rotation degree)  
beta (y-rotation degree)   
gamma (z-rotation degree)    
Note: It is the coordinate axis of MagicaVoxel not Minecraft.  

![magicavoxel2mcpi_rotaion](https://user-images.githubusercontent.com/33368327/44855928-1a909900-aca7-11e8-9182-99df906f43be.jpg)

## Animation:  
Create a few voxel-model and export "ply" and move ".ply" files into "mcpipy" folder

Edit magicavoxel2mcpi_animation.py     

```
magicavoxel2mcpi_animation.py
ply_files = ['xxx1.ply', 'xxx2.ply', 'xxx3.ply',...]
```

Terminal command     

```
python magicavoxel2mcpi_animation.py
```

![w6zcgpvpav9c3iza](https://user-images.githubusercontent.com/33368327/44870045-05793180-acca-11e8-8d97-84c9c7cde7c2.gif)

## Rotating Animation

Divide the rotating parts, Create a voxel-model and export "ply" and move ".ply" files into "mcpipy" folder    

Edit magicavoxel2mcpi_rotation_robot.py or rotation_drone.py    

Terminal command     

```
python magicavoxel2mcpi_rotation_robot.py
```


![5bbdsr7pmh3g5fcp](https://user-images.githubusercontent.com/33368327/44958372-48314880-af1a-11e8-94f7-c198547c6eba.gif)

## Walking Cat

Create and separate body and limb. Export "ply" and move ".ply" files into "mcpipy" folder    

Edit magicavoxel2mcpi_walking_cat.py    

Terminal command     

```
python magicavoxel2mcpi_walking_cat.py
```

![z-ew2x_n_dmwhkfi](https://user-images.githubusercontent.com/33368327/45431860-77e30c00-b6e3-11e8-9c9b-9ef99bb9fdbe.gif)




