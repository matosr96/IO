"""
Ejercicio: Asignación de Tareas a Programadores
Problema de Asignación - Modelo de Investigación de Operaciones

Objetivo: Minimizar el tiempo total asignando 4 tareas a 4 programadores
"""

import itertools

try:
    import numpy as np
    from scipy.optimize import linear_sum_assignment
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False


def resolver_asignacion():
    """
    Resuelve el problema de asignación usando el algoritmo húngaro.
    
    Matriz de costos (tiempos en horas):
    Filas: Programadores (Matos, Tania, Valeria, Salvador)
    Columnas: Tareas (1, 2, 3, 4)
    """
    if not SCIPY_AVAILABLE:
        print("scipy no está disponible. Usando solución con PuLP.")
        return None, None
    
    # Matriz de tiempos estimados (en horas)
    # Filas: Matos, Tania, Valeria, Salvador
    # Columnas: Tarea 1, Tarea 2, Tarea 3, Tarea 4
    tiempos = np.array([
        [6, 8, 7, 9],  # Matos
        [9, 6, 8, 7],  # Tania
        [7, 5, 9, 6],  # Valeria
        [8, 7, 6, 5]   # Salvador
    ])
    
    programadores = ['Matos', 'Tania', 'Valeria', 'Salvador']
    tareas = ['Tarea 1', 'Tarea 2', 'Tarea 3', 'Tarea 4']
    
    print("=" * 70)
    print("PROBLEMA DE ASIGNACIÓN: TAREAS A PROGRAMADORES")
    print("=" * 70)
    print("\nMatriz de tiempos estimados (horas):")
    print("-" * 70)
    print(f"{'Programador':<12}", end="")
    for tarea in tareas:
        print(f"{tarea:<12}", end="")
    print()
    print("-" * 70)
    
    for i, prog in enumerate(programadores):
        print(f"{prog:<12}", end="")
        for j in range(len(tareas)):
            print(f"{tiempos[i, j]:<12}", end="")
        print()
    print("-" * 70)
    
    # Resolver usando el algoritmo húngaro (minimización)
    # linear_sum_assignment encuentra la asignación óptima
    filas_asignadas, columnas_asignadas = linear_sum_assignment(tiempos)
    
    # Calcular el tiempo total mínimo
    tiempo_total = tiempos[filas_asignadas, columnas_asignadas].sum()
    
    print("\n" + "=" * 70)
    print("SOLUCIÓN ÓPTIMA")
    print("=" * 70)
    print("\nAsignaciones:")
    print("-" * 70)
    
    asignaciones = []
    for i, j in zip(filas_asignadas, columnas_asignadas):
        programador = programadores[i]
        tarea = tareas[j]
        tiempo = tiempos[i, j]
        asignaciones.append((programador, tarea, tiempo))
        print(f"{programador:<12} -> {tarea:<12} (Tiempo: {tiempo} horas)")
    
    print("-" * 70)
    print(f"\nTiempo total mínimo: {tiempo_total} horas")
    print("=" * 70)
    
    return asignaciones, tiempo_total


def resolver_sin_dependencias():
    """
    Resuelve el problema usando solo la biblioteca estándar de Python.
    Usa fuerza bruta con permutaciones (factible para problemas pequeños).
    """
    # Matriz de tiempos estimados (en horas)
    # Filas: Matos, Tania, Valeria, Salvador
    # Columnas: Tarea 1, Tarea 2, Tarea 3, Tarea 4
    tiempos = [
        [6, 8, 7, 9],  # Matos
        [9, 6, 8, 7],  # Tania
        [7, 5, 9, 6],  # Valeria
        [8, 7, 6, 5]   # Salvador
    ]
    
    programadores = ['Matos', 'Tania', 'Valeria', 'Salvador']
    tareas = ['Tarea 1', 'Tarea 2', 'Tarea 3', 'Tarea 4']
    
    print("=" * 70)
    print("PROBLEMA DE ASIGNACIÓN: TAREAS A PROGRAMADORES")
    print("SOLUCIÓN CON BIBLIOTECA ESTÁNDAR (sin dependencias)")
    print("=" * 70)
    print("\nMatriz de tiempos estimados (horas):")
    print("-" * 70)
    print(f"{'Programador':<12}", end="")
    for tarea in tareas:
        print(f"{tarea:<12}", end="")
    print()
    print("-" * 70)
    
    for i, prog in enumerate(programadores):
        print(f"{prog:<12}", end="")
        for j in range(len(tareas)):
            print(f"{tiempos[i][j]:<12}", end="")
        print()
    print("-" * 70)
    
    # Generar todas las permutaciones posibles de asignaciones
    # Cada permutación representa qué tarea hace cada programador
    # (índice de permutación = programador, valor = tarea)
    n = len(programadores)
    mejor_asignacion = None
    tiempo_minimo = float('inf')
    
    # Probar todas las permutaciones de [0, 1, 2, 3] que representan las tareas
    for permutacion in itertools.permutations(range(n)):
        tiempo_total = sum(tiempos[i][permutacion[i]] for i in range(n))
        if tiempo_total < tiempo_minimo:
            tiempo_minimo = tiempo_total
            mejor_asignacion = permutacion
    
    print("\n" + "=" * 70)
    print("SOLUCIÓN ÓPTIMA")
    print("=" * 70)
    print("\nAsignaciones:")
    print("-" * 70)
    
    asignaciones = []
    for i, tarea_idx in enumerate(mejor_asignacion):
        programador = programadores[i]
        tarea = tareas[tarea_idx]
        tiempo = tiempos[i][tarea_idx]
        asignaciones.append((programador, tarea, tiempo))
        print(f"{programador:<12} -> {tarea:<12} (Tiempo: {tiempo} horas)")
    
    print("-" * 70)
    print(f"\nTiempo total mínimo: {tiempo_minimo} horas")
    print("=" * 70)
    
    return asignaciones, tiempo_minimo


def resolver_con_pulp():
    """
    Resuelve el problema usando programación lineal con PuLP.
    Muestra la formulación completa del modelo.
    """
    try:
        import pulp
        
        print("\n" + "=" * 70)
        print("SOLUCIÓN ALTERNATIVA: PROGRAMACIÓN LINEAL (PuLP)")
        print("=" * 70)
        
        # Crear el problema de minimización
        problema = pulp.LpProblem("Asignacion_Tareas", pulp.LpMinimize)
        
        # Datos
        programadores = ['Matos', 'Tania', 'Valeria', 'Salvador']
        tareas = ['Tarea1', 'Tarea2', 'Tarea3', 'Tarea4']
        
        tiempos = {
            ('Matos', 'Tarea1'): 6, ('Matos', 'Tarea2'): 8, ('Matos', 'Tarea3'): 7, ('Matos', 'Tarea4'): 9,
            ('Tania', 'Tarea1'): 9, ('Tania', 'Tarea2'): 6, ('Tania', 'Tarea3'): 8, ('Tania', 'Tarea4'): 7,
            ('Valeria', 'Tarea1'): 7, ('Valeria', 'Tarea2'): 5, ('Valeria', 'Tarea3'): 9, ('Valeria', 'Tarea4'): 6,
            ('Salvador', 'Tarea1'): 8, ('Salvador', 'Tarea2'): 7, ('Salvador', 'Tarea3'): 6, ('Salvador', 'Tarea4'): 5
        }
        
        # Variables de decisión binarias
        x = pulp.LpVariable.dicts("Asignacion", 
                                   [(p, t) for p in programadores for t in tareas],
                                   cat='Binary')
        
        # Función objetivo: Minimizar tiempo total
        problema += pulp.lpSum([tiempos[(p, t)] * x[(p, t)] 
                                for p in programadores for t in tareas])
        
        # Restricciones: Cada tarea debe ser asignada a exactamente un programador
        for t in tareas:
            problema += pulp.lpSum([x[(p, t)] for p in programadores]) == 1
        
        # Restricciones: Cada programador debe recibir exactamente una tarea
        for p in programadores:
            problema += pulp.lpSum([x[(p, t)] for t in tareas]) == 1
        
        # Resolver
        problema.solve(pulp.PULP_CBC_CMD(msg=0))
        
        print("\nAsignaciones:")
        print("-" * 70)
        tiempo_total = 0
        for p in programadores:
            for t in tareas:
                if pulp.value(x[(p, t)]) == 1:
                    tiempo = tiempos[(p, t)]
                    tiempo_total += tiempo
                    print(f"{p:<12} -> {t:<12} (Tiempo: {tiempo} horas)")
        
        print("-" * 70)
        print(f"\nTiempo total mínimo: {tiempo_total} horas")
        print(f"Estado de la solución: {pulp.LpStatus[problema.status]}")
        print("=" * 70)
        
    except ImportError:
        print("\nPuLP no está instalado. Instálalo con: pip install pulp")
        print("Usando solo la solución con scipy.")


if __name__ == "__main__":
    # Solución que funciona sin dependencias (biblioteca estándar)
    print("\n" + "=" * 70)
    print("MÉTODO 1: SOLUCIÓN CON BIBLIOTECA ESTÁNDAR")
    print("=" * 70)
    asignaciones_std, tiempo_std = resolver_sin_dependencias()
    
    # Solución usando algoritmo húngaro (scipy) - si está disponible
    if SCIPY_AVAILABLE:
        print("\n" + "=" * 70)
        print("MÉTODO 2: ALGORITMO HÚNGARO (scipy)")
        print("=" * 70)
        asignaciones_scipy, tiempo_scipy = resolver_asignacion()
    
    # Solución usando programación lineal (PuLP) - si está disponible
    try:
        import pulp
        print("\n" + "=" * 70)
        print("MÉTODO 3: PROGRAMACIÓN LINEAL (PuLP)")
        print("=" * 70)
        resolver_con_pulp()
    except ImportError:
        pass
    
    print("\n" + "=" * 70)
    print("RESUMEN Y NOTAS:")
    print("=" * 70)
    print("- La solución con biblioteca estándar funciona sin instalar nada")
    print("- El algoritmo húngaro (scipy) es el más eficiente para problemas grandes")
    print("- La programación lineal (PuLP) muestra la formulación completa del modelo")
    print("- Todas las soluciones deben dar el mismo resultado óptimo")
    if not SCIPY_AVAILABLE:
        print("\nPara usar métodos avanzados, instala dependencias:")
        print("  pip install -r requirements.txt")
    print("=" * 70)

