# https://youtu.be/Gq1Azv_B4-4

import gym
import numpy as np

env = gym.make('MountainCar-v0')

LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPISODES = 5000

SHOW_EVERY = 500

DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)  # covered all the space with 20 x 20 = 400 discrete points
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE

# do more random exploration at the beginning and less in the end
epsilon = 0.5
START_EPSILON_DECAYING = 1
END_EPSILON_DECAYING = EPISODES // 2
epsilon_decay_value = epsilon / (END_EPSILON_DECAYING - START_EPSILON_DECAYING)

q_table = np.random.uniform(
    low=-2,  # env reward is -1 or 0, but we initialize table with random range (-2, 0]
    high=0,
    size=(DISCRETE_OS_SIZE + [env.action_space.n])  # number of discrete points x number of actions
)


def get_discrete_state(state):
    """Convert continuous state to discrete"""
    dis_state = (state - env.observation_space.low) / discrete_os_win_size
    return tuple(dis_state.astype(np.int))


for episode in range(EPISODES):

    render = (episode % SHOW_EVERY == 0)
    if render:
        print(episode)

    discrete_state = get_discrete_state(env.reset())

    done = False
    while not done:

        if np.random.random() > epsilon:
            action = np.argmax(q_table[discrete_state])  # select action with the max reword in the table
        else:
            action = np.random.randint(0, env.action_space.n)

        new_state, revard, done, _ = env.step(action)
        new_discrete_state = get_discrete_state(new_state)

        if render:
            env.render()

        if not done:
            max_future_q = np.max(q_table[new_discrete_state])
            current_q = q_table[discrete_state + (action, )]

            # Q value function
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (revard + DISCOUNT * max_future_q)
            q_table[discrete_state + (action, )] = new_q

        elif new_state[0] >= env.goal_position:
            print(f'We made it on episode {episode}')
            q_table[discrete_state + (action, )] = 0
            done = True

        discrete_state = new_discrete_state

    if END_EPSILON_DECAYING >= episode >= START_EPSILON_DECAYING:
        epsilon -= epsilon_decay_value

env.close()
