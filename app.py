#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generador de Personas Físicas - Aplicación Web
"""

from flask import Flask, render_template, request, send_file, jsonify
import random
from datetime import datetime, timedelta
import os
import io

app = Flask(__name__)

# Variable global para almacenar el contenido generado en memoria
archivo_generado = None

# Nombres masculinos comunes en Argentina
NOMBRES_MASCULINOS = [
    "Juan", "Carlos", "Luis", "Miguel", "Jose", "Pedro", "Alejandro", "Fernando",
    "Sergio", "Diego", "Roberto", "Daniel", "Pablo", "Ricardo", "Mario", "Gustavo",
    "Sebastian", "Facundo", "Nicolas", "Matias", "Ezequiel", "Andres", "Martin",
    "Rodrigo", "Javier", "Gonzalo", "Leonardo", "Maximo", "Emiliano", "Ignacio",
    "Adrian", "Agustin", "Alberto", "Alexis", "Antonio", "Ariel", "Armando", "Arturo",
    "Augusto", "Benjamin", "Bruno", "Camilo", "Cesar", "Cristian", "Dario", "David",
    "Edgar", "Eduardo", "Enzo", "Ernesto", "Esteban", "Fabian", "Federico", "Felipe",
    "Francisco", "Gabriel", "Gerardo", "Hector", "Hernan", "Horacio", "Hugo", "Ivan",
    "Jorge", "Julian", "Julio", "Lautaro", "Lucas", "Manuel", "Marcelo",
    "Marcos", "Mauricio", "Maximiliano", "Nahuel", "Omar", "Oscar", "Patricio", "Raul",
    "Rene", "Ruben", "Samuel", "Santiago", "Tomas", "Ulises", "Victor", "Walter"
]

# Nombres femeninos comunes en Argentina
NOMBRES_FEMENINOS = [
    "Maria", "Ana", "Laura", "Carmen", "Sofia", "Lucia", "Elena", "Patricia",
    "Monica", "Andrea", "Veronica", "Cristina", "Silvia", "Natalia", "Carolina",
    "Gabriela", "Daniela", "Mariana", "Valeria", "Fernanda", "Julieta", "Agustina",
    "Martina", "Catalina", "Isabella", "Emma", "Olivia", "Victoria", "Milagros", "Camila",
    "Adriana", "Alejandra", "Alicia", "Amanda", "Angela", "Antonella", "Araceli", "Beatriz",
    "Belen", "Bianca", "Claudia", "Constanza", "Diana", "Dolores", "Elizabeth", "Emilia",
    "Esperanza", "Estela", "Esther", "Eva", "Fabiana", "Fatima", "Florencia", "Francisca",
    "Gloria", "Graciela", "Guadalupe", "Ines", "Irene", "Iris", "Isabel", "Jazmin",
    "Jimena", "Josefina", "Juana", "Julia", "Karina", "Leticia", "Liliana", "Lorena",
    "Lourdes", "Luisa", "Magdalena", "Manuela", "Marcela", "Margarita", "Marta", "Melisa",
    "Mercedes", "Miriam", "Nancy", "Noelia", "Norma", "Paula", "Pilar", "Raquel",
    "Rebeca", "Rocio", "Rosa", "Roxana", "Sabrina", "Sandra", "Susana", "Teresa"
]

# Apellidos comunes en Argentina
APELLIDOS = [
    "Garcia", "Rodriguez", "Gonzalez", "Fernandez", "Lopez", "Martinez", "Sanchez",
    "Perez", "Gomez", "Martin", "Jimenez", "Ruiz", "Hernandez", "Diaz", "Moreno",
    "Alvarez", "Munoz", "Romero", "Alonso", "Gutierrez", "Navarro", "Torres",
    "Dominguez", "Vazquez", "Ramos", "Gil", "Ramirez", "Serrano", "Blanco", "Suarez",
    "Molina", "Morales", "Ortega", "Delgado", "Castro", "Ortiz", "Rubio", "Marin",
    "Sanz", "Iglesias", "Nunez", "Medina", "Garrido", "Cortes", "Castillo", "Lozano",
    "Aguilar", "Arias", "Benítez", "Bravo", "Cabrera", "Calvo", "Campos", "Cano",
    "Carrasco", "Carvajal", "Contreras", "Cruz", "Duran", "Escobar", "Estrada", "Flores",
    "Fuentes", "Gallardo", "Guerra", "Guerrero", "Herrera", "Ibarra", "Jaramillo", "Lara",
    "Leal", "Leon", "Luna", "Madrid", "Mendez", "Mendoza", "Montes", "Mora",
    "Nieto", "Ochoa", "Oliva", "Pacheco", "Padilla", "Palacios", "Pardo", "Pastor",
    "Peña", "Ponce", "Quesada", "Quintero", "Reyes", "Rivas", "Robles", "Rocha",
    "Salazar", "Salinas", "Santos", "Sierra", "Silva", "Solano", "Soler", "Soto",
    "Tapia", "Toledo", "Valdez", "Valencia", "Vega", "Vidal", "Villa", "Yáñez", "Zamora"
]


def generar_nombre_completo():
    """Genera un nombre completo aleatorio (1 nombre, 1 apellido)"""
    es_mujer = random.choice([True, False])
    
    # Seleccionar un solo nombre
    nombres_lista = NOMBRES_FEMENINOS if es_mujer else NOMBRES_MASCULINOS
    nombre = random.choice(nombres_lista)
    
    # Seleccionar un solo apellido
    apellido = random.choice(APELLIDOS)
    
    nombre_completo = f"{nombre} {apellido}"
    
    # Determinar género basado en el nombre
    es_femenino = nombre in NOMBRES_FEMENINOS
    
    return nombre_completo, es_femenino


def generar_dni():
    """Genera un DNI argentino aleatorio (7-8 dígitos)"""
    longitud = random.choice([7, 8])
    dni = ''.join([str(random.randint(0, 9)) for _ in range(longitud)])
    return dni.zfill(8)


def calcular_cuil(dni, es_femenino):
    """Calcula un CUIL válido basado en el DNI y género"""
    prefijo = "27" if es_femenino else "20"
    cuil_sin_verificador = prefijo + dni
    multiplicadores = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    
    suma = 0
    for i, digito in enumerate(cuil_sin_verificador):
        suma += int(digito) * multiplicadores[i]
    
    resto = suma % 11
    if resto < 2:
        verificador = resto
    else:
        verificador = 11 - resto
    
    cuil = cuil_sin_verificador + str(verificador)
    return cuil


def generar_fecha_ingreso():
    """Genera una fecha de ingreso aleatoria (no mayor a 20 años, formato DDMMAA)"""
    hoy = datetime.now()
    # Fecha mínima: hace 20 años (más antigua)
    fecha_min = hoy - timedelta(days=365 * 20)
    # Fecha máxima: hace 1 año (más reciente)
    fecha_max = hoy - timedelta(days=365)
    
    # Calcular diferencia en días (siempre positiva)
    diferencia_dias = (fecha_max - fecha_min).days
    
    # Generar fecha aleatoria entre fecha_min y fecha_max
    dias_aleatorios = random.randint(0, diferencia_dias)
    fecha = fecha_min + timedelta(days=dias_aleatorios)
    
    return fecha.strftime("%d%m%y")


def rellenar_espacios(texto, longitud, alineacion='izquierda'):
    """Rellena un texto con espacios hasta alcanzar la longitud especificada"""
    texto = str(texto)
    if len(texto) > longitud:
        texto = texto[:longitud]
    
    if alineacion == 'izquierda':
        return texto.ljust(longitud)
    else:
        return texto.rjust(longitud, '0')


def generar_persona():
    """Genera los datos de una persona según las especificaciones"""
    nombre_completo, es_femenino = generar_nombre_completo()
    nombre_formateado = rellenar_espacios(nombre_completo, 25)
    
    dni = generar_dni()
    documento_formateado = rellenar_espacios(dni, 8, 'derecha')
    
    lugar_pago = rellenar_espacios("01011", 5)
    lugar_pago2 = rellenar_espacios("", 5)
    numero_control = rellenar_espacios("01012594", 8)
    cargo = rellenar_espacios("010171", 6)
    
    haberes_sin_aporte = rellenar_espacios("0", 9, 'derecha')
    haberes_con_aporte = rellenar_espacios("0", 9, 'derecha')
    haberes_brutos = rellenar_espacios("0", 9, 'derecha')
    total_descuentos = rellenar_espacios("0", 9, 'derecha')
    
    panta = random.choice(["P", "C", "D"])
    
    salario_familiar = rellenar_espacios("0", 9, 'derecha')
    importe_liquido = rellenar_espacios("0", 9, 'derecha')
    
    fecha_ingreso = generar_fecha_ingreso()
    
    cuil = calcular_cuil(dni, es_femenino)
    cuil_formateado = rellenar_espacios(cuil, 11, 'derecha')
    
    sexo = "M" if es_femenino else "V"
    
    otros = rellenar_espacios("0", 9, 'derecha')
    
    linea = (
        nombre_formateado + documento_formateado + lugar_pago + lugar_pago2 +
        numero_control + cargo + haberes_sin_aporte + haberes_con_aporte +
        haberes_brutos + total_descuentos + panta + salario_familiar +
        importe_liquido + fecha_ingreso + cuil_formateado + sexo + otros
    )
    
    return linea


@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')


@app.route('/generar', methods=['POST'])
def generar():
    """Endpoint para generar personas"""
    global archivo_generado
    try:
        cantidad = int(request.json.get('cantidad', 0))
        
        if cantidad <= 0 or cantidad > 100000:
            return jsonify({'error': 'La cantidad debe ser entre 1 y 100000'}), 400
        
        # Generar personas
        lineas = []
        for i in range(cantidad):
            linea = generar_persona()
            lineas.append(linea)
        
        # Crear contenido en memoria (no guardar en disco)
        contenido = '\n'.join(lineas)
        archivo_generado = contenido
        
        return jsonify({
            'success': True,
            'cantidad': cantidad,
            'mensaje': f'Se generaron {cantidad} personas exitosamente'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/descargar')
def descargar():
    """Endpoint para descargar el archivo generado"""
    global archivo_generado
    try:
        if archivo_generado is None:
            return jsonify({'error': 'No hay archivo generado'}), 404
        
        # Crear archivo en memoria desde los datos almacenados
        archivo = io.BytesIO()
        archivo.write(archivo_generado.encode('utf-8'))
        archivo.seek(0)
        
        nombre_archivo = "personas_generadas.txt"
        return send_file(
            archivo,
            as_attachment=True,
            download_name=nombre_archivo,
            mimetype='text/plain'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Obtener la IP local
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print("=" * 60)
    print("Generador de Personas Físicas - Servidor Web")
    print("=" * 60)
    print(f"\n✓ Servidor iniciado en:")
    print(f"  Local:   http://127.0.0.1:5000")
    print(f"  Red:     http://{local_ip}:5000")
    print(f"\n✓ Presiona Ctrl+C para detener el servidor\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)

