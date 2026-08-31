import matplotlib.pyplot as plt
from pyvis.network import Network

def main():
    """
    Main function.
    """

    ## Edge list (list of two-element lists)
    graph = [['A','B'],['A','C'],['A','D'],['A','E'],['A','F'],['B','F'],['C','D'],['E','F'],['E','G']]
    print('graph:',graph)

    #print on each line
    for i in graph:
        print(i)

    #count edges
    count_edges = len(graph)
    print(count_edges)

    #list of nodes assigned to variable nodes
    nodes = []
    for edge in graph:
        node1 = edge[0]
        node2 = edge[1]
        print("EDGE:", node1, node2)
        if node1 not in nodes: 
            nodes.append(node1)
        if node2 not in nodes:
            nodes.append(node2)
    print('nodes:', nodes)

    #count and print nodes
    count_nodes = len(nodes)
    print(count_nodes)

    viz_graph(graph,nodes,'graph.html')
    print('hello')

    return # done with main()

def viz_graph(edgelist,nodes,outfile):
    """
    Visualize a graph represented as the edgelist
    and writes it to an HTML file.
    :param: edgelist - list of two-element lists
    :param: nodes - list of strings
    :param: outfile - string outfile that ends in '.html'
    :returns: None
    """

    G = Network(directed=False) # create undirected graph
    for n in nodes:
        d = get_degree(n, edgelist)
        print(n,d)
        G.add_node(n, label=n, color="#8FD4F9", shape = 'dot', size = d*5)
    for u,v in edgelist:
        G.add_edge(u, v, color='#000000')
    G.toggle_physics(True) 
    G.show_buttons(filter_=['physics'])
    G.write_html(outfile)

    return

def get_degree(node,edgelist):
    """
    Given a node and an edgelist, return the node's degree.
    :param: node - string
    :param: edgelist - lis of two-element lists
    :returns: int
    """
    
    degrees = 0
    for i in edgelist:
        if i[0] == node:
            degrees = degrees + 1
        if i[1] == node:
            degrees = degrees + 1
    return degrees

# keep this at the bottom of your file.
if __name__ == '__main__':
    main()