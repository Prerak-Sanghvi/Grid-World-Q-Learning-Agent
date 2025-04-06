import matplotlib.pyplot as plt
import numpy as np

def smooth(data, weight=0.9):
    smoothed = []
    last = data[0]
    for point in data:
        smoothed_val = last * weight + (1 - weight) * point
        smoothed.append(smoothed_val)
        last = smoothed_val
    return smoothed

def plot_learning(rewards, steps):
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 2, 1)
    plt.plot(rewards, color='lightblue')
    plt.plot(smooth(rewards), color='orange')
    plt.title("Rewards")
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")

    plt.subplot(1, 2, 2)
    plt.plot(steps, color='lightblue')
    plt.plot(smooth(steps), color='orange')
    plt.title("Steps per Episode")
    plt.xlabel("Episode")
    plt.ylabel("Steps")

    plt.tight_layout()
    plt.show()

def visualize_policy(agent, env):
    policy_grid = np.full(env.size, '', dtype=object)
    arrows = ['↑', '↓', '←', '→']
    for y in range(env.size[1]):
        for x in range(env.size[0]):
            if (x, y) == env.start:
                policy_grid[x, y] = 'S'
            elif (x, y) == env.goal:
                policy_grid[x, y] = 'G'
            elif (x, y) in env.obstacles:
                policy_grid[x, y] = '#'
            else:
                best_action = np.argmax(agent.q_table[x, y])
                policy_grid[x, y] = arrows[best_action]

    for row in policy_grid:
        print(' '.join(row))
