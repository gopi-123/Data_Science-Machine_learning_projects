import gym
import itertools
import numpy as np
import random
random.seed(10)

env = gym.make('FrozenLake-v0')
# https://gym.openai.com/envs/FrozenLake-v0/

def epsilon_Greedy_Policy(state, Q, epsilon):
    """  ******** Complete the function *****************
    Implement epsilon-greedy policy

    :param state: current state
    :param Q: numpy ndarray,
        Q-table
    :param epsilon:
    :return: int,
        return an action based on the policy
    """
    pass


def q_Learning(env, num_episodes, discount_factor=0.95, alpha=0.6, epsilon=0.4):
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
    for i in range(num_episodes):
        # Implement Q-Learning from the lecture slides
        # ******** Complete the function *****************
        pass
    return Q_table

if __name__=='__main__':
    Q_table= q_Learning(env, 1000)
    print(Q_table)
