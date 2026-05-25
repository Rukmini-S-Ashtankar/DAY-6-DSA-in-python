class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []

    def addChild(self, childNode):
        self.children.append(childNode)

    def __str__(self, level=0):

        result = " " * level + self.data + "\n"

        for child in self.children:
            result += child.__str__(level + 2)

        return result


# Creating Nodes
drinks = TreeNode("Drinks")

hot = TreeNode("Hot")
cold = TreeNode("Cold")

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")

nonAlcoholic = TreeNode("Non-Alcoholic")
alcoholic = TreeNode("Alcoholic")


# Building Tree
drinks.addChild(hot)
drinks.addChild(cold)

hot.addChild(tea)
hot.addChild(coffee)

cold.addChild(nonAlcoholic)
cold.addChild(alcoholic)


# Printing Tree
print(drinks)