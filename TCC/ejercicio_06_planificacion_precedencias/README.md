# Ejercicio 6: Planificación con Precedencias (CPM/PERT)

## Descripción del Problema

Determinar la **ruta crítica** en un pequeño proyecto de integración y despliegue. El proyecto está compuesto por tareas con relaciones de precedencia y duraciones determinísticas.

Este problema se resuelve usando el **Método de Ruta Crítica (CPM - Critical Path Method)**.

## Modelo de Investigación de Operaciones

Se utiliza el **Método CPM** porque:
- ✔ El proyecto tiene **tareas con precedencias** (dependencias)
- ✔ Las duraciones son **determinísticas** (conocidas con certeza)
- ✔ Se busca identificar la **ruta crítica** (camino más largo)
- ✔ Permite calcular **holguras** (tiempos de margen)

## Datos del Problema

### Tareas y Precedencias

| Tarea | Duración | Predecesores |
|-------|----------|--------------|
| A | 3 | Ninguna |
| B | 2 | A |
| C | 4 | A |
| D | 2 | B, C |
| E | 3 | C |
| F | 1 | D, E |

### Representación Gráfica

```
    A (3)
   / \
  B(2) C(4)
   \ / \
    D(2) E(3)
     \ /
      F(1)
```

## Formulación del Modelo

### Variables

- **ES** (Earliest Start): Tiempo más temprano de inicio
- **EF** (Earliest Finish): Tiempo más temprano de finalización
- **LS** (Latest Start): Tiempo más tardío de inicio
- **LF** (Latest Finish): Tiempo más tardío de finalización
- **Holgura** (Slack): Margen de tiempo disponible = LS - ES = LF - EF

### Cálculos

#### Escalada hacia adelante (Forward Pass)

Para cada tarea:
- **ES** = max(EF de todos los predecesores)
- **EF** = ES + Duración

#### Escalada hacia atrás (Backward Pass)

Para cada tarea:
- **LF** = min(LS de todos los sucesores)
- **LS** = LF - Duración

#### Ruta Crítica

Tareas con **holgura = 0** forman la ruta crítica.

## Solución

### Resultados del Análisis

**Tiempos más tempranos (ES, EF):**
- A: ES=0, EF=3
- B: ES=3, EF=5
- C: ES=3, EF=7
- D: ES=7, EF=9
- E: ES=7, EF=10
- F: ES=10, EF=11

**Tiempos más tardíos (LS, LF):**
- A: LS=0, LF=3
- B: LS=6, LF=8
- C: LS=3, LF=7
- D: LS=8, LF=10
- E: LS=7, LF=10
- F: LS=10, LF=11

**Holguras:**
- A: 0 (crítica)
- B: 3
- C: 0 (crítica)
- D: 1
- E: 0 (crítica)
- F: 0 (crítica)

### Ruta Crítica

**Tareas en ruta crítica:** A → C → E → F

**Duración del proyecto (tiempo mínimo): 11 unidades de tiempo**

## Interpretación

Las actividades en la **ruta crítica** no admiten holgura; cualquier retraso en estas tareas se traduce directamente en retraso de la entrega del proyecto.

**Recomendaciones:**
- Asignar recursos adicionales a las tareas críticas para reducir la duración
- Monitorear de cerca las tareas A, C, E y F
- Las tareas B y D tienen holgura, permitiendo cierta flexibilidad

Este modelo es esencial para:
- Planificación de proyectos de software
- Gestión de dependencias en CI/CD
- Optimización de pipelines de despliegue
- Identificación de cuellos de botella

## Uso

```bash
python3 cpm_pert.py
```

## Archivos

- `cpm_pert.py`: Implementación del método CPM
- `README.md`: Esta documentación

