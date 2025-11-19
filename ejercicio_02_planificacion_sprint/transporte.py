"""
Ejercicio 2: Planificación de Sprint con Recursos Limitados
Modelo de Transporte - Modelo de Investigación de Operaciones

Objetivo: Distribuir horas entre equipos para cubrir historias de usuario
respetando capacidad.
"""

try:
    import numpy as np
    from scipy.optimize import linprog
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False


def resolver_transporte():
    """
    Resuelve el problema de transporte para planificación de sprint.
    """
    # Equipos (origen) con horas disponibles
    equipos = ['Equipo A', 'Equipo B', 'Equipo C']
    oferta = [40, 50, 30]  # horas disponibles por equipo
    
    # Tipos de tareas (destino) con horas requeridas
    tareas = ['Tarea 1', 'Tarea 2', 'Tarea 3', 'Tarea 4']
    demanda = [30, 35, 25, 30]  # horas requeridas por tarea
    
    # Matriz de costos (costo = prioridad inversa o tiempo por asignación)
    # costo[i][j] = costo de asignar 1 hora del equipo i a la tarea j
    costos = [
        [2, 3, 4, 2],  # Equipo A
        [3, 2, 3, 4],  # Equipo B
        [4, 3, 2, 3]   # Equipo C
    ]
    
    print("=" * 70)
    print("PLANIFICACIÓN DE SPRINT - MODELO DE TRANSPORTE")
    print("=" * 70)
    
    print("\nOferta (horas disponibles por equipo):")
    print("-" * 70)
    for i, equipo in enumerate(equipos):
        print(f"{equipo}: {oferta[i]} horas")
    
    print("\nDemanda (horas requeridas por tarea):")
    print("-" * 70)
    for j, tarea in enumerate(tareas):
        print(f"{tarea}: {demanda[j]} horas")
    
    print("\nMatriz de costos:")
    print("-" * 70)
    print(f"{'Equipo\\Tarea':<15}", end="")
    for tarea in tareas:
        print(f"{tarea[:10]:<12}", end="")
    print()
    print("-" * 70)
    for i, equipo in enumerate(equipos):
        print(f"{equipo:<15}", end="")
        for j in range(len(tareas)):
            print(f"{costos[i][j]:<12}", end="")
        print()
    print("-" * 70)
    
    # Verificar balance (oferta total vs demanda total)
    oferta_total = sum(oferta)
    demanda_total = sum(demanda)
    
    print(f"\nOferta total: {oferta_total} horas")
    print(f"Demanda total: {demanda_total} horas")
    
    if oferta_total != demanda_total:
        print("\n⚠ Problema desbalanceado. Agregando dummy...")
        if oferta_total > demanda_total:
            # Agregar destino dummy
            tareas.append('Dummy')
            demanda.append(oferta_total - demanda_total)
            for i in range(len(equipos)):
                costos[i].append(0)
        else:
            # Agregar origen dummy
            equipos.append('Dummy')
            oferta.append(demanda_total - oferta_total)
            costos.append([0] * len(tareas))
    
    # Resolver con programación lineal
    if SCIPY_AVAILABLE:
        resolver_con_scipy(equipos, tareas, oferta, demanda, costos)
    else:
        resolver_con_pulp(equipos, tareas, oferta, demanda, costos)


def resolver_con_scipy(equipos, tareas, oferta, demanda, costos):
    """Resuelve usando scipy.optimize.linprog"""
    m = len(equipos)
    n = len(tareas)
    
    # Vector de costos (aplanar matriz)
    c = [costos[i][j] for i in range(m) for j in range(n)]
    
    # Restricciones de oferta: suma por fila <= oferta
    A_ub = []
    b_ub = []
    for i in range(m):
        row = [0] * (m * n)
        for j in range(n):
            row[i * n + j] = 1
        A_ub.append(row)
        b_ub.append(oferta[i])
    
    # Restricciones de demanda: suma por columna == demanda
    A_eq = []
    b_eq = []
    for j in range(n):
        row = [0] * (m * n)
        for i in range(m):
            row[i * n + j] = 1
        A_eq.append(row)
        b_eq.append(demanda[j])
    
    # Límites: x >= 0
    bounds = [(0, None)] * (m * n)
    
    # Resolver
    resultado = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, 
                       bounds=bounds, method='highs')
    
    if resultado.success:
        print("\n" + "=" * 70)
        print("SOLUCIÓN ÓPTIMA")
        print("=" * 70)
        
        x = resultado.x.reshape(m, n)
        costo_total = resultado.fun
        
        print("\nAsignaciones (horas):")
        print("-" * 70)
        print(f"{'Equipo\\Tarea':<15}", end="")
        for tarea in tareas:
            print(f"{tarea[:10]:<12}", end="")
        print("Total")
        print("-" * 70)
        
        for i, equipo in enumerate(equipos):
            print(f"{equipo:<15}", end="")
            total_fila = 0
            for j in range(n):
                valor = x[i][j]
                if valor > 1e-6:  # Solo mostrar valores significativos
                    print(f"{valor:<12.2f}", end="")
                    total_fila += valor
                else:
                    print(f"{'0.00':<12}", end="")
            print(f"{total_fila:.2f}")
        
        print("-" * 70)
        print(f"{'Total':<15}", end="")
        for j in range(n):
            total_col = sum(x[i][j] for i in range(m))
            print(f"{total_col:<12.2f}", end="")
        print()
        print("-" * 70)
        print(f"\nCosto total mínimo: {costo_total:.2f}")
        print("=" * 70)
    else:
        print("\nNo se encontró solución óptima.")


def resolver_con_pulp(equipos, tareas, oferta, demanda, costos):
    """Resuelve usando PuLP"""
    try:
        import pulp
        
        m = len(equipos)
        n = len(tareas)
        
        # Crear problema
        problema = pulp.LpProblem("Transporte_Sprint", pulp.LpMinimize)
        
        # Variables: x[i][j] = horas asignadas del equipo i a la tarea j
        x = {}
        for i in range(m):
            for j in range(n):
                x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", lowBound=0)
        
        # Función objetivo: minimizar costo total
        problema += pulp.lpSum([costos[i][j] * x[(i, j)] 
                               for i in range(m) for j in range(n)])
        
        # Restricciones de oferta
        for i in range(m):
            problema += pulp.lpSum([x[(i, j)] for j in range(n)]) <= oferta[i]
        
        # Restricciones de demanda
        for j in range(n):
            problema += pulp.lpSum([x[(i, j)] for i in range(m)]) == demanda[j]
        
        # Resolver
        problema.solve(pulp.PULP_CBC_CMD(msg=0))
        
        if problema.status == pulp.LpStatusOptimal:
            print("\n" + "=" * 70)
            print("SOLUCIÓN ÓPTIMA")
            print("=" * 70)
            
            print("\nAsignaciones (horas):")
            print("-" * 70)
            print(f"{'Equipo\\Tarea':<15}", end="")
            for tarea in tareas:
                print(f"{tarea[:10]:<12}", end="")
            print("Total")
            print("-" * 70)
            
            costo_total = 0
            for i, equipo in enumerate(equipos):
                print(f"{equipo:<15}", end="")
                total_fila = 0
                for j in range(n):
                    valor = pulp.value(x[(i, j)])
                    if valor and valor > 1e-6:
                        print(f"{valor:<12.2f}", end="")
                        total_fila += valor
                        costo_total += costos[i][j] * valor
                    else:
                        print(f"{'0.00':<12}", end="")
                print(f"{total_fila:.2f}")
            
            print("-" * 70)
            print(f"\nCosto total mínimo: {costo_total:.2f}")
            print("=" * 70)
        else:
            print("\nNo se encontró solución óptima.")
            
    except ImportError:
        print("\nPuLP no está instalado. Instálalo con: pip install pulp")
        print("O instala scipy: pip install scipy numpy")


if __name__ == "__main__":
    resolver_transporte()

