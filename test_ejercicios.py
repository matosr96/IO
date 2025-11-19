#!/usr/bin/env python3
"""
Script de prueba para verificar que todos los ejercicios funcionen correctamente.
"""

import subprocess
import sys
import os

ejercicios = [
    ("Ejercicio 1: Asignación de Tareas", "ejercicio_01_asignacion_tareas", "asignacion_tareas.py"),
    ("Ejercicio 2: Planificación de Sprint", "ejercicio_02_planificacion_sprint", "transporte.py"),
    ("Ejercicio 3: Asignación de Revisores", "ejercicio_03_revisores_codigo", "asignacion_revisores.py"),
    ("Ejercicio 4: Priorización de Requerimientos", "ejercicio_04_priorizacion_requerimientos", "knapsack.py"),
    ("Ejercicio 5: Optimización del Backlog", "ejercicio_05_optimizacion_backlog", "lp_backlog.py"),
    ("Ejercicio 6: Planificación con Precedencias", "ejercicio_06_planificacion_precedencias", "cpm_pert.py"),
    ("Ejercicio 7: Gestión de Dependencias", "ejercicio_07_gestion_dependencias", "max_flow.py"),
    ("Ejercicio 8: Estado de Bugs (Markov)", "ejercicio_08_estado_bugs", "markov.py"),
    ("Ejercicio 9: Cola M/M/1 CI/CD", "ejercicio_09_cola_cicd", "cola_mm1.py"),
    ("Ejercicio 10: Optimización Multiobjetivo", "ejercicio_10_optimizacion_multiobjetivo", "multiobjetivo.py"),
]

def verificar_dependencias():
    """Verifica qué dependencias están instaladas."""
    dependencias = {
        'numpy': False,
        'scipy': False,
        'pulp': False,
        'networkx': False
    }
    
    for dep in dependencias:
        try:
            __import__(dep)
            dependencias[dep] = True
        except ImportError:
            pass
    
    return dependencias

def probar_ejercicio(nombre, directorio, archivo):
    """Prueba un ejercicio y retorna el resultado."""
    ruta_completa = os.path.join(directorio, archivo)
    
    if not os.path.exists(ruta_completa):
        return False, f"Archivo no encontrado: {ruta_completa}"
    
    try:
        resultado = subprocess.run(
            [sys.executable, archivo],
            cwd=directorio,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if resultado.returncode == 0:
            # Verificar que haya salida útil
            salida = resultado.stdout
            if "SOLUCIÓN" in salida or "ÓPTIMA" in salida or "RESULTADO" in salida or len(salida) > 100:
                return True, "OK"
            else:
                return False, "Sin salida útil"
        else:
            return False, f"Error: {resultado.stderr[:100]}"
    except subprocess.TimeoutExpired:
        return False, "Timeout"
    except Exception as e:
        return False, f"Excepción: {str(e)[:100]}"

def main():
    print("=" * 70)
    print("PRUEBA DE LOS 10 EJERCICIOS DE INVESTIGACIÓN DE OPERACIONES")
    print("=" * 70)
    
    # Verificar dependencias
    print("\n📦 Dependencias instaladas:")
    deps = verificar_dependencias()
    for dep, instalada in deps.items():
        estado = "✅" if instalada else "❌"
        print(f"  {estado} {dep}")
    
    # Probar cada ejercicio
    print("\n" + "=" * 70)
    print("RESULTADOS DE PRUEBAS")
    print("=" * 70)
    
    resultados = []
    for nombre, directorio, archivo in ejercicios:
        print(f"\n🔍 Probando {nombre}...")
        exito, mensaje = probar_ejercicio(nombre, directorio, archivo)
        estado = "✅" if exito else "⚠️"
        resultados.append((nombre, exito, mensaje))
        print(f"  {estado} {mensaje}")
    
    # Resumen
    print("\n" + "=" * 70)
    print("RESUMEN")
    print("=" * 70)
    
    exitosos = sum(1 for _, exito, _ in resultados if exito)
    total = len(resultados)
    
    print(f"\nEjercicios exitosos: {exitosos}/{total}")
    print("\nDetalle:")
    for nombre, exito, mensaje in resultados:
        estado = "✅" if exito else "⚠️"
        print(f"  {estado} {nombre}: {mensaje}")
    
    if exitosos < total:
        print("\n💡 Para instalar dependencias faltantes:")
        print("   pip install -r requirements.txt")
    
    print("=" * 70)
    
    return 0 if exitosos == total else 1

if __name__ == "__main__":
    sys.exit(main())

