import torch
import random
import numpy as np
from collections import deque
from imagecurl import Image

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    def setup(self):
        self.game = Image().getImage()

    def get_state(self):
        self.game.show()

    def get_action(self):
        pass

    def remember(self):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self):
        pass

def train():
    a = Agent()
    a.setup()
    a.get_state()

if __name__ == '__main__':
    train()