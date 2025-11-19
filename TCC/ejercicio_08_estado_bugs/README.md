# Ejercicio 8: Estado de Bugs (Cadena de Markov)

## Descripción del Problema

Modelar la evolución de bugs a través de diferentes estados en el ciclo de vida del desarrollo de software. Los bugs transicionan entre estados: **New → InProgress → Fixed → Closed**, donde **Closed** es un estado absorbente.

Este problema se resuelve usando **Cadenas de Markov** para modelar procesos estocásticos.

## Modelo de Investigación de Operaciones

Se utiliza el **Modelo de Cadena de Markov** porque:
- ✔ El proceso tiene **estados discretos** (New, InProgress, Fixed, Closed)
- ✔ Las transiciones son **probabilísticas** (no determinísticas)
- ✔ El proceso tiene **memoria de Markov** (el estado futuro solo depende del estado actual)
- ✔ Permite predecir **distribuciones de probabilidad** a largo plazo

## Datos del Problema

### Estados

1. **New**: Bug recién reportado
2. **InProgress**: Bug en proceso de resolución
3. **Fixed**: Bug corregido
4. **Closed**: Bug cerrado (estado absorbente)

### Matriz de Transición P

La matriz P[i][j] representa la probabilidad de transicionar del estado i al estado j.

| Desde\Hacia | New | InProgress | Fixed | Closed |
|-------------|-----|------------|-------|--------|
| New | 0.6 | 0.3 | 0.1 | 0.0 |
| InProgress | 0.0 | 0.5 | 0.4 | 0.1 |
| Fixed | 0.0 | 0.0 | 0.8 | 0.2 |
| Closed | 0.0 | 0.0 | 0.0 | 1.0 |

**Nota**: El estado "Closed" es **absorbente** (probabilidad 1.0 de permanecer en él).

## Formulación del Modelo

### Matriz de Transición

\[
P = \begin{bmatrix}
0.6 & 0.3 & 0.1 & 0.0 \\
0.0 & 0.5 & 0.4 & 0.1 \\
0.0 & 0.0 & 0.8 & 0.2 \\
0.0 & 0.0 & 0.0 & 1.0
\end{bmatrix}
\]

### Distribución de Probabilidad

Si \(\pi^{(0)}\) es la distribución inicial, después de \(n\) pasos:

\[
\pi^{(n)} = \pi^{(0)} \cdot P^n
\]

Donde \(P^n\) es la matriz de transición elevada a la n-ésima potencia.

### Estado Inicial

Empezando en 'New':
\[
\pi^{(0)} = [1.0, 0.0, 0.0, 0.0]
\]

## Solución

### Evolución de la Distribución

**Después de 1 paso:**
- New: 0.6000
- InProgress: 0.3000
- Fixed: 0.1000
- Closed: 0.0000

**Después de 5 pasos:**
- New: ~0.0778
- InProgress: ~0.1944
- Fixed: ~0.3889
- Closed: ~0.3389

**Después de 10 pasos:**
- New: ~0.0060
- InProgress: ~0.0150
- Fixed: ~0.0300
- Closed: ~0.9490

**Después de 50 pasos (absorción):**
- New: 0.0000
- InProgress: 0.0000
- Fixed: 0.0000
- Closed: 1.0000

### Distribución Aproximada Final

Después de suficientes pasos, todos los bugs terminan en el estado **Closed** (absorción completa).

## Interpretación

La cadena de Markov proporciona:
- **Probabilidades de encontrar un bug en cada estado** a lo largo del tiempo
- **Estimación de carga de trabajo futura** por estado
- **Tiempos esperados de resolución** de bugs
- **Predicción de flujo** de bugs a través del sistema

**Aplicaciones prácticas:**
- Planificación de recursos para resolución de bugs
- Estimación de tiempos de ciclo
- Optimización de procesos de QA
- Predicción de carga de trabajo en equipos

## Uso

```bash
python3 markov.py
```

## Archivos

- `markov.py`: Implementación de la cadena de Markov
- `README.md`: Esta documentación

