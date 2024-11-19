import pygame

class TileKind:
    def __init__(self, name, image, is_solid):
        self.name = name
        self.image = pygame.image.load(image)
        self.is_solid = is_solid

class Map:
    def __init__(self, map_file, tile_kinds, tile_size):
        self.tile_kinds = tile_kinds
        self.tile_size = tile_size
        self.load_map(map_file)

    def load_map(self, map_file):
        # Load the data from the map file
        with open(map_file, "r") as file:
            data = file.read()

        # Set up the tiles from the loaded data
        self.tiles = []
        for line in data.split("\n"):
            row = [int(tile) for tile in line if tile.isdigit()]
            self.tiles.append(row)

    def draw(self, screen):
        # Go row by row
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                if tile < len(self.tile_kinds):
                    location = (x * self.tile_size, y * self.tile_size)
                    image = self.tile_kinds[tile].image
                    screen.blit(image, location)
