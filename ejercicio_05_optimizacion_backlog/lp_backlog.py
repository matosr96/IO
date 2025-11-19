"""
Ejercicio 5: Optimización del Backlog como Problema de Programación Lineal
Modelo de Programación Lineal Continua - Modelo de Investigación de Operaciones

Objetivo: Asignar proporciones de trabajo a features para maximizar valor
útil en planificación a nivel épico.
"""

try:
    from scipy.optimize import linprog
    import numpy as np
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False


def resolver_lp_backlog():
    """
    Resuelve el problema de optimización del backlog usando LP continua.
    """
    # Features con valor y esfuerzo
    features = [
        {"nombre": "Login OAuth", "valor": 10, "esfuerzo": 40},
        {"nombre": "Reporting Module", "valor": 15, "esfuerzo": 70},
        {"nombre": "Payment Gateway", "valor": 20, "esfuerzo": 90},
        {"nombre": "Admin Dashboard", "valor": 8, "esfuerzo": 30},
        {"nombre": "Notifications", "valor": 7, "esfuerzo": 20},
        {"nombre": "Analytics", "valor": 12, "esfuerzo": 50}
    ]
    
    capacidad = 200  # horas disponibles
    
    print("=" * 70)
    print("OPTIMIZACIÓN DEL BACKLOG - PROGRAMACIÓN LINEAL CONTINUA")
    print("=" * 70)
    print("\nFeatures disponibles:")
    print("-" * 70)
    print(f"{'Feature':<25} {'Valor':<10} {'Esfuerzo (h)':<15} {'Ratio':<10}")
    print("-" * 70)
    
    for feat in features:
        ratio = feat["valor"] / feat["esfuerzo"]
        print(f"{feat['nombre']:<25} {feat['valor']:<10} {feat['esfuerzo']:<15} {ratio:<10.3f}")
    
    print("-" * 70)
    print(f"\nCapacidad disponible: {capacidad} horas")
    print("\nNota: Las variables y_j representan la proporción [0,1] de cada feature completada.")
    
    if SCIPY_AVAILABLE:
        resolver_con_scipy(features, capacidad)
    else:
        resolver_con_pulp(features, capacidad)


def resolver_con_scipy(features, capacidad):
    """Resuelve usando scipy.optimize.linprog"""
    n = len(features)
    
    # Vector de coeficientes (negativo porque linprog minimiza)
    # Maximizar valor = Minimizar -valor
    c = [-feat["valor"] for feat in features]
    
    # Restricción de capacidad: suma(esfuerzo_j * y_j) <= capacidad
    A_ub = [[feat["esfuerzo"] for feat in features]]
    b_ub = [capacidad]
    
    # Límites: 0 <= y_j <= 1
    bounds = [(0, 1) for _ in range(n)]
    
    # Resolver
    resultado = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
    
    if resultado.success:
        print("\n" + "=" * 70)
        print("SOLUCIÓN ÓPTIMA")
        print("=" * 70)
        
        y = resultado.x
        valor_total = -resultado.fun  # Negativo porque minimizamos -valor
        esfuerzo_total = sum(features[i]["esfuerzo"] * y[i] for i in range(n))
        
        print("\nProporciones asignadas:")
        print("-" * 70)
        print(f"{'Feature':<25} {'Proporción':<15} {'Valor':<10} {'Esfuerzo':<10}")
        print("-" * 70)
        
        for i, feat in enumerate(features):
            prop = y[i]
            if prop > 1e-6:  # Solo mostrar valores significativos
                valor_parcial = feat["valor"] * prop
                esfuerzo_parcial = feat["esfuerzo"] * prop
                print(f"{feat['nombre']:<25} {prop:<15.3f} {valor_parcial:<10.2f} {esfuerzo_parcial:<10.2f}")
        
        print("-" * 70)
        print(f"\nValor total máximo: {valor_total:.2f}")
        print(f"Esfuerzo total utilizado: {esfuerzo_total:.2f} horas")
        print(f"Esfuerzo restante: {capacidad - esfuerzo_total:.2f} horas")
        print("=" * 70)
    else:
        print("\nNo se encontró solución óptima.")


def resolver_con_pulp(features, capacidad):
    """Resuelve usando PuLP"""
    try:
        import pulp
        
        # Crear problema
        problema = pulp.LpProblem("Backlog_Optimization", pulp.LpMaximize)
        
        # Variables: y_j ∈ [0,1] proporción de cada feature
        y = {}
        for i, feat in enumerate(features):
            y[i] = pulp.LpVariable(f"y_{i}", lowBound=0, upBound=1)
        
        # Función objetivo: maximizar valor total
        problema += pulp.lpSum([feat["valor"] * y[i] 
                              for i, feat in enumerate(features)])
        
        # Restricción de capacidad
        problema += pulp.lpSum([feat["esfuerzo"] * y[i] 
                                for i, feat in enumerate(features)]) <= capacidad
        
        # Resolver
        problema.solve(pulp.PULP_CBC_CMD(msg=0))
        
        if problema.status == pulp.LpStatusOptimal:
            print("\n" + "=" * 70)
            print("SOLUCIÓN ÓPTIMA")
            print("=" * 70)
            
            print("\nProporciones asignadas:")
            print("-" * 70)
            print(f"{'Feature':<25} {'Proporción':<15} {'Valor':<10} {'Esfuerzo':<10}")
            print("-" * 70)
            
            valor_total = 0
            esfuerzo_total = 0
            
            for i, feat in enumerate(features):
                prop = pulp.value(y[i])
                if prop and prop > 1e-6:
                    valor_parcial = feat["valor"] * prop
                    esfuerzo_parcial = feat["esfuerzo"] * prop
                    valor_total += valor_parcial
                    esfuerzo_total += esfuerzo_parcial
                    print(f"{feat['nombre']:<25} {prop:<15.3f} {valor_parcial:<10.2f} {esfuerzo_parcial:<10.2f}")
            
            print("-" * 70)
            print(f"\nValor total máximo: {valor_total:.2f}")
            print(f"Esfuerzo total utilizado: {esfuerzo_total:.2f} horas")
            print(f"Esfuerzo restante: {capacidad - esfuerzo_total:.2f} horas")
            print("=" * 70)
        else:
            print("\nNo se encontró solución óptima.")
            
    except ImportError:
        print("\nPuLP no está instalado. Instálalo con: pip install pulp")
        print("O instala scipy: pip install scipy numpy")


if __name__ == "__main__":
    resolver_lp_backlog()

