import numpy as np

def train_agent(env, agent, episodes=1000, max_steps=200):
    rewards = []
    steps_per_episode = []

    for ep in range(episodes):
        state = env.reset()
        total_reward = 0

        for step in range(max_steps):
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.learn(state, action, reward, next_state)
            state = next_state
            total_reward += reward
            if done:
                break

        agent.update_epsilon()
        rewards.append(total_reward)
        steps_per_episode.append(step + 1)

        if (ep + 1) % 100 == 0:
            print(f"Episode {ep+1}: Reward={total_reward}, Steps={step+1}, Epsilon={agent.epsilon:.3f}")

    return rewards, steps_per_episode
