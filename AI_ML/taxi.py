import time

import gym
import numpy as np

env = gym.make('Taxi-v3' , render_mode="human")
print()

alpha = 0.5  
gamma = 0.99  
epsilon = 0.01  
max_epsilon = 1.0 
min_epsilon = 0.01  
decay_rate = 0.9  

counter = 0

num_states = env.observation_space.n
num_actions = env.action_space.n
Q = np.load(file="Q_table.npy")

num_episodes = 1000000
max_steps_per_episode = 30

for episode in range(num_episodes):
    counter = counter + 1

    """if(counter %1000 == 0):
        np.save(file="Q_table.npy" ,arr=Q)"""


    state = env.reset()[0]

    for step in range(max_steps_per_episode):

        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state, :])

        new_state, reward, done, _, info = env.step(action)

        Q[state, action] = Q[state, action] + alpha * (reward + gamma * np.max(Q[new_state, :]) - Q[state, action])

        state = new_state

        if done:
            break

    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)
    print("Epsilon:",epsilon , "Episode :" , episode , "Reward :",reward)

print()

total_reward = 0
num_eval_episodes = 100
max_eval_steps_per_episode = 1000

for episode in range(num_eval_episodes):
    state = env.reset()

    for step in range(max_eval_steps_per_episode):
        action = np.argmax(Q[state, :])
        state, reward, done, info = env.step(action)
        total_reward += reward

        if done:
            break

mean_reward = total_reward / num_eval_episodes
print(f"Mean reward: {mean_reward:.2f}")
