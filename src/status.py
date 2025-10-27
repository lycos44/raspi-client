import json
import logging

logger = logging.getLogger(__name__)

class Status:
    def __init__(self, x):
        self.datetime = x.datetime
        self.direction = x.direction
        self.speed = x.speed
        self.looking = x.looking
        self.distance = x.distance
        self.position = x.position
        self.color = x.color
        self.angle = x.angle
