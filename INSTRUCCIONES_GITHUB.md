# 📤 Instrucciones para Subir a GitHub

## Paso 1: Crear un repositorio en GitHub

1. Ve a [GitHub](https://github.com) e inicia sesión
2. Haz clic en el botón "+" en la esquina superior derecha
3. Selecciona "New repository"
4. Completa los siguientes campos:
   - **Repository name**: `generador-personas-fisicas` (o el nombre que prefieras)
   - **Description**: "Generador de datos de personas físicas con Flask"
   - **Visibility**: Público o Privado (según tu preferencia)
   - **NO marques** "Initialize this repository with a README" (ya tenemos uno)
5. Haz clic en "Create repository"

## Paso 2: Inicializar Git en tu proyecto

Abre la terminal en la carpeta del proyecto y ejecuta:

```bash
cd "C:\Users\jledesma\Desktop\Generador\Generador 2"
git init
```

## Paso 3: Agregar todos los archivos

```bash
git add .
```

## Paso 4: Hacer el primer commit

```bash
git commit -m "Initial commit: Generador de Personas Físicas"
```

## Paso 5: Conectar con el repositorio remoto

Reemplaza `TU_USUARIO` con tu nombre de usuario de GitHub:

```bash
git remote add origin https://github.com/TU_USUARIO/generador-personas-fisicas.git
```

## Paso 6: Subir el código

```bash
git branch -M main
git push -u origin main
```

## Comandos Adicionales Útiles

### Ver el estado de los archivos
```bash
git status
```

### Ver los cambios realizados
```bash
git diff
```

### Agregar cambios específicos
```bash
git add nombre_archivo.py
```

### Hacer commit con mensaje
```bash
git commit -m "Descripción de los cambios"
```

### Subir cambios al repositorio
```bash
git push
```

### Ver el historial de commits
```bash
git log
```

## Actualizar el README.md

Antes de subir, recuerda actualizar el README.md con:
- Tu nombre de usuario de GitHub en la URL del repositorio
- Tu información de contacto si lo deseas
- Cualquier otra información relevante

## Notas Importantes

- El archivo `.gitignore` ya está configurado para ignorar archivos innecesarios como `venv/`, `__pycache__/`, etc.
- Los archivos `.bat` son específicos para Windows. Si quieres agregar scripts para Linux/Mac, puedes crear archivos `.sh`
- Asegúrate de no subir información sensible como contraseñas o API keys

## Problemas Comunes

### Error: "remote origin already exists"
Si ya existe un remoto, puedes eliminarlo y agregarlo de nuevo:
```bash
git remote remove origin
git remote add origin https://github.com/TU_USUARIO/generador-personas-fisicas.git
```

### Error: "Authentication failed"
Asegúrate de estar autenticado en GitHub. Puedes usar:
- GitHub Desktop
- GitHub CLI
- Personal Access Token en lugar de contraseña

### Error: "Permission denied"
Verifica que tengas permisos para escribir en el repositorio y que la URL sea correcta.

## Siguiente Paso

Una vez que hayas subido el código, puedes:
1. Agregar una descripción al repositorio
2. Agregar tags/releases
3. Configurar GitHub Pages si deseas hospedar la aplicación
4. Agregar badges al README
5. Configurar GitHub Actions para CI/CD

¡Listo! Tu proyecto ahora está en GitHub. 🎉

