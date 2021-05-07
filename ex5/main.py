from bayesian_network import BayesianNetwork

def run_method(name, evidence, query, steps, option):
    net = BayesianNetwork('assets/' + name)

    if option == 'mcmc':
        res = net.mcmc(evidence=evidence, query=query, step=steps)
    elif option == 'markov_blanket':
        net.markov_blanket(evidence)

run_method("alarm.json", {"burglary": "T"}, ["John_calls"], 10000, "mcmc")