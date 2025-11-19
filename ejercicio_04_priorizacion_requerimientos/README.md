# Ejercicio 4: Priorización de Requerimientos (Problema de la Mochila 0-1)

## Descripción del Problema

Seleccionar un conjunto de features que **maximizan el valor (beneficio)** sujeto a la **capacidad de horas del sprint**. Cada feature puede ser incluida o no (decisión binaria), y se busca optimizar la priorización del backlog.

Este problema corresponde al **Problema de la Mochila 0-1** (0-1 Knapsack Problem).

## Modelo de Investigación de Operaciones

Se utiliza el **Modelo de Knapsack 0-1** porque:
- ✔ Cada feature puede ser **seleccionada o no** (decisión binaria)
- ✔ Existe una **restricción de capacidad** (horas disponibles)
- ✔ El objetivo es **maximizar el valor total**
- ✔ No se pueden fraccionar las features

## Datos del Problema

### Features Disponibles

| Feature | Valor | Esfuerzo (horas) |
|---------|-------|------------------|
| Login OAuth | 10 | 40 |
| Reporting Module | 15 | 70 |
| Payment Gateway | 20 | 90 |
| Admin Dashboard | 8 | 30 |
| Notifications | 7 | 20 |
| Analytics | 12 | 50 |

**Capacidad del sprint: 200 horas**

## Formulación del Modelo

### Variables de Decisión

\[
x_j = \begin{cases}
1 & \text{si la feature } j \text{ es seleccionada} \\
0 & \text{en caso contrario}
\end{cases}
\]

### Función Objetivo

Maximizar el valor total:

\[
\text{Max } Z = \sum_{j=1}^{n} v_j \cdot x_j
\]

Donde \(v_j\) es el valor de la feature \(j\).

### Restricciones

#### Restricción de capacidad:

\[
\sum_{j=1}^{n} w_j \cdot x_j \leq W
\]

Donde:
- \(w_j\) es el esfuerzo (peso) de la feature \(j\)
- \(W = 200\) es la capacidad del sprint

#### Variables binarias:

\[
x_j \in \{0,1\} \quad \forall j
\]

## Solución

### Resultado Óptimo

**Valor total máximo: 49**

**Features seleccionadas:**
- Login OAuth (Valor: 10, Esfuerzo: 40h)
- Payment Gateway (Valor: 20, Esfuerzo: 90h)
- Notifications (Valor: 7, Esfuerzo: 20h)
- Analytics (Valor: 12, Esfuerzo: 50h)

**Esfuerzo total utilizado: 200 horas** (capacidad completa)

### Método de Solución

El código implementa **Programación Dinámica** para resolver el problema de la mochila 0-1:

1. **Tabla DP**: `dp[i][w]` = máximo valor con los primeros `i` items y capacidad `w`
2. **Recurrencia**: 
   \[
   dp[i][w] = \max(dp[i-1][w], dp[i-1][w-w_i] + v_i)
   \]
3. **Reconstrucción**: Se reconstruye la solución óptima desde la tabla DP

**Complejidad**: O(n × W) donde n es el número de features y W es la capacidad.

## Interpretación

La solución óptima prioriza features con mejor **ratio valor/esfuerzo** pero respetando el límite de horas. El resultado propone un backlog seleccionado para el sprint que maximiza el valor entregado.

Este modelo es muy útil para:
- Priorización de features en sprints
- Selección de historias de usuario
- Optimización de backlogs
- Planificación de releases

## Uso

```bash
python3 knapsack.py
```

## Archivos

- `knapsack.py`: Implementación con programación dinámica
- `README.md`: Esta documentación

