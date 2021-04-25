from PIL import Image
import numpy as np
from cell import Cell
import argparse

def main(args):
    image_size = (int(args['image_width']), int(args['image_height']))
    positions = None
    cells = []
    frames = []
    pad = int(args['padding'])

    # reads input file containing [frame cell_id x y parent_id]
    with open(args['input_file'], 'r') as input_file:
        positions = input_file.readlines()

    for pos in positions:
        items = pos.split(' ')
        # Save only frame, id, x, y
        cells.append(Cell(items[0], items[1], items[2], items[3]))
        frames.append(items[0])

    frames = np.unique(frames)

    for frame in frames:
        # Select cells from each frame
        frame_cells = [c for c in cells if c.get_frame() == frame]
        mask = np.zeros(image_size)
        for cell in frame_cells:
            mask[cell.get_x()-pad:cell.get_x()+pad, cell.get_y()-pad:cell.get_y()+pad] = cell.get_id()
        
        im = Image.fromarray(mask)
        image_name = ""
        # TODO: Improve this nasty if else
        if len(frame) == 1:
            image_name = args['output_directory'] + "/mask00" + str(frame) + ".tif"
        elif len(frame) == 2:
            image_name = args['output_directory'] + "/mask0" + str(frame) + ".tif"
        else:
            image_name = args['output_directory'] + "/mask" + str(frame) + ".tif"
        
        im.save(image_name)
        print("image_saved: ", frame)

if __name__ == '__main__':
    '''
        Example of usage: python create_tiff.py -o dataset_name -i tracking.states -he 512 -w 512 -p 10
    '''
    
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output_directory", required=True)
    ap.add_argument("-i", "--input_file", required=True)
    ap.add_argument("-w", "--image_width", required=True)
    ap.add_argument("-he", "--image_height", required=True)
    ap.add_argument("-p", "--padding", required=True)
    args = vars(ap.parse_args())

    main(args)