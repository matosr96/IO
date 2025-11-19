"""
Ejercicio 8: Estado de Bugs (Cadena de Markov)
Modelo de Cadena de Markov - Modelo de Investigación de Operaciones

Objetivo: Modelar la evolución de bugs a través de diferentes estados.
"""

import numpy as np


def multiplicar_matrices(matriz1, matriz2):
    """Multiplica dos matrices."""
    n = len(matriz1)
    resultado = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return resultado


def potencia_matriz(matriz, n):
    """Calcula la n-ésima potencia de una matriz."""
    if n == 1:
        return matriz
    if n == 0:
        # Matriz identidad
        size = len(matriz)
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    
    resultado = matriz
    for _ in range(n - 1):
        resultado = multiplicar_matrices(resultado, matriz)
    return resultado


def resolver_markov():
    """
    Resuelve el problema de evolución de bugs usando cadenas de Markov.
    """
    # Estados: New, InProgress, Fixed, Closed
    estados = ['New', 'InProgress', 'Fixed', 'Closed']
    
    # Matriz de transición P
    # P[i][j] = probabilidad de pasar del estado i al estado j
    P = [
        [0.6, 0.3, 0.1, 0.0],  # New
        [0.0, 0.5, 0.4, 0.1],  # InProgress
        [0.0, 0.0, 0.8, 0.2],  # Fixed
        [0.0, 0.0, 0.0, 1.0]   # Closed (absorbente)
    ]
    
    print("=" * 70)
    print("ESTADO DE BUGS - CADENA DE MARKOV")
    print("=" * 70)
    print("\nEstados:")
    for i, estado in enumerate(estados):
        print(f"  {i}: {estado}")
    
    print("\nMatriz de transición P:")
    print("-" * 70)
    print(f"{'Desde\\Hacia':<15}", end="")
    for estado in estados:
        print(f"{estado[:12]:<15}", end="")
    print()
    print("-" * 70)
    
    for i, estado in enumerate(estados):
        print(f"{estado:<15}", end="")
        for j in range(len(estados)):
            print(f"{P[i][j]:<15.3f}", end="")
        print()
    
    print("-" * 70)
    
    # Estado inicial: empezando en 'New'
    estado_inicial = [1.0, 0.0, 0.0, 0.0]  # 100% en New
    
    print("\nEstado inicial:")
    print("-" * 70)
    for i, estado in enumerate(estados):
        print(f"{estado}: {estado_inicial[i]:.3f}")
    
    # Calcular distribución después de varios pasos
    pasos = [1, 5, 10, 20, 50]
    
    print("\n" + "=" * 70)
    print("EVOLUCIÓN DE LA DISTRIBUCIÓN")
    print("=" * 70)
    
    for n in pasos:
        P_n = potencia_matriz(P, n)
        
        # Calcular distribución después de n pasos
        distribucion = [0.0] * len(estados)
        for j in range(len(estados)):
            for i in range(len(estados)):
                distribucion[j] += estado_inicial[i] * P_n[i][j]
        
        print(f"\nDespués de {n} pasos:")
        print("-" * 70)
        for i, estado in enumerate(estados):
            print(f"{estado}: {distribucion[i]:.4f}")
    
    # Distribución estacionaria/absorción (después de muchos pasos)
    P_50 = potencia_matriz(P, 50)
    distribucion_final = [0.0] * len(estados)
    for j in range(len(estados)):
        for i in range(len(estados)):
            distribucion_final[j] += estado_inicial[i] * P_50[i][j]
    
    print("\n" + "=" * 70)
    print("DISTRIBUCIÓN APROXIMADA (50 pasos - absorción)")
    print("=" * 70)
    for i, estado in enumerate(estados):
        print(f"{estado}: {distribucion_final[i]:.4f}")
    
    print("\n" + "=" * 70)
    print("INTERPRETACIÓN")
    print("=" * 70)
    print("La cadena de Markov modela la evolución de bugs a través de estados.")
    print("El estado 'Closed' es absorbente (probabilidad 1.0 de permanecer).")
    print("Después de suficientes pasos, todos los bugs terminan en 'Closed'.")
    print("=" * 70)
    
    return {
        "estados": estados,
        "matriz_transicion": P,
        "distribucion_final": distribucion_final
    }


if __name__ == "__main__":
    resolver_markov()

