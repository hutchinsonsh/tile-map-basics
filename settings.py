class Settings():
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.grey = (48, 49, 46)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)

        self.w = 1024   # 32 tiles
        self.h = 768    # 24
        self.FPS = 60

        self.title = "Tile Map One"
        self.BGColor = self.grey

        self.tileSize = 32
        self.gridWidth = self.w/self.tileSize
        self.gridHeight = self.h/self.tileSize

        self.playerSpeed = 5
