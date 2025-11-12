# 🚀 Despliegue Rápido - Render.com

## Pasos Rápidos (5 minutos)

### 1. Subir a GitHub
```bash
git add .
git commit -m "Preparado para despliegue"
git push
```

### 2. Crear cuenta en Render
1. Ve a [render.com](https://render.com)
2. Crea cuenta con GitHub
3. Verifica email

### 3. Crear Web Service
1. Click en **"New +"** → **"Web Service"**
2. Conecta tu repositorio
3. Configura:
   - **Name**: `generador-personas-fisicas`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn wsgi:app`
4. Click **"Create Web Service"**

### 4. ¡Listo! 🎉
- Espera 5-10 minutos
- Tu app estará en: `https://generador-personas-fisicas.onrender.com`

## Notas Importantes

- **Plan Gratuito**: La app puede "dormir" después de 15 min de inactividad
- **Primer inicio**: Puede tardar 30-60 segundos si está dormida
- **SSL**: Automático y gratuito
- **Dominio**: Puedes agregar dominio personalizado después

## Solución Rápida de Problemas

**Error en build?**
- Verifica que `requirements.txt` tenga todas las dependencias
- Revisa los logs en Render

**App no responde?**
- Espera 30-60 segundos (puede estar "despertando")
- Revisa los logs en Render

**¿Necesitas más ayuda?**
- Revisa `DESPLIEGUE.md` para instrucciones detalladas
- Consulta la documentación de Render: https://render.com/docs
