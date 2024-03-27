#  Escribir en Python las instrucciones para el desarrollo de un sistema inteligente que a partir de una base de conocimiento escrito en reglas lógicas, desarrolle la mejor ruta para moverse desde un punto A y un punto B en el sistema de transporte masivo local.


import networkx as nx

Rutas = nx.DiGraph()
Rutas.add_edge("ESTACION A","ESTACION B",weight=7.0)
Rutas.add_edge("ESTACION A","ESTACION C",weight=11.0)
Rutas.add_edge("ESTACION A","ESTACION D",weight=42.0)
Rutas.add_edge("ESTACION B","ESTACION A",weight=7.0)
Rutas.add_edge("ESTACION B","ESTACION D",weight=5.0)
Rutas.add_edge("ESTACION B","ESTACION E",weight=15.0)
Rutas.add_edge("ESTACION B","ESTACION F",weight=5.0)
Rutas.add_edge("ESTACION C","ESTACION D",weight=3.0)
Rutas.add_edge("ESTACION D","ESTACION B",weight=5.0)
Rutas.add_edge("ESTACION D","ESTACION F",weight=20.0)
Rutas.add_edge("ESTACION E","ESTACION F",weight=19.0)
Rutas.add_edge("ESTACION F","ESTACION B",weight=5.0)

source = input("Por favor ingresar el nombre de la ESTACION inicial:")
target = input("Por favor ingresar el nombre de la ESTACION final:")

MejorRuta = nx.dijkstra_path(Rutas, source= source, target= target)
RecorridoRuta = nx.dijkstra_path_length(Rutas, source= "ESTACION E", target="ESTACION B");

print("El mejor recorrido");
print(MejorRuta);
print("Km recorridos de la ruta =");
print(RecorridoRuta);
