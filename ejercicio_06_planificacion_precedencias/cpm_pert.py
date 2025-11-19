"""
Ejercicio 6: Planificación con Precedencias (CPM/PERT)
Problema de Ruta Crítica - Modelo de Investigación de Operaciones

Objetivo: Determinar la ruta crítica en un proyecto de integración y despliegue.
"""


def calcular_tiempos_tempranos(tareas):
    """
    Calcula los tiempos más tempranos de inicio (ES) y finalización (EF).
    
    Args:
        tareas: Diccionario con estructura {tarea: {"dur": duracion, "pred": [predecesores]}}
    
    Returns:
        es: Tiempos más tempranos de inicio
        ef: Tiempos más tempranos de finalización
    """
    es = {}
    ef = {}
    
    # Encontrar tareas sin predecesores (inicio del proyecto)
    tareas_procesadas = set()
    
    while len(tareas_procesadas) < len(tareas):
        for tarea, info in tareas.items():
            if tarea in tareas_procesadas:
                continue
            
            pred = info["pred"]
            dur = info["dur"]
            
            # Si no tiene predecesores o todos están procesados
            if not pred or all(p in tareas_procesadas for p in pred):
                # ES = max(EF de predecesores)
                if not pred:
                    es[tarea] = 0
                else:
                    es[tarea] = max(ef[p] for p in pred)
                
                ef[tarea] = es[tarea] + dur
                tareas_procesadas.add(tarea)
    
    return es, ef


def calcular_tiempos_tardios(tareas, es, ef):
    """
    Calcula los tiempos más tardíos de inicio (LS) y finalización (LF).
    
    Args:
        tareas: Diccionario con estructura de tareas
        es: Tiempos más tempranos de inicio
        ef: Tiempos más tempranos de finalización
    
    Returns:
        ls: Tiempos más tardíos de inicio
        lf: Tiempos más tardíos de finalización
    """
    # Duración del proyecto = max(EF)
    duracion_proyecto = max(ef.values())
    
    ls = {}
    lf = {}
    
    # Construir grafo inverso (sucesores)
    sucesores = {t: [] for t in tareas}
    for tarea, info in tareas.items():
        for pred in info["pred"]:
            sucesores[pred].append(tarea)
    
    # Encontrar tareas sin sucesores (fin del proyecto)
    tareas_procesadas = set()
    
    while len(tareas_procesadas) < len(tareas):
        for tarea in tareas:
            if tarea in tareas_procesadas:
                continue
            
            # Si no tiene sucesores o todos están procesados
            if not sucesores[tarea] or all(s in tareas_procesadas for s in sucesores[tarea]):
                # LF = min(LS de sucesores) o duración del proyecto si no tiene sucesores
                if not sucesores[tarea]:
                    lf[tarea] = duracion_proyecto
                else:
                    lf[tarea] = min(ls[s] for s in sucesores[tarea])
                
                ls[tarea] = lf[tarea] - tareas[tarea]["dur"]
                tareas_procesadas.add(tarea)
    
    return ls, lf


def calcular_holguras(es, ef, ls, lf):
    """
    Calcula las holguras (slack) de cada tarea.
    
    Holgura = LS - ES = LF - EF
    """
    holguras = {}
    for tarea in es:
        holguras[tarea] = ls[tarea] - es[tarea]
    return holguras


def encontrar_ruta_critica(holguras):
    """
    Encuentra la ruta crítica (tareas con holgura = 0).
    """
    return [tarea for tarea, holgura in holguras.items() if holgura == 0]


def resolver_cpm():
    """
    Resuelve el problema de planificación con precedencias usando CPM.
    """
    # Datos: Tareas con duración y predecesores
    tareas = {
        "A": {"dur": 3, "pred": []},
        "B": {"dur": 2, "pred": ["A"]},
        "C": {"dur": 4, "pred": ["A"]},
        "D": {"dur": 2, "pred": ["B", "C"]},
        "E": {"dur": 3, "pred": ["C"]},
        "F": {"dur": 1, "pred": ["D", "E"]}
    }
    
    print("=" * 70)
    print("PLANIFICACIÓN CON PRECEDENCIAS - MÉTODO CPM (RUTA CRÍTICA)")
    print("=" * 70)
    print("\nTareas del proyecto:")
    print("-" * 70)
    print(f"{'Tarea':<10} {'Duración':<15} {'Predecesores':<20}")
    print("-" * 70)
    
    for tarea, info in tareas.items():
        pred_str = ", ".join(info["pred"]) if info["pred"] else "Ninguna"
        print(f"{tarea:<10} {info['dur']:<15} {pred_str:<20}")
    
    print("-" * 70)
    
    # Calcular tiempos tempranos
    es, ef = calcular_tiempos_tempranos(tareas)
    
    # Calcular tiempos tardíos
    ls, lf = calcular_tiempos_tardios(tareas, es, ef)
    
    # Calcular holguras
    holguras = calcular_holguras(es, ef, ls, lf)
    
    # Encontrar ruta crítica
    ruta_critica = encontrar_ruta_critica(holguras)
    
    # Duración del proyecto
    duracion_proyecto = max(ef.values())
    
    print("\n" + "=" * 70)
    print("RESULTADOS DEL ANÁLISIS CPM")
    print("=" * 70)
    
    print("\nTiempos más tempranos:")
    print("-" * 70)
    print(f"{'Tarea':<10} {'ES':<10} {'EF':<10}")
    print("-" * 70)
    for tarea in sorted(es.keys()):
        print(f"{tarea:<10} {es[tarea]:<10} {ef[tarea]:<10}")
    
    print("\nTiempos más tardíos:")
    print("-" * 70)
    print(f"{'Tarea':<10} {'LS':<10} {'LF':<10}")
    print("-" * 70)
    for tarea in sorted(ls.keys()):
        print(f"{tarea:<10} {ls[tarea]:<10} {lf[tarea]:<10}")
    
    print("\nHolguras:")
    print("-" * 70)
    print(f"{'Tarea':<10} {'Holgura':<10}")
    print("-" * 70)
    for tarea in sorted(holguras.keys()):
        print(f"{tarea:<10} {holguras[tarea]:<10}")
    
    print("\n" + "=" * 70)
    print("RUTA CRÍTICA")
    print("=" * 70)
    print(f"\nTareas en ruta crítica: {' → '.join(ruta_critica)}")
    print(f"Duración del proyecto (tiempo mínimo): {duracion_proyecto} unidades de tiempo")
    print("=" * 70)
    
    return {
        "es": es,
        "ef": ef,
        "ls": ls,
        "lf": lf,
        "holguras": holguras,
        "ruta_critica": ruta_critica,
        "duracion": duracion_proyecto
    }


if __name__ == "__main__":
    resolver_cpm()

