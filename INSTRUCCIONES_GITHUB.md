# Instrucciones para Subir a GitHub

## Pasos para inicializar y subir el repositorio

### 1. Inicializar Git (si no está inicializado)

```bash
git init
```

### 2. Agregar todos los archivos

```bash
git add .
```

### 3. Hacer el primer commit

```bash
git commit -m "Initial commit: 10 ejercicios de Investigación de Operaciones"
```

### 4. Crear repositorio en GitHub

1. Ve a [GitHub](https://github.com)
2. Crea un nuevo repositorio (público o privado)
3. **NO** inicialices con README, .gitignore o licencia (ya los tenemos)

### 5. Conectar repositorio local con GitHub

```bash
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
```

Reemplaza `TU_USUARIO` y `TU_REPOSITORIO` con tus datos.

### 6. Subir el código

```bash
git branch -M main
git push -u origin main
```

## Estructura del repositorio

El repositorio contiene:

```
IO/
├── .gitignore                    # Archivos a ignorar
├── README.md                      # Documentación principal
├── requirements.txt               # Dependencias de Python
├── test_ejercicios.py            # Script de prueba
├── RESULTADOS_PRUEBAS.md         # Resultados de pruebas
├── INSTRUCCIONES_GITHUB.md       # Este archivo
├── EJEMPLO .pdf                  # Documento original (opcional)
└── ejercicio_XX_*/              # 10 carpetas con ejercicios
    ├── README.md                  # Documentación del ejercicio
    └── *.py                       # Código Python
```

## Archivos incluidos en .gitignore

El archivo `.gitignore` está configurado para ignorar:

- ✅ Archivos compilados de Python (`__pycache__/`, `*.pyc`)
- ✅ Entornos virtuales (`venv/`, `.venv/`, `env/`)
- ✅ Archivos de IDEs (`.vscode/`, `.idea/`)
- ✅ Archivos temporales y logs
- ✅ Archivos del sistema (`.DS_Store` en macOS)
- ✅ Archivos de distribución y build

## Verificar antes de subir

```bash
# Ver qué archivos se van a subir
git status

# Ver archivos ignorados
git status --ignored
```

## Comandos útiles

### Ver cambios
```bash
git status
```

### Agregar cambios específicos
```bash
git add archivo.py
git commit -m "Descripción del cambio"
```

### Actualizar repositorio remoto
```bash
git push
```

### Clonar el repositorio (desde otra máquina)
```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO
pip install -r requirements.txt
```

## Notas importantes

1. **El PDF "EJEMPLO .pdf" se incluirá** en el repositorio (no está en .gitignore)
   - Si es muy grande, puedes agregarlo a .gitignore
   - O usar Git LFS para archivos grandes

2. **Los resultados de pruebas** (`RESULTADOS_PRUEBAS.md`) se incluyen para documentación

3. **Las dependencias** están en `requirements.txt` para fácil instalación

4. **Cada ejercicio** tiene su propia documentación en `README.md`

## Licencia (opcional)

Si quieres agregar una licencia, crea un archivo `LICENSE` o agrégalo desde GitHub al crear el repositorio.

## Badges útiles para README.md (opcional)

Puedes agregar badges al README principal:

```markdown
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-complete-success.svg)
```

