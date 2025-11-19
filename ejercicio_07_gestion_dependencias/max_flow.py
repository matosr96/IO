"""
Ejercicio 7: Gestión de Dependencias y Flujo de Trabajo (Redes de Flujo)
Modelo de Flujo Máximo - Modelo de Investigación de Operaciones

Objetivo: Asignar capacidad de integración entre ramas y entornos para
maximizar throughput de entregas.
"""

try:
    import networkx as nx
    NETWORKX_AVAILABLE = True
except ImportError:
    NETWORKX_AVAILABLE = False


def resolver_max_flow():
    """
    Resuelve el problema de flujo máximo para gestión de dependencias.
    """
    print("=" * 70)
    print("GESTIÓN DE DEPENDENCIAS - FLUJO MÁXIMO")
    print("=" * 70)
    
    # Definir la red
    # Nodos representan colas/entornos
    # Arcos representan capacidades de integración
    
    if NETWORKX_AVAILABLE:
        resolver_con_networkx()
    else:
        resolver_con_pulp()


def resolver_con_networkx():
    """Resuelve usando NetworkX (algoritmo de Edmonds-Karp)"""
    # Crear grafo dirigido
    G = nx.DiGraph()
    
    # Agregar nodos
    # Fuente: desarrollo
    # Nodos intermedios: ramas y entornos
    # Sumidero: producción
    
    nodos = {
        'source': 'Desarrollo',
        'branch_dev': 'Rama Dev',
        'branch_staging': 'Rama Staging',
        'env_test': 'Entorno Test',
        'env_staging': 'Entorno Staging',
        'env_prod': 'Entorno Prod',
        'sink': 'Producción'
    }
    
    # Agregar arcos con capacidades
    # (origen, destino, capacidad)
    arcos = [
        ('source', 'branch_dev', 10),
        ('source', 'branch_staging', 8),
        ('branch_dev', 'env_test', 6),
        ('branch_dev', 'env_staging', 5),
        ('branch_staging', 'env_staging', 7),
        ('env_test', 'env_staging', 4),
        ('env_staging', 'env_prod', 8),
        ('env_prod', 'sink', 10)
    ]
    
    G.add_weighted_edges_from(arcos, weight='capacity')
    
    print("\nRed de flujo:")
    print("-" * 70)
    print("Nodos (colas/entornos):")
    for nodo, nombre in nodos.items():
        print(f"  {nodo}: {nombre}")
    
    print("\nArcos (capacidades de integración):")
    print("-" * 70)
    print(f"{'Origen':<20} {'Destino':<20} {'Capacidad':<15}")
    print("-" * 70)
    for origen, destino, capacidad in arcos:
        print(f"{nodos.get(origen, origen):<20} {nodos.get(destino, destino):<20} {capacidad:<15}")
    
    # Calcular flujo máximo
    valor_flujo, flujo_dict = nx.maximum_flow(G, 'source', 'sink', capacity='capacity')
    
    print("\n" + "=" * 70)
    print("SOLUCIÓN: FLUJO MÁXIMO")
    print("=" * 70)
    print(f"\nValor del flujo máximo: {valor_flujo}")
    
    print("\nFlujo por arco:")
    print("-" * 70)
    print(f"{'Origen':<20} {'Destino':<20} {'Flujo':<15} {'Capacidad':<15}")
    print("-" * 70)
    
    for origen, destino, capacidad in arcos:
        flujo = flujo_dict[origen].get(destino, 0)
        print(f"{nodos.get(origen, origen):<20} {nodos.get(destino, destino):<20} {flujo:<15} {capacidad:<15}")
    
    # Identificar cuellos de botella (arcos saturados)
    print("\nCuellos de botella (arcos saturados):")
    print("-" * 70)
    cuellos = []
    for origen, destino, capacidad in arcos:
        flujo = flujo_dict[origen].get(destino, 0)
        if abs(flujo - capacidad) < 1e-6:  # Saturado
            cuellos.append((origen, destino, capacidad))
            print(f"  {nodos.get(origen, origen)} -> {nodos.get(destino, destino)} (capacidad: {capacidad})")
    
    if not cuellos:
        print("  No hay cuellos de botella identificados.")
    
    print("\n" + "=" * 70)
    print("INTERPRETACIÓN")
    print("=" * 70)
    print(f"El throughput máximo del pipeline es {valor_flujo} entregas/unidad de tiempo.")
    print("Para aumentar el throughput, considera:")
    print("  - Aumentar capacidad en cuellos de botella")
    print("  - Paralelizar pipelines")
    print("  - Optimizar procesos de integración")
    print("=" * 70)
    
    return valor_flujo, flujo_dict


def resolver_con_pulp():
    """Resuelve usando PuLP (formulación de programación lineal)"""
    try:
        import pulp
        
        print("\n⚠ NetworkX no está instalado. Usando PuLP...")
        print("   Instala NetworkX para mejor rendimiento: pip install networkx")
        
        # Definir red (mismo ejemplo)
        nodos = ['source', 'branch_dev', 'branch_staging', 'env_test', 
                'env_staging', 'env_prod', 'sink']
        
        arcos = [
            ('source', 'branch_dev', 10),
            ('source', 'branch_staging', 8),
            ('branch_dev', 'env_test', 6),
            ('branch_dev', 'env_staging', 5),
            ('branch_staging', 'env_staging', 7),
            ('env_test', 'env_staging', 4),
            ('env_staging', 'env_prod', 8),
            ('env_prod', 'sink', 10)
        ]
        
        # Crear problema
        problema = pulp.LpProblem("Max_Flow", pulp.LpMaximize)
        
        # Variables: flujo en cada arco
        f = {}
        for origen, destino, capacidad in arcos:
            f[(origen, destino)] = pulp.LpVariable(f"f_{origen}_{destino}", 
                                                     lowBound=0, upBound=capacidad)
        
        # Función objetivo: maximizar flujo al sumidero
        problema += pulp.lpSum([f[(origen, destino)] 
                                for origen, destino, _ in arcos 
                                if destino == 'sink'])
        
        # Restricciones de conservación de flujo (para cada nodo intermedio)
        nodos_intermedios = [n for n in nodos if n not in ['source', 'sink']]
        for nodo in nodos_intermedios:
            # Flujo entrante = Flujo saliente
            flujo_entrante = pulp.lpSum([f[(o, d)] for o, d, _ in arcos if d == nodo])
            flujo_saliente = pulp.lpSum([f[(o, d)] for o, d, _ in arcos if o == nodo])
            problema += flujo_entrante == flujo_saliente
        
        # Resolver
        problema.solve(pulp.PULP_CBC_CMD(msg=0))
        
        if problema.status == pulp.LpStatusOptimal:
            print("\n" + "=" * 70)
            print("SOLUCIÓN: FLUJO MÁXIMO")
            print("=" * 70)
            
            valor_flujo = pulp.value(problema.objective)
            print(f"\nValor del flujo máximo: {valor_flujo}")
            
            print("\nFlujo por arco:")
            print("-" * 70)
            for origen, destino, capacidad in arcos:
                flujo = pulp.value(f[(origen, destino)])
                print(f"{origen} -> {destino}: {flujo:.2f} / {capacidad}")
            
            print("=" * 70)
        else:
            print("\nNo se encontró solución óptima.")
            
    except ImportError:
        print("\nPuLP no está instalado. Instálalo con: pip install pulp")
        print("O instala NetworkX: pip install networkx")


if __name__ == "__main__":
    resolver_max_flow()

