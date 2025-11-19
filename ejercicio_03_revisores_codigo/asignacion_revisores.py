"""
Ejercicio 3: Asignación de Revisores de Código
Modelo de Asignación con Preferencias - Modelo de Investigación de Operaciones

Objetivo: Asignar revisores a pull requests considerando compatibilidad
y carga de trabajo.
"""

try:
    import pulp
    PULP_AVAILABLE = True
except ImportError:
    PULP_AVAILABLE = False


def resolver_asignacion_revisores():
    """
    Resuelve el problema de asignación de revisores a pull requests.
    """
    # Revisores disponibles
    revisores = ['Alice', 'Bob', 'Charlie', 'Diana']
    
    # Pull requests a revisar
    pull_requests = ['PR-001', 'PR-002', 'PR-003', 'PR-004', 'PR-005']
    
    # Matriz de costos (penalizaciones por incompatibilidad)
    # costo[i][j] = costo de asignar el revisor i al PR j
    # Costo bajo = buena compatibilidad, Costo alto = incompatibilidad
    costos = {
        ('Alice', 'PR-001'): 2, ('Alice', 'PR-002'): 5, ('Alice', 'PR-003'): 3,
        ('Alice', 'PR-004'): 4, ('Alice', 'PR-005'): 2,
        ('Bob', 'PR-001'): 4, ('Bob', 'PR-002'): 2, ('Bob', 'PR-003'): 5,
        ('Bob', 'PR-004'): 3, ('Bob', 'PR-005'): 4,
        ('Charlie', 'PR-001'): 3, ('Charlie', 'PR-002'): 4, ('Charlie', 'PR-003'): 2,
        ('Charlie', 'PR-004'): 5, ('Charlie', 'PR-005'): 3,
        ('Diana', 'PR-001'): 5, ('Diana', 'PR-002'): 3, ('Diana', 'PR-003'): 4,
        ('Diana', 'PR-004'): 2, ('Diana', 'PR-005'): 5
    }
    
    # Capacidad máxima de revisiones por revisor
    capacidad_maxima = {
        'Alice': 2,
        'Bob': 2,
        'Charlie': 2,
        'Diana': 2
    }
    
    print("=" * 70)
    print("ASIGNACIÓN DE REVISORES DE CÓDIGO")
    print("=" * 70)
    
    print("\nRevisores disponibles:")
    for revisor in revisores:
        print(f"  - {revisor} (máximo {capacidad_maxima[revisor]} PRs)")
    
    print("\nPull Requests a revisar:")
    for pr in pull_requests:
        print(f"  - {pr}")
    
    print("\nMatriz de costos (compatibilidad):")
    print("  (Valor bajo = buena compatibilidad, Valor alto = incompatibilidad)")
    print("-" * 70)
    print(f"{'Revisor\\PR':<15}", end="")
    for pr in pull_requests:
        print(f"{pr:<10}", end="")
    print()
    print("-" * 70)
    for revisor in revisores:
        print(f"{revisor:<15}", end="")
        for pr in pull_requests:
            costo = costos.get((revisor, pr), 999)
            print(f"{costo:<10}", end="")
        print()
    print("-" * 70)
    
    if PULP_AVAILABLE:
        resolver_con_pulp(revisores, pull_requests, costos, capacidad_maxima)
    else:
        resolver_con_fuerza_bruta(revisores, pull_requests, costos, capacidad_maxima)


def resolver_con_pulp(revisores, pull_requests, costos, capacidad_maxima):
    """Resuelve usando programación lineal entera con PuLP"""
    # Crear problema
    problema = pulp.LpProblem("Asignacion_Revisores", pulp.LpMinimize)
    
    # Variables de decisión binarias
    x = pulp.LpVariable.dicts("Asignacion",
                              [(r, pr) for r in revisores for pr in pull_requests],
                              cat='Binary')
    
    # Función objetivo: minimizar costo total
    problema += pulp.lpSum([costos.get((r, pr), 999) * x[(r, pr)]
                           for r in revisores for pr in pull_requests])
    
    # Restricción: Cada PR debe ser asignado a exactamente un revisor
    for pr in pull_requests:
        problema += pulp.lpSum([x[(r, pr)] for r in revisores]) == 1
    
    # Restricción: Cada revisor tiene capacidad máxima
    for r in revisores:
        problema += pulp.lpSum([x[(r, pr)] for pr in pull_requests]) <= capacidad_maxima[r]
    
    # Resolver
    problema.solve(pulp.PULP_CBC_CMD(msg=0))
    
    if problema.status == pulp.LpStatusOptimal:
        print("\n" + "=" * 70)
        print("SOLUCIÓN ÓPTIMA")
        print("=" * 70)
        
        asignaciones = {}
        costo_total = 0
        
        for r in revisores:
            asignaciones[r] = []
            for pr in pull_requests:
                if pulp.value(x[(r, pr)]) == 1:
                    asignaciones[r].append(pr)
                    costo_total += costos.get((r, pr), 999)
        
        print("\nAsignaciones:")
        print("-" * 70)
        for r in revisores:
            if asignaciones[r]:
                prs_str = ", ".join(asignaciones[r])
                print(f"{r:<15} -> {prs_str}")
            else:
                print(f"{r:<15} -> (sin asignaciones)")
        
        print("-" * 70)
        print(f"\nCosto total mínimo: {costo_total}")
        print(f"Estado: {pulp.LpStatus[problema.status]}")
        print("=" * 70)
    else:
        print("\nNo se encontró solución factible.")


def resolver_con_fuerza_bruta(revisores, pull_requests, costos, capacidad_maxima):
    """Resuelve usando fuerza bruta (para problemas pequeños)"""
    from itertools import product
    
    print("\n⚠ PuLP no está instalado. Usando método de fuerza bruta...")
    print("   Instala PuLP para mejor rendimiento: pip install pulp")
    
    # Generar todas las asignaciones posibles
    mejor_costo = float('inf')
    mejor_asignacion = None
    
    # Cada PR puede ser asignado a cualquier revisor
    for asignacion in product(revisores, repeat=len(pull_requests)):
        # Verificar restricciones de capacidad
        conteo = {r: 0 for r in revisores}
        for pr_idx, revisor in enumerate(asignacion):
            conteo[revisor] += 1
        
        # Verificar si cumple capacidad máxima
        factible = all(conteo[r] <= capacidad_maxima[r] for r in revisores)
        
        if factible:
            # Calcular costo
            costo = sum(costos.get((asignacion[i], pull_requests[i]), 999)
                       for i in range(len(pull_requests)))
            
            if costo < mejor_costo:
                mejor_costo = costo
                mejor_asignacion = asignacion
    
    if mejor_asignacion:
        print("\n" + "=" * 70)
        print("SOLUCIÓN ÓPTIMA")
        print("=" * 70)
        
        asignaciones = {r: [] for r in revisores}
        for i, revisor in enumerate(mejor_asignacion):
            asignaciones[revisor].append(pull_requests[i])
        
        print("\nAsignaciones:")
        print("-" * 70)
        for r in revisores:
            if asignaciones[r]:
                prs_str = ", ".join(asignaciones[r])
                print(f"{r:<15} -> {prs_str}")
            else:
                print(f"{r:<15} -> (sin asignaciones)")
        
        print("-" * 70)
        print(f"\nCosto total mínimo: {mejor_costo}")
        print("=" * 70)


if __name__ == "__main__":
    resolver_asignacion_revisores()

