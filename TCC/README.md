# Trabajo de Conclusión de Curso (TCC)
## Aplicación de Modelos de Investigación de Operaciones al Ciclo de Desarrollo de Software

Este trabajo presenta la aplicación de modelos y herramientas de Investigación de Operaciones (IO) al ciclo de desarrollo de software, abordando problemas reales de planificación, asignación de recursos, modelado estocástico y análisis de sistemas.

---

## Objetivo del Trabajo

El objetivo principal de este TCC es demostrar cómo los modelos de Investigación de Operaciones pueden ser aplicados efectivamente para optimizar procesos en el desarrollo de software, mejorando la eficiencia, reduciendo tiempos y optimizando la utilización de recursos.

---

## Modelos Teóricos Implementados

Este trabajo desarrolla en profundidad **cuatro modelos principales** de Investigación de Operaciones:

### 1. Modelo de Asignación (Assignment Problem)
**Fundamento Teórico:** El problema de asignación es un caso especial de programación lineal entera donde se busca asignar n tareas a n agentes minimizando el costo total. La formulación matemática utiliza variables binarias y puede resolverse mediante el algoritmo húngaro o programación lineal entera.

**Teoría Aplicada:**
- Programación Lineal Entera (Integer Linear Programming)
- Algoritmo Húngaro (Hungarian Algorithm)
- Teorema de Birkhoff-von Neumann

**Ubicación:** `ejercicio_01_asignacion_tareas/`

[Ver desarrollo completo](ejercicio_01_asignacion_tareas/README.md)

---

### 2. Método de Ruta Crítica (CPM/PERT)
**Fundamento Teórico:** El Critical Path Method (CPM) y Program Evaluation and Review Technique (PERT) son técnicas de gestión de proyectos que utilizan grafos dirigidos acíclicos (DAG) para identificar la secuencia de actividades que determina la duración mínima del proyecto.

**Teoría Aplicada:**
- Teoría de Grafos
- Cálculo de tiempos tempranos y tardíos
- Identificación de holguras y ruta crítica
- Análisis de precedencias

**Ubicación:** `ejercicio_06_planificacion_precedencias/`

[Ver desarrollo completo](ejercicio_06_planificacion_precedencias/README.md)

---

### 3. Cadenas de Markov (Markov Chains)
**Fundamento Teórico:** Las cadenas de Markov son procesos estocásticos que modelan sistemas que evolucionan en el tiempo, donde el estado futuro depende únicamente del estado actual (propiedad de Markov). Se utilizan matrices de transición para modelar probabilidades de cambio de estado.

**Teoría Aplicada:**
- Procesos Estocásticos
- Cadenas de Markov de tiempo discreto
- Estados absorbentes y distribuciones estacionarias
- Teoría de probabilidades y matrices estocásticas

**Ubicación:** `ejercicio_08_estado_bugs/`

[Ver desarrollo completo](ejercicio_08_estado_bugs/README.md)

---

### 4. Teoría de Colas M/M/1
**Fundamento Teórico:** El modelo M/M/1 es un sistema de colas donde las llegadas siguen un proceso de Poisson (M), los tiempos de servicio son exponenciales (M), y existe un solo servidor (1). Este modelo permite analizar el comportamiento de sistemas con llegadas aleatorias y servicio estocástico.

**Teoría Aplicada:**
- Proceso de Poisson
- Distribución Exponencial
- Fórmulas de Little
- Análisis de sistemas de colas
- Teoría de procesos estocásticos

**Ubicación:** `ejercicio_09_cola_cicd/`

[Ver desarrollo completo](ejercicio_09_cola_cicd/README.md)

---

## Estructura del Trabajo

```
TCC/
├── README.md                                    # Este documento
├── MARCO_TEORICO.md                             # Marco teórico completo
├── ANALISIS_SENSIBILIDAD.md                     # Análisis de sensibilidad realizado
├── PROPUESTAS_PRACTICAS.md                      # Propuestas de implementación
│
├── ejercicio_01_asignacion_tareas/              # Modelo de Asignación
│   ├── README.md                                # Documentación teórica y práctica
│   ├── asignacion_tareas.py                     # Implementación
│   └── requirements.txt                         # Dependencias
│
├── ejercicio_06_planificacion_precedencias/       # CPM/PERT
│   ├── README.md                                # Documentación teórica y práctica
│   └── cpm_pert.py                              # Implementación
│
├── ejercicio_08_estado_bugs/                    # Cadenas de Markov
│   ├── README.md                                # Documentación teórica y práctica
│   └── markov.py                                # Implementación
│
└── ejercicio_09_cola_cicd/                      # Teoría de Colas
    ├── README.md                                # Documentación teórica y práctica
    └── cola_mm1.py                              # Implementación
```

---

## Metodología

### Fase 1: Revisión Teórica
Se realizó una revisión bibliográfica de los modelos de Investigación de Operaciones aplicables al desarrollo de software, identificando los modelos más relevantes y sus fundamentos matemáticos.

### Fase 2: Formulación de Problemas
Se formularon problemas reales del ciclo de desarrollo de software que pueden ser modelados mediante los métodos de IO seleccionados.

### Fase 3: Implementación
Se implementaron los modelos utilizando Python, aplicando los algoritmos y métodos teóricos estudiados.

### Fase 4: Análisis y Validación
Se realizó análisis de sensibilidad, validación de resultados y comparación con métodos alternativos.

### Fase 5: Propuestas de Aplicación
Se desarrollaron propuestas prácticas para la implementación de estos modelos en empresas tecnológicas.

---

## Resultados Obtidos

### Ejercicio 1: Modelo de Asignación
**Resultado:** Se obtuvo la asignación óptima que minimiza el tiempo total a 24 horas, asignando:
- Ana → Tarea 1 (6 horas)
- Luis → Tarea 2 (6 horas)
- Marta → Tarea 4 (6 horas)
- Carlos → Tarea 3 (6 horas)

**Validación:** La solución fue verificada mediante tres métodos independientes (fuerza bruta, algoritmo húngaro, programación lineal), confirmando la optimalidad.

### Ejercicio 6: CPM/PERT
**Resultado:** Se identificó la ruta crítica del proyecto: A → C → E → F, con duración mínima de 11 unidades de tiempo. Las tareas B y D presentan holguras de 3 y 1 unidades respectivamente.

**Validación:** Los cálculos de tiempos tempranos, tardíos y holguras fueron verificados mediante escalada hacia adelante y atrás.

### Ejercicio 8: Cadena de Markov
**Resultado:** Se modeló la evolución de bugs a través de estados, determinando que después de 50 pasos temporales, todos los bugs convergen al estado absorbente "Closed" con probabilidad 1.0.

**Validación:** La distribución estacionaria fue calculada mediante potenciación de la matriz de transición y verificada analíticamente.

### Ejercicio 9: Cola M/M/1
**Resultado:** Para un sistema con λ = 2.0 jobs/hora y μ = 3.0 jobs/hora, se obtuvo:
- Factor de utilización: ρ = 0.6667
- Número esperado en sistema: L = 2.0 jobs
- Tiempo esperado en sistema: W = 1.0 horas
- Número esperado en cola: Lq = 1.3333 jobs
- Tiempo esperado en cola: Wq = 0.6667 horas

**Validación:** Los resultados fueron verificados mediante las fórmulas analíticas del modelo M/M/1.

---

## Análisis de Sensibilidad Realizado

Para cada modelo se realizó análisis de sensibilidad evaluando:

1. **Modelo de Asignación:** Variación de tiempos estimados, disponibilidad de recursos, cambios en número de tareas/programadores.

2. **CPM/PERT:** Efecto de cambios en duraciones, impacto de retrasos, análisis de escenarios optimistas/pesimistas.

3. **Cadena de Markov:** Sensibilidad a probabilidades de transición, efecto de diferentes políticas, impacto de mejoras en procesos.

4. **Teoría de Colas:** Variación de tasas de llegada y servicio, dimensionamiento óptimo, análisis de diferentes configuraciones.

[Ver análisis detallado](ANALISIS_SENSIBILIDAD.md)

---

## Propuestas de Implementación Práctica

Se desarrollaron propuestas concretas para la implementación de estos modelos en empresas tecnológicas, incluyendo:

- Integración con herramientas existentes (Jira, GitHub, CI/CD)
- Desarrollo de dashboards y visualizaciones
- Sistemas de automatización y recomendación
- Métricas y KPIs derivados
- Análisis de ROI

[Ver propuestas completas](PROPUESTAS_PRACTICAS.md)

---

## Herramientas y Tecnologías Utilizadas

### Lenguaje de Programación
- **Python 3.8+**: Implementación de todos los modelos

### Librerías Científicas
- **NumPy**: Operaciones numéricas y álgebra lineal
- **SciPy**: Optimización y algoritmos científicos
- **PuLP**: Programación lineal entera
- **NetworkX**: Manipulación de grafos (para CPM/PERT)

### Herramientas de Análisis
- **Jupyter Notebook**: Análisis interactivo
- **Matplotlib/Seaborn**: Visualización de resultados
- **Pandas**: Análisis de datos

---

## Referencias Bibliográficas

### Libros Fundamentales
1. Hillier, F. S., & Lieberman, G. J. (2015). *Introduction to Operations Research* (10th ed.). McGraw-Hill Education.

2. Taha, H. A. (2017). *Operations Research: An Introduction* (10th ed.). Pearson.

3. Winston, W. L. (2004). *Operations Research: Applications and Algorithms* (4th ed.). Brooks/Cole.

4. Ross, S. M. (2014). *Introduction to Probability Models* (11th ed.). Academic Press.

5. Gross, D., Shortle, J. F., Thompson, J. M., & Harris, C. M. (2008). *Fundamentals of Queueing Theory* (4th ed.). Wiley.

### Artículos Científicos
- Aplicaciones de programación lineal en gestión de proyectos de software
- Modelado estocástico de procesos de desarrollo
- Teoría de colas aplicada a sistemas CI/CD
- Optimización de recursos en equipos de desarrollo ágil

---

## Conclusiones

Este trabajo demuestra que los modelos de Investigación de Operaciones son altamente aplicables al ciclo de desarrollo de software, proporcionando:

1. **Optimización de recursos:** Los modelos de asignación permiten distribuir eficientemente tareas entre programadores.

2. **Planificación efectiva:** El método CPM/PERT identifica tareas críticas y permite optimizar tiempos de proyecto.

3. **Predicción y modelado:** Las cadenas de Markov permiten modelar y predecir el comportamiento de procesos estocásticos.

4. **Análisis de sistemas:** La teoría de colas proporciona herramientas para dimensionar y optimizar infraestructura.

Los resultados obtenidos validan la aplicabilidad de estos modelos y demuestran su potencial para mejorar la eficiencia en el desarrollo de software.

---

## Ejecución de los Modelos

### Instalación de Dependencias

```bash
pip install numpy scipy pulp networkx matplotlib seaborn
```

### Ejecución

Cada ejercicio puede ejecutarse independientemente desde su directorio:

```bash
# Modelo de Asignación
cd ejercicio_01_asignacion_tareas
python3 asignacion_tareas.py

# CPM/PERT
cd ejercicio_06_planificacion_precedencias
python3 cpm_pert.py

# Cadena de Markov
cd ejercicio_08_estado_bugs
python3 markov.py

# Teoría de Colas
cd ejercicio_09_cola_cicd
python3 cola_mm1.py
```

---

**Trabajo de Conclusión de Curso**  
**Aplicación de Modelos de Investigación de Operaciones al Ciclo de Desarrollo de Software**
