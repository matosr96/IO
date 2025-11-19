# Ejercicio 1: Asignación de Tareas a Programadores

## Descripción del Problema

Una empresa de desarrollo de software debe asignar **4 tareas** a **4 programadores**, cada uno con habilidades y tiempos distintos por tarea. El objetivo es **minimizar el tiempo total** del desarrollo asignando cada tarea a un único programador.

Este problema corresponde a un **Modelo de Asignación**, un caso especial de la **Programación Lineal Entera**.

## Modelo de Investigación de Operaciones

Se utiliza el **Modelo de Asignación** porque:
- ✔ Cada programador puede hacer **solo una tarea**
- ✔ Cada tarea debe ser asignada a **exactamente un programador**
- ✔ El objetivo (minimizar tiempo) es **lineal**

## Datos del Problema

### Matriz de Tiempos Estimados (horas)

| Programador | Tarea 1 | Tarea 2 | Tarea 3 | Tarea 4 |
|-------------|---------|---------|---------|---------|
| Matos       | 6       | 8       | 7       | 9       |
| Tania       | 9       | 6       | 8       | 7       |
| Valeria     | 7       | 5       | 9       | 6       |
| Salvador    | 8       | 7       | 6       | 5       |

## Formulación del Modelo

### Variables de Decisión

\[
x_{ij} = \begin{cases}
1 & \text{si el programador } i \text{ realiza la tarea } j \\
0 & \text{en caso contrario}
\end{cases}
\]

Donde:
- **Programadores:** Matos (i=1), Tania (i=2), Valeria (i=3), Salvador (i=4)
- **Tareas:** T1 (j=1), T2 (j=2), T3 (j=3), T4 (j=4)

### Función Objetivo

Minimizar el tiempo total:

\[
\begin{aligned}
\text{Min } Z = 
&6x_{11} + 8x_{12} + 7x_{13} + 9x_{14} + \\
&9x_{21} + 6x_{22} + 8x_{23} + 7x_{24} + \\
&7x_{31} + 5x_{32} + 9x_{33} + 6x_{34} + \\
&8x_{41} + 7x_{42} + 6x_{43} + 5x_{44}
\end{aligned}
\]

### Restricciones

#### Cada tarea debe ser asignada a exactamente un programador:

\[
x_{1j} + x_{2j} + x_{3j} + x_{4j} = 1 \quad \forall j \in \{1,2,3,4\}
\]

#### Cada programador debe recibir exactamente una tarea:

\[
x_{i1} + x_{i2} + x_{i3} + x_{i4} = 1 \quad \forall i \in \{1,2,3,4\}
\]

#### Variables de decisión binarias:

\[
x_{ij} \in \{0,1\} \quad \forall i,j
\]

## Solución

### Resultado Óptimo

**Asignación óptima encontrada:**
- Matos → Tarea 1 (6 horas)
- Tania → Tarea 2 (6 horas)
- Valeria → Tarea 4 (6 horas)
- Salvador → Tarea 3 (6 horas)

**Tiempo total mínimo: 24 horas**

### Métodos de Solución Implementados

El código incluye tres métodos:

1. **Búsqueda completa con permutaciones** (biblioteca estándar)
   - Evalúa todas las asignaciones posibles
   - Funciona sin dependencias externas

2. **Algoritmo Húngaro** (scipy.optimize.linear_sum_assignment)
   - Método más eficiente para problemas grandes
   - Requiere: `scipy` y `numpy`

3. **Programación Lineal Entera** (PuLP)
   - Muestra la formulación completa del modelo
   - Requiere: `pulp`

## Interpretación

La solución óptima asigna las tareas de manera que cada programador trabaje en la tarea donde tiene mejor rendimiento relativo. Esto minimiza el tiempo total del sprint y permite una distribución eficiente de la carga de trabajo.

Este tipo de modelos es muy usado en contextos reales de operación y planificación en empresas tecnológicas, especialmente para:
- Asignación de tareas en sprints
- Distribución de recursos en proyectos
- Optimización de equipos de desarrollo

## Uso

```bash
# Ejecutar con biblioteca estándar (sin dependencias)
python3 asignacion_tareas.py

# Con dependencias opcionales
pip install -r requirements.txt
python3 asignacion_tareas.py
```

## Archivos

- `asignacion_tareas.py`: Código principal con las tres implementaciones
- `requirements.txt`: Dependencias opcionales (scipy, numpy, pulp)
- `README.md`: Esta documentación

