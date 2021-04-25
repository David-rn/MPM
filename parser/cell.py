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