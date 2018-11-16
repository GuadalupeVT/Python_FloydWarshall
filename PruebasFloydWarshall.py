#https://www.sanfoundry.com/python-program-implement-floyd-warshall-algorithm/
'''
Created on 16/11/2018

@author: GVT
'''
class Graph:
    def __init__(self):
        # dictionary containing auxs that map to the corresponding Vertice object
        self.vertices = {}
 
    def agregarVertice(self, aux):
        #Agrega un vertice en el aux al grafo
        """Add a Vertice with the given aux to the graph."""
        Vertice = Vertice(aux)
        self.vertices[aux] = Vertice
 
    def getVertice(self, aux):
        """Return Vertice object with the corresponding aux."""
        return self.vertices[aux]
 
    def __contains__(self, aux):
        return aux in self.vertices
 
    def agregar_edge(self, src_aux, dest_aux, weight=1):
        """Add edge from src_aux to dest_aux with given weight."""
        self.vertices[src_aux].add_neighbour(self.vertices[dest_aux], weight)
 
    def existeEdge(self, src_aux, dest_aux):
        """Return True if there is an edge from src_aux to dest_aux."""
        return self.vertices[src_aux].does_it_point_to(self.vertices[dest_aux])
 
    def __longitud__(self):
        return len(self.vertices)
 
    def __iter__(self):
        return iter(self.vertices.values())