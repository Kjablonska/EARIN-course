# [TO DO]:


from bayesian_network import BayesianNetwork


if __name__ == "__main__":
    net = BayesianNetwork('alarm.json')
    # print(net)
    net.markov_blanket('burglary')