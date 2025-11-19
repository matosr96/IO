# Ejercicio 1: Asignación de Tareas a Programadores

## Descripción del Problema

Una empresa de desarrollo de software debe asignar **4 tareas** a **4 programadores**, cada uno con habilidades y tiempos distintos por tarea. El objetivo es **minimizar el tiempo total** del desarrollo asignando cada tarea a un único programador.

Este problema corresponde a un **Modelo de Asignación** (Assignment Problem), un caso especial de la **Programación Lineal Entera**.

---

## Modelo de Investigación de Operaciones

### Justificación del Modelo

Se utiliza el **Modelo de Asignación** porque:

- ✔ Cada programador puede hacer **solo una tarea**
- ✔ Cada tarea debe ser asignada a **exactamente un programador**
- ✔ El objetivo (minimizar tiempo) es **lineal**
- ✔ Las variables de decisión son **binarias** (0 o 1)

Este modelo es un caso especial de programación lineal donde la matriz de restricciones tiene una estructura particular que permite el uso de algoritmos especializados más eficientes que el método simplex general.

---

## Datos del Problema

### Matriz de Tiempos Estimados (horas)

| Programador | Tarea 1 | Tarea 2 | Tarea 3 | Tarea 4 |
|-------------|---------|---------|---------|---------|
| Matos       | 6       | 8       | 7       | 9       |
| Tania       | 9       | 6       | 8       | 7       |
| Valeria     | 7       | 5       | 9       | 6       |
| Salvador    | 8       | 7       | 6       | 5       |

**Interpretación:** El valor en la posición (i, j) representa el tiempo estimado (en horas) que tarda el programador i en completar la tarea j.

---

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

En forma general:

\[
\text{Min } Z = \sum_{i=1}^{4} \sum_{j=1}^{4} t_{ij} \cdot x_{ij}
\]

Donde \(t_{ij}\) es el tiempo que tarda el programador \(i\) en la tarea \(j\).

### Restricciones

#### Cada tarea debe ser asignada a exactamente un programador:

\[
\sum_{i=1}^{4} x_{ij} = 1 \quad \forall j \in \{1,2,3,4\}
\]

En forma expandida:
\[
\begin{aligned}
x_{1j} + x_{2j} + x_{3j} + x_{4j} = 1 \quad \forall j
\end{aligned}
\]

#### Cada programador debe recibir exactamente una tarea:

\[
\sum_{j=1}^{4} x_{ij} = 1 \quad \forall i \in \{1,2,3,4\}
\]

En forma expandida:
\[
\begin{aligned}
x_{i1} + x_{i2} + x_{i3} + x_{i4} = 1 \quad \forall i
\end{aligned}
\]

#### Variables de decisión binarias:

\[
x_{ij} \in \{0,1\} \quad \forall i,j
\]

---

## Método de Solución: Algoritmo Húngaro

### Fundamentos Teóricos

El **Algoritmo Húngaro** (también conocido como Método Húngaro o Hungarian Algorithm) fue desarrollado por **Harold W. Kuhn** en 1955 y es el método estándar para resolver problemas de asignación.

#### Historia y Desarrollo

- **1955:** Harold W. Kuhn desarrolla el algoritmo, nombrado así en honor a los matemáticos húngaros Dénes Kőnig y Jenő Egerváry, cuyos trabajos fundamentaron el método.
- **1956:** James R. Munkres publica una versión mejorada, a veces llamada "Método de Munkres".
- **Aplicación:** Ampliamente utilizado en investigación de operaciones, ciencias de la computación y optimización.

#### Principios del Algoritmo

El algoritmo se basa en el **Teorema de Kőnig-Egerváry**, que establece que en una matriz de costos, el máximo número de asignaciones independientes de costo cero es igual al mínimo número de líneas (filas o columnas) necesarias para cubrir todos los ceros.

#### Pasos del Algoritmo

1. **Reducción de filas:** Restar el mínimo de cada fila a todos los elementos de esa fila
2. **Reducción de columnas:** Restar el mínimo de cada columna a todos los elementos de esa columna
3. **Cobertura de ceros:** Encontrar el mínimo número de líneas que cubren todos los ceros
4. **Ajuste de la matriz:** Si el número de líneas es menor que n, ajustar la matriz y repetir
5. **Asignación óptima:** Cuando el número de líneas es igual a n, se encuentra la asignación óptima

#### Complejidad Computacional

- **Complejidad temporal:** O(n³) donde n es el número de programadores/tareas
- **Complejidad espacial:** O(n²) para almacenar la matriz
- **Ventaja:** Más eficiente que resolver el problema como programación lineal general

#### Teorema Fundamental

**Teorema:** Una asignación es óptima si y solo si todos los elementos de la matriz reducida son no negativos y existe una asignación completa de ceros (una asignación donde cada fila y columna tiene exactamente un cero asignado).

### Implementación

La implementación utiliza `scipy.optimize.linear_sum_assignment`, que implementa una versión eficiente del algoritmo húngaro basada en el método de Munkres.

```python
from scipy.optimize import linear_sum_assignment

# Resolver el problema de asignación
filas_asignadas, columnas_asignadas = linear_sum_assignment(tiempos)
```

Esta función encuentra la asignación que minimiza la suma de costos (tiempos en este caso).

---

## Solución

### Resultado Óptimo

**Asignación óptima encontrada mediante Algoritmo Húngaro:**

| Programador | Tarea Asignada | Tiempo (horas) |
|-------------|----------------|----------------|
| Matos       | Tarea 1        | 6              |
| Tania       | Tarea 2        | 6              |
| Valeria     | Tarea 4        | 6              |
| Salvador    | Tarea 3        | 6              |

**Tiempo total mínimo: 24 horas**

### Validación

La solución fue validada mediante **Programación Lineal Entera** usando PuLP, confirmando que:

- ✓ La solución es óptima
- ✓ Todas las restricciones se cumplen
- ✓ El tiempo total de 24 horas es el mínimo posible

### Análisis de la Solución

**Características de la solución óptima:**

1. **Balance de tiempos:** Todos los programadores tienen tareas con tiempos similares (6 horas cada uno), lo que indica un buen balance de carga.

2. **Eficiencia:** La asignación aprovecha las fortalezas relativas de cada programador:
   - Matos es más eficiente en Tarea 1 (6h vs 9h, 7h, 8h de otros)
   - Tania es más eficiente en Tarea 2 (6h vs 8h, 5h, 7h de otros)
   - Valeria es más eficiente en Tarea 4 (6h vs 9h, 7h, 5h de otros)
   - Salvador es más eficiente en Tarea 3 (6h vs 7h, 8h, 9h de otros)

3. **Optimalidad:** No existe otra asignación que produzca un tiempo total menor que 24 horas.

---

## Comparación con Otros Métodos

### Algoritmo Húngaro vs Programación Lineal

| Aspecto | Algoritmo Húngaro | Programación Lineal |
|---------|-------------------|---------------------|
| **Especificidad** | Específico para asignación | Genérico para muchos problemas |
| **Complejidad** | O(n³) | O(n³) a O(n⁴) dependiendo del método |
| **Eficiencia** | Muy eficiente | Eficiente pero más general |
| **Reconocimiento académico** | Método estándar para asignación | Método general de IO |
| **Implementación** | Algoritmo especializado | Método simplex o punto interior |

**Conclusión:** Para problemas de asignación, el Algoritmo Húngaro es el método preferido por ser específico, eficiente y ampliamente reconocido académicamente.

---

## Interpretación y Aplicaciones

### Interpretación de la Solución

La solución óptima demuestra que mediante un análisis cuantitativo sistemático es posible:

1. **Minimizar tiempos:** Reducir el tiempo total del proyecto de manera óptima
2. **Balancear carga:** Distribuir tareas de manera equitativa
3. **Aprovechar fortalezas:** Asignar tareas según las habilidades relativas de cada programador

### Aplicaciones Prácticas

Este modelo es ampliamente aplicable en:

- **Asignación de tareas en sprints ágiles:** Optimizar la distribución de historias de usuario
- **Distribución de recursos en proyectos:** Asignar recursos humanos de manera eficiente
- **Optimización de equipos de desarrollo:** Maximizar productividad del equipo
- **Planificación de recursos:** Asignar programadores a módulos o componentes
- **Gestión de carga de trabajo:** Balancear el trabajo entre miembros del equipo

### Ventajas de la Aplicación

- **Decisiones basadas en datos:** Elimina la subjetividad en asignaciones
- **Optimización cuantificable:** Resultados medibles y verificables
- **Escalabilidad:** Funciona para equipos de cualquier tamaño
- **Automatización:** Puede integrarse en herramientas de gestión de proyectos

---

## Uso

### Instalación de Dependencias

```bash
pip install numpy scipy
```

### Ejecución

```bash
python3 asignacion_tareas.py
```

### Salida Esperada

El programa mostrará:
1. Descripción del problema
2. Matriz de tiempos estimados
3. Fundamentos teóricos del Algoritmo Húngaro
4. Solución óptima con asignaciones
5. Análisis e interpretación de la solución
6. Validación mediante Programación Lineal Entera

---

## Referencias Bibliográficas

### Referencia Principal

Kuhn, H. W. (1955). The Hungarian method for the assignment problem. *Naval Research Logistics Quarterly*, 2(1-2), 83-97. https://doi.org/10.1002/nav.3800020109

### Referencias Complementarias

Munkres, J. (1957). Algorithms for the assignment and transportation problems. *Journal of the Society for Industrial and Applied Mathematics*, 5(1), 32-38.

Hillier, F. S., & Lieberman, G. J. (2015). *Introduction to Operations Research* (10th ed.). McGraw-Hill Education. (Capítulo 8: The Transportation and Assignment Problems)

Taha, H. A. (2017). *Operations Research: An Introduction* (10th ed.). Pearson. (Capítulo 5: Transportation Model and Its Variants)

---

## Archivos

- `asignacion_tareas.py`: Implementación principal usando Algoritmo Húngaro
- `requirements.txt`: Dependencias (numpy, scipy)
- `README.md`: Esta documentación

---

**Nota:** Este ejercicio forma parte del Trabajo Colaborativo Contextualizado (TCC) sobre "Aplicación de Modelos de Investigación de Operaciones al Ciclo de Desarrollo de Software".
