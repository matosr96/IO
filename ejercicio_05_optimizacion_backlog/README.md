# Ejercicio 5: Optimización del Backlog (Programación Lineal Continua)

## Descripción del Problema

Asignar **proporciones de trabajo** a features (si se permiten fraccionar tareas) para **maximizar el valor** sujeto a la capacidad disponible. Útil en planificación a nivel épico donde las tareas pueden completarse parcialmente.

Este problema corresponde a **Programación Lineal Continua** (variables continuas en lugar de binarias).

## Modelo de Investigación de Operaciones

Se utiliza **Programación Lineal Continua** porque:
- ✔ Las variables representan **proporciones** [0,1] de completitud
- ✔ Se permite **fraccionar tareas** (útil a nivel épico)
- ✔ El objetivo es **maximizar valor** (lineal)
- ✔ Existe una **restricción de capacidad** (horas disponibles)

## Datos del Problema

### Features Disponibles

| Feature | Valor | Esfuerzo (horas) | Ratio (Valor/Esfuerzo) |
|---------|-------|-------------------|------------------------|
| Login OAuth | 10 | 40 | 0.250 |
| Reporting Module | 15 | 70 | 0.214 |
| Payment Gateway | 20 | 90 | 0.222 |
| Admin Dashboard | 8 | 30 | 0.267 |
| Notifications | 7 | 20 | 0.350 |
| Analytics | 12 | 50 | 0.240 |

**Capacidad disponible: 200 horas**

## Formulación del Modelo

### Variables de Decisión

\[
y_j \in [0,1] \quad \text{proporción de la feature } j \text{ completada}
\]

### Función Objetivo

Maximizar el valor total:

\[
\text{Max } Z = \sum_{j=1}^{n} v_j \cdot y_j
\]

Donde \(v_j\) es el valor de la feature \(j\).

### Restricciones

#### Restricción de capacidad:

\[
\sum_{j=1}^{n} w_j \cdot y_j \leq W
\]

Donde:
- \(w_j\) es el esfuerzo (peso) de la feature \(j\)
- \(W = 200\) es la capacidad disponible

#### Límites de las variables:

\[
0 \leq y_j \leq 1 \quad \forall j
\]

## Solución

### Método de Solución

El código implementa **Programación Lineal** usando:

1. **scipy.optimize.linprog** (método simplex o punto interior)
2. **PuLP** (alternativa con formulación explícita)

### Resultado Óptimo

La solución asigna proporciones a cada feature maximizando el valor total y respetando la capacidad. Las features con mejor **ratio valor/esfuerzo** tienden a recibir mayor proporción.

## Interpretación

Este modelo es útil cuando:
- **Planificación a nivel épico**: Las features grandes pueden completarse parcialmente
- **Flexibilidad en asignación**: Se permite trabajar en múltiples features simultáneamente
- **Maximización de valor**: Prioriza features con mejor retorno de inversión

**Diferencias con Knapsack 0-1:**
- Knapsack: Decisión binaria (incluir o no)
- LP Continua: Proporciones fraccionarias (0 a 1)

**Aplicaciones prácticas:**
- Planificación de releases
- Optimización de backlogs a nivel estratégico
- Asignación de recursos entre múltiples proyectos
- Priorización de inversión en desarrollo

## Uso

```bash
# Con scipy (recomendado)
pip install scipy numpy
python3 lp_backlog.py

# O con PuLP
pip install pulp
python3 lp_backlog.py
```

## Archivos

- `lp_backlog.py`: Implementación de programación lineal continua
- `README.md`: Esta documentación

