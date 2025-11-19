"""
Ejercicio 10: Optimización Multiobjetivo
Modelo de Programación Lineal Entera Multiobjetivo - Modelo de Investigación de Operaciones

Objetivo: Asignación de tareas donde además de tiempo se consideran costos
(salarios por hora distintos) y se requiere equilibrio entre ambas métricas.
"""

try:
    import pulp
    PULP_AVAILABLE = True
except ImportError:
    PULP_AVAILABLE = False


def resolver_multiobjetivo():
    """
    Resuelve el problema de optimización multiobjetivo.
    """
    # Programadores con salarios por hora
    programadores = ['Ana', 'Luis', 'Marta', 'Carlos']
    salarios = {
        'Ana': 50,    # $/hora
        'Luis': 45,
        'Marta': 55,
        'Carlos': 40
    }
    
    # Tareas con tiempos estimados
    tareas = ['Tarea 1', 'Tarea 2', 'Tarea 3', 'Tarea 4']
    
    # Matriz de tiempos (horas)
    tiempos = {
        ('Ana', 'Tarea 1'): 6, ('Ana', 'Tarea 2'): 8, ('Ana', 'Tarea 3'): 7, ('Ana', 'Tarea 4'): 9,
        ('Luis', 'Tarea 1'): 9, ('Luis', 'Tarea 2'): 6, ('Luis', 'Tarea 3'): 8, ('Luis', 'Tarea 4'): 7,
        ('Marta', 'Tarea 1'): 7, ('Marta', 'Tarea 2'): 5, ('Marta', 'Tarea 3'): 9, ('Marta', 'Tarea 4'): 6,
        ('Carlos', 'Tarea 1'): 8, ('Carlos', 'Tarea 2'): 7, ('Carlos', 'Tarea 3'): 6, ('Carlos', 'Tarea 4'): 5
    }
    
    # Calcular costos (tiempo * salario)
    costos = {}
    for (p, t), tiempo in tiempos.items():
        costos[(p, t)] = tiempo * salarios[p]
    
    print("=" * 70)
    print("OPTIMIZACIÓN MULTIOBJETIVO: TIEMPO vs COSTO")
    print("=" * 70)
    
    print("\nProgramadores y salarios:")
    print("-" * 70)
    for p in programadores:
        print(f"  {p}: ${salarios[p]}/hora")
    
    print("\nMatriz de tiempos (horas):")
    print("-" * 70)
    print(f"{'Programador\\Tarea':<20}", end="")
    for t in tareas:
        print(f"{t[:10]:<12}", end="")
    print()
    print("-" * 70)
    for p in programadores:
        print(f"{p:<20}", end="")
        for t in tareas:
            print(f"{tiempos.get((p, t), 0):<12}", end="")
        print()
    
    print("\nMatriz de costos ($):")
    print("-" * 70)
    print(f"{'Programador\\Tarea':<20}", end="")
    for t in tareas:
        print(f"{t[:10]:<12}", end="")
    print()
    print("-" * 70)
    for p in programadores:
        print(f"{p:<20}", end="")
        for t in tareas:
            costo = costos.get((p, t), 0)
            print(f"${costo:<11}", end="")
        print()
    
    if PULP_AVAILABLE:
        generar_frente_pareto(programadores, tareas, tiempos, costos)
    else:
        print("\n⚠ PuLP no está instalado. Instálalo con: pip install pulp")


def generar_frente_pareto(programadores, tareas, tiempos, costos):
    """Genera el frente de Pareto variando el peso α"""
    print("\n" + "=" * 70)
    print("GENERACIÓN DEL FRENTE DE PARETO")
    print("=" * 70)
    print("\nVariando α (peso del tiempo) de 0 a 1:")
    print("  α = 0: Solo minimizar costo")
    print("  α = 1: Solo minimizar tiempo")
    print("  0 < α < 1: Balance entre tiempo y costo")
    
    resultados = []
    alphas = [0.0, 0.25, 0.5, 0.75, 1.0]
    
    for alpha in alphas:
        tiempo_total, costo_total, asignaciones = resolver_con_alpha(
            programadores, tareas, tiempos, costos, alpha
        )
        resultados.append({
            'alpha': alpha,
            'tiempo': tiempo_total,
            'costo': costo_total,
            'asignaciones': asignaciones
        })
    
    print("\n" + "=" * 70)
    print("RESULTADOS DEL FRENTE DE PARETO")
    print("=" * 70)
    print(f"{'α':<10} {'Tiempo (h)':<15} {'Costo ($)':<15} {'Asignaciones':<30}")
    print("-" * 70)
    
    for res in resultados:
        asign_str = ", ".join([f"{p}->{t[:6]}" for p, t in res['asignaciones']])
        print(f"{res['alpha']:<10.2f} {res['tiempo']:<15} {res['costo']:<15.2f} {asign_str[:30]}")
    
    print("\n" + "=" * 70)
    print("INTERPRETACIÓN")
    print("=" * 70)
    print("El frente de Pareto muestra las soluciones no dominadas.")
    print("Cada punto representa un equilibrio diferente entre tiempo y costo.")
    print("Selecciona el α según la prioridad del proyecto:")
    print("  - Proyectos con deadline estricto: α alto (priorizar tiempo)")
    print("  - Proyectos con presupuesto limitado: α bajo (priorizar costo)")
    print("  - Balance: α = 0.5")
    print("=" * 70)


def resolver_con_alpha(programadores, tareas, tiempos, costos, alpha):
    """Resuelve el problema con un peso α dado"""
    # Crear problema
    problema = pulp.LpProblem("Multiobjetivo", pulp.LpMinimize)
    
    # Variables binarias
    x = pulp.LpVariable.dicts("Asignacion",
                              [(p, t) for p in programadores for t in tareas],
                              cat='Binary')
    
    # Función objetivo combinada: α*Tiempo + (1-α)*Costo
    tiempo_total = pulp.lpSum([tiempos[(p, t)] * x[(p, t)]
                               for p in programadores for t in tareas])
    costo_total = pulp.lpSum([costos[(p, t)] * x[(p, t)]
                              for p in programadores for t in tareas])
    
    problema += alpha * tiempo_total + (1 - alpha) * costo_total
    
    # Restricciones: cada tarea a un programador, cada programador una tarea
    for t in tareas:
        problema += pulp.lpSum([x[(p, t)] for p in programadores]) == 1
    
    for p in programadores:
        problema += pulp.lpSum([x[(p, t)] for t in tareas]) == 1
    
    # Resolver
    problema.solve(pulp.PULP_CBC_CMD(msg=0))
    
    if problema.status == pulp.LpStatusOptimal:
        asignaciones = []
        tiempo_real = 0
        costo_real = 0
        
        for p in programadores:
            for t in tareas:
                if pulp.value(x[(p, t)]) == 1:
                    asignaciones.append((p, t))
                    tiempo_real += tiempos[(p, t)]
                    costo_real += costos[(p, t)]
        
        return tiempo_real, costo_real, asignaciones
    
    return None, None, []


if __name__ == "__main__":
    resolver_multiobjetivo()

