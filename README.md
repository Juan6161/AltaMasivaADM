# 🔷 Generador de Personas Físicas

Aplicación web desarrollada en Flask para generar datos de personas físicas con nombres, DNIs, CUILs y demás información requerida para uso en sistemas.

## 🚀 Características

- **Generación masiva**: Genera hasta 100,000 registros de personas físicas
- **Datos realistas**: Utiliza nombres y apellidos comunes de Argentina
- **CUIL válido**: Calcula automáticamente CUILs válidos según el DNI y género
- **Interfaz web moderna**: Interfaz intuitiva y responsiva
- **Sin almacenamiento en disco**: Los archivos se generan en memoria y se descargan directamente
- **Formato específico**: Genera datos en el formato requerido para sistemas de gestión

## 📋 Requisitos

- Python 3.6 o superior
- Flask 3.0.0 o superior
- Gunicorn (para producción) - Ya incluido en requirements.txt

## 🛠️ Instalación

### Método Rápido (Windows)

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/generador-personas-fisicas.git
   cd generador-personas-fisicas
   ```

2. **Ejecutar el script de instalación**
   - Haz doble clic en `instalar.bat`
   - Este script creará el entorno virtual e instalará las dependencias automáticamente

3. **Ejecutar la aplicación**
   - Haz doble clic en `ejecutar.bat`
   - El servidor se iniciará en http://127.0.0.1:5000

### Método Manual

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/generador-personas-fisicas.git
   cd generador-personas-fisicas
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar entorno virtual**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

4. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

6. **Abrir en el navegador**
   - Navega a http://127.0.0.1:5000

## 📖 Uso

1. Abre la aplicación en tu navegador web
2. Ingresa la cantidad de personas que deseas generar (entre 1 y 100,000)
3. Haz clic en "Generar Personas"
4. Espera a que se complete la generación
5. Haz clic en "Descargar Archivo" (el botón se activará en verde cuando esté listo)
6. El archivo se descargará en formato de texto plano

## 📁 Estructura del Proyecto

```
generador-personas-fisicas/
│
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
├── DESPLIEGUE.md         # Guía de despliegue en la nube
├── LICENSE               # Licencia MIT
├── .gitignore            # Archivos ignorados por Git
├── Procfile              # Configuración para Heroku/Railway
├── runtime.txt           # Versión de Python
├── render.yaml           # Configuración para Render
├── ejecutar.bat          # Script para ejecutar en Windows
├── instalar.bat          # Script para instalar en Windows
└── templates/            # Plantillas HTML
    └── index.html        # Interfaz web principal
```

## 🔧 Tecnologías Utilizadas

- **Python 3.6+**: Lenguaje de programación
- **Flask 3.0.0**: Framework web
- **HTML/CSS/JavaScript**: Frontend
- **Bootstrap**: Estilos (incluidos en el HTML)

## 📝 Formato de Salida

El archivo generado contiene una línea por persona con el siguiente formato:
- Nombre completo (25 caracteres)
- DNI (8 dígitos)
- Lugar de pago (5 caracteres)
- Número de control (8 caracteres)
- Cargo (6 caracteres)
- Haberes y descuentos (varios campos de 9 dígitos)
- Fecha de ingreso (DDMMAA)
- CUIL (11 dígitos)
- Sexo (M/V)
- Otros campos

## 🎯 Características de los Datos Generados

- **Nombres**: 80 nombres masculinos y 80 nombres femeninos comunes en Argentina
- **Apellidos**: 96 apellidos comunes en Argentina
- **DNI**: Números de 7-8 dígitos formateados a 8 dígitos
- **CUIL**: Cálculo válido según algoritmo oficial argentino
- **Fechas**: Fechas de ingreso aleatorias (hasta 20 años atrás)
- **Género**: Determinado automáticamente según el nombre

## 🌐 Despliegue en la Nube

Esta aplicación está lista para desplegarse en plataformas de hosting como Render, Railway, PythonAnywhere, Fly.io, o Heroku.

### Despliegue Rápido en Render (Recomendado - 5 minutos)

**Guía rápida**: Consulta [DESPLIEGUE_RAPIDO.md](DESPLIEGUE_RAPIDO.md) para instrucciones paso a paso.

**Resumen**:
1. Crea una cuenta en [Render](https://render.com)
2. Conecta tu repositorio de GitHub
3. Crea un nuevo Web Service
4. Configuración:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Plan: Free
5. Despliega - ¡Tu aplicación estará disponible en minutos!

Para instrucciones detalladas de despliegue en diferentes plataformas, consulta el archivo [DESPLIEGUE.md](DESPLIEGUE.md)

### Plataformas Soportadas

- ✅ **Render** - Plan gratuito disponible, muy fácil de usar
- ✅ **Railway** - Plan gratuito con $5 de créditos
- ✅ **PythonAnywhere** - Específico para Python
- ✅ **Fly.io** - Plan gratuito generoso
- ✅ **Heroku** - Requiere tarjeta de crédito para plan gratuito

## 🐛 Solución de Problemas

### Error: "No module named 'flask'"
- Asegúrate de haber activado el entorno virtual
- Verifica que Flask esté instalado: `pip list | findstr flask`
- Si no está instalado: `pip install flask`

### Error: "TemplateNotFound: index.html"
- Verifica que existe la carpeta `templates` en el mismo directorio que `app.py`
- Verifica que existe el archivo `index.html` dentro de la carpeta `templates`

### Error de puerto en uso
- Si el puerto 5000 está ocupado, puedes cambiar el puerto en `app.py` (línea 260):
  ```python
  app.run(host='0.0.0.0', port=5000, debug=True)
  ```
  Cambia `5000` por otro puerto, por ejemplo `5001`

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## 👥 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 🌐 Despliegue en Producción

Esta aplicación está lista para desplegarse en diferentes plataformas de hosting:

### Opciones de Hosting Gratuito

- **Render.com** (Recomendado) - Fácil de usar, despliegue automático desde GitHub
- **Railway.app** - $5 créditos gratuitos mensuales
- **PythonAnywhere** - Hosting especializado en Python
- **Fly.io** - Opción moderna con buena documentación

### Instrucciones de Despliegue

Consulta el archivo [DESPLIEGUE.md](DESPLIEGUE.md) para instrucciones detalladas sobre cómo desplegar la aplicación en cada plataforma.

### Despliegue Rápido en Render.com

1. Sube tu código a GitHub
2. Ve a [render.com](https://render.com) y crea una cuenta
3. Crea un nuevo "Web Service"
4. Conecta tu repositorio de GitHub
5. Configura:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn wsgi:app`
6. ¡Listo! Tu aplicación estará disponible en una URL pública

## 📧 Contacto

Para preguntas o sugerencias, por favor abre un issue en el repositorio.

## 🙏 Agradecimientos

- Flask por el excelente framework web
- La comunidad de Python por las herramientas y recursos

---

⭐ Si te gusta este proyecto, considera darle una estrella en GitHub!

