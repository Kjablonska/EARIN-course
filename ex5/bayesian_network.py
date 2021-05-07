import json
import os
from node import Node, get_node
import numpy as np
import itertools
# from mcmc import mcmc_gibss_sampling

class BayesianNetwork:

    def __init__(self, file_path=''):
        self.json = {}
        self.nodes = []
        self.file_path = file_path

        self.read_file()
        if self.json:
            self._parse_nodes()
            self._match_children()

    def markov_blanket(self, name):
        node = get_node(self.nodes, name)
        markov_out = {}
        markov_out["parents"] = node.parents
        markov_out["children"] = node.children

        children_parents = {}
        for child in node.children:
            child_node = get_node(self.nodes, child)
            children_parents[child] = child_node.parents
        markov_out["children parents"] = children_parents
        # print(markov_out)

        return markov_out

    def _parse_nodes(self):
        for node in self.json["nodes"]:
            prob = self.json["relations"][node]["probabilities"]
            vals = []
            for el in list(prob.keys()):
                vals.append(el[-1])

            self.nodes.append(Node(
                node, self.json["relations"][node]["parents"], self.json["relations"][node]["probabilities"], vals))
        self._validate_probabilities()


    # Redundant since it's one of the assumptions.
    def _validate_probabilities(self):
        for node in self.nodes:
            probabilities = list(node.probabilities.values())

            try:
                if len(probabilities) != 2 ** (len(node.parents) + 1):
                    raise ValueError('[{}] Number of parents is not valid for given probabilities'.format(node.node_name))

                for iter in range(0, len(probabilities), 2):
                    if probabilities[iter] + probabilities[iter+1] != 1:
                        raise ValueError('[{}] Probabilities has to be equal to 1'.format(node.node_name))
            except ValueError:
                raise


    def _match_children(self):
        for node in self.nodes:
            for parent in node.parents:
                parent_node = get_node(self.nodes, parent)
                parent_node.add_child(node.node_name)

    def read_file(self):
        with open(os.path.join(os.path.abspath(os.getcwd()), self.file_path), "r") as file:
            self.json = json.load(file)


    # evidence={"node1": 1}, query=["node2", "node3"]
    # mcmc_gibss_sampling(evidence, query, step, self.nodes)
    def mcmc(self, evidence, query, step):
        non_evidence = []
        for node in self.nodes:
            if not node.node_name in evidence.keys():
                non_evidence.append(node)
            else:
                node.value = evidence[node.node_name]

        for el in non_evidence:
            el.value = np.random.choice(el.outputValues)             # Assign random value from all possible values to each non-evidence node.

        counter = {}    # alarm : {"T" : 0}

        for el in query:
            node = get_node(self.nodes, el)
            values = {}
            for p in node.outputValues:
                values[p] = 0
            counter[el] = values

        step = 1000
        s = 0
        # Xi ← Random(G − E)
        for i in range(step):

            # change it to use random.choice() method
            Xi_id = np.random.randint(0, len(non_evidence))
            Xi = non_evidence[Xi_id]

            Xi.value = self.sample(Xi)

            for el in query:
                counter[el][get_node(self.nodes, el).value] += 1.0

        for res in counter:
            s = sum(list(counter[res].values()))

        for res in counter:
            for el in counter[res].keys():
                counter[res][el] /= s

        # Print result.
        for res in counter:
            print("Query:  " + res)
            print(counter[res])


    # TODO
    def sample(self, X):
        mb = self.markov_blanket(X.node_name)
        probabilities_dict = {}

        for xj in X.outputValues:
            X.value = xj

            X_parent = ""
            for parent in mb["parents"]:
                parent_node = get_node(self.nodes, parent)
                X_parent += str(parent_node.value) + ','
            X_parent += X.value

            prob_parent = X.probabilities[X_parent]

            X_children = ""
            prob = 1
            for children in mb["children"]:
                child_node = get_node(self.nodes, children)
                parent_node_val = []
                for parent in mb["children parents"][children]:
                    parent_node = get_node(self.nodes, parent)
                    parent_node_val.append(str(parent_node.value))
                parent_node_val.append(str(child_node.value))

                X_children = ','.join(parent_node_val)

                prob *= child_node.probabilities[X_children]


            final_prob = prob_parent * prob
            probabilities_dict[xj] = final_prob     # xj : final_prob


        # Roulette selection.

        # We normalize vector in order to create roulette wheel.
        s = sum(list(probabilities_dict.values()))
        normal_prob = [el / s for el in list(probabilities_dict.values())]

        wheel = []
        prev = 0
        for el in normal_prob:
            curr = prev + el
            wheel.append(curr)
            prev = curr

        roulette_pick = np.random.uniform(0, 1)     # wheel is created using normalized vector so it sums up to 1.
        i = 0
        while i in range(len(wheel)) and wheel[i] < roulette_pick:
            i += 1

        if i > len(wheel) - 1:
            i =- 1

        res = (list(probabilities_dict.items())[i])
        return res[0]

