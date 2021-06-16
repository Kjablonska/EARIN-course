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

    # Read trained model from file.
    Q = np.genfromtxt(MODEL_FILE, delimiter=',')

    # Create enivronment.
    env = gym.make("Taxi-v3")

    test_rewards = []
    frames = []
    result = {}

    for episode in range(TEST_EPISODES):
        state = env.reset()
        sum_rewards = 0

        for step in range(MAX_STEPS):
            # Take the action (index) that have the maximum expected future reward given that state
            action = np.argmax(Q[state, :])
            new_state, reward, done, info = env.step(action)
            sum_rewards += reward
            state = new_state

            # For animation purpose.
            frames.append({
                'frame': env.render(mode='ansi'),
                'state': state,
                'action': action,
                'reward': reward
            })

            if done:
                result[episode] = sum_rewards
                break

        test_rewards.append(sum_rewards)

    env.close()

    print_frames(frames)
    print(line)
    print("=   Test score over time: " + str(sum(test_rewards)/TEST_EPISODES))
    for eps in result:
        print("=   Cumulative reward for episode {}: {}".format(
            eps, result[eps]))


if __name__ == "__main__":
    print(chr(27) + "[2J")
    print(line)
    print('=   Authors: ')
    print('=   - Karolina Jablonska, 295813')
    print('=   - Wojciech Marosek, 295818')
    print(line)
    print('=   EARIN | Exercise 8 | Reinforcement | Visualization')
    print(line)

    visualise()
