# Ejercicio 7: Gestión de Dependencias y Flujo de Trabajo (Redes de Flujo)

## Descripción del Problema

Asignar capacidad de integración entre ramas y entornos (limitar cuellos de botella) para **maximizar el throughput de entregas**. El objetivo es identificar y optimizar el flujo máximo a través de la red de dependencias.

Este problema se resuelve usando el **Modelo de Flujo Máximo** en redes.

## Modelo de Investigación de Operaciones

Se utiliza el **Modelo de Flujo Máximo** porque:
- ✔ Existe una **red dirigida** con nodos y arcos
- ✔ Los arcos tienen **capacidades** (límites de flujo)
- ✔ Se busca **maximizar el flujo** desde la fuente al sumidero
- ✔ Se deben respetar **restricciones de conservación** de flujo

## Datos del Problema

### Red de Flujo

**Nodos (colas/entornos):**
- `source`: Desarrollo (fuente)
- `branch_dev`: Rama Dev
- `branch_staging`: Rama Staging
- `env_test`: Entorno Test
- `env_staging`: Entorno Staging
- `env_prod`: Entorno Prod
- `sink`: Producción (sumidero)

**Arcos (capacidades de integración):**

| Origen | Destino | Capacidad |
|--------|---------|-----------|
| Desarrollo | Rama Dev | 10 |
| Desarrollo | Rama Staging | 8 |
| Rama Dev | Entorno Test | 6 |
| Rama Dev | Entorno Staging | 5 |
| Rama Staging | Entorno Staging | 7 |
| Entorno Test | Entorno Staging | 4 |
| Entorno Staging | Entorno Prod | 8 |
| Entorno Prod | Producción | 10 |

## Formulación del Modelo

### Variables de Decisión

\[
f_{ij} = \text{flujo a través del arco } (i,j)
\]

### Función Objetivo

Maximizar el flujo al sumidero:

\[
\text{Max } Z = \sum_{j} f_{sj}
\]

Donde \(s\) es el sumidero.

### Restricciones

#### Conservación de flujo (para cada nodo intermedio):

\[
\sum_{i} f_{ij} = \sum_{k} f_{jk} \quad \forall j \text{ (nodo intermedio)}
\]

#### Capacidad de arcos:

\[
0 \leq f_{ij} \leq c_{ij} \quad \forall (i,j)
\]

Donde \(c_{ij}\) es la capacidad del arco \((i,j)\).

## Solución

### Método de Solución

El código implementa dos métodos:

1. **NetworkX (algoritmo de Edmonds-Karp)**
   - Implementación eficiente del algoritmo de flujo máximo
   - Identifica automáticamente cuellos de botella

2. **PuLP (formulación de programación lineal)**
   - Alternativa con formulación explícita
   - Útil para problemas más complejos

### Resultado

El algoritmo encuentra el **flujo máximo** a través de la red y identifica los **cuellos de botella** (arcos saturados que limitan el throughput).

## Interpretación

El flujo máximo representa el **throughput máximo** del pipeline de CI/CD. Los cuellos de botella son los arcos que limitan este throughput.

**Recomendaciones:**
- **Aumentar capacidad** en cuellos de botella
- **Paralelizar pipelines** para aumentar throughput
- **Optimizar procesos** de integración y despliegue
- **Dimensionar infraestructura** según el flujo máximo

**Aplicaciones prácticas:**
- Dimensionamiento de pipelines CI/CD
- Optimización de flujos de trabajo
- Identificación de cuellos de botella
- Planificación de infraestructura

## Uso

```bash
# Con NetworkX (recomendado)
pip install networkx
python3 max_flow.py

# O con PuLP
pip install pulp
python3 max_flow.py
```

## Archivos

- `max_flow.py`: Implementación del algoritmo de flujo máximo
- `README.md`: Esta documentación

