import gym
import itertools
import numpy as np
import random
random.seed(10)
np.random.seed(10)
env = gym.make('FrozenLake-v0')


def epsilonGreedyPolicy(state, Q, epsilon):
    """  ******** Complete the function *****************
    Implement epsilon-greedy policy

    :param state: current state
    :param Q: numpy ndarray,
        Q-table
    :param epsilon:
    :return: int,
        return an action based on the policy
    """
    if random.random() > epsilon:
        return np.argmax(Q[state, :])  # exploit action with max Q value
    else:
        return env.action_space.sample() # explore different random action


def qLearning(env, num_episodes, discount_factor=0.95, alpha=0.6, epsilon=1):
    """ Implements Q-Learning

    :param env: an instance of gym env
    :param num_episodes: int,
        number of episodes
    :param discount_factor: float,
        discount factor as in the lecture slides
    :param alpha: float,
        learning rate
    :param epsilon: float,
        epsilon-greedy strategy
    :return:
    """
    print(env.observation_space.n, env.action_space.n)
    Q_table = np.zeros([env.observation_space.n, env.action_space.n])
    total_reward = []
    for i in range(num_episodes):
        state = env.reset()
        episodic_reward = 0
        for j in itertools.count():
            action = epsilonGreedyPolicy(state, Q_table, epsilon) # #action chosen by epsilon-greedy
            next_state, reward, done, _ = env.step(action)  ##observe reward and state
            Q_table[state, action] = Q_table[state, action] + alpha * (reward + discount_factor * np.max(Q_table[next_state, :]) - Q_table[state, action])
            episodic_reward += reward
            state = next_state
            if done:
                break
        total_reward.append(episodic_reward)
    return Q_table, total_reward

Q_table, rewards = qLearning(env, 1000)
print(Q_table)
#print(len(Q_table))
#print(rewards)
