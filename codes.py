import qrcode
from PIL import Image
import datetime
import schedule
import time
import random
import string
import os

def generar_codigo_aleatorio(length=10):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(length))

def generar_qr(nombre_archivo):
    # Enlace base al que se redireccionará después de escanear el código QR
    enlace_base = "https://destino.com/"

    # Generar un código aleatorio para agregar al enlace base
    codigo_aleatorio = generar_codigo_aleatorio()

    # Generar el contenido del código QR con el enlace base y el código aleatorio
    contenido = enlace_base + codigo_aleatorio
    imagen = qrcode.make(contenido)

    # Guardar el código QR como imagen con el nombre especificado
    imagen.save(nombre_archivo)

    print("QR generado a las:", datetime.datetime.now())

def eliminar_qr(nombre_archivo):
    # Eliminar el código QR al siguiente día a las 7 PM
    os.remove(nombre_archivo)
    print("QR eliminado a las:", datetime.datetime.now())

def generar_y_programar_qr():
    # Generar un nuevo nombre de archivo basado en la fecha y hora actual
    nombre_archivo = datetime.datetime.now().strftime("%Y-%m-%d") + "_qr.png"

    # Verificar si el archivo ya existe
    if not os.path.exists(nombre_archivo):
        # Generar un nuevo código QR con el nombre de archivo generado
        generar_qr(nombre_archivo)

    # Programar la generación de un nuevo código QR todos los días a las 8 PM
    schedule.every().day.at("10:20").do(generar_qr, nombre_archivo)

    # Programar la eliminación del código QR al siguiente día a las 7 PM
    schedule.every().day.at("10:17").do(eliminar_qr, nombre_archivo)

    # Mantener el programa en ejecución para que las tareas programadas se ejecuten
    while True:
        schedule.run_pending()
        time.sleep(1)

# Iniciar la generación y programación de los códigos QR
generar_y_programar_qr()
