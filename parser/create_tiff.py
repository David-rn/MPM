from PIL import Image
import numpy as np 

class Cell:
    def __init__(self, frame, id, x, y):
        super().__init__()
        self.id = id
        self.frame = frame
        self.x = int(x)
        self.y = int(y)

    def get_id(self):
        return self.id

    def get_frame(self):
        return self.frame
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

image_size = (512, 512)
positions = None

with open('prueba.txt', 'r') as state_file:
    positions = state_file.readlines()

cells = []
frames = []

for pos in positions:
    items = pos.split(' ')
    cells.append(Cell(items[0], items[1], items[2], items[3]))
    frames.append(items[0])

frames = np.unique(frames)

for frame in frames:
    # Select cells from each frame
    frame_cells = [c for c in cells if c.get_frame() == frame]
    mask = np.zeros(image_size)
    for cell in frame_cells:
        mask[cell.get_x()-7:cell.get_x()+7, cell.get_y()-7:cell.get_y()+7] = cell.get_id()
    
    im = Image.fromarray(mask)
    image_name = ""
    if len(frame) == 1:
        image_name = "prueba_tif/mask00" + str(frame) + ".tif"
    else:
        image_name = "prueba_tif/mask0" + str(frame) + ".tif"
    
    im.save(image_name)
    print("image_saved: ", frame)    