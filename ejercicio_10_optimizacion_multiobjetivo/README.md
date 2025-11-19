# Ejercicio 10: Optimización Multiobjetivo

## Descripción del Problema

Asignación de tareas donde además de **tiempo** se consideran **costos** (salarios por hora distintos) y se requiere equilibrio entre ambas métricas. El objetivo es encontrar soluciones que balanceen tiempo y costo según las prioridades del proyecto.

Este problema corresponde a **Programación Lineal Entera Multiobjetivo**.

## Modelo de Investigación de Operaciones

Se utiliza **Optimización Multiobjetivo** porque:
- ✔ Existen **múltiples objetivos** (minimizar tiempo y minimizar costo)
- ✔ Los objetivos pueden ser **conflictivos** (mejor tiempo puede implicar mayor costo)
- ✔ Se busca generar el **frente de Pareto** (soluciones no dominadas)
- ✔ Las variables son **binarias** (asignación de tareas)

## Datos del Problema

### Programadores y Salarios

| Programador | Salario ($/hora) |
|-------------|------------------|
| Matos | 50 |
| Tania | 45 |
| Valeria | 55 |
| Salvador | 40 |

### Matriz de Tiempos (horas)

| Programador\Tarea | Tarea 1 | Tarea 2 | Tarea 3 | Tarea 4 |
|-------------------|---------|---------|---------|---------|
| Matos | 6 | 8 | 7 | 9 |
| Tania | 9 | 6 | 8 | 7 |
| Valeria | 7 | 5 | 9 | 6 |
| Salvador | 8 | 7 | 6 | 5 |

### Matriz de Costos ($)

Los costos se calculan como: **Costo = Tiempo × Salario**

| Programador\Tarea | Tarea 1 | Tarea 2 | Tarea 3 | Tarea 4 |
|-------------------|---------|---------|---------|---------|
| Matos | $300 | $400 | $350 | $450 |
| Tania | $405 | $270 | $360 | $315 |
| Valeria | $385 | $275 | $495 | $330 |
| Salvador | $320 | $280 | $240 | $200 |

## Formulación del Modelo

### Variables de Decisión

\[
x_{ij} = \begin{cases}
1 & \text{si el programador } i \text{ realiza la tarea } j \\
0 & \text{en caso contrario}
\end{cases}
\]

### Funciones Objetivo

#### Objetivo 1: Minimizar Tiempo

\[
\text{Min } Z_1 = \sum_{i} \sum_{j} t_{ij} \cdot x_{ij}
\]

#### Objetivo 2: Minimizar Costo

\[
\text{Min } Z_2 = \sum_{i} \sum_{j} c_{ij} \cdot x_{ij}
\]

Donde \(c_{ij} = t_{ij} \times s_i\) (tiempo × salario).

### Función Objetivo Combinada

Para generar el frente de Pareto, se combinan los objetivos con un peso α:

\[
\text{Min } Z = \alpha \cdot Z_1 + (1 - \alpha) \cdot Z_2
\]

Donde:
- **α = 0**: Solo minimizar costo
- **α = 1**: Solo minimizar tiempo
- **0 < α < 1**: Balance entre tiempo y costo

### Restricciones

#### Cada tarea asignada a exactamente un programador:

\[
\sum_{i} x_{ij} = 1 \quad \forall j
\]

#### Cada programador recibe exactamente una tarea:

\[
\sum_{j} x_{ij} = 1 \quad \forall i
\]

#### Variables binarias:

\[
x_{ij} \in \{0,1\} \quad \forall i,j
\]

## Solución

### Método de Solución

El código genera el **frente de Pareto** variando el peso α de 0 a 1:

1. **α = 0.0**: Prioriza costo mínimo
2. **α = 0.25**: Prioriza costo, con algo de tiempo
3. **α = 0.5**: Balance entre tiempo y costo
4. **α = 0.75**: Prioriza tiempo, con algo de costo
5. **α = 1.0**: Prioriza tiempo mínimo

### Resultado

Cada valor de α produce una solución diferente que representa un equilibrio entre tiempo y costo. El conjunto de todas las soluciones forma el **frente de Pareto**.

## Interpretación

### Frente de Pareto

El frente de Pareto muestra las **soluciones no dominadas**, donde:
- No existe otra solución con mejor tiempo Y mejor costo simultáneamente
- Cada punto representa un trade-off diferente

### Selección de α

La elección de α depende de las prioridades del proyecto:

- **α alto (0.75-1.0)**: Proyectos con deadline estricto
  - Prioriza minimizar tiempo
  - Acepta mayor costo si reduce tiempo

- **α bajo (0.0-0.25)**: Proyectos con presupuesto limitado
  - Prioriza minimizar costo
  - Acepta mayor tiempo si reduce costo

- **α medio (0.5)**: Balance general
  - Equilibra tiempo y costo
  - Útil cuando ambos objetivos son importantes

### Aplicaciones Prácticas

- Planificación de proyectos con restricciones múltiples
- Optimización de equipos considerando tiempo y presupuesto
- Toma de decisiones con objetivos conflictivos
- Análisis de sensibilidad de prioridades

## Uso

```bash
pip install pulp
python3 multiobjetivo.py
```

## Archivos

- `multiobjetivo.py`: Implementación de optimización multiobjetivo
- `README.md`: Esta documentación

