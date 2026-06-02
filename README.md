# Manhattan Distance Heightmap Generator

A python heightmap generator based on manhattan distance. 

The program creates a zero matrix of height*width, then randomly generates centres which have an initial height (cap). The values spread out from these centres until they reach 0. Overlapping values are added together, creating the terrain.

<p float="left">
  <img src="images/single.png" width="45%" />
  <img src="images/double.png" width="45%" />
</p>

*(Note: Change image1.png and image2.png to match your actual filenames in the /images folder)*

## Features
* Colours can be edited in coloursettings.py
* Includes a crude terminal interface to create maps, smoothen them, or colour them.
* Can be run directly or imported as a module.

## How to use

To start the terminal interface:
```bash
python3 main.py
```
