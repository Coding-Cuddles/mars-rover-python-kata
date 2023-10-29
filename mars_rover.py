from dataclasses import dataclass


@dataclass
class Location:
    x: int
    y: int
    orientation: str


class MarsRover:

    def __init__(self, location: Location):
        self.location = location

    def move(self, commands: str):
        pass
