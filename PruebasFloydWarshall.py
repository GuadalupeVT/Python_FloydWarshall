# http://micaminomaster.com.co/grafo-algoritmo/dijkstra-floyd-warshall-python/
'''
Created on 16/11/2018

@author: GVT
'''
def floydWarshall(self):
    nodes = list(self.graph.nodes)
 
    for i in nodes:
        dict_i = {}
        for j in nodes:
            if i == j:
                dict_i[j] = 0
                continue
            try:
                dict_i[j] = self.graph[i][j]['weight']
            except:
                dict_i[j] = float("inf")
 
        self.distances[i] = dict_i
 
    for i in nodes:
        for j in nodes:
            for k in nodes:
                ij = self.distances[i][j]
                ik = self.distances[i][k]
                kj = self.distances[k][j]
 
                if ij > ik + kj:
                    self.distances[i][j] = ik + kj
 
    return self.distances