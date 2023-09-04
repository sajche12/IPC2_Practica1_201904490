class Nodo:
    
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
class ListaEnlazada:
    
    def __init__(self):
        self.cabeza = None
    
    #Metodo para agregar un nodo a la lista
    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            aux = self.cabeza
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nuevo
    
    #Metodo para volver iterable la lista
    def __iter__(self):
        aux = self.cabeza
        while aux is not None:
            yield aux.dato
            aux = aux.siguiente
    
    