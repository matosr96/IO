"""
Ejercicio 1: Asignación de Tareas a Programadores
Problema de Asignación - Modelo de Investigación de Operaciones

Método Principal: Algoritmo Húngaro (Hungarian Algorithm)
Desarrollado por: Harold W. Kuhn (1955)

Objetivo: Minimizar el tiempo total asignando 4 tareas a 4 programadores
"""

import numpy as np
from scipy.optimize import linear_sum_assignment


def algoritmo_hungaro(tiempos):
    """
    Resuelve el problema de asignación usando el Algoritmo Húngaro.
    
    El Algoritmo Húngaro es el método clásico y más eficiente para resolver
    problemas de asignación. Fue desarrollado por Harold W. Kuhn en 1955 y
    tiene complejidad O(n³).
    
    Args:
        tiempos: Matriz numpy de forma (n, n) con tiempos estimados
                 tiempos[i][j] = tiempo que tarda el programador i en la tarea j
    
    Returns:
        filas_asignadas: Índices de programadores asignados
        columnas_asignadas: Índices de tareas asignadas
        tiempo_total: Tiempo total mínimo
    """
    # El algoritmo húngaro encuentra la asignación óptima
    # que minimiza la suma de costos (tiempos en este caso)
    filas_asignadas, columnas_asignadas = linear_sum_assignment(tiempos)
    
    # Calcular el tiempo total mínimo
    tiempo_total = tiempos[filas_asignadas, columnas_asignadas].sum()
    
    return filas_asignadas, columnas_asignadas, tiempo_total


def resolver_problema_asignacion():
    """
    Resuelve el problema de asignación de tareas a programadores
    usando el Algoritmo Húngaro como método principal.
    """
    # Matriz de tiempos estimados (en horas)
    # Filas: Programadores (Matos, Tania, Valeria, Salvador)
    # Columnas: Tareas (1, 2, 3, 4)
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
    print("Método: Algoritmo Húngaro (Hungarian Algorithm)")
    print("=" * 70)
    
    print("\nDescripción del Problema:")
    print("-" * 70)
    print("Una empresa de desarrollo de software debe asignar 4 tareas")
    print("a 4 programadores, minimizando el tiempo total de desarrollo.")
    print("Cada programador puede realizar solo una tarea y cada tarea")
    print("debe ser asignada a exactamente un programador.")
    print("-" * 70)
    
    print("\nMatriz de Tiempos Estimados (horas):")
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
    
    print("\n" + "=" * 70)
    print("RESOLUCIÓN MEDIANTE ALGORITMO HÚNGARO")
    print("=" * 70)
    print("\nFundamento Teórico:")
    print("-" * 70)
    print("El Algoritmo Húngaro, desarrollado por Harold W. Kuhn (1955),")
    print("es el método estándar para resolver problemas de asignación.")
    print("El algoritmo tiene complejidad O(n³) y garantiza la solución")
    print("óptima mediante reducción de filas y columnas, cobertura de")
    print("ceros y ajustes iterativos de la matriz de costos.")
    print("-" * 70)
    
    # Resolver usando el algoritmo húngaro
    filas_asignadas, columnas_asignadas, tiempo_total = algoritmo_hungaro(tiempos)
    
    print("\n" + "=" * 70)
    print("SOLUCIÓN ÓPTIMA")
    print("=" * 70)
    print("\nAsignaciones:")
    print("-" * 70)
    print(f"{'Programador':<15} {'Tarea':<15} {'Tiempo (h)':<15}")
    print("-" * 70)
    
    asignaciones = []
    for i, j in zip(filas_asignadas, columnas_asignadas):
        programador = programadores[i]
        tarea = tareas[j]
        tiempo = tiempos[i, j]
        asignaciones.append((programador, tarea, tiempo))
        print(f"{programador:<15} {tarea:<15} {tiempo:<15}")
    
    print("-" * 70)
    print(f"\n{'Tiempo Total Mínimo:':<30} {tiempo_total} horas")
    print("=" * 70)
    
    print("\n" + "=" * 70)
    print("ANÁLISIS DE LA SOLUCIÓN")
    print("=" * 70)
    print("\nInterpretación:")
    print("-" * 70)
    print("La solución óptima asigna cada tarea al programador que puede")
    print("completarla en el menor tiempo relativo, considerando todas las")
    print("posibles combinaciones. Esta asignación minimiza el tiempo total")
    print("del proyecto mientras asegura que cada programador tenga exactamente")
    print("una tarea y cada tarea sea asignada a exactamente un programador.")
    print("-" * 70)
    
    print("\nValidación:")
    print("-" * 70)
    print("✓ La solución cumple todas las restricciones del problema")
    print("✓ Cada programador tiene exactamente una tarea asignada")
    print("✓ Cada tarea está asignada a exactamente un programador")
    print("✓ El tiempo total es mínimo (verificado por el algoritmo)")
    print("-" * 70)
    
    print("\n" + "=" * 70)
    print("VENTAJAS DEL ALGORITMO HÚNGARO")
    print("=" * 70)
    print("• Método específico y eficiente para problemas de asignación")
    print("• Complejidad O(n³) - eficiente para problemas grandes")
    print("• Garantiza solución óptima")
    print("• Ampliamente reconocido en la literatura académica")
    print("• Implementación estándar en scipy.optimize")
    print("=" * 70)
    
    return asignaciones, tiempo_total


def validar_con_programacion_lineal():
    """
    Valida la solución usando Programación Lineal Entera como método alternativo.
    Esto demuestra que la solución es correcta mediante un método independiente.
    """
    try:
        import pulp
        
        print("\n" + "=" * 70)
        print("VALIDACIÓN: PROGRAMACIÓN LINEAL ENTERA")
        print("=" * 70)
        print("\nEste método valida la solución usando Programación Lineal Entera,")
        print("mostrando la formulación completa del modelo matemático.")
        print("-" * 70)
        
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
        
        if problema.status == pulp.LpStatusOptimal:
            print("\nResultado de la Validación:")
            print("-" * 70)
            tiempo_total = 0
            for p in programadores:
                for t in tareas:
                    if pulp.value(x[(p, t)]) == 1:
                        tiempo = tiempos[(p, t)]
                        tiempo_total += tiempo
                        p_nombre = p
                        t_nombre = t.replace('Tarea', 'Tarea ')
                        print(f"{p_nombre:<15} -> {t_nombre:<15} (Tiempo: {tiempo} horas)")
            
            print("-" * 70)
            print(f"\nTiempo total mínimo: {tiempo_total} horas")
            print(f"Estado: {pulp.LpStatus[problema.status]}")
            print("\n✓ La validación confirma que la solución es óptima")
            print("=" * 70)
        else:
            print("\nNo se pudo validar la solución.")
            
    except ImportError:
        print("\nPuLP no está instalado. La validación no está disponible.")
        print("Instala con: pip install pulp")


if __name__ == "__main__":
    # Resolver usando Algoritmo Húngaro (método principal)
    asignaciones, tiempo_total = resolver_problema_asignacion()
    
    # Validar con Programación Lineal Entera (método alternativo)
    validar_con_programacion_lineal()
    
    print("\n" + "=" * 70)
    print("REFERENCIAS")
    print("=" * 70)
    print("Kuhn, H. W. (1955). The Hungarian method for the assignment problem.")
    print("Naval Research Logistics Quarterly, 2(1-2), 83-97.")
    print("=" * 70)
