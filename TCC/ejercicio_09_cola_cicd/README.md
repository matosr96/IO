# Ejercicio 9: Cola M/M/1 para Pipeline CI/CD

## Descripción del Problema

Modelar la llegada de jobs a un sistema de CI (Continuous Integration) y el tiempo de servicio por runner. El objetivo es analizar el comportamiento del sistema de colas para optimizar la capacidad y reducir tiempos de espera.

Este problema se resuelve usando el **Modelo de Cola M/M/1** de la teoría de colas.

## Modelo de Investigación de Operaciones

Se utiliza el **Modelo M/M/1** porque:
- ✔ Las llegadas siguen un **proceso de Poisson** (M)
- ✔ Los tiempos de servicio son **exponenciales** (M)
- ✔ Hay **un solo servidor** (1 runner)
- ✔ La cola es **infinita** y sigue disciplina **FIFO**

### Notación

- **λ (lambda)**: Tasa de llegada (jobs/hora)
- **μ (mu)**: Tasa de servicio (jobs/hora)
- **ρ (rho)**: Factor de utilización = λ/μ

## Datos del Problema

### Parámetros del Ejemplo

- **Tasa de llegada (λ)**: 2.0 jobs/hora
- **Tasa de servicio (μ)**: 3.0 jobs/hora

## Formulación del Modelo

### Condición de Estabilidad

El sistema es estable si y solo si:
\[
\rho = \frac{\lambda}{\mu} < 1
\]

### Fórmulas de Little y Métricas

#### Factor de Utilización
\[
\rho = \frac{\lambda}{\mu}
\]

#### Número Esperado en el Sistema (L)
\[
L = \frac{\rho}{1 - \rho} = \frac{\lambda}{\mu - \lambda}
\]

#### Tiempo Esperado en el Sistema (W)
\[
W = \frac{1}{\mu - \lambda}
\]

#### Número Esperado en la Cola (Lq)
\[
L_q = \frac{\rho^2}{1 - \rho} = \frac{\lambda^2}{\mu(\mu - \lambda)}
\]

#### Tiempo Esperado en la Cola (Wq)
\[
W_q = \frac{\rho}{\mu - \lambda} = \frac{\lambda}{\mu(\mu - \lambda)}
\]

#### Probabilidad de Sistema Vacío (P0)
\[
P_0 = 1 - \rho
\]

#### Probabilidad de n Jobs en el Sistema (Pn)
\[
P_n = \rho^n \cdot P_0 = \rho^n (1 - \rho)
\]

## Solución

### Resultados Teóricos

Con λ = 2.0 y μ = 3.0:

- **Factor de utilización (ρ)**: 0.6667
  - 66.67% del tiempo el servidor está ocupado

- **Número esperado en el sistema (L)**: 2.0 jobs
  - Promedio de jobs en el sistema (en servicio + en cola)

- **Tiempo esperado en el sistema (W)**: 1.0 horas
  - Tiempo promedio desde que llega hasta que termina

- **Número esperado en la cola (Lq)**: 1.3333 jobs
  - Promedio de jobs esperando en la cola

- **Tiempo esperado en la cola (Wq)**: 0.6667 horas
  - Tiempo promedio de espera antes de ser atendido

- **Probabilidad de sistema vacío (P0)**: 0.3333
  - 33.33% del tiempo el servidor está libre

## Interpretación

### Análisis del Factor de Utilización

- **ρ < 0.7**: Sistema bien dimensionado
- **0.7 ≤ ρ < 0.9**: Carga moderada, considerar monitoreo
- **ρ ≥ 0.9**: Alta carga, riesgo de colapso

### Recomendaciones

1. **Si ρ cerca de 1**: El sistema colapsa, aumentar capacidad
2. **Dimensionar μ**: Aumentar runners o optimizar jobs
3. **Reducir λ**: Implementar batching o priorización
4. **Monitoreo**: Usar métricas para detectar cuellos de botella

### Aplicaciones Prácticas

- Dimensionamiento de infraestructura CI/CD
- Optimización de pipelines de despliegue
- Planificación de recursos computacionales
- Análisis de cuellos de botella en procesos automatizados

## Uso

```bash
python3 cola_mm1.py
```

## Archivos

- `cola_mm1.py`: Implementación del modelo M/M/1
- `README.md`: Esta documentación

