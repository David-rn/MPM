import cv2
import numpy as np
import os


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

    
positions = None

with open('prueba.txt', 'r') as state_file:
    positions = state_file.readlines()

cells = []
frames = []

for pos in positions:
    items = pos.split(' ')
    cells.append(Cell(items[0], items[1], items[2], items[3]))
    frames.append(items[0])

frames = list(np.unique(frames))
frames.sort(key=int)

dataset_path = "./images/"
images = [name for name in os.listdir(dataset_path)]
images = sorted(images)

if len(frames) != len(images):
    print("NOT THE SAME LENGTH")

for frame, image in enumerate(images, 0):
    img = cv2.imread(dataset_path+image, cv2.IMREAD_COLOR)
    frame_cells = [c for c in cells if int(c.get_frame()) == frame] 
    for cell in frame_cells:
        img = cv2.circle(img, (cell.get_x(), cell.get_y()), radius=5, color=(0, 0, 255), thickness=-1)

    cv2.imshow("Cells", img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
