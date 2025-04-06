import numpy as np

class GridWorld:
    def __init__(self, size=(10, 10), start=(0, 0), goal=(9, 9), obstacles=None):
        self.size = size
        self.start = start
        self.goal = goal
        self.obstacles = obstacles or []
        self.reset()

    def reset(self):
        self.agent_pos = self.start
        return self.agent_pos

    def step(self, action):
        x, y = self.agent_pos
        if action == 0: y = max(0, y - 1)      # up
        elif action == 1: y = min(self.size[1] - 1, y + 1)  # down
        elif action == 2: x = max(0, x - 1)      # left
        elif action == 3: x = min(self.size[0] - 1, x + 1)  # right

        next_pos = (x, y)
        if next_pos in self.obstacles:
            next_pos = self.agent_pos  # hit wall

        self.agent_pos = next_pos

        if self.agent_pos == self.goal:
            return self.agent_pos, 100, True
        elif self.agent_pos in self.obstacles:
            return self.agent_pos, -100, False
        else:
            return self.agent_pos, -1, False

    def get_state_space(self):
        return self.size[0] * self.size[1]

    def get_action_space(self):
        return 4
