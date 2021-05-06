import json
import os
from node import Node
import numpy as np
import itertools

class BayesianNetwork:

    def __init__(self, file_path=''):
        self.json = {}
        self.nodes = []
        self.file_path = file_path

        self.read_file()
        if self.json:
            self._parse_nodes()
            self._match_children()

    def __repr__(self):
        for node in self.nodes:
            print(node)
        return ""

    def markov_blanket(self, name):
        node = self._get_by_name(name)
        markov_out = {}
        markov_out["parents"] = node.parents
        markov_out["children"] = node.children

        children_parents = {}
        for child in node.children:
            child_node = self._get_by_name(child)
            children_parents[child] = child_node.parents


        markov_out["children parents"] = children_parents
        print(markov_out)
        return markov_out

    def _parse_nodes(self):
        for node in self.json["nodes"]:
            prob = self.json["relations"][node]["probabilities"]
            vals = []
            for el in list(prob.keys()):
                vals.append(el[0])              # We get first element from each "T,T,T" etc because it means value of the node.

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
                parent_node = self._get_by_name(parent)
                parent_node.add_child(node.node_name)

    def read_file(self):
        with open(os.path.join(os.path.abspath(os.getcwd()), self.file_path), "r") as file:
            self.json = json.load(file)

    def _get_by_name(self, name):
        for node in self.nodes:
            if node.node_name == name:
                return node
        return Node

    # evidence={"node1": 1}, query=["node2", "node3"]
    def MCMC(self, evidence, query):
        non_evidence = []
        for node in self.nodes:
            if not node.node_name in evidence.keys():
                non_evidence.append(node)
            else:
                node.value = 'T'


        for el in non_evidence:
            # Assign random value from all possible values to each non-evidence node.
            el.value = np.random.choice(el.outputValues)

        counter = {}    # alarm : {"T" : 0}

        for el in query:
            node = self._get_by_name(el)
            values = {}
            for p in node.outputValues:
                values[p] = 0
            counter[el] = values

        print("--------------------COUNTER------------------")
        print(counter)

        step = 1000
        for i in range(step):
            # Xi ← Random(G − E)

            # change it to use random.choice() method
            Xi_id = np.random.randint(0, len(non_evidence))
            Xi = non_evidence[Xi_id]

            Xi.value = self.sample(Xi)

            for el in query:
                counter[el][self._get_by_name(el).value] += 1.0/step

        # Print counter
        for res in counter:
            print("Query:  " + res)
            print(counter[res])


    # TODO
    def sample(self, X):
        mb = self.markov_blanket(X.node_name)
        print("--------------------MARKOV------------------")
        print(mb)
        probabilities_dict = {}

        for xj in X.outputValues:
            X.value = xj

            X_parent = ""
            X_parent += X.value
            for parent in mb["parents"]:
                parent_node = self._get_by_name(parent)
                X_parent += ',' + str(parent_node.value)

            print("PARENT")
            print(X_parent)

            print("P PARENT")
            prob_parent = X.probabilities[X_parent]
            print(prob_parent)


            # TODO: use join()
            X_children = ""
            prob = 1
            for children in mb["children"]:
                child_node = self._get_by_name(children)
                parent_node_val = []
                for parent in mb["children parents"][children]:
                    parent_node = self._get_by_name(parent)
                    parent_node_val.append(str(parent_node.value))
                parent_node_val.append(str(child_node.value))

                X_children = ','.join(parent_node_val)

                print("x children" + X_children + children)
                prob *= child_node.probabilities[X_children]

            print("P CHILDREN")
            print(prob)

            final_prob = prob_parent * prob

            probabilities_dict[xj] = final_prob     # xj : final_prob

        normal_prob = np.linalg.norm(list(probabilities_dict.values()))

        print("============================================")
        # Rullete   rulette_val : {xj : final_prob}
        # id = np.random.uniform(0, 1)
        # rullete_val[id] => rulette_val : {xj : final_prob}

        # prob + prev_prob : probability_dict
        roulette = {}
        wheel = []
        prev = 0
        for el in probabilities_dict:    # F
            curr = prev + probabilities_dict[el]
            print(probabilities_dict[el], el)
            # wheel.append(curr)
            roulette[curr] = el
            prev = curr

        print(roulette)

        roulette_vals = list(roulette.keys())
        roulette_pick = np.random.uniform(0, roulette_vals[-1])

        i = 0
        while i in range(len(roulette_vals)) and roulette_vals[i] < roulette_pick:
            i += 1

        if i > len(roulette_vals) - 1:
            i =- 1
        res = roulette[roulette_vals[i]]
        print(res)

        return res








# 0.1, 0.2, 04
# => rullete= [0, 0+0.1, 0.1+0.2, 0.1+0.2+0.4] = 1
#   id = np.random.uniform(0, 1)
#   return rullete[id]
#

