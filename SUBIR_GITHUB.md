# Instrucciones para Subir a GitHub

El repositorio Git ya está inicializado y el commit inicial está hecho. Sigue estos pasos para subirlo a GitHub:

## Paso 1: Crear Repositorio en GitHub

1. Ve a [GitHub](https://github.com) e inicia sesión
2. Haz clic en el botón **"+"** (arriba a la derecha) → **"New repository"**
3. Configura el repositorio:
   - **Repository name:** `IO` (o el nombre que prefieras)
   - **Description:** "Aplicación de Modelos de Investigación de Operaciones al Desarrollo de Software"
   - **Visibility:** Público o Privado (según prefieras)
   - **NO marques** "Add a README file" (ya lo tenemos)
   - **NO marques** "Add .gitignore" (ya lo tenemos)
   - **NO marques** "Choose a license" (opcional)
4. Haz clic en **"Create repository"**

## Paso 2: Conectar Repositorio Local con GitHub

Después de crear el repositorio, GitHub te mostrará comandos. Ejecuta estos comandos (reemplaza `TU_USUARIO` y `TU_REPOSITORIO`):

```bash
cd /Users/matos/repositorios/IO

# Conectar con GitHub (reemplaza con tu URL)
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git

# O si usas SSH:
# git remote add origin git@github.com:TU_USUARIO/TU_REPOSITORIO.git

# Verificar que se agregó correctamente
git remote -v
```

## Paso 3: Subir el Código

```bash
# Asegurarse de estar en la rama main
git branch -M main

# Subir el código a GitHub
git push -u origin main
```

Si GitHub te pide autenticación:
- **HTTPS:** Usa un Personal Access Token (no tu contraseña)
- **SSH:** Asegúrate de tener tu clave SSH configurada

## Verificación

Después de hacer push, verifica en GitHub:
- ✅ Todos los archivos están presentes
- ✅ La estructura de carpetas es correcta
- ✅ Los README.md se muestran correctamente
- ✅ El .gitignore está funcionando

## Comandos Útiles para el Futuro

### Ver estado
```bash
git status
```

### Agregar cambios
```bash
git add .
git commit -m "Descripción de los cambios"
git push
```

### Ver historial
```bash
git log --oneline
```

### Actualizar desde GitHub (si trabajas en varias máquinas)
```bash
git pull
```

## Estructura que se Subirá

```
IO/
├── .gitignore
├── README.md
├── requirements.txt
├── test_ejercicios.py
├── RESULTADOS_PRUEBAS.md
├── INSTRUCCIONES_GITHUB.md
├── SUBIR_GITHUB.md (este archivo)
├── TCC/
│   ├── README.md
│   ├── MARCO_TEORICO.md
│   ├── ANALISIS_SENSIBILIDAD.md
│   ├── PROPUESTAS_PRACTICAS.md
│   └── ejercicio_XX_*/
└── ejercicio_XX_*/ (10 ejercicios)
```

## Notas Importantes

- El archivo `EJEMPLO .pdf` se incluirá (si es muy grande, considera usar Git LFS)
- Todos los archivos `.py`, `.md`, `.txt` se subirán
- Los archivos en `.gitignore` (como `__pycache__/`) NO se subirán
- La carpeta `TCC/` contiene el trabajo principal del TCC

## Solución de Problemas

### Error: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
```

### Error de autenticación
- Para HTTPS: Crea un Personal Access Token en GitHub Settings → Developer settings → Personal access tokens
- Para SSH: Configura tu clave SSH en GitHub Settings → SSH and GPG keys

### Error: "failed to push some refs"
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

---

**¡Listo!** Una vez completados estos pasos, tu proyecto estará en GitHub.

