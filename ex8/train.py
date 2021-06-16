import numpy as np
import matplotlib.pyplot as plt
import gym
import random
from constants import TRAIN_EPISODES, ALPHA, GAMMA, EPS, MAX_EPSILON, MIN_EPSILON, DECAY_RATE, MODEL_FILE, MAX_STEPS


def create_enivronment():
    env = gym.make("Taxi-v3")
    action_size = env.action_space.n
    state_size = env.observation_space.n

    print("=   Action space size: ", action_size)
    print("=   State space size: ", state_size)

    return env, action_size, state_size


def plot_data(training_rewards):
    print("=   Training score over time: " +
          str(sum(training_rewards)/TRAIN_EPISODES))
    x = range(TRAIN_EPISODES)

    plt.plot(x, training_rewards)
    plt.xlabel('episode')
    plt.ylabel('Training cumulative reward')
    plt.savefig('result.png', dpi=300)
    plt.show()


def save_model(Q):
    model = np.asarray(Q)
    np.savetxt(MODEL_FILE, model, delimiter=",")


def main():
    env = gym.make("Taxi-v3")
    action_size = env.action_space.n
    state_size = env.observation_space.n

    print("=   Action space size: ", action_size)
    print("=   State space size: ", state_size)

    # Create Q matrix [500 x 6] of zeros, 500 states, 6 actions
    Q = np.zeros((state_size, action_size))
    training_rewards = []
    epsilon = EPS

    for episode in range(TRAIN_EPISODES):
        # Resets the environment and returns a random initial state.
        state = env.reset()
        cumulative_training_rewards = 0
        done = False

        for step in range(MAX_STEPS):
            # Decide whether to pick a random action or to exploit the already computed Q-values (Exploitation).
            # Prevent Q-values tendency of converge
            if random.uniform(0, 1) > epsilon:
                action = np.argmax(Q[state, :])
            else:
                action = env.action_space.sample()

            # env.step - step the environment by one timestep. reward - if action is beneficial or not
            new_state, reward, done, info = env.step(action)

            # Update the Q array. Calculate the maximum Q-value for the actions corresponding to the next_stat
            # Bellman equation:
            Q[state, action] = (1 - ALPHA) * Q[state, action] + ALPHA * \
                (reward + GAMMA * np.max(Q[new_state, :]) - Q[state, action])
            cumulative_training_rewards += reward
            state = new_state

            # The end of the peisode.
            if done == True:
                print("=   Cumulative reward for episode {}: {}".format(
                    episode, cumulative_training_rewards))
                break


        # Reduce epsilon since there is a need for less exploration each time.
        epsilon = MIN_EPSILON + \
            (MAX_EPSILON - MIN_EPSILON) * np.exp(-DECAY_RATE*episode)
        training_rewards.append(cumulative_training_rewards)

    plot_data(training_rewards)
    save_model(Q)


if __name__ == "__main__":
    line = '============================================================'

    print(chr(27) + "[2J")
    print(line)
    print('=   Authors: ')
    print('=   - Karolina Jablonska, 295813')
    print('=   - Wojciech Marosek, 295818')
    print(line)
    print('=   EARIN | Exercise 8 | Reinforcement | Training program')
    print(line)

    main()
