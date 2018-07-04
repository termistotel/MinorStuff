import random
import networkx as nx
import matplotlib.pyplot as plt

def plot_deg_dist(G):

	all_degrees = [j for (i,j) in nx.degree(G)]
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


def erdos_renyi(G, p):

	nodes = list(G.nodes())
	brojNodes = len(nodes)
	for i in range(0, brojNodes):
		node1 = nodes[i]
		print(i)
		for j in range(i, brojNodes):
			node2 = nodes[j]
			if node1 != node2:
				r = random.random()
				if r <= p:
					G.add_edge(node1, node2)
					ne = [(node1, node2)]
					display_graph(G, '', ne)
				else:
					display_graph(G, '', '')


def main():
	# n=int(raw_input('Unesi n: '))
	# p=float(raw_input('Unesi p: '))
	n = 5
	p = 0.3

	G = nx.Graph()
	G.add_nodes_from( range(n) )

	# Ispisi inicijalni graf
	display_graph(G, '', '')

	# Dodaj edgeve u graf
	erdos_renyi(G, p)

	# Ispisi distribuciju
	plot_deg_dist(G)	


main()