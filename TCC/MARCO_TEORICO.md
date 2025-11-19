# Marco Teórico
## Fundamentos de Investigación de Operaciones Aplicados al Desarrollo de Software

Este documento presenta el marco teórico que fundamenta los modelos implementados en este trabajo de conclusión de curso.

---

## 1. Fundamentos de Investigación de Operaciones

### 1.1 Definición y Alcance

La Investigación de Operaciones (IO) es una disciplina científica que utiliza métodos analíticos avanzados para tomar mejores decisiones. Según Hillier & Lieberman (2015), la IO se caracteriza por:

- **Enfoque científico:** Utiliza el método científico para resolver problemas
- **Enfoque interdisciplinario:** Combina conocimientos de matemáticas, estadística, ciencias de la computación
- **Optimización:** Busca la mejor solución posible dentro de restricciones dadas
- **Modelado:** Representa sistemas complejos mediante modelos matemáticos

### 1.2 Proceso de Modelado

El proceso de modelado en IO sigue estas etapas:

1. **Formulación del problema:** Identificar objetivos, variables y restricciones
2. **Construcción del modelo:** Representar matemáticamente el problema
3. **Solución del modelo:** Aplicar algoritmos y métodos de solución
4. **Validación:** Verificar que el modelo representa correctamente el sistema
5. **Implementación:** Aplicar la solución en el contexto real

---

## 2. Modelo de Asignación (Assignment Problem)

### 2.1 Fundamentos Teóricos

El problema de asignación es un caso especial de programación lineal donde se busca asignar n tareas a n agentes minimizando el costo total, sujeto a que cada tarea sea asignada a exactamente un agente y cada agente reciba exactamente una tarea.

#### 2.1.1 Formulación Matemática

**Variables de decisión:**
\[
x_{ij} = \begin{cases}
1 & \text{si el agente } i \text{ es asignado a la tarea } j \\
0 & \text{en caso contrario}
\end{cases}
\]

**Función objetivo:**
\[
\text{Min } Z = \sum_{i=1}^{n} \sum_{j=1}^{n} c_{ij} \cdot x_{ij}
\]

Donde \(c_{ij}\) es el costo de asignar el agente \(i\) a la tarea \(j\).

**Restricciones:**
\[
\sum_{i=1}^{n} x_{ij} = 1 \quad \forall j \quad \text{(cada tarea asignada a un agente)}
\]
\[
\sum_{j=1}^{n} x_{ij} = 1 \quad \forall i \quad \text{(cada agente recibe una tarea)}
\]
\[
x_{ij} \in \{0,1\} \quad \forall i,j
\]

#### 2.1.2 Algoritmo Húngaro

El algoritmo húngaro, desarrollado por Harold Kuhn (1955), resuelve el problema de asignación en tiempo \(O(n^3)\). El algoritmo se basa en:

1. **Reducción de filas y columnas:** Restar el mínimo de cada fila y columna
2. **Cobertura de ceros:** Encontrar el mínimo número de líneas que cubren todos los ceros
3. **Iteración:** Ajustar la matriz hasta encontrar la asignación óptima

**Teorema fundamental:** Una asignación es óptima si y solo si todos los elementos de la matriz reducida son no negativos y existe una asignación completa de ceros.

#### 2.1.3 Programación Lineal Entera

El problema de asignación puede resolverse como un problema de programación lineal entera (PLE), donde las variables son binarias. Los métodos de solución incluyen:

- **Método Simplex:** Para problemas de asignación, el método simplex garantiza solución entera
- **Branch and Bound:** Para problemas más complejos
- **Algoritmos especializados:** Como el algoritmo húngaro

---

## 3. Método de Ruta Crítica (CPM/PERT)

### 3.1 Fundamentos Teóricos

El Critical Path Method (CPM) fue desarrollado por DuPont y Remington Rand en 1957 para gestionar proyectos. El PERT (Program Evaluation and Review Technique) fue desarrollado por la Marina de los EE.UU. en 1958.

#### 3.1.1 Representación mediante Grafos

Un proyecto se representa mediante un grafo dirigido acíclico (DAG) \(G = (V, E)\), donde:
- \(V\): Conjunto de nodos (actividades o eventos)
- \(E\): Conjunto de arcos (precedencias)

#### 3.1.2 Cálculo de Tiempos

**Tiempos Tempranos (Forward Pass):**

Para cada actividad \(i\):
\[
ES_i = \max\{EF_j : j \in \text{predecesores}(i)\}
\]
\[
EF_i = ES_i + d_i
\]

Donde:
- \(ES_i\): Tiempo más temprano de inicio
- \(EF_i\): Tiempo más temprano de finalización
- \(d_i\): Duración de la actividad \(i\)

**Tiempos Tardíos (Backward Pass):**

Para cada actividad \(i\):
\[
LF_i = \min\{LS_j : j \in \text{sucesores}(i)\}
\]
\[
LS_i = LF_i - d_i
\]

Donde:
- \(LS_i\): Tiempo más tardío de inicio
- \(LF_i\): Tiempo más tardío de finalización

**Holgura (Slack):**

\[
\text{Holgura}_i = LS_i - ES_i = LF_i - EF_i
\]

#### 3.1.3 Ruta Crítica

La ruta crítica es el camino más largo desde el inicio hasta el fin del proyecto. Las actividades en la ruta crítica tienen holgura cero.

**Teorema:** La duración mínima del proyecto es igual a la longitud de la ruta crítica.

---

## 4. Cadenas de Markov

### 4.1 Fundamentos Teóricos

Una cadena de Markov es un proceso estocástico que satisface la **propiedad de Markov** (o propiedad de falta de memoria):

\[
P(X_{n+1} = j | X_n = i, X_{n-1} = i_{n-1}, ..., X_0 = i_0) = P(X_{n+1} = j | X_n = i)
\]

Es decir, el estado futuro depende únicamente del estado actual, no de la historia previa.

#### 4.1.1 Matriz de Transición

Para una cadena de Markov de tiempo discreto con espacio de estados finito \(S = \{1, 2, ..., n\}\), la matriz de transición \(P\) tiene elementos:

\[
P_{ij} = P(X_{n+1} = j | X_n = i)
\]

**Propiedades:**
- \(P_{ij} \geq 0\) para todo \(i, j\)
- \(\sum_{j=1}^{n} P_{ij} = 1\) para todo \(i\)

#### 4.1.2 Distribución de Probabilidad

Si \(\pi^{(n)}\) es el vector de distribución de probabilidad en el tiempo \(n\), entonces:

\[
\pi^{(n+1)} = \pi^{(n)} \cdot P
\]

Y después de \(k\) pasos:

\[
\pi^{(n+k)} = \pi^{(n)} \cdot P^k
\]

#### 4.1.3 Estados Absorbentes

Un estado \(i\) es absorbente si \(P_{ii} = 1\) y \(P_{ij} = 0\) para \(j \neq i\). Una vez que el proceso entra en un estado absorbente, permanece allí permanentemente.

#### 4.1.4 Distribución Estacionaria

Para cadenas ergódicas, existe una distribución estacionaria \(\pi^*\) tal que:

\[
\pi^* = \pi^* \cdot P
\]

Esta distribución representa el comportamiento a largo plazo del sistema.

---

## 5. Teoría de Colas M/M/1

### 5.1 Fundamentos Teóricos

El modelo M/M/1 es un sistema de colas con:
- **M (llegadas):** Proceso de Poisson con tasa \(\lambda\)
- **M (servicio):** Distribución exponencial con tasa \(\mu\)
- **1 (servidor):** Un solo servidor
- **Disciplina:** First In First Out (FIFO)

#### 5.1.1 Proceso de Poisson

El proceso de Poisson es un proceso estocástico que modela llegadas aleatorias. Para un proceso de Poisson con tasa \(\lambda\):

\[
P(N(t) = n) = \frac{(\lambda t)^n e^{-\lambda t}}{n!}
\]

Donde \(N(t)\) es el número de llegadas en el intervalo \([0, t]\).

#### 5.1.2 Distribución Exponencial

Los tiempos entre llegadas y tiempos de servicio siguen una distribución exponencial:

\[
f(t) = \lambda e^{-\lambda t}, \quad t \geq 0
\]

Con media \(E[T] = \frac{1}{\lambda}\).

#### 5.1.3 Factor de Utilización

El factor de utilización del servidor es:

\[
\rho = \frac{\lambda}{\mu}
\]

**Condición de estabilidad:** \(\rho < 1\) (si \(\rho \geq 1\), el sistema es inestable y la cola crece indefinidamente).

#### 5.1.4 Fórmulas de Little

Las fórmulas de Little relacionan las métricas del sistema:

\[
L = \lambda W
\]
\[
L_q = \lambda W_q
\]

Donde:
- \(L\): Número esperado en el sistema
- \(L_q\): Número esperado en la cola
- \(W\): Tiempo esperado en el sistema
- \(W_q\): Tiempo esperado en la cola

#### 5.1.5 Fórmulas del Modelo M/M/1

**Número esperado en el sistema:**
\[
L = \frac{\rho}{1 - \rho} = \frac{\lambda}{\mu - \lambda}
\]

**Tiempo esperado en el sistema:**
\[
W = \frac{1}{\mu - \lambda}
\]

**Número esperado en la cola:**
\[
L_q = \frac{\rho^2}{1 - \rho} = \frac{\lambda^2}{\mu(\mu - \lambda)}
\]

**Tiempo esperado en la cola:**
\[
W_q = \frac{\rho}{\mu - \lambda} = \frac{\lambda}{\mu(\mu - \lambda)}
\]

**Probabilidad de sistema vacío:**
\[
P_0 = 1 - \rho
\]

**Probabilidad de n clientes en el sistema:**
\[
P_n = \rho^n (1 - \rho) = \rho^n P_0
\]

---

## 6. Aplicación al Desarrollo de Software

### 6.1 Justificación de la Aplicación

Los modelos de IO son aplicables al desarrollo de software porque:

1. **Problemas de optimización:** Asignación de tareas, distribución de recursos
2. **Gestión de proyectos:** Planificación, estimación de tiempos, identificación de dependencias
3. **Procesos estocásticos:** Modelado de bugs, predicción de carga de trabajo
4. **Análisis de sistemas:** Dimensionamiento de infraestructura, optimización de pipelines

### 6.2 Ventajas de la Aplicación

- **Decisiones basadas en datos:** Los modelos proporcionan soluciones cuantitativas
- **Optimización:** Mejora de eficiencia y reducción de tiempos
- **Predicción:** Capacidad de predecir comportamientos futuros
- **Análisis de escenarios:** Evaluación de diferentes alternativas

---

## Referencias

1. Hillier, F. S., & Lieberman, G. J. (2015). *Introduction to Operations Research* (10th ed.). McGraw-Hill Education.

2. Taha, H. A. (2017). *Operations Research: An Introduction* (10th ed.). Pearson.

3. Ross, S. M. (2014). *Introduction to Probability Models* (11th ed.). Academic Press.

4. Gross, D., Shortle, J. F., Thompson, J. M., & Harris, C. M. (2008). *Fundamentals of Queueing Theory* (4th ed.). Wiley.

5. Kuhn, H. W. (1955). The Hungarian method for the assignment problem. *Naval Research Logistics Quarterly*, 2(1-2), 83-97.

6. Kelley, J. E., & Walker, M. R. (1959). Critical-path planning and scheduling. *Proceedings of the Eastern Joint Computer Conference*, 160-173.

---

**Marco Teórico - Trabajo de Conclusión de Curso**

