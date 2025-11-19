# Ejercicio 2: Planificación de Sprint con Recursos Limitados

## Descripción del Problema

Tres equipos (origen) con horas disponibles y cuatro tipos de tareas (destinos) que requieren horas. El objetivo es **minimizar el costo** (costo = prioridad inversa o tiempo por asignación) distribuyendo horas entre equipos para cubrir historias de usuario respetando capacidad.

Este problema corresponde al **Modelo de Transporte**, un caso especial de programación lineal.

## Modelo de Investigación de Operaciones

Se utiliza el **Modelo de Transporte** porque:
- ✔ Existen **orígenes** (equipos) con oferta limitada
- ✔ Existen **destinos** (tareas) con demanda específica
- ✔ Se busca **minimizar el costo** de asignación
- ✔ Las variables representan **cantidades** (horas) a transportar

## Datos del Problema

### Oferta (horas disponibles por equipo)

| Equipo | Horas Disponibles |
|--------|-------------------|
| Equipo A | 40 |
| Equipo B | 50 |
| Equipo C | 30 |

**Total: 120 horas**

### Demanda (horas requeridas por tarea)

| Tarea | Horas Requeridas |
|-------|------------------|
| Tarea 1 | 30 |
| Tarea 2 | 35 |
| Tarea 3 | 25 |
| Tarea 4 | 30 |

**Total: 120 horas**

### Matriz de Costos

Costo de asignar 1 hora del equipo i a la tarea j:

| Equipo\Tarea | Tarea 1 | Tarea 2 | Tarea 3 | Tarea 4 |
|--------------|---------|---------|---------|---------|
| Equipo A | 2 | 3 | 4 | 2 |
| Equipo B | 3 | 2 | 3 | 4 |
| Equipo C | 4 | 3 | 2 | 3 |

## Formulación del Modelo

### Variables de Decisión

\[
x_{ij} = \text{horas asignadas del equipo } i \text{ a la tarea } j
\]

Donde:
- \(i \in \{A, B, C\}\) (equipos)
- \(j \in \{1, 2, 3, 4\}\) (tareas)

### Función Objetivo

Minimizar el costo total:

\[
\text{Min } Z = \sum_{i} \sum_{j} c_{ij} \cdot x_{ij}
\]

Donde \(c_{ij}\) es el costo de asignar 1 hora del equipo i a la tarea j.

### Restricciones

#### Restricciones de Oferta (capacidad de equipos):

\[
\sum_{j} x_{ij} \leq s_i \quad \forall i
\]

Donde \(s_i\) es la oferta (horas disponibles) del equipo i.

#### Restricciones de Demanda (requerimientos de tareas):

\[
\sum_{i} x_{ij} = d_j \quad \forall j
\]

Donde \(d_j\) es la demanda (horas requeridas) de la tarea j.

#### No Negatividad:

\[
x_{ij} \geq 0 \quad \forall i,j
\]

## Método de Solución

El código implementa dos métodos:

1. **Programación Lineal con scipy.optimize.linprog**
   - Método simplex o punto interior
   - Eficiente para problemas medianos

2. **Programación Lineal con PuLP**
   - Alternativa con formulación explícita
   - Útil para problemas más complejos

### Métodos Clásicos (mencionados en documentación)

- **Método de Vogel**: Para encontrar solución inicial
- **Método MODI**: Para optimizar la solución

## Interpretación

La solución óptima distribuye las horas de los equipos entre las tareas minimizando el costo total. Esto permite:

- **Optimizar la asignación de recursos** en sprints
- **Respetar capacidades** de los equipos
- **Cubrir requerimientos** de todas las tareas
- **Minimizar costos** (tiempo, prioridad inversa, etc.)

Este modelo es muy útil para:
- Planificación de sprints
- Distribución de carga de trabajo
- Asignación de recursos en proyectos
- Optimización de equipos de desarrollo

## Uso

```bash
# Con scipy (recomendado)
pip install scipy numpy
python3 transporte.py

# O con PuLP
pip install pulp
python3 transporte.py
```

## Archivos

- `transporte.py`: Implementación del modelo de transporte
- `README.md`: Esta documentación

