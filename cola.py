import os
import graphviz
from empresa import Empresa

class ListaSimple():
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def estaVacia(self):
        return self.primero==None

    def agregarPrimero(self, id, nombre, abreviatura):
        nuevo=Empresa(id, nombre, abreviatura)

        if self.estaVacia==True:
            self.primero=self.ultimo=nuevo
        else:
            temp=nuevo
            temp.siguiente=self.primero
            self.primero=temp

    def agregarUltimo(self, id, nombre, abreviatura):
        nuevo=Empresa(id, nombre, abreviatura)

        if self.estaVacia==True:
            self.primero=self.ultimo=nuevo
        else:
            temp=self.primero
            while temp.siguiente is not None:
                temp=temp.siguiente
            temp.siguiente=nuevo
    
    '''def agregarUltimo2(self, id, nombre, abreviatura):
        nuevo=Empresa(id, nombre, abreviatura)
        if self.estaVacia==True:
            self.primero=self.ultimo=nuevo
        else:
            temp=self.ultimo
            temp.siguiente=nuevo
            self.ultimo=temp'''

    def recorrido(self):
        temp=self.primero
        while temp!=None:
            print(temp.id, temp.nombre, temp.abreviatura)
            temp=temp.siguiente

    def buscar(self,id,nombre,abreviatura):
        busqueda=Empresa(id,nombre,abreviatura)

        aux=self.primero
        while aux:
            if aux.nombre==busqueda.nombre:
                print("Encontrado")
                return True
                
            else:
                aux=aux.siguiente
                if aux==self.primero:
                    return False