#https://www.sanfoundry.com/python-program-implement-floyd-warshall-algorithm/
'''
Created on 16/11/2018

@author: GVT
'''
class Grafo:
    def __init__(self):
        
        self.vertices = {}
 
    def agregarVertice(self, aux):
        #Agrega un vertice en el aux al grafo
        Vertice = Vertice(aux)
        self.vertices[aux] = Vertice
 
    def getVertice(self, aux):
        return self.vertices[aux]
 
    def __contains__(self, aux):
        return aux in self.vertices
 
    def agregar_edge(self, src_aux, dest_aux, weight=1):
        self.vertices[src_aux].add_neighbour(self.vertices[dest_aux], weight)
 
    def existeEdge(self, src_aux, dest_aux):
        return self.vertices[src_aux].does_it_point_to(self.vertices[dest_aux])
 
    def __longitud__(self):
        return len(self.vertices)
 
    def __iter__(self):
        return iter(self.vertices.values())
    
class Vertice:
    def __init__(self, aux):
        self.aux = aux
        self.points_to = {}
 
    def get_aux(self):
        return self.aux
 
    def add_neighbour(self, dest, weight):
        self.points_to[dest] = weight
 
    def get_neighbours(self):
        return self.points_to.auxs()
 
    def get_pesos(self, dest):
        return self.points_to[dest]
 
    def apuntaA(self, dest):
        return dest in self.points_to