#!/usr/bin/env python3
import numpy as np
from PIL import Image
from subprocess import run
from time import time

height, width = 2160,3840
matrix = np.zeros((height, width), dtype=np.float32) 

cap = np.random.randint(300,900)
num_cores = 1 + int(np.sqrt(height * width) // 2) 

cores_y = np.random.randint(0, height, size=num_cores)
cores_x = np.random.randint(0, width, size=num_cores)
matrix[cores_y, cores_x] = cap

k_size = 2 * cap + 1
y_indices, x_indices = np.ogrid[-cap:cap+1, -cap:cap+1]
kernel = cap - (np.abs(y_indices) + np.abs(x_indices))
kernel[kernel < 0] = 0  

for cy, cx in zip(cores_y, cores_x):
    y_min, y_max = cy - cap, cy + cap + 1
    x_min, x_max = cx - cap, cx + cap + 1
    
    for i, (y_start, y_end) in enumerate([(y_min, y_max)]):
        y_idx = np.arange(y_min, y_max) % height
        x_idx = np.arange(x_min, x_max) % width
        
        matrix[y_idx[:, None], x_idx] += kernel


matmin = matrix.min()
matmax = matrix.max()

normalized = (matrix - matmin)/(matmax - matmin)

scaled = normalized*255

def smooth(matrix, smoothval):
    kernel = np.ones((smoothval, smoothval), dtype=np.float32) / (smoothval ** 2)
    return np.fft.ifft2(np.fft.fft2(matrix) * np.fft.fft2(kernel, matrix.shape)).real

scaled = smooth(scaled, np.random.randint(10,51))

coloured = np.zeros((height, width, 3), dtype=np.uint8)

coloured[scaled <= 16]  = [0, 0, 102]    # Deep Ocean
coloured[(scaled > 16)  & (scaled <= 70)]  = [0, 102, 204]  # Ocean
coloured[(scaled > 70)  & (scaled <= 85)]  = [102, 178, 255]# Shore 

coloured[(scaled > 85)  & (scaled <= 100)]  = [230, 204, 153]# Sand 

coloured[(scaled > 100)  & (scaled <= 120)] = [112, 219, 112]# Grass 
coloured[(scaled > 120) & (scaled <= 160)] = [34, 139, 34]  # Forest 
coloured[(scaled > 160) & (scaled <= 180)] = [25, 77, 51]   # Taiga perhaps

coloured[(scaled > 180) & (scaled <= 220)] = [128, 128, 128] # Stone
coloured[scaled > 220] = [240, 248, 255] # Snow



SAVEPATH = "/home/rawat/Pictures"

run(f"rm {SAVEPATH}/tempwall_*.png", shell=True)

image = Image.fromarray(coloured)
name = f"tempwall_{int(time())}"
image.save(f"{SAVEPATH}/{name}.png")

run(["plasma-apply-wallpaperimage", f"{SAVEPATH}/{name}.png"])
