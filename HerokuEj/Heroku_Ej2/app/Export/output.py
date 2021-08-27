import graphviz

def init():
    global output
    global ast
    global graph
    output = ""
    ast = None
    graph = graphviz.Digraph()

def addNode(id, label):
    graph.node(id, str(label))

def addEdges(fromNode, to):
    graph.edge(fromNode, to)