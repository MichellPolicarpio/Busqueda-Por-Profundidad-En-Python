# 🔍 Implementación de Búsqueda por Profundidad (DFS) en Grafos

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python 3.x">
  <img src="https://img.shields.io/badge/Curso-IA-green.svg" alt="Curso IA">
  <img src="https://img.shields.io/badge/UV-FIEE-purple.svg" alt="UV FIEE">
</div>

## 📝 Descripción
Este repositorio contiene dos implementaciones de búsqueda por profundidad (DFS - Depth-First Search) en grafos utilizando Python. Las implementaciones muestran el proceso paso a paso de la búsqueda, permitiendo visualizar el estado de la pila, los nodos visitados y el orden de visita en tiempo real. La búsqueda por profundidad explora un camino hasta su máxima profundidad antes de retroceder y explorar otros caminos.

## 🗂️ Estructura del Repositorio
```
📦 dfs-grafos
 ┣ 📜 grafo1.py - Implementación con grafo numérico
 ┗ 📜 grafo2.py - Implementación con grafo de nombres
```

## ✨ Características
- 📊 Visualización paso a paso del proceso de búsqueda
- 🔍 Seguimiento de nodos visitados usando pila (LIFO)
- 📝 Impresión del estado de la pila en cada paso
- 📈 Manejo de grafos mediante listas de adyacencia
- ⚡ Implementación usando pilas para exploración en profundidad

## 💻 Ejemplos de Uso

### 🔢 Grafo 1 (Numérico)
```python
grafo = {
    '1': ['2', '5'],
    '2': ['1', '5', '3'],
    '3': ['4', '2'],
    '4': ['5', '3'],
    '5': ['1', '2', '4'],
    '6': ['4']
}
origen = '6'
```

### 👥 Grafo 2 (Nombres)
```python
grafo = {
    'Lupe': ['Ernesto'],
    'Ernesto': ['Amaia', 'Juan'],
    'Amaia': ['Amilcar', 'Pedro', 'Ernesto'],
    'Pedro': ['Amilcar', 'Amaia'],
    'Amilcar': ['Amaia', 'Pedro', 'Juan'],
    'Ana': ['Pedro', 'Juan'],
    'Juan': ['Amilcar', 'Ana', 'Pepe', 'Ernesto'],
    'Pepe': ['Juan']
}
origen = 'Ernesto'
```

## 🚀 Ejecución
Para ejecutar cualquiera de los scripts:
```bash
# Ejecutar grafo numérico
python grafo1.py

# Ejecutar grafo de nombres
python grafo2.py
```

## 🛠️ Funcionalidades
- ✅ Implementación de DFS con seguimiento detallado
- 📊 Visualización del proceso de exploración en profundidad
- 🔄 Manejo de conjuntos para control de nodos visitados
- 📝 Impresión de estados intermedios durante la búsqueda
- 🔍 Exploración completa de cada rama antes de retroceder

## 📋 Requisitos
- Python 3.x
- No requiere módulos adicionales (usa listas nativas de Python como pilas)

## 📊 Ejemplo de Salida
La ejecución mostrará paso a paso:
- 🎯 Nodo actual en proceso
- ✅ Nodos marcados como visitados
- 📝 Estado de la pila LIFO
- 🔍 Nodos adyacentes no visitados
- 📊 Orden final de visita (exploración en profundidad)
- 🔄 Proceso de retroceso (backtracking) cuando se alcanza un nodo hoja

---
<div align="center">
  <small>Desarrollado con ❤️ para el curso de Introducción a la Inteligencia Artificial</small>
</div>
