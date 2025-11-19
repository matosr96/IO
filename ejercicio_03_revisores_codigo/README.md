# Ejercicio 3: Asignación de Revisores de Código

## Descripción del Problema

Asignar revisores a pull requests considerando **compatibilidad** y **carga de trabajo**. El objetivo es minimizar el costo total (penalizaciones por incompatibilidad) mientras se respeta la capacidad máxima de revisiones por revisor.

Este problema corresponde a un **Modelo de Asignación con Restricciones Adicionales** (capacidad por revisor).

## Modelo de Investigación de Operaciones

Se utiliza el **Modelo de Asignación con Penalizaciones** porque:
- ✔ Cada PR debe ser asignado a **exactamente un revisor**
- ✔ Existen **costos de incompatibilidad** entre revisores y PRs
- ✔ Hay **restricciones de capacidad** (máximo revisiones por revisor)
- ✔ Las variables son **binarias** (asignar o no asignar)

## Datos del Problema

### Revisores Disponibles

| Revisor | Capacidad Máxima |
|---------|------------------|
| Alice | 2 PRs |
| Bob | 2 PRs |
| Charlie | 2 PRs |
| Diana | 2 PRs |

### Pull Requests a Revisar

- PR-001
- PR-002
- PR-003
- PR-004
- PR-005

### Matriz de Costos (Compatibilidad)

Costo de asignar revisor i al PR j (valor bajo = buena compatibilidad):

| Revisor\PR | PR-001 | PR-002 | PR-003 | PR-004 | PR-005 |
|------------|--------|--------|--------|--------|--------|
| Alice | 2 | 5 | 3 | 4 | 2 |
| Bob | 4 | 2 | 5 | 3 | 4 |
| Charlie | 3 | 4 | 2 | 5 | 3 |
| Diana | 5 | 3 | 4 | 2 | 5 |

## Formulación del Modelo

### Variables de Decisión

\[
x_{ij} = \begin{cases}
1 & \text{si el revisor } i \text{ revisa el PR } j \\
0 & \text{en caso contrario}
\end{cases}
\]

### Función Objetivo

Minimizar el costo total (incompatibilidad):

\[
\text{Min } Z = \sum_{i} \sum_{j} c_{ij} \cdot x_{ij}
\]

Donde \(c_{ij}\) es el costo de asignar el revisor i al PR j.

### Restricciones

#### Cada PR debe ser asignado a exactamente un revisor:

\[
\sum_{i} x_{ij} = 1 \quad \forall j
\]

#### Capacidad máxima por revisor:

\[
\sum_{j} x_{ij} \leq C_i \quad \forall i
\]

Donde \(C_i\) es la capacidad máxima del revisor i.

#### Variables binarias:

\[
x_{ij} \in \{0,1\} \quad \forall i,j
\]

## Solución

El código implementa dos métodos:

1. **Programación Lineal Entera con PuLP** (recomendado)
   - Método eficiente para problemas de asignación
   - Maneja restricciones de capacidad

2. **Fuerza Bruta** (fallback)
   - Útil para problemas pequeños
   - Evalúa todas las asignaciones posibles

### Resultado Óptimo

La solución asigna cada PR a un revisor minimizando el costo total y respetando las capacidades máximas.

## Interpretación

La solución óptima:
- **Minimiza incompatibilidades** entre revisores y PRs
- **Distribuye equitativamente** la carga de trabajo
- **Respeta capacidades** de cada revisor
- **Asegura cobertura** de todos los PRs

Este modelo es muy útil para:
- Automatización de asignación de revisores
- Optimización de procesos de code review
- Balanceo de carga en equipos
- Mejora de calidad de revisiones

## Uso

```bash
# Con PuLP (recomendado)
pip install pulp
python3 asignacion_revisores.py

# Sin dependencias (fuerza bruta, solo problemas pequeños)
python3 asignacion_revisores.py
```

## Archivos

- `asignacion_revisores.py`: Implementación del modelo
- `README.md`: Esta documentación

