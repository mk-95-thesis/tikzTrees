from itertools import product
import re
import os

allTrees={1:
          {
              1:("\oItI","\{}f")
          },
          2:
          {
              1:("\oIItI","\{}fu{}f")
          },
          3:
          {
              1:("\oIIItI","\{}fuu{}f{}f"),
              2:("\oIIItII","\{}fu{}fu{}f")
          },
          4:
          {
              1:("\oIVtI","\{}fuuu{}f{}f{}f"),
              2:("\oIVtII","\{}fuu{}fu{}f{}f"),
              3:("\oIVtIII","\{}fu{}fuu{}f{}f"),
              4:("\oIVtIV","\{}fu{}fu{}fu{}f")
          }
          }

Node = "\{}Node"
rNode = "\R{}Node"

strNodes = ["I","Q","ImQ"] # string nodes
nodes = [Node.format(strNode) for strNode in strNodes] # regular nodes
rnodes = [rNode.format(strNode) for strNode in strNodes] # root nodes


directoryName = "./trees/"
if not os.path.exists(directoryName):
    os.makedirs(directoryName)

for order in allTrees.keys():
    command = "\\newcommand{{{}}}{{" +"{}"+ "".join(["{{{}}}" for _ in range(order)]) + "}}"

    trees = eval("list(product(rnodes"+ "".join([",nodes" for _ in range(order-1)])+"))")
    strTrees = eval("list(product(strNodes"+ "".join([",strNodes" for _ in range(order-1)])+"))")

    with open(directoryName + "order{}.tex".format(order),"w") as file:
        for key in allTrees[order].keys():
            file.write("% ======================================\n")
            file.write("% trees of order {} and type {}\n".format(order,key))
            file.write("% ======================================\n")
            for tree, strTree in zip(trees,strTrees):
                newcommand = command.format(allTrees[order][key][1].format(*strTree),allTrees[order][key][0],*tree)
                file.write(newcommand+"\n")
