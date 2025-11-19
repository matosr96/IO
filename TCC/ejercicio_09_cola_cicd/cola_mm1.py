"""
Ejercicio 9: Cola M/M/1 para Pipeline CI/CD
Modelo de Teoría de Colas - Modelo de Investigación de Operaciones

Objetivo: Modelar la llegada de jobs a CI y tiempo de servicio por runner.
"""

import math


def cola_mm1(lambda_arrival, mu_service):
    """
    Calcula las métricas de una cola M/M/1.
    
    Args:
        lambda_arrival: Tasa de llegada (jobs/hora)
        mu_service: Tasa de servicio (jobs/hora)
    
    Returns:
        Diccionario con todas las métricas
    """
    # Factor de utilización
    rho = lambda_arrival / mu_service
    
    # Verificar estabilidad (rho < 1)
    if rho >= 1:
        return {
            "estable": False,
            "mensaje": "El sistema es inestable (rho >= 1). Aumenta mu o reduce lambda."
        }
    
    # Número esperado en el sistema
    L = rho / (1 - rho)
    
    # Tiempo esperado en el sistema
    W = 1 / (mu_service - lambda_arrival)
    
    # Número esperado en la cola
    Lq = (rho ** 2) / (1 - rho)
    
    # Tiempo esperado en la cola
    Wq = rho / (mu_service - lambda_arrival)
    
    # Probabilidad de que el sistema esté vacío
    P0 = 1 - rho
    
    # Probabilidad de n jobs en el sistema
    def Pn(n):
        return (rho ** n) * P0
    
    return {
        "estable": True,
        "rho": rho,
        "L": L,
        "W": W,
        "Lq": Lq,
        "Wq": Wq,
        "P0": P0,
        "Pn": Pn
    }


def resolver_cola_cicd():
    """
    Resuelve el problema de cola M/M/1 para pipeline CI/CD.
    """
    # Parámetros del ejemplo
    lambda_arrival = 2.0  # jobs/hora
    mu_service = 3.0      # jobs/hora
    
    print("=" * 70)
    print("COLA M/M/1 PARA PIPELINE CI/CD")
    print("=" * 70)
    print("\nParámetros:")
    print("-" * 70)
    print(f"Tasa de llegada (λ): {lambda_arrival} jobs/hora")
    print(f"Tasa de servicio (μ): {mu_service} jobs/hora")
    print("-" * 70)
    
    # Calcular métricas
    resultados = cola_mm1(lambda_arrival, mu_service)
    
    if not resultados["estable"]:
        print(f"\n{resultados['mensaje']}")
        return resultados
    
    print("\n" + "=" * 70)
    print("RESULTADOS TEÓRICOS")
    print("=" * 70)
    
    print(f"\nFactor de utilización (ρ = λ/μ): {resultados['rho']:.4f}")
    print(f"  → {resultados['rho']*100:.2f}% del tiempo el servidor está ocupado")
    
    print(f"\nNúmero esperado en el sistema (L): {resultados['L']:.4f} jobs")
    print(f"  → Promedio de jobs en el sistema (en servicio + en cola)")
    
    print(f"\nTiempo esperado en el sistema (W): {resultados['W']:.4f} horas")
    print(f"  → Tiempo promedio desde que llega hasta que termina")
    
    print(f"\nNúmero esperado en la cola (Lq): {resultados['Lq']:.4f} jobs")
    print(f"  → Promedio de jobs esperando en la cola")
    
    print(f"\nTiempo esperado en la cola (Wq): {resultados['Wq']:.4f} horas")
    print(f"  → Tiempo promedio de espera antes de ser atendido")
    
    print(f"\nProbabilidad de sistema vacío (P0): {resultados['P0']:.4f}")
    print(f"  → {resultados['P0']*100:.2f}% del tiempo el servidor está libre")
    
    print("\n" + "=" * 70)
    print("PROBABILIDADES DE ESTADO")
    print("=" * 70)
    print(f"{'n (jobs)':<15} {'P(n)':<15}")
    print("-" * 70)
    for n in range(0, 11):
        prob = resultados['Pn'](n)
        print(f"{n:<15} {prob:.6f}")
    
    print("\n" + "=" * 70)
    print("INTERPRETACIÓN")
    print("=" * 70)
    if resultados['rho'] < 0.7:
        print("✓ Sistema bien dimensionado (ρ < 0.7)")
        print("  El servidor tiene capacidad suficiente.")
    elif resultados['rho'] < 0.9:
        print("⚠ Sistema con carga moderada (0.7 ≤ ρ < 0.9)")
        print("  Considera monitorear y planificar escalamiento.")
    else:
        print("⚠ Sistema con alta carga (ρ ≥ 0.9)")
        print("  Riesgo de colapso. Dimensiona aumentando μ o reduciendo λ.")
    
    print("\nRecomendaciones:")
    print("- Si ρ cerca de 1, el sistema colapsa")
    print("- Dimensionar μ aumentando runners o optimizando jobs")
    print("- Reducir λ mediante batching o priorización")
    print("=" * 70)
    
    return resultados


if __name__ == "__main__":
    resolver_cola_cicd()

