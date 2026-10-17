# DDYA parcial práctico tercio 2

Explicaciones (En cuanto el funcionamiento principal de cada punto, no incluye resiliencia a erores)

El grafo se representa por medio de una lista de adyacencia, la cual es un diccionario que expresa las listas de vecinos con llaves que son cada elemento en el grafo.

BFS se implementó por medio de una cola de atención, se van atendiendo los nuevos nodos encontrados por cada proceso, siempre siguiendo la lógica FIFO, donde el frente es el inicio de la lista que es la cola.

DFS se aplica a través de un recorrido recursivo, el cual va cambiando el recorrido y los visitados, para finalmente darnos el orden adecuado por profundidad.

La mayoría de funciones se sintetizaron dentro de una sola clase, RedSocial.

La búsqueda de una nueva ruta, se provee requiriendo un origen y un objetivo, se navega por medio de BFS el grafo, en el proceso no es necesario registrar recorrido, entonces la diferencia es que se almacenan los padres de cada nodo visitado, de esta manera se almacena un recorrido desde el objetivo a el origen en la lista de padres, así solo obtenemos la ruta de interés, como se recorre desde el objetivo, al final aplicamos reverse, y el output es el recorrido más corto.

El agregar un nuevo usuario, se hace insertando el nombre del nuevo nodo, para después por medio de una función esencial de unión bidireccional, se entrelacen los nodos ya existentes seleccionados, con el usuario nuevo insertado.

