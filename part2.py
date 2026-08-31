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
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    print(nodes)

    #count and print nodes
    count_nodes = len(nodes)
    print(count_nodes)

    viz_graph(graph,nodes,'graph.html')

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
        G.add_node(n, label=n, color='#FFFFFF', shape = 'diamond')
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
    

    return 

# keep this at the bottom of your file.
if __name__ == '__main__':
    main()
