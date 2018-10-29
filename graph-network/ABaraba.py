import random
import networkx as nx
import matplotlib.pyplot as plt

def plot_deg_dist(G):

	all_degrees = [j for (i,j) in G.degree()]
	# all_degrees = []
	# for par in G.degree():
	#	all_degrees.append(par[1])

	unique_degrees = list(set(all_degrees))
	unique_degrees.sort()
	
	count_of_degrees = []
	for i in unique_degrees:
		c = all_degrees.count(i)
		count_of_degrees.append(c)

	# print(unique_degrees)
	# print(count_of_degrees)

	plt.plot(unique_degrees, count_of_degrees, 'ro-')
	plt.xlabel('Stupanj')
	plt.ylabel('Broj cvorova')
	plt.title('Distribucija')
	plt.show()

def display_graph(G, cvor, ne):
	pos = nx.circular_layout(G)
	if cvor == '' and ne == '':
		novi_cvor = []
		ostali_cvorovi =G.nodes()
		novi_rub = []
		ostali_rubovi = G.edges()

	elif cvor== '':
		novi_cvor = []
		ostali_cvorovi = G.nodes()
		novi_rub = ne
		ostali_rubovi = list( set(G.edges()) - set(novi_rub) - set([(b,a) for (a,b) in novi_rub]) )

	else:
	 	novi_cvor = [cvor]
	 	ostali_cvorovi = list( set(G.nodes()) - set(novi_cvor) )
	 	novi_rub = ne
	 	ostali_rubovi = list( set(G.nodes()) - set(novi_rub) - set([(b,a) for (a,b) in novi_rub]) )

	nx.draw_networkx_nodes(G, pos, nodelist = novi_cvor, node_color='g')
	nx.draw_networkx_nodes(G, pos, nodelist = ostali_cvorovi, node_color='r')
	nx.draw_networkx_edges(G, pos, edgelist = novi_rub, edge_color='b', style='dashdot')
	nx.draw_networkx_edges(G, pos, edgelist = ostali_rubovi, edge_color='r')

	plt.show()

# def add_nodes_barabasi(G, n, m0):
# 	m = m0 - 1

# 	for i in range(m0+1, n+1):
# 		G.add_node(i)

# 		degrees = nx.degree(G)
# 		node_probabilities = {}

# 		for each in G.nodes():
# 			node_probabilities[each] = (float)(degrees[each])/sum(degrees.values())

# 		node_probabilities_cum = []
# 		prev = 0

# 		for (n,p) in node_probabilities.items()
# 			temp = [n, prev+p]
# 			node_probabilities_cum.append(temp)
# 			prev = prev + p

def main():
	n = 100
	m0 = 7

	G = nx.path_graph(m0)
	m = m0-1

	G.add_node(30)
	G.add_node(29)

	# display_graph(G, '', '')
	# add_nodes_barabasi(G, n, m0)
	for i in nx.degree(G):
		print i
main()