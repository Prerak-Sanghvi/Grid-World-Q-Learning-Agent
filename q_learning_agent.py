import numpy as np

class QLearningAgent:
    def __init__(self, env, alpha=0.1, gamma=0.99, epsilon=1.0, epsilon_decay=0.995, min_epsilon=0.01):
        self.env = env
        self.q_table = np.zeros((env.size[0], env.size[1], env.get_action_space()))
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = min_epsilon

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.choice(4)
        x, y = state
        return np.argmax(self.q_table[x, y])

    def learn(self, state, action, reward, next_state):
        x, y = state
        nx, ny = next_state
        predict = self.q_table[x, y, action]
        target = reward + self.gamma * np.max(self.q_table[nx, ny])
        self.q_table[x, y, action] += self.alpha * (target - predict)

    def update_epsilon(self):
        self.epsilon = max(self.epsilon * self.epsilon_decay, self.min_epsilon)
