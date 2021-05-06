# [TO DO]:


from bayesian_network import BayesianNetwork


if __name__ == "__main__":
    net = BayesianNetwork('alarm.json')
    print(net)
    print("-------------------------------------------------")
    res = net.MCMC({"burglary":1}, ["John_calls"])
    print(net)
    # print(net)
    # net.markov_blanket('burglary')