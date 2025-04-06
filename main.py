from environment import GridWorld
from q_learning_agent import QLearningAgent
from train import train_agent
from visualize import plot_learning, visualize_policy
from config import ENV_CONFIG, AGENT_CONFIG

if __name__ == "__main__":
    env = GridWorld(**ENV_CONFIG)
    agent = QLearningAgent(env, **AGENT_CONFIG)

    rewards, steps = train_agent(env, agent, episodes=1000)
    plot_learning(rewards, steps)
    visualize_policy(agent, env)


