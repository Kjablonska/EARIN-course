from bayesian_network import BayesianNetwork

def run_method(name, evidence, query, steps, option):
    net = BayesianNetwork('assets/' + name)

    if option == 'mcmc':
        res = net.mcmc(evidence=evidence, query=query, step=steps)
    elif option == 'markov_blanket':
        net.markov_blanket(evidence)

#run_method("alarm.json", {"burglary": "T"}, ["John_calls"], 10000, "mcmc")
run_method("alarm.json", "burglary", ["John_calls"], 10000, "markov_blanket")
#run_method("flower.json", {"flower_species": "rose"}, ["color"], 10000, "mcmc")
# run_method("flower.json", "flower_species", ["color"], 100, "markov_blanket")