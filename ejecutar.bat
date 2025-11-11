@echo off
chcp 65001 >nul
title Generador de Personas Físicas

echo ============================================================
echo   Generador de Personas Físicas - Iniciando Servidor
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
echo.

REM Verificar si existe el entorno virtual
if exist "venv\Scripts\activate.bat" (
    echo [✓] Activando entorno virtual...
    call venv\Scripts\activate.bat
) else (
    echo [INFO] No se encontró entorno virtual. Usando Python global...
    echo [INFO] Si prefieres usar un entorno virtual, ejecuta:
    echo        python -m venv venv
    echo        venv\Scripts\activate.bat
    echo.
)

REM Verificar si Flask está instalado
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo [INFO] Flask no está instalado. Instalando...
    pip install flask
    if errorlevel 1 (
        echo [ERROR] No se pudo instalar Flask
        pause
        exit /b 1
    )
    echo [✓] Flask instalado correctamente
    echo.
) else (
    echo [✓] Flask está instalado
    echo.
)

REM Verificar si existe la carpeta templates
if not exist "templates" (
    echo [INFO] Creando carpeta templates...
    mkdir templates
)

REM Verificar si existe index.html
if not exist "templates\index.html" (
    echo [ADVERTENCIA] No se encontró templates\index.html
    echo La aplicación puede no funcionar correctamente sin este archivo.
    echo.
)

echo ============================================================
echo   Iniciando servidor...
echo ============================================================
echo.
echo El servidor se abrirá en: http://127.0.0.1:5000
echo Presiona Ctrl+C para detener el servidor
echo.

REM Ejecutar la aplicación
python app.py

REM Si la aplicación se cierra, mostrar mensaje
echo.
echo [INFO] Servidor detenido
pause

