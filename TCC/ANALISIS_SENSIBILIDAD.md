# Análisis de Sensibilidad - Guía para el TCC

Este documento proporciona una guía para realizar análisis de sensibilidad en los 4 ejercicios principales del TCC.

---

## 1. Análisis de Sensibilidad - Asignación de Tareas

### Variaciones a Analizar

#### 1.1 Cambios en Tiempos Estimados
```python
# Ejemplo: Variar tiempos de ±10%, ±20%, ±30%
tiempos_variados = {
    'baseline': tiempos_originales,
    'mas_10%': tiempos_originales * 1.1,
    'menos_10%': tiempos_originales * 0.9,
    'mas_20%': tiempos_originales * 1.2,
    'menos_20%': tiempos_originales * 0.8
}
```

**Preguntas de investigación:**
- ¿La solución óptima cambia con pequeñas variaciones?
- ¿Qué tan robusta es la asignación actual?
- ¿Qué programador es más crítico (mayor impacto si cambia)?

#### 1.2 Disponibilidad de Programadores
- ¿Qué pasa si un programador no está disponible?
- ¿Cuál es el impacto de agregar un nuevo programador?
- ¿Qué pasa si un programador puede hacer múltiples tareas?

#### 1.3 Cambios en Número de Tareas
- ¿Cómo escala la solución con más tareas?
- ¿Cuál es el tiempo mínimo con 5, 6, 7 tareas?
- ¿Qué tareas son más críticas?

### Métricas a Calcular
- Tiempo total mínimo para cada variación
- Cambio porcentual respecto a la solución base
- Robustez de la solución (cuántas variaciones mantienen la misma asignación)

---

## 2. Análisis de Sensibilidad - CPM/PERT

### Variaciones a Analizar

#### 2.1 Cambios en Duraciones de Tareas
```python
# Escenarios: Optimista, Más Probable, Pesimista (PERT)
duraciones = {
    'optimista': duracion_base * 0.8,
    'mas_probable': duracion_base,
    'pesimista': duracion_base * 1.5
}
```

**Preguntas de investigación:**
- ¿Cómo cambia la ruta crítica con diferentes duraciones?
- ¿Qué tareas son más sensibles (mayor impacto en duración total)?
- ¿Cuál es la probabilidad de cumplir el deadline?

#### 2.2 Retrasos en Tareas
- Impacto de retraso en tarea crítica vs no crítica
- ¿Cuánto retraso puede tolerar una tarea no crítica?
- Efecto de retrasos en cascada

#### 2.3 Agregar/Quitar Tareas
- ¿Cómo afecta agregar una nueva tarea?
- ¿Qué pasa si se elimina una tarea de la ruta crítica?
- Impacto de paralelizar tareas

### Métricas a Calcular
- Duración del proyecto para cada escenario
- Holguras actualizadas
- Probabilidad de cumplir deadline (si se usa PERT)
- Tareas que cambian de críticas a no críticas

---

## 3. Análisis de Sensibilidad - Cadena de Markov

### Variaciones a Analizar

#### 3.1 Cambios en Probabilidades de Transición
```python
# Variar probabilidades de transición
probabilidades = {
    'baseline': matriz_P_original,
    'mejora_proceso': matriz_P_mejorada,  # Más probabilidad de avanzar
    'empeora_proceso': matriz_P_empeorada  # Más probabilidad de retroceder
}
```

**Preguntas de investigación:**
- ¿Cómo cambia el tiempo hasta absorción?
- ¿Qué probabilidades tienen mayor impacto?
- ¿Qué mejoras en proceso tienen mayor ROI?

#### 3.2 Diferentes Políticas
- Política agresiva: más recursos en resolución
- Política conservadora: más tiempo en revisión
- Política balanceada: equilibrio entre velocidad y calidad

#### 3.3 Estados Iniciales Diferentes
- ¿Qué pasa si empiezan en diferentes estados?
- Impacto de backlog inicial
- Efecto de "días malos" vs "días buenos"

### Métricas a Calcular
- Tiempo esperado hasta absorción
- Distribución estacionaria
- Probabilidades de estado en diferentes pasos temporales
- Tasa de resolución de bugs

---

## 4. Análisis de Sensibilidad - Cola M/M/1

### Variaciones a Analizar

#### 4.1 Cambios en Tasa de Llegada (λ)
```python
# Escenarios de carga
lambdas = {
    'baja': 1.0,      # jobs/hora
    'normal': 2.0,    # jobs/hora (baseline)
    'alta': 3.5,      # jobs/hora
    'critica': 4.5    # jobs/hora (cerca del límite)
}
```

**Preguntas de investigación:**
- ¿A qué punto el sistema colapsa?
- ¿Cuál es el impacto de picos de carga?
- ¿Cómo afecta el tiempo de espera?

#### 4.2 Cambios en Tasa de Servicio (μ)
```python
# Mejoras en capacidad
mus = {
    'actual': 3.0,           # jobs/hora
    'mejorado_10%': 3.3,      # jobs/hora
    'mejorado_20%': 3.6,      # jobs/hora
    'duplicado': 6.0          # jobs/hora (más runners)
}
```

**Preguntas de investigación:**
- ¿Cuánto mejora el sistema con más capacidad?
- ¿Cuál es el ROI de agregar runners?
- ¿Cuál es el punto óptimo de capacidad?

#### 4.3 Diferentes Configuraciones
- Sistema M/M/1 (un servidor)
- Sistema M/M/c (múltiples servidores)
- Sistema con prioridades

### Métricas a Calcular
- Factor de utilización (ρ) para cada escenario
- Número esperado en sistema (L)
- Tiempo esperado en sistema (W)
- Probabilidad de cola vacía
- Costo total (considerando costo de espera + costo de servidores)

---

## Scripts de Ejemplo para Análisis

### Template para Análisis de Sensibilidad

```python
import numpy as np
import matplotlib.pyplot as plt

def analisis_sensibilidad(parametro_base, variaciones, funcion_objetivo):
    """
    Realiza análisis de sensibilidad variando un parámetro.
    
    Args:
        parametro_base: Valor base del parámetro
        variaciones: Lista de factores de variación (ej: [0.8, 0.9, 1.0, 1.1, 1.2])
        funcion_objetivo: Función que calcula el objetivo para un valor del parámetro
    
    Returns:
        resultados: Diccionario con variaciones y valores del objetivo
    """
    resultados = {}
    
    for factor in variaciones:
        parametro_variado = parametro_base * factor
        valor_objetivo = funcion_objetivo(parametro_variado)
        resultados[factor] = valor_objetivo
    
    return resultados

# Ejemplo de uso
variaciones = [0.5, 0.75, 0.9, 1.0, 1.1, 1.25, 1.5]
resultados = analisis_sensibilidad(
    parametro_base=2.0,
    variaciones=variaciones,
    funcion_objetivo=lambda x: resolver_problema(x)
)

# Visualizar
plt.plot(variaciones, list(resultados.values()))
plt.xlabel('Factor de variación')
plt.ylabel('Valor del objetivo')
plt.title('Análisis de Sensibilidad')
plt.grid(True)
plt.show()
```

---

## Visualizaciones Recomendadas

### Para Asignación
- Heatmap de tiempos
- Gráfico de barras comparando asignaciones
- Gráfico de sensibilidad del tiempo total

### Para CPM/PERT
- Diagrama de Gantt
- Grafo de red con ruta crítica resaltada
- Gráfico de holguras
- Gráfico de sensibilidad de duración

### Para Markov
- Gráfico de evolución temporal de probabilidades
- Diagrama de estados con probabilidades
- Gráfico de tiempo hasta absorción

### Para Colas
- Gráfico de métricas vs factor de utilización
- Gráfico de costo total vs capacidad
- Dashboard de métricas del sistema

---

## Interpretación de Resultados

### Criterios de Sensibilidad

**Alta sensibilidad:**
- Pequeños cambios en parámetros causan grandes cambios en resultados
- Requiere monitoreo constante
- Solución puede no ser robusta

**Baja sensibilidad:**
- Cambios en parámetros causan cambios pequeños en resultados
- Solución es robusta
- Menor necesidad de ajustes frecuentes

### Recomendaciones

1. **Identificar parámetros críticos** (alta sensibilidad)
2. **Monitorear parámetros críticos** más de cerca
3. **Desarrollar estrategias** para manejar variaciones
4. **Establecer rangos aceptables** para parámetros
5. **Crear alertas** cuando parámetros salen de rango

---

## Próximos Pasos

1. Implementar scripts de análisis de sensibilidad para cada ejercicio
2. Generar visualizaciones de resultados
3. Documentar hallazgos y conclusiones
4. Crear dashboards interactivos
5. Desarrollar recomendaciones prácticas basadas en análisis

