class Node:

    def __init__(self, name, parents, probabilities, output_values):
        self.node_name = name
        self.parents = parents
        self.probabilities = probabilities
        self.children = []
        self.value = ''
        self.outputValues = output_values


    def __repr__(self):
        return '\n[Name]: ' + str(self.node_name) +\
               '\n[Parents]: ' + str(self.parents) +\
               '\n[Probabilities]: ' + str(self.probabilities) +\
               '\n[Children]: ' + str(self.children)

    def add_child(self, child):
        self.children.append(child)
