# import numpy as np
# from bayesian_network import get_node


# def mcmc_gibss_sampling(evidence, query, step, nodes):
#     non_evidence = []
#     for node in nodes:
#         if not node.node_name in evidence.keys():
#             non_evidence.append(node)
#         else:
#             node.value = 'T'


#     for el in non_evidence:
#         # Assign random value from all possible values to each non-evidence node.
#         el.value = np.random.choice(el.outputValues)

#     counter = {}    # alarm : {"T" : 0}

#     for el in query:
#         node = get_node(nodes, el)
#         values = {}
#         for p in node.outputValues:
#             values[p] = 0
#         counter[el] = values

#     print("--------------------COUNTER------------------")
#     print(counter)

#     step = 1000
#     s = 0
#     for i in range(step):
#         # Xi ← Random(G − E)

#         # change it to use random.choice() method
#         Xi_id = np.random.randint(0, len(non_evidence))
#         Xi = non_evidence[Xi_id]

#         Xi.value = sample(Xi, nodes)

#         for el in query:
#             counter[el][get_node(nodes, el).value] += 1.0

#     # chyba wystarczy podzielić przez step bo to sie powinno zsumowac do step
#     for res in counter:
#         s = sum(list(counter[res].values()))

#     for res in counter:
#         for el in counter[res].keys():
#             counter[res][el] /= s

#     # Print result.
#     for res in counter:
#         print("Query:  " + res)
#         print(counter[res])


# def sample(X, nodes):
#     mb = markov_blanket(X.node_name)
#     # print("--------------------MARKOV------------------")
#     # print(mb)
#     probabilities_dict = {}

#     for xj in X.outputValues:
#         X.value = xj

#         X_parent = ""
#         for parent in mb["parents"]:
#             parent_node = get_node(nodes, parent)
#             X_parent += str(parent_node.value) + ','
#         X_parent += X.value

#         prob_parent = X.probabilities[X_parent]

#         # TODO: use join()
#         X_children = ""
#         prob = 1
#         for children in mb["children"]:
#             child_node = get_node(nodes, children)
#             parent_node_val = []
#             for parent in mb["children parents"][children]:
#                 parent_node = get_node(nodes, parent)
#                 parent_node_val.append(str(parent_node.value))
#             parent_node_val.append(str(child_node.value))

#             X_children = ','.join(parent_node_val)

#             prob *= child_node.probabilities[X_children]


#         final_prob = prob_parent * prob
#         probabilities_dict[xj] = final_prob     # xj : final_prob

#         return roulette_selection(probabilities_dict)


# # Roulette selection.
# def roulette_selection(probabilities_dict):
#     # We normalize vector in order to create roulette wheel.
#     s = sum(list(probabilities_dict.values()))
#     normal_prob = [el / s for el in list(probabilities_dict.values())]

#     roulette = {}
#     wheel = []
#     prev = 0
#     for el in normal_prob:
#         curr = prev + el
#         wheel.append(curr)
#         prev = curr

#     roulette_pick = np.random.uniform(0, 1)     # wheel is created using normalized vector so it sums up to 1.
#     i = 0
#     while i in range(len(wheel)) and wheel[i] < roulette_pick:
#         i += 1

#     if i > len(wheel) - 1:
#         i =- 1

#     res = (list(probabilities_dict.items())[i])
#     return res[0]


