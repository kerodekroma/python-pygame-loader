import pygame
import json
import time

class AtlasSpritesheet:
    """
    A single class used to render a png spritesheet file which has a json file as a metadata

    """
    def __init__(self, image_path, json_path, scale=1):
        """
        Parameters:
        -----------
        image_path: str
            The path of the file in png format
        json_path: str
            The path of the file in json format which contains the metadata
        scale: int, optional
            How much to do you want to scale the sprite, by default is 1
        """
        self.spritesheet = pygame.image.load(image_path).convert_alpha()
        self.sprite_datalist = []
        self.current_frame = 0
        self.start_time = time.time()
        self.scale = scale
        with open(json_path) as file:
            self.data = json.load(file)
        file.close()
        self.sprite_datalist = list(self.data['frames'])
    
    def get_width(self):
        """
        Returns:
        -----------
        width
            the width of the sprite from the json file, using the first frame as a reference
        """
        return self.data['frames'][self.sprite_datalist[0]]['frame']['w'] * self.scale

    def get_height(self):
        """
        Returns:
        -----------
        height
            the height of the sprite from the json file, using the first frame as a reference
        """
        return self.data['frames'][self.sprite_datalist[0]]['frame']['h'] * self.scale

    def setup(self, position=(0,0), frame_rate=0, repeat=False):
        """
        Parameters:
        -----------
        position:  tuple, optional
            this param is to define the position of the sprite in the screen, by default (0,0)
        
        frame_rate: int, optional
            this param is to set a custom animation speed, by default is 0, that means that it will take the default speed of the json file data

        repeat: bool, optional
            this param defines if the animation must be shown as a loop or not
        """
        self.position = position
        self.frame_rate = frame_rate
        self.repeat = repeat
        
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width * self.scale, height * self.scale))
        sprite.set_colorkey((0,0,0))
        spritesheet_scaled = pygame.transform.scale(self.spritesheet, (self.spritesheet.get_width() * self.scale, self.spritesheet.get_height() * self.scale))
        sprite.blit(spritesheet_scaled, (0, 0), (x * self.scale, y * self.scale, width * self.scale, height * self.scale))
        return sprite

    def get_frame_rate(self, frame=0):
        if self.frame_rate > 0:
            return self.frame_rate
        return self.data['frames'][self.sprite_datalist[frame]]['duration'] 

    def parse_sprite(self, frame = 0):
        sprite = self.data['frames'][self.sprite_datalist[frame]]['frame']
        x, y, w, h = sprite['x'], sprite['y'], sprite['w'], sprite['h']
        image = self.get_sprite(x, y, w, h)
        return image

    def play(self, screen):
        """
            Parameters:
            -----------
            screen: Surface
                this param is to indicate in which surface the sprite must be shown
        """
        frame_rate = self.get_frame_rate(self.current_frame) 
        diff_time = (time.time() - self.start_time )
        if diff_time >  float(1/frame_rate):
            self.start_time = time.time()
            if self.current_frame < len(self.sprite_datalist):
                self.current_frame += 1
            if self.repeat == False and self.current_frame == len(self.sprite_datalist):
                self.current_frame = len(self.sprite_datalist) - 1
            if self.repeat == True and self.current_frame == len(self.sprite_datalist):
                self.current_frame = 0
        screen.blit(self.parse_sprite(self.current_frame), self.position)