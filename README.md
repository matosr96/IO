# Colección de 10 Ejercicios de Investigación de Operaciones

**Tema general:** Aplicación de modelos y herramientas de Investigación de Operaciones al ciclo de desarrollo de software.

Este repositorio contiene 10 ejercicios completos con implementaciones en Python y documentación detallada para cada uno.

## Estructura del Proyecto

```
IO/
├── ejercicio_01_asignacion_tareas/      # Modelo de Asignación
├── ejercicio_02_planificacion_sprint/  # Modelo de Transporte
├── ejercicio_03_revisores_codigo/      # Asignación con Restricciones
├── ejercicio_04_priorizacion_requerimientos/  # Problema de la Mochila 0-1
├── ejercicio_05_optimizacion_backlog/  # Programación Lineal Continua
├── ejercicio_06_planificacion_precedencias/  # CPM/PERT
├── ejercicio_07_gestion_dependencias/  # Flujo Máximo
├── ejercicio_08_estado_bugs/           # Cadena de Markov
├── ejercicio_09_cola_cicd/            # Teoría de Colas M/M/1
└── ejercicio_10_optimizacion_multiobjetivo/  # Optimización Multiobjetivo
```

Cada carpeta contiene:
- Código Python con la implementación
- `README.md` con documentación detallada del ejercicio
- Datos y ejemplos del problema

## Ejercicios

### ✅ Ejercicio 1: Asignación de Tareas a Programadores
**Modelo:** Método de asignación (algoritmo húngaro / programación lineal entera)

Asignar 4 tareas a 4 programadores para minimizar el tiempo total.

**Solución:** Ana→T1, Luis→T2, Marta→T4, Carlos→T3 (24 horas)

[Ver detalles](ejercicio_01_asignacion_tareas/README.md)

---

### ✅ Ejercicio 2: Planificación de Sprint con Recursos Limitados
**Modelo:** Modelo de transporte (minimizar costo)

Distribuir horas entre equipos para cubrir historias de usuario respetando capacidad.

[Ver detalles](ejercicio_02_planificacion_sprint/README.md)

---

### ✅ Ejercicio 3: Asignación de Revisores de Código
**Modelo:** Asignación con penalizaciones y restricciones de capacidad

Asignar revisores a pull requests considerando compatibilidad y carga de trabajo.

[Ver detalles](ejercicio_03_revisores_codigo/README.md)

---

### ✅ Ejercicio 4: Priorización de Requerimientos (0-1 Knapsack)
**Modelo:** Problema de la mochila 0-1 (programación dinámica)

Seleccionar conjunto de features que maximizan valor sujeto a capacidad de horas.

**Solución:** Login OAuth, Payment Gateway, Notifications, Analytics (Valor: 49)

[Ver detalles](ejercicio_04_priorizacion_requerimientos/README.md)

---

### ✅ Ejercicio 5: Optimización del Backlog (LP Continua)
**Modelo:** Programación lineal continua (variables fraccionarias)

Asignar proporciones de trabajo a features para maximizar valor (útil a nivel épico).

[Ver detalles](ejercicio_05_optimizacion_backlog/README.md)

---

### ✅ Ejercicio 6: Planificación con Precedencias (CPM/PERT)
**Modelo:** Método de ruta crítica (CPM)

Determinar ruta crítica en un proyecto de integración y despliegue.

**Solución:** Ruta crítica: A → C → E → F (11 unidades de tiempo)

[Ver detalles](ejercicio_06_planificacion_precedencias/README.md)

---

### ✅ Ejercicio 7: Gestión de Dependencias (Redes de Flujo)
**Modelo:** Flujo máximo en red (algoritmo de Edmonds-Karp)

Asignar capacidad de integración entre ramas y entornos para maximizar throughput.

[Ver detalles](ejercicio_07_gestion_dependencias/README.md)

---

### ✅ Ejercicio 8: Estado de Bugs (Cadena de Markov)
**Modelo:** Cadena de Markov (proceso estocástico)

Modelar la evolución de bugs: New → InProgress → Fixed → Closed.

[Ver detalles](ejercicio_08_estado_bugs/README.md)

---

### ✅ Ejercicio 9: Cola M/M/1 para Pipeline CI/CD
**Modelo:** Teoría de colas M/M/1

Modelar llegada de jobs a CI y tiempo de servicio por runner.

**Parámetros:** λ = 2.0 jobs/h, μ = 3.0 jobs/h → L = 2.0, W = 1.0h

[Ver detalles](ejercicio_09_cola_cicd/README.md)

---

### ✅ Ejercicio 10: Optimización Multiobjetivo
**Modelo:** Programación lineal entera multiobjetivo

Asignación de tareas considerando tiempo y costo, generando frente de Pareto.

[Ver detalles](ejercicio_10_optimizacion_multiobjetivo/README.md)

---

## Requisitos

### Dependencias Principales

```bash
pip install -r requirements.txt
```

Las dependencias incluyen:
- `numpy`: Operaciones numéricas
- `scipy`: Optimización y algoritmos científicos
- `pulp`: Programación lineal entera
- `networkx`: Grafos y redes (opcional, para ejercicio 7)

### Dependencias por Ejercicio

| Ejercicio | Dependencias | Funciona sin dependencias |
|-----------|--------------|---------------------------|
| 1 | scipy, pulp (opcionales) | ✅ Sí (fuerza bruta) |
| 2 | scipy o pulp | ❌ No |
| 3 | pulp (opcional) | ✅ Sí (fuerza bruta) |
| 4 | Ninguna | ✅ Sí |
| 5 | scipy o pulp | ❌ No |
| 6 | Ninguna | ✅ Sí |
| 7 | networkx o pulp | ❌ No |
| 8 | Ninguna | ✅ Sí |
| 9 | Ninguna | ✅ Sí |
| 10 | pulp | ❌ No |

## Uso Rápido

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutar un ejercicio:**
   ```bash
   cd ejercicio_01_asignacion_tareas
   python3 asignacion_tareas.py
   ```

3. **Leer documentación:**
   Cada carpeta contiene un `README.md` con:
   - Descripción del problema
   - Formulación matemática
   - Solución implementada
   - Interpretación de resultados

## Observaciones para TCC

### Ejercicios Principales Recomendados

Para un TCC, se recomienda desarrollar en profundidad 3-4 casos principales:

1. **Asignación (Ejercicio 1)**: Modelo fundamental, fácil de entender
2. **CPM/PERT (Ejercicio 6)**: Muy aplicado en gestión de proyectos
3. **Cadena de Markov (Ejercicio 8)**: Modelado estocástico
4. **Teoría de Colas (Ejercicio 9)**: Análisis de sistemas

### Análisis Adicional Recomendado

Para cada ejercicio principal, considera agregar:

- **Análisis de sensibilidad**: Cómo cambia la solución ante variaciones en parámetros
- **Propuestas prácticas**: Aplicaciones reales en empresas tecnológicas
- **Comparación de métodos**: Diferentes algoritmos para el mismo problema
- **Visualizaciones**: Gráficos de resultados, redes, etc.

### Herramientas Recomendadas

- **Python**: `pandas`, `numpy`, `scipy`, `pulp`, `networkx`
- **Visualización**: `matplotlib`, `seaborn`, `plotly`
- **Análisis**: `jupyter notebook` para análisis interactivo

## Licencia

Este material es de uso educativo para TCC.

## Autor

Colección de ejercicios de Investigación de Operaciones aplicados al desarrollo de software.

---

**Última actualización:** 2025-01-19
