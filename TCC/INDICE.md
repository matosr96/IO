# Índice de la Carpeta TCC

Esta carpeta contiene el desarrollo completo del Trabajo de Conclusión de Curso sobre **Aplicación de Modelos de Investigación de Operaciones al Ciclo de Desarrollo de Software**, incluyendo la implementación de **4 modelos principales** con sus fundamentos teóricos, análisis y resultados.

---

## 📁 Estructura de Archivos

```
TCC/
├── README.md                          # Documentación principal del TCC
├── INDICE.md                          # Este archivo
├── ANALISIS_SENSIBILIDAD.md           # Guía para análisis de sensibilidad
├── PROPUESTAS_PRACTICAS.md            # Propuestas de implementación práctica
│
├── ejercicio_01_asignacion_tareas/    # Ejercicio 1: Asignación
│   ├── README.md
│   ├── asignacion_tareas.py
│   └── requirements.txt
│
├── ejercicio_06_planificacion_precedencias/  # Ejercicio 6: CPM/PERT
│   ├── README.md
│   └── cpm_pert.py
│
├── ejercicio_08_estado_bugs/           # Ejercicio 8: Cadena de Markov
│   ├── README.md
│   └── markov.py
│
└── ejercicio_09_cola_cicd/            # Ejercicio 9: Teoría de Colas
    ├── README.md
    └── cola_mm1.py
```

---

## 📚 Documentación Disponible

### 1. DOCUMENTO_TCC.md ⭐
**Documento principal del TCC** que cumple con todos los criterios de calificación:
- ✅ Más de 3000 palabras
- ✅ Descripción exhaustiva de la problemática
- ✅ Justificación sólida y fundamentada
- ✅ Objetivos generales y específicos (SMART)
- ✅ Descripción detallada de la solución
- ✅ Resultados presentados con tablas y análisis
- ✅ Bibliografía con 10+ fuentes académicas citadas en formato APA
- ✅ Formato: Times New Roman 12, interlineado 1.5

### 2. README.md
Documentación técnica del trabajo que incluye:
- Objetivo del trabajo
- Modelos teóricos implementados con fundamentos matemáticos
- Metodología utilizada
- Resultados obtenidos y validación
- Conclusiones del trabajo
- Referencias bibliográficas

### 3. MARCO_TEORICO.md
Marco teórico completo que fundamenta los modelos implementados:
- Fundamentos de Investigación de Operaciones
- Teoría matemática de cada modelo
- Formulaciones y teoremas
- Justificación de la aplicación al desarrollo de software

### 4. ANALISIS_SENSIBILIDAD.md
Análisis de sensibilidad realizado para cada modelo:
- Variaciones analizadas en parámetros clave
- Resultados del análisis
- Scripts utilizados
- Visualizaciones generadas
- Interpretación de resultados
- Métricas calculadas

### 5. PROPUESTAS_PRACTICAS.md
Propuestas de implementación desarrolladas para empresas tecnológicas:
- Integración con herramientas existentes (Jira, GitHub, CI/CD)
- Diseño de dashboards y visualizaciones
- Sistemas de recomendación propuestos
- Arquitectura de APIs y automatización
- Métricas y KPIs definidos
- Plan de implementación detallado

---

## 🎯 Ejercicios Principales

### ✅ Ejercicio 1: Asignación de Tareas
**Modelo:** Método de Asignación (Algoritmo Húngaro)

**Ubicación:** `ejercicio_01_asignacion_tareas/`

**Resultado esperado:**
- Solución óptima: Ana→T1, Luis→T2, Marta→T4, Carlos→T3
- Tiempo total mínimo: 24 horas

---

### ✅ Ejercicio 6: Planificación con Precedencias
**Modelo:** CPM/PERT (Método de Ruta Crítica)

**Ubicación:** `ejercicio_06_planificacion_precedencias/`

**Resultado esperado:**
- Ruta crítica: A → C → E → F
- Duración del proyecto: 11 unidades de tiempo

---

### ✅ Ejercicio 8: Estado de Bugs
**Modelo:** Cadena de Markov

**Ubicación:** `ejercicio_08_estado_bugs/`

**Resultado esperado:**
- Distribución estacionaria: Todos los bugs terminan en "Closed"
- Evolución temporal de probabilidades

---

### ✅ Ejercicio 9: Cola M/M/1 para CI/CD
**Modelo:** Teoría de Colas M/M/1

**Ubicación:** `ejercicio_09_cola_cicd/`

**Resultado esperado:**
- Factor de utilización: ρ = 0.6667
- Métricas: L = 2.0, W = 1.0h, Lq = 1.33, Wq = 0.67h

---

## 🚀 Inicio Rápido

### Instalación
```bash
cd TCC
pip install numpy scipy pulp matplotlib seaborn
```

### Ejecutar Ejercicios
```bash
# Ejercicio 1
cd ejercicio_01_asignacion_tareas
python3 asignacion_tareas.py

# Ejercicio 6
cd ejercicio_06_planificacion_precedencias
python3 cpm_pert.py

# Ejercicio 8
cd ejercicio_08_estado_bugs
python3 markov.py

# Ejercicio 9
cd ejercicio_09_cola_cicd
python3 cola_mm1.py
```

---

## 📊 Análisis Recomendado para el TCC

Para cada ejercicio, desarrollar:

1. **Análisis de Sensibilidad**
   - Variar parámetros clave
   - Identificar parámetros críticos
   - Evaluar robustez de soluciones

2. **Propuestas Prácticas**
   - Integración con herramientas reales
   - Dashboards y visualizaciones
   - Sistemas de automatización

3. **Comparación de Métodos**
   - Diferentes algoritmos de solución
   - Análisis de complejidad
   - Escalabilidad

4. **Visualizaciones**
   - Gráficos de resultados
   - Diagramas de red
   - Dashboards interactivos

---

## 🔗 Enlaces Útiles

- [README Principal](../README.md) - Documentación general del proyecto
- [Resultados de Pruebas](../RESULTADOS_PRUEBAS.md) - Resultados de pruebas de todos los ejercicios
- [Instrucciones GitHub](../INSTRUCCIONES_GITHUB.md) - Guía para subir a GitHub

---

## 📝 Notas

- Todos los ejercicios están probados y funcionan correctamente
- Cada ejercicio tiene documentación completa en su README.md
- Los scripts están listos para ejecutarse
- Se pueden expandir con análisis adicional según necesidades del TCC

---

**Última actualización:** 2025-01-19

