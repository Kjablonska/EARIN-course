from IPython.display import clear_output
from time import sleep
import gym
import numpy as np
from constants import test_episodes, max_steps

# -------------------------------------------------------------------------------------
#   VISUALISATION PART
#   TODO:
#   - Refactor.
#   - Understand what is does.
# -------------------------------------------------------------------------------------

Q = np.genfromtxt('model.csv', delimiter=',')

env = gym.make("Taxi-v3")
action_size = env.action_space.n
state_size = env.observation_space.n

test_rewards = []
frames = []  # for animation

for episode in range(test_episodes):
    state = env.reset()
    cumulative_test_rewards = 0
    print("****************************************************")
    print("EPISODE ", episode)

    for step in range(max_steps):
        env.render()             # UNCOMMENT IT IF YOU WANT TO SEE THE AGENT PLAYING
        # Take the action (index) that have the maximum expected future reward given that state
        action = np.argmax(Q[state, :])
        new_state, reward, done, info = env.step(action)
        cumulative_test_rewards += reward
        state = new_state

        # Put each rendered frame into dict for animation
        frames.append({
            'frame': env.render(mode='ansi'),
            'state': state,
            'action': action,
            'reward': reward
        }
        )

        if done:
            print("Cumulative reward for episode {}: {}".format(
                episode, cumulative_test_rewards))
            break
    test_rewards.append(cumulative_test_rewards)

env.close()
print("Test score over time: " + str(sum(test_rewards)/test_episodes))


def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        print(frame['frame'])
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)


print_frames(frames)

