# Policarpio Moran Michell Alexis - zS21002379 - Ingenieria Informática - FIEE - UV
# Busqueda por profundidad - Grafo 1 - Introduccion A La Inteligencia Artificial

def dfs_paso_a_paso(grafo, origen):
    # Crea un conjunto para almacenar los nodos visitados
    visitados = set()
    
    # Crea una lista para almacenar el orden de visita de los nodos
    orden_visita = []
    
    # Crea una pila con el nodo de origen como elemento inicial
    pila = [origen]
    
    # Imprime un mensaje indicando el inicio de la búsqueda
    print(f"Iniciando búsqueda desde el nodo que ha elegido {origen}...")
    
    # Imprime el grafo utilizado en la búsqueda
    # Recuerda agruparlos como CONJUNTO ya que es un grupo de elementos que se 
    # encuentran acotados de forma desordenada y NO pueden existir elementos 
    # duplicados en los conjuntos
    print(f"El Grafo es: {grafo}")
    
    # Imprime la pila inicial con el nodo de origen
    print(f"Nodo inicial: {pila}")
    
    # Inicia un bucle while que continúa hasta que la memoria LIFO esté vacía.
    while pila:
        # Extrae el nodo que está en el tope de la pila.
        nodo = pila.pop()
        
        # Imprime el nodo actual en proceso
        print(f"\nProcesando nodo: {nodo}")
        
        # Verifica si el nodo actual no ha sido visitado
        if nodo not in visitados:
            # Imprime un mensaje indicando que se marca el nodo como visitado
            print(f"Marcando {nodo} como visitado")
            
            # Agrega el nodo actual al conjunto de nodos visitados
            visitados.add(nodo)
            
            # Agrega el nodo actual a la lista de orden de visita
            orden_visita.append(nodo)
            
            # Obtiene los adyacentes del nodo actual que no han sido visitados
            # Los invertimos para mantener el orden de exploración deseado
            adyacentes = [adyacente for adyacente in reversed(grafo[nodo]) if adyacente not in visitados]
            
            # Imprime un mensaje con los NODOS adyacentes NO visitados del nodo actual
            print(f"Nodos adyacentes no visitados de {nodo}: {adyacentes}")
            
            # Agrega los adyacentes no visitados a la pila
            pila.extend(adyacentes)
        
        # Imprime la pila actual después de procesar el nodo
        print(f"Pila actual: {pila}")
        
        # Imprime la lista de nodos visitados hasta el momento.
        print(f"Nodos visitados hasta ahora: {orden_visita}")
    
    # Imprime un mensaje indicando el final de la búsqueda.
    print(f"\nBúsqueda finalizada. Orden de visita en que se realizo la busqueda: {orden_visita}")
    
    # Retorna la lista de nodos visitados en el orden de visita.
    return orden_visita

# Verificando el Grafo si el script se ejecuta directamente (no importado)
# usando __name__== "__main__" el nombre del entorno de máximo nivel del programa
if __name__ == "__main__":
    # Definiendo el grafo del ejemplo mediante una lista de adyacencia
    grafo = {
        '1': ['2', '5'],
        '2': ['1', '5', '3'],
        '3': ['4', '2'],
        '4': ['5', '3'],
        '5': ['1', '2', '4'],
        '6': ['4']
    }
    # Selecciona el nodo de origen para la búsqueda
    origen = '6'
    
    # Ejecuta la función dfs_paso_a_paso con el grafo y nodo de origen
    dfs_paso_a_paso(grafo, origen)