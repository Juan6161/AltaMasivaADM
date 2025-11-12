# 🚀 Guía de Despliegue - Generador de Personas Físicas

Esta guía te ayudará a desplegar tu aplicación Flask en diferentes plataformas de hosting gratuitas.

## 📋 Opciones de Hosting Gratuito

### 1. Render.com (Recomendado) ⭐
- **Gratis**: Sí (con limitaciones)
- **URL personalizada**: Sí (ej: `tu-app.onrender.com`)
- **SSL**: Sí (automático)
- **Facilidad**: ⭐⭐⭐⭐⭐

### 2. Railway.app
- **Gratis**: $5 créditos mensuales
- **URL personalizada**: Sí
- **SSL**: Sí (automático)
- **Facilidad**: ⭐⭐⭐⭐

### 3. PythonAnywhere
- **Gratis**: Sí (con limitaciones)
- **URL personalizada**: Sí (ej: `tu-usuario.pythonanywhere.com`)
- **SSL**: Sí
- **Facilidad**: ⭐⭐⭐

### 4. Fly.io
- **Gratis**: Sí (con limitaciones)
- **URL personalizada**: Sí
- **SSL**: Sí (automático)
- **Facilidad**: ⭐⭐⭐

---

## 🌐 Opción 1: Desplegar en Render.com

### Paso 1: Preparar el Repositorio
1. Sube tu código a GitHub (si no lo has hecho)
2. Asegúrate de que todos los archivos estén en el repositorio

### Paso 2: Crear Cuenta en Render
1. Ve a [render.com](https://render.com)
2. Crea una cuenta (puedes usar tu cuenta de GitHub)
3. Verifica tu email

### Paso 3: Crear Nuevo Web Service
1. En el dashboard, haz clic en **"New +"**
2. Selecciona **"Web Service"**
3. Conecta tu repositorio de GitHub
4. Selecciona el repositorio `generador-personas-fisicas`

### Paso 4: Configurar el Servicio
Completa los siguientes campos:

- **Name**: `generador-personas-fisicas` (o el nombre que prefieras)
- **Region**: Elige la región más cercana
- **Branch**: `main` (o `master`)
- **Root Directory**: (dejar vacío)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn wsgi:app`

### Paso 5: Variables de Entorno (Opcional)
En la sección "Advanced", puedes agregar variables de entorno:
- `FLASK_ENV=production`
- `PYTHON_VERSION=3.11.6`

### Paso 6: Desplegar
1. Haz clic en **"Create Web Service"**
2. Espera a que Render construya y despliegue tu aplicación (5-10 minutos)
3. Una vez completado, obtendrás una URL como: `https://generador-personas-fisicas.onrender.com`

### Paso 7: Acceder a tu Aplicación
- Abre la URL en tu navegador
- ¡Tu aplicación está en vivo! 🎉

### Notas Importantes para Render:
- La aplicación puede "dormir" después de 15 minutos de inactividad (plan gratuito)
- El primer inicio después de dormir puede tardar 30-60 segundos
- Puedes configurar un "health check" para mantenerla activa

---

## 🚂 Opción 2: Desplegar en Railway.app

### Paso 1: Crear Cuenta
1. Ve a [railway.app](https://railway.app)
2. Crea una cuenta (puedes usar GitHub)

### Paso 2: Crear Nuevo Proyecto
1. Haz clic en **"New Project"**
2. Selecciona **"Deploy from GitHub repo"**
3. Conecta tu repositorio

### Paso 3: Configurar
1. Railway detectará automáticamente que es una aplicación Python
2. Usará el archivo `railway.json` para la configuración
3. El despliegue comenzará automáticamente

### Paso 4: Obtener URL
1. Una vez desplegado, Railway te dará una URL
2. Puedes personalizarla en la sección "Settings" > "Networking"

### Notas para Railway:
- Tienes $5 de créditos gratuitos mensuales
- La aplicación se despliega automáticamente en cada push a GitHub
- Puedes ver los logs en tiempo real

---

## 🐍 Opción 3: Desplegar en PythonAnywhere

### Paso 1: Crear Cuenta
1. Ve a [pythonanywhere.com](https://www.pythonanywhere.com)
2. Crea una cuenta gratuita

### Paso 2: Subir Archivos
1. Ve a la pestaña **"Files"**
2. Sube todos los archivos del proyecto
3. Asegúrate de mantener la estructura de carpetas

### Paso 3: Configurar Web App
1. Ve a la pestaña **"Web"**
2. Haz clic en **"Add a new web app"**
3. Selecciona **"Flask"**
4. Elige la versión de Python (3.10 o superior)
5. Selecciona el archivo `app.py`

### Paso 4: Configurar WSGI
1. Edita el archivo WSGI (en la pestaña "Web")
2. Reemplaza el contenido con:
```python
import sys
path = '/home/tu-usuario/generador-personas-fisicas'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

### Paso 5: Instalar Dependencias
1. Ve a la pestaña **"Tasks"**
2. Crea una nueva tarea con:
```bash
pip3.10 install --user -r requirements.txt
```

### Paso 6: Recargar
1. Ve a la pestaña **"Web"**
2. Haz clic en **"Reload"**
3. Tu aplicación estará disponible en `tu-usuario.pythonanywhere.com`

---

## ✈️ Opción 4: Desplegar en Fly.io

### Paso 1: Instalar Fly CLI
```bash
# Windows (PowerShell)
iwr https://fly.io/install.ps1 -useb | iex

# O descarga desde: https://fly.io/docs/getting-started/installing-flyctl/
```

### Paso 2: Crear Cuenta
```bash
fly auth signup
```

### Paso 3: Crear Aplicación
```bash
cd "C:\Users\jledesma\Desktop\Generador\Generador 2"
fly launch
```

### Paso 4: Desplegar
```bash
fly deploy
```

### Paso 5: Ver URL
```bash
fly open
```

---

## 🔧 Solución de Problemas Comunes

### Error: "Module not found"
- Verifica que `requirements.txt` incluya todas las dependencias
- Asegúrate de que el entorno virtual no esté incluido en el repositorio

### Error: "Application failed to respond"
- Verifica que el puerto esté configurado correctamente (debe usar la variable `PORT`)
- Asegúrate de que `gunicorn` esté en `requirements.txt`

### Error: "Template not found"
- Verifica que la carpeta `templates` esté en el repositorio
- Asegúrate de que `index.html` esté en `templates/`

### La aplicación se duerme (Render)
- Esto es normal en el plan gratuito
- Considera usar un servicio de "ping" para mantenerla activa
- O actualiza al plan pago

### Error de memoria
- Reduce la cantidad máxima de personas generadas
- Optimiza el código para usar menos memoria

---

## 📝 Checklist Pre-Despliegue

Antes de desplegar, asegúrate de:

- [ ] Todos los archivos están en el repositorio
- [ ] `requirements.txt` está actualizado
- [ ] `.gitignore` excluye `venv/` y `__pycache__/`
- [ ] `Procfile` existe y es correcto
- [ ] `wsgi.py` existe
- [ ] `runtime.txt` especifica la versión de Python
- [ ] La aplicación funciona localmente
- [ ] No hay información sensible en el código

---

## 🔄 Actualizar la Aplicación

Para actualizar tu aplicación después de hacer cambios:

1. **GitHub + Render/Railway**: Simplemente haz push a GitHub, el despliegue es automático
2. **PythonAnywhere**: Sube los archivos nuevos y recarga la aplicación
3. **Fly.io**: Ejecuta `fly deploy` de nuevo

---

## 🌍 Dominio Personalizado

La mayoría de plataformas permiten usar un dominio personalizado:

1. **Render**: Settings > Custom Domain
2. **Railway**: Settings > Networking > Custom Domain
3. **PythonAnywhere**: Web > Web app > Static files / Static files mapping
4. **Fly.io**: `fly domains add tu-dominio.com`

---

## 📞 Soporte

Si tienes problemas:
1. Revisa los logs de la aplicación en la plataforma
2. Verifica que todos los archivos estén correctos
3. Consulta la documentación de la plataforma
4. Abre un issue en GitHub

---

## 🎉 ¡Listo!

Una vez desplegado, tu aplicación estará disponible 24/7 en una URL pública. ¡Ya no necesitarás ejecutar el archivo `.bat` manualmente!

**Recomendación**: Empieza con **Render.com** ya que es la opción más fácil y tiene buena documentación.
