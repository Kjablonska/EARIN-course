import numpy as np
import matplotlib.pyplot as plt
import gym
import random
from constants import TEST_EPISODES, MAX_STEPS, TRAIN_EPISODES, ALPHA, GAMMA, EPS, MAX_EPSILON, MIN_EPSILON, DECAY_RATE, MODEL_FILE


def create_enivronment():
    env = gym.make("Taxi-v3")
    action_size = env.action_space.n
    state_size = env.observation_space.n
    print("Action space size: ", action_size)
    print("State space size: ", state_size)
    return env, action_size, state_size


def plot_data(training_rewards):
    print("Training score over time: " +
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
    print("Action space size: ", action_size)
    print("State space size: ", state_size)
    Q = np.zeros((state_size, action_size))
    training_rewards = []
    epsilon = EPS

    for episode in range(TRAIN_EPISODES):
        state = env.reset()
        cumulative_training_rewards = 0
        done = False

        while not done:
            # Choosing an action among the possible states.
            # If this number > epsilon, select the action corresponding to the biggest Q value for this state (Exploitation)
            if random.uniform(0, 1) > epsilon:
                action = np.argmax(Q[state, :])
            # Choose a random action (Exploration)
            else:
                action = env.action_space.sample()

            new_state, reward, done, info = env.step(action)

            # Update the Q array.
            # Bellman equation:
            Q[state, action] = (1 - ALPHA) * Q[state, action] + ALPHA * \
                (reward + GAMMA * np.max(Q[new_state, :]) - Q[state, action])
            cumulative_training_rewards += reward
            state = new_state

        print("Cumulative reward for episode {}: {}".format(
                    episode, cumulative_training_rewards))


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
