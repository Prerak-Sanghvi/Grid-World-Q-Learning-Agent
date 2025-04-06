This project is a simple yet powerful demonstration of **Reinforcement Learning** using the **Q-Learning** algorithm in a custom **GridWorld environment**. The goal was to teach an agent how to reach a target position from a starting point while avoiding obstacles and minimizing the number of steps taken.

## Project Objectives

- Implement the Q-Learning algorithm from scratch
- Design a custom GridWorld environment with obstacles and rewards
- Train the agent to learn the optimal policy using epsilon-greedy exploration
- Visualize the learning process using reward and step trends
- Display the final learned path taken by the agent

- ## How It Works

The GridWorld is a 10x10 grid where:
- `S` is the start position
- `G` is the goal position
- `#` are obstacles
- `→, ↓, ←, ↑` represent the agent’s final optimal path

- ### Q-Learning Highlights:
- Uses **Q-Table** to store and update action values
- Applies **Epsilon-Greedy** strategy to balance exploration and exploitation
- Updates Q-values using the Bellman Equation:

- Q(state, action) = Q(state, action) + alpha * (reward + gamma * max(Q(next_state)) - Q(state, action))
