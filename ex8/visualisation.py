from IPython.display import clear_output
from time import sleep
import gym
import numpy as np
from constants import TEST_EPISODES, MAX_STEPS, MODEL_FILE

line = '============================================================'


def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        print('\n')
        print(frame['frame'])
        print("=   Step: {}".format(i))
        print("=   State: {}".format(frame["state"]))
        print("=   Action: {}".format(frame['action']))
        print("=   Reward: {}.".format(frame['reward']))
        sleep(.1)

def visualise():

    print(chr(27) + "[2J")
    print(line)
    print('=   Authors: ')
    print('=   - Karolina Jablonska, 295813')
    print('=   - Wojciech Marosek, 295818')
    print(line)
    print('=   EARIN | Exercise 8 | Reinforcement | Visualization')
    print(line)

    # Read trained model from file.
    Q = np.genfromtxt(MODEL_FILE, delimiter=',')

    # Create enivronment.
    env = gym.make("Taxi-v3")

    test_rewards = []
    frames = []

    for episode in range(TEST_EPISODES):
        state = env.reset()
        cumulative_test_rewards = 0

        print(line)
        print("=   Episode", episode)

        for step in range(MAX_STEPS):
            env.render()
            # Take the action (index) that have the maximum expected future reward given that state
            action = np.argmax(Q[state, :])
            new_state, reward, done, info = env.step(action)
            cumulative_test_rewards += reward
            state = new_state

            # For animation purpose.
            frames.append({
                'frame': env.render(mode='ansi'),
                'state': state,
                'action': action,
                'reward': reward
            }
            )

            if done:
                print("=   Cumulative reward for episode {}: {}\n".format(
                    episode, cumulative_test_rewards))
                break
        test_rewards.append(cumulative_test_rewards)

    env.close()
    print("=   Test score over time: " + str(sum(test_rewards)/TEST_EPISODES))
    print_frames(frames)


visualise()