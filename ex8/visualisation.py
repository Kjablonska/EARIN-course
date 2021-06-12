test_rewards = []

for episode in range(test_episodes):
    state = env.reset()
    cumulative_test_rewards = 0
    frames = []
    print("****************************************************")
    print("EPISODE ", episode)

    for step in range(max_steps):
        env.render()
        # Take the action (index) that have the maximum expected future reward given that state
        action = np.argmax(Q[state, :])
        new_state, reward, done, info = env.step(action)
        cumulative_test_rewards += reward
        state = new_state

        if done:
            print("Cumulative reward for episode {}: {}".format(
                episode, cumulative_test_rewards))
            break
    test_rewards.append(cumulative_test_rewards)

env.close()
print("Test score over time: " + str(sum(test_rewards)/test_episodes))
