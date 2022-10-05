from doctest import Example
from xml.dom import minidom
from cola import ListaSimple

doc = minidom.parse("C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab IPC2/Proyecto 2/Archivos de Entrada/Example.XML")

"""name = doc.getElementsByTagName("nombre")[0]
print(name.firstChild.data)

lista_empresas = doc.getElementsByTagName("empresa")
for empresa in lista_empresas:
       sid = empresa.getAttribute("id")
       print(sid)"""

lista = ListaSimple()
lista.agregarPrimero(2,"Hola","Penecito")
lista.recorrido()
lista.buscar(2,"Hola","Penecito")