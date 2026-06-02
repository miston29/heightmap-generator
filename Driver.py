import numpy as np
from tqdm import tqdm
from PIL import Image
from coloursettings import colours
Image.MAX_IMAGE_PIXELS = None


class Wave:
    def __init__(self, height, width, cap, smoothval=5, savename=None):
        self.height = height
        self.width = width
        self.cap = cap
        self.savename = savename if savename is not None else "".join(np.random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 8))
        self.smoothval = smoothval

    def create(self):
        map = self.heightmap()
        print(f"heightmap created and saved as {self.savename}.png")
        smooth = self.heightmap_smoothner(map)
        print(f"heightmap edges poslished, smoothness value : {self.smoothval}")
        self.heightmap_colour(smooth)
        print(f"heoghtmap coloured and saved files as : {self.savename}c.png")

    def heightmap(self):
        num_cores = 1 + int(np.sqrt(self.height * self.width) // 2) 

        cores_y = np.random.randint(0, self.height, size=num_cores)
        cores_x = np.random.randint(0, self.width, size=num_cores)

        matrix = np.zeros((self.height, self.width), dtype=np.float32) 

        matrix[cores_y, cores_x] = self.cap

        k_size = 2 * self.cap + 1
        y_indices, x_indices = np.ogrid[-self.cap:self.cap+1, -self.cap:self.cap+1]
        kernel = self.cap - (np.abs(y_indices) + np.abs(x_indices))
        kernel[kernel < 0] = 0  

        for cy, cx in tqdm(zip(cores_y, cores_x), total=num_cores, desc="Processing cores"):
            y_min, y_max = cy - self.cap, cy + self.cap + 1
            x_min, x_max = cx - self.cap, cx + self.cap + 1
            
            for i, (y_start, y_end) in enumerate([(y_min, y_max)]):
                y_idx = np.arange(y_min, y_max) % self.height
                x_idx = np.arange(x_min, x_max) % self.width
                
                matrix[y_idx[:, None], x_idx] += kernel
    

        matmin = matrix.min()
        matmax = matrix.max()

        normalized = (matrix - matmin)/(matmax - matmin)
        scaled = normalized*255

        Image.fromarray(scaled.astype(np.uint8)).save(f"{self.savename}.png")

        return scaled

    def heightmap_smoothner(self, matrix=None,openfile=None):
        if openfile is None and matrix is None:
            print("both files can't be None, provide any one")
            return
        
        elif matrix is None:
            matrix = np.asarray(Image.open(openfile))

        kernel = np.ones((self.smoothval, self.smoothval), dtype=np.float32) / (self.smoothval ** 2)
        nmat = np.fft.ifft2(np.fft.fft2(matrix) * np.fft.fft2(kernel, matrix.shape)).real

        
        if openfile is not None:
            openfile = openfile.split(".")[0] + f"_{self.smoothval}.png"
            Image.fromarray(nmat.astype(np.uint8)).save(openfile)

            self.heightmap_colour(matrix=None, openfile=openfile)
        else:
            return nmat

    def heightmap_colour(self, matrix=None, openfile=None):
        if openfile is None and matrix is None:
            print("both files can't be None, provide any one")
            return
        
        elif matrix is None:
            matrix = np.asarray(Image.open(openfile))
            coloured = np.zeros((len(matrix), len(matrix[0]), 3), dtype=np.uint8)

        else:
            coloured = np.zeros((self.height, self.width, 3), dtype=np.uint8)


        coloured[matrix <= colours[0][1]] = colours[0][2]
        for low, high, rgb in colours[1:]:
            coloured[(matrix > low)  & (matrix <= high)]  = rgb 


    
        image = Image.fromarray(coloured)
        if openfile is None:
            image.save(f"{self.savename}c.png")

        else:
            image.save(openfile.split(".")[0] + "_new_colour.png")

