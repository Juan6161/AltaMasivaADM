@echo off
chcp 65001 >nul
title Instalación - Generador de Personas Físicas

echo ============================================================
echo   Instalación - Generador de Personas Físicas
echo ============================================================
echo.

REM Cambiar al directorio del script
cd /d "%~dp0"

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no está instalado o no está en el PATH
    echo Por favor, instala Python desde https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [✓] Python detectado
python --version
echo.

REM Crear entorno virtual
echo [1/4] Creando entorno virtual...
if exist "venv" (
    echo [INFO] El entorno virtual ya existe. Omitiendo creación...
) else (
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] No se pudo crear el entorno virtual
        pause
        exit /b 1
    )
    echo [✓] Entorno virtual creado
)
echo.

REM Activar entorno virtual
echo [2/4] Activando entorno virtual...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] No se pudo activar el entorno virtual
    pause
    exit /b 1
)
echo [✓] Entorno virtual activado
echo.

REM Instalar dependencias
echo [3/4] Instalando dependencias...
if exist "requirements.txt" (
    pip install -r requirements.txt
) else (
    pip install flask
)
if errorlevel 1 (
    echo [ERROR] No se pudieron instalar las dependencias
    pause
    exit /b 1
)
echo [✓] Dependencias instaladas
echo.

REM Crear carpeta templates si no existe
echo [4/4] Verificando estructura del proyecto...
if not exist "templates" (
    mkdir templates
    echo [✓] Carpeta templates creada
) else (
    echo [✓] Carpeta templates existe
)

if not exist "templates\index.html" (
    echo [INFO] No se encontró templates\index.html
    echo        Este archivo es necesario para que la aplicación funcione.
)
echo.

echo ============================================================
echo   ¡Instalación completada!
echo ============================================================
echo.
echo Para ejecutar la aplicación, usa el archivo: ejecutar.bat
echo O ejecuta manualmente: python app.py
echo.
pause

