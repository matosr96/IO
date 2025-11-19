"""
Ejercicio 4: Priorización de Requerimientos (Problema de la Mochila 0-1)
Problema de Knapsack - Modelo de Investigación de Operaciones

Objetivo: Seleccionar conjunto de features que maximizan valor (beneficio)
sujeto a capacidad de horas del sprint.
"""


def knapsack_01_dinamico(items, capacidad):
    """
    Resuelve el problema de la mochila 0-1 usando programación dinámica.
    
    Args:
        items: Lista de tuplas (nombre, valor, peso)
        capacidad: Capacidad máxima (horas disponibles)
    
    Returns:
        valor_maximo, items_seleccionados
    """
    n = len(items)
    
    # Crear tabla DP: dp[i][w] = máximo valor con i items y capacidad w
    dp = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]
    
    # Llenar la tabla
    for i in range(1, n + 1):
        nombre, valor, peso = items[i - 1]
        for w in range(capacidad + 1):
            # No tomar el item
            dp[i][w] = dp[i - 1][w]
            
            # Tomar el item si cabe
            if peso <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - peso] + valor)
    
    # Reconstruir la solución
    valor_maximo = dp[n][capacidad]
    items_seleccionados = []
    w = capacidad
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            nombre, valor, peso = items[i - 1]
            items_seleccionados.append(nombre)
            w -= peso
    
    items_seleccionados.reverse()
    return valor_maximo, items_seleccionados


def knapsack_01_fuerza_bruta(items, capacidad):
    """
    Resuelve el problema de la mochila 0-1 usando fuerza bruta.
    Útil para problemas pequeños o verificación.
    """
    from itertools import combinations
    
    n = len(items)
    mejor_valor = 0
    mejor_combinacion = []
    
    # Probar todas las combinaciones posibles
    for r in range(1, n + 1):
        for combo in combinations(range(n), r):
            peso_total = sum(items[i][2] for i in combo)
            valor_total = sum(items[i][1] for i in combo)
            
            if peso_total <= capacidad and valor_total > mejor_valor:
                mejor_valor = valor_total
                mejor_combinacion = [items[i][0] for i in combo]
    
    return mejor_valor, mejor_combinacion


def resolver_priorizacion():
    """
    Resuelve el problema de priorización de requerimientos.
    """
    # Datos: (Nombre, Valor, Esfuerzo en horas)
    features = [
        ["Login OAuth", 10, 40],
        ["Reporting Module", 15, 70],
        ["Payment Gateway", 20, 90],
        ["Admin Dashboard", 8, 30],
        ["Notifications", 7, 20],
        ["Analytics", 12, 50]
    ]
    
    capacidad = 200  # horas disponibles en el sprint
    
    print("=" * 70)
    print("PRIORIZACIÓN DE REQUERIMIENTOS - PROBLEMA DE LA MOCHILA 0-1")
    print("=" * 70)
    print("\nFeatures disponibles:")
    print("-" * 70)
    print(f"{'Feature':<25} {'Valor':<10} {'Esfuerzo (h)':<15}")
    print("-" * 70)
    
    for nombre, valor, esfuerzo in features:
        print(f"{nombre:<25} {valor:<10} {esfuerzo:<15}")
    
    print("-" * 70)
    print(f"\nCapacidad del sprint: {capacidad} horas")
    
    # Resolver con programación dinámica
    valor_maximo, items_seleccionados = knapsack_01_dinamico(features, capacidad)
    
    # Calcular esfuerzo total de items seleccionados
    esfuerzo_total = sum(item[2] for item in features if item[0] in items_seleccionados)
    
    print("\n" + "=" * 70)
    print("SOLUCIÓN ÓPTIMA")
    print("=" * 70)
    print(f"\nValor total máximo: {valor_maximo}")
    print(f"Esfuerzo total utilizado: {esfuerzo_total} horas")
    print(f"Esfuerzo restante: {capacidad - esfuerzo_total} horas")
    print("\nFeatures seleccionadas:")
    print("-" * 70)
    
    for item in features:
        if item[0] in items_seleccionados:
            nombre, valor, esfuerzo = item
            ratio = valor / esfuerzo
            print(f"✓ {nombre:<25} Valor: {valor:<5} Esfuerzo: {esfuerzo:<5} Ratio: {ratio:.3f}")
    
    print("-" * 70)
    print("=" * 70)
    
    return valor_maximo, items_seleccionados


if __name__ == "__main__":
    resolver_priorizacion()

