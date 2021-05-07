import json
import os
from node import Node, get_node
import numpy as np
import itertools
# from mcmc import mcmc_gibss_sampling


# -------------------------------------------------------------------------------------
#
#   Bayesian Network.
#   It parses the given JSON file and stores each node in Node structure.
#
#   Class responsibilites:
#   * Parses JSON file.
#   * Creates Markov Blanket.
#   * Returns the probability distribution of the selected query variables based on the evidence.
#   * Checks input probabilites - they must sum up to 1.
#   * Prints network
#   * Prints Markov Blanekt.
#
# -------------------------------------------------------------------------------------
class BayesianNetwork:

    def __init__(self, file_path=''):
        self.json = {}
        self.nodes = []
        self.file_path = file_path

        self.read_file()
        if self.json:
            self._parse_nodes()
            self._match_children()

    # -------------------------------------------------------------------------------------
    #
    #   Markov Blanket.
    #   For the given node, it stores its parents, children and parents of children.
    #
    # -------------------------------------------------------------------------------------
    def create_markov_blanket(self, name):
        node = get_node(self.nodes, name)
        markov_out = {}
        markov_out["parents"] = node.parents
        markov_out["children"] = node.children

        children_parents = {}
        for child in node.children:
            child_node = get_node(self.nodes, child)
            children_parents[child] = child_node.parents
        markov_out["children parents"] = children_parents
        return markov_out

    def markov_blanket(self, name):
        mb = self.create_markov_blanket(name)
        print("Markov Blanket for node " + name)
        print(mb)

    def _parse_nodes(self):
        for node in self.json["nodes"]:
            prob = self.json["relations"][node]["probabilities"]
            vals = []
            for el in list(prob.keys()):
                probs = el.split(",")
                vals.append(probs[-1])

            self.nodes.append(Node(
                node, self.json["relations"][node]["parents"], self.json["relations"][node]["probabilities"], vals))
        self._validate_probabilities()


    def _validate_probabilities(self):
        for node in self.nodes:
            probabilities = list(node.probabilities.values())
            parents = node.parents

            try:
                for el in list(node.probabilities.keys()):
                    probs = el.split(",")
                    if len(probs) != len(parents) + 1:
                        raise ValueError('[{}] Number of parents is not valid for given probabilities'.format(node.node_name))
            except ValueError:
                raise

            # try:
            #     if len(probabilities) != 2 ** (len(node.parents) + 1):
            #         raise ValueError('[{}] Number of parents is not valid for given probabilities'.format(node.node_name))

            #     for iter in range(0, len(probabilities), 2):
            #         if probabilities[iter] + probabilities[iter+1] != 1:
            #             raise ValueError('[{}] Probabilities has to be equal to 1'.format(node.node_name))
            # except ValueError:
            #     raise


    def _match_children(self):
        for node in self.nodes:
            for parent in node.parents:
                parent_node = get_node(self.nodes, parent)
                parent_node.add_child(node.node_name)

    def read_file(self):
        with open(os.path.join(os.path.abspath(os.getcwd()), self.file_path), "r") as file:
            self.json = json.load(file)


    # -------------------------------------------------------------------------------------
    #
    #   MCMC algorithm with Gibbs sampling
    #   Method takes as an arguments evidence dictionary, query array and number of steps as a number.
    #
    #   Description:
    #   It starts from asinging values for all nodes. Those who are in evidence dictionary are set to the provided value. Non-evidence nodes are set randomly.
    #   Counter stores values for evidence nodes.
    #
    #   Accepted variables:
    #   * Given evidence value must be set in the same way as probabilites!
    #       For instance: See alarm.json and flower.json in ../assets dictionary. The evidence and query for those networks should look as follows:
    #       evidence={"burglary": "T", "alarm": "T"}
    #       evidence={"flower_species": "rose"}, query=["color"]
    #   * step must be an integer value, greater than 0.
    #
    #   Sampling:
    #   After values assignment and counter initialization, the program proceeds to sampling.
    #   It iterates as many times, as specified by step variable:
    #       1. Randomly select non_evidence node X.
    #       2. Calculate probabilities.
    #       3. Draw one sample using roulete wheel and assign it to the X value.
    #       4. Increase counter.
    #   Normalize counter values.
    #   Print result.
    #
    # -------------------------------------------------------------------------------------
    def mcmc(self, evidence, query, step):
        non_evidence = []
        for node in self.nodes:
            if not node.node_name in evidence.keys():
                non_evidence.append(node)
            else:
                print(evidence[node.node_name])
                node.value = evidence[node.node_name]

        for el in non_evidence:
            el.value = np.random.choice(el.outputValues)             # Assign random value from all possible values to each non-evidence node.

        counter = {}    # alarm : {"T" : 0}

        for el in query:
            node = get_node(self.nodes, el)
            print(el, query)
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


    # -------------------------------------------------------------------------------------
    #
    #   Probabilities calculation for node X
    #   Implemntation of the formula: P(X = xj | MB(X))
    #
    #   It uses Markov Blanket - MB, for the given node X.
    #   Then, it iterates over all possible probability values {x1, x2, ... xj} of X and:
    #   1. P(X = xj | Parents(X))
    #       * For each parent p, it takes p.value and crates string indicating conditional probability for node X and its parents.
    #       For instance: X.value = T, p1.value = F, p2.value = F, probability = FFT
    #       Having such string, we can find the value of such probability.
    #   2. For each children Zi, find: P( Zi = zi | Parents(Zi) )
    #       * Take all possible probaility values and for them take all possible parents values and create probability as in the previuos step.
    #   3. Multiply all probabilites from step 2 by probability from step 1.
    #
    #   Roulette selection:
    #   It takes all calculated probabilites as a vector and normalize it so as all values sumes up to 1.
    #   Creation of roulette wheel:
    #   For each value of normalized vector of probabilites, create wheel as previous vale + current value.
    #   After wheel is created, we randomly draw a number between 0 and 1 (using np.random.uniform()) which indicates the interval in the wheel and indicates the probility.
    #
    # -------------------------------------------------------------------------------------

    def sample(self, X):
        mb = self.create_markov_blanket(X.node_name)
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

        return self.roulette_selection(probabilities_dict)


    def roulette_selection(self, probabilities_dict):
        # We normalize vector in order to create roulette wheel.
        s = sum(list(probabilities_dict.values()))
        normal_prob = [el / s for el in list(probabilities_dict.values())]

        wheel = []
        prev = 0
        for el in normal_prob:
            curr = prev + el
            wheel.append(curr)
            prev = curr

        roulette_pick = np.random.uniform(0, 1)
        i = 0
        while i in range(len(wheel)) and wheel[i] < roulette_pick:
            i += 1

        if i > len(wheel) - 1:
            i =- 1

        res = (list(probabilities_dict.items())[i])
        return res[0]
