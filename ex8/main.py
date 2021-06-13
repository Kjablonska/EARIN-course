import numpy as np
import matplotlib.pyplot as plt
import gym
import random
from constants import test_episodes, max_steps, train_episodes, alpha, gamma, epsilon, max_epsilon, min_epsilon, decay_rate
# -------------------------------------------------------------------------------------
#   MODEL TRAINING PART
#   TODO:
#   - Refactor.
#   - Understand what the code below does.
#   - Play with parameters.
# -------------------------------------------------------------------------------------

# CREATE THE ENVIRONMENT
env = gym.make("Taxi-v3")
action_size = env.action_space.n
state_size = env.observation_space.n
print("Action space size: ", action_size)
print("State space size: ", state_size)

# INITIALISE Q TABLE TO ZERO
Q = np.zeros((state_size, action_size))

# TRAINING PHASE
training_rewards = []   # list of rewards

for episode in range(train_episodes):
    state = env.reset()    # Reset the environment
    cumulative_training_rewards = 0

    for step in range(max_steps):
        # Choose an action (a) among the possible states (s)
        exp_exp_tradeoff = random.uniform(0, 1)   # choose a random number

        # If this number > epsilon, select the action corresponding to the biggest Q value for this state (Exploitation)
        if exp_exp_tradeoff > epsilon:
            action = np.argmax(Q[state, :])
        # Else choose a random action (Exploration)
        else:
            action = env.action_space.sample()

        # Perform the action (a) and observe the outcome state(s') and reward (r)
        new_state, reward, done, info = env.step(action)

        # Update the Q table using the Bellman equation: Q(s,a):= Q(s,a) + lr [R(s,a) + gamma * max Q(s',a') - Q(s,a)]
        Q[state, action] = Q[state, action] + alpha * \
            (reward + gamma * np.max(Q[new_state, :]) - Q[state, action])
        cumulative_training_rewards += reward  # increment the cumulative reward
        state = new_state         # Update the state

        # If we reach the end of the episode
        if done == True:
            print("Cumulative reward for episode {}: {}".format(
                episode, cumulative_training_rewards))
            break

    # Reduce epsilon (because we need less and less exploration)
    epsilon = min_epsilon + (max_epsilon - min_epsilon) * \
        np.exp(-decay_rate*episode)

    # append the episode cumulative reward to the list
    training_rewards.append(cumulative_training_rewards)

print("Training score over time: " + str(sum(training_rewards)/train_episodes))
x = range(train_episodes)
plt.plot(x, training_rewards)
plt.xlabel('episode')
plt.ylabel('Training cumulative reward')
plt.savefig('Q_learning_simple_update.png', dpi=300)
plt.show()


# Save Q array to .csv file.
a = np.asarray(Q)
np.savetxt("model.csv", a, delimiter=",")